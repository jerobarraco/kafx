--[[
Prueba de Overlua by Zheo
D:
]]

-- Set up some parameters
timing_input_file = overlua_datastring
-- Just the font name to use.
font_name = "Bernard MT Condensed"
font_size = 30
-- This is the position of the _baseline_ of the text, neither top, bottom nor center!
ypos = 45
-- Duration of fadein/out in seconds
fadetime = 0.5

-- Error out if no file name was given (data= in Avisynth invocation)
assert(timing_input_file, "Missing timing input file for sample effect.")


-- ASS file reading stuff
function parsenum(str)
	return tonumber(str) or 0
end
function parse_ass_time(ass)
	local h, m, s, cs = ass:match("(%d+):(%d+):(%d+)%.(%d+)")
	return parsenum(cs)/100 + parsenum(s) + parsenum(m)*60 + parsenum(h)*3600
end

function parse_k_timing(text)
	local syls = {}
	local i = 1
	for timing, syltext in text:gmatch("{\\k(%d+)}([^{]*)") do
		local syl = {dur = parsenum(timing)/100, text = syltext, i = i}
		table.insert(syls, syl)
		i = i + 1
	end
	return syls
end

function read_input_file(name)
	for line in io.lines(name) do
		local start_time, end_time, style, fx, text = line:match("Dialogue: 0,(.-),(.-),(.-),.-,0000,0000,0000,(.-),(.*)")
		if text then
			local ls = {}
			ls.start_time = parse_ass_time(start_time)
			ls.end_time = parse_ass_time(end_time)
			ls.style = style
			ls.fx = fx
			ls.rawtext = text
			ls.kara = parse_k_timing(text)
			ls.cleantext = text:gsub("{.-}", "")
			table.insert(lines, ls)
		end
	end
end

function init()
	if inited then return end
	inited = true
	
	lines = {}
	read_input_file(timing_input_file)
end


-- Get/create a "sparks" texture, singleton-style
function get_sparks_texture(width, height)
	-- Check if it already exists, just return it then
	if sparks_texture then return sparks_texture end
	-- We'll make a 100x100 black image with some blurred whitish spots on
	local surf = cairo.image_surface_create(100, 100, "argb32")
	local c = surf.create_context()
	-- Paint it all black
	c.set_source_rgb(0,0.5,1)
	c.paint()
	-- Then create a very light yellow
	c.set_source_rgb(1,1,0.9)
	
	-- And create 100 small, random circles
	for i = 1, 200 do
		local x, y = math.random(150)+4, math.random(200)+4
		c.arc(x, y, 5, 0, 10*math.pi)
		c.fill()
	end
	-- And blur the result
	raster.directional_blur(surf, 360, 5)
	
	-- Then create a texture of it.
	-- sparks_texture becomes a global variable
	sparks_texture = cairo.pattern_create_for_surface(surf)
	sparks_texture.set_extend("repeat")
	
	return sparks_texture
end


function render_frame(f, t)
	init()
	
	-- Create a blurred copy of the video frame
	local fsurf = f.create_cairo_surface()
	raster.gaussian_blur(fsurf, 5)
	
	-- Function to create "wobble" effect on the text
	local function blubble_mapper(x, y)
		local nx = x + math.sin(x/30 + y/10 + t*2.5)*2
		local ny = y + math.cos(y/20 + x/20 + t*2.8)*2
		return nx, ny
	end
	
	-- Find lines to be drawn
	for i, line in pairs(lines) do
		-- Check if the line is within time range.
		-- "In time range" means starts fadetime seconds later than current time or ends "fadetime" seconds earlier.
		if line.start_time <= t+fadetime and line.end_time > t-fadetime then
			local x = 0
			local y = ypos
			
			-- Prepare a surface to draw on
			local surf = cairo.image_surface_create(f.width, 300, "argb32")
			local c = surf.create_context()
			-- Select the font
			c.select_font_face(font_name)
			c.set_font_size(font_size)
			-- Get the text extents for the line text if we don't have them already
			if not line.te then line.te = c.text_extents(line.cleantext); line.fe = c.font_extents() end
			-- And calculate the start X to have the line centered
			x = (f.width - line.te.width) / 2 - line.te.x_bearing
			-- Then make a path for the text
			c.move_to(x, y)
			c.text_path(line.cleantext)
			
			-- Create the "wobble" effect on the text
			-- First get a Path object for the text
			local path = c.copy_path()
			-- Run the path through the mapping function
			path.map_coords(blubble_mapper)
			-- Clear the path in the context
			c.new_path()
			-- And add the modified path back
			c.append_path(path)
			
			-- Prepare drawing the text outline
			c.set_line_width(8)
			-- Red outline
			c.set_source_rgba(155, 0, 0, 2)
			-- Stroke it but keep the path in the canvas
			c.stroke_preserve()
			-- Blur this outline
			raster.directional_blur(surf, math.random(-360, 360), 8)
			-- raster.gaussian_blur(surf, 3)
			-- Prepare another, smaller outline on top
			c.set_line_width(3)
			-- This one is white
			c.set_source_rgba(1, 1, 1, 1)
			-- Stroke that one too, but clear the path afterwards
			c.stroke()
			
			-- Now loop over the syllables to draw them one by one
			local sumdur = line.start_time
			for j, syl in pairs(line.kara) do
				-- Get the text extents for this syllable
				if not syl.te then syl.te = c.text_extents(syl.text) end
				-- Prepare the path
				c.move_to(x, y)
				c.text_path(syl.text)
				-- Wobble the path; this will work because the mapper is deterministic on X, Y and timestamp
				local path = c.copy_path()
				path.map_coords(blubble_mapper)
				c.new_path()
				c.append_path(path)
				-- And advance X position
				x = x + syl.te.x_advance
				-- Now figure out whether this syllable is the active one or not
				-- Use a more complicated test, this makes the first syllable be highlighted
				-- also while the line is fading in, and the last while the line is fading out.
				if (syl.i == 1 and t < sumdur+syl.dur) or
						(syl.i == #line.kara and t > sumdur) or
						(t >= sumdur and t < sumdur+syl.dur) then
					-- Get the "sparks" texture
					local sparks = get_sparks_texture()
					-- Prepare a transformation matrix for it
					local texmat = cairo.matrix_create()
					texmat.init_rotate(t/10)
					texmat.scale(3, 3)
					sparks.set_matrix(texmat)
					-- Use the texture
					c.set_source(sparks)
										-- And fill the path
					c.fill()
				else
					-- Not the active syllable, fill it with a blurred video frame
					-- Remember fsurf is the blurred video frame
					c.set_source_surface(fsurf, 0, 0)
					c.fill_preserve()
					-- Also add a slight darkening to the fill
					c.set_source_rgba(0.2, 0, 0, 0.3)
					c.fill()
				end
				-- Advance the sum of syllable durations
				sumdur = sumdur + syl.dur
			end
			
			-- Figure out whether we're past the actual start/end time of the line and do some fading then
			local final = surf
			if t < line.start_time or t > line.end_time then
				-- Make invisibility the amount the line is invisible
				local invisibility
				if t < line.start_time then
					invisibility = (line.start_time - t) / fadetime
				else
					invisibility = (t - line.end_time) / fadetime
				end
				-- We'll need a new surface object here
				final = cairo.image_surface_create(surf.get_width(), surf.get_height(), "argb32")
				local c = final.create_context()
				-- So we can alpha-blend the original drawn text image onto it using invisibility as alpha
				c.set_source_surface(surf, 0, 0)
				c.paint_with_alpha(1-invisibility)
				-- And then do some heavy blur-out
				raster.gaussian_blur(final, invisibility*15)
			end
		
			-- Finally just overlay the text image on the video
			f.overlay_cairo_surface(final, 0, 0)
		end
	end
end