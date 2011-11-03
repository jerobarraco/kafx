--[[

Script para cargar  archivos .ASS en Overlua
y aplicar FXs

Algunos ejemplos fueron tomados de distintos tutoriales de Cairo
y modificados por mi, para hacerlos funcionar en Overlua.

Creado por Zheo
zheo@japanrevolution.com

]]

--------------------------------------------------VARIABLES Y CONFIGURACION--------------------------------------------------

-- overlua_datastring: es el string que hace llamar al AVS.
timing_input_file = overlua_datastring
-- Acá uno va colocando variables, que serán globales.
font_name = "Bandy"
font_size = 26
fadetime = 0.5

-- Chequeo del Archivo, si esta mal, saldra el mensaje de error
assert(timing_input_file, "ERROR: Missing input file")


-- string que convierte en numeros
function parsenum(str)
	return tonumber(str) or 0
end
-- Conversor de tiempos para el .ASS
function parse_ass_time(ass)
	local h, m, s, cs = ass:match("(%d+):(%d+):(%d+)%.(%d+)")
	return parsenum(cs)/100 + parsenum(s) + parsenum(m)*60 + parsenum(h)*3600
end

-- Capturador de los \K
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

-- Capturador de lineas de .ASS
function read_input_file(name)
	for line in io.lines(name) do
		-- Capturador del Estilo (Style)
		local start_time, end_time, style, fx, text = line:match("Dialogue: 0,(.-),(.-),(.-),.-,0000,0000,0000,(.-),(.*)")
		if text then
			local ls = {}
			ls.start_time = parse_ass_time(start_time)
			ls.end_time = parse_ass_time(end_time)
			ls.style = style
			ls.fx = fx
			ls.rawtext = text
			ls.kara = parse_k_timing(text)
			-- Limpiador
			ls.cleantext = text:gsub("{.-}", "")
			table.insert(lines, ls)
		end
	end
end

--------------------------------------------------CODIGO DEL FX--------------------------------------------------


-- Iniciador de Overlua. Empieza en el Frame 1,
-- por eso es recomendable dejar una linea en blanco al comienzo del .ASS
-- para que reconozca el archivo

-- Comienza el iniciador de los FX
function init()
	if inited then return end
	inited = true
	
	lines = {}
	read_input_file(timing_input_file)
end

-- Creación de textura dentro de cada silaba
function get_sparks_texture(width, height)
	-- Chequea si ya existe, sino, la crea
	if sparks_texture then return sparks_texture end
	-- Tamaño de la imagen y colorido
	local surf = cairo.image_surface_create(50, 50, "argb32")
	local c = surf.create_context()
	-- Pintura de la silaba
	c.set_source_rgb(0,0,1,1)
	c.paint()
	-- Otra pintura
	c.set_source_rgb(1,0,0,1)
	
	-- Creacion de circulos al interior del colorido
	for i = 1, 200 do
		local x, y = math.random(150)+4, math.random(200)+4
		c.arc(x, y, 5, 0, 10*math.pi)
		c.fill()
	end
	-- Un poco de Blur xD
	raster.directional_blur(surf, 360, 5)
	
	-- Y se termina la creación
	-- sparks_texture se convierte en variable global
	sparks_texture = cairo.pattern_create_for_surface(surf)
	sparks_texture.set_extend("repeat")
	
	return sparks_texture
end

-- La matrix de Overlua. Captura los Puntos Flotantes
-- y los renderiza en dibujos
function render_frame(f, t)
	-- Iniciador de render
	init()
	
-- Acá comienza la estructura de los FX
	local fsurf = f.create_cairo_surface()
	for i, line in pairs(lines) do
		if line.start_time <= t+fadetime and line.end_time > t-fadetime then
			-- Posicion inicial de lineas X-Y
			local x = 0
			local y = 30
			
			-- Dibujando los  Surface y Context
			local surf = cairo.image_surface_create(f.width, f.height, "argb32")
			local c = surf.create_context()
			
			-- Seleccion de la Font que se dio en la Variable al comienzo
			c.select_font_face(font_name)
			c.set_font_size(font_size)
			
			-- Calculo de tamaño de Font y largo de linea
			if not line.te then line.te = c.text_extents(line.cleantext); line.fe = c.font_extents() end
			-- Calculo de la posición central
			x = (f.width - line.te.width) / 2 - line.te.x_bearing
			
			-- Produce el Text Path
			c.move_to(x, y)
			c.text_path(line.cleantext)
			
-- Dibujo del borde de las letras
			c.set_line_width(5) --tamaño borde
			c.set_line_join("round") -- Union de lineas (Ver Documentacion)
			c.set_source_rgba(2, 5, 1, 1) --Se trabaja con ROJO-VERDE-AZUL-ALFA
			c.set_line_width(3) --tamaño borde
			c.set_line_join("bevel") -- Union de lineas (Ver Documentacion)
			c.set_source_rgba(0, 0, 0, 1) --Se trabaja con ROJO-VERDE-AZUL-ALFA
			-- "preserve" hace que se conserve el Texto
			c.stroke_preserve()
			-- Un poco de Blur, es como \be1, para el degrado detras de la silaba
			raster.box_blur(surf, 5) -- el numero indica la cantidad de Blur	
			c.fill()	
			
-- Silaba FX (colorido)
			local sumdur = line.start_time
			for j, syl in pairs(line.kara) do
				-- Obtebgo el Text Extents
				if not syl.te then syl.te = c.text_extents(syl.text) end
				-- Preparo el path
				c.move_to(x, y)
				c.text_path(syl.text)
				-- y la posicion X
				x = x + syl.te.x_advance
				-- Configuración para la Silaba Activa
				if (syl.i == 1 and t < sumdur+syl.dur) or
						(syl.i == #line.kara and t > sumdur) or
						(t >= sumdur and t < sumdur+syl.dur) then
					-- Obtengo el la textura "sparks"
					local sparks = get_sparks_texture()
					-- Cambio el matrix
					local texmat = cairo.matrix_create()
					texmat.init_rotate(t/10)
					texmat.scale(3, 3)
					sparks.set_matrix(texmat)
					-- Uso la textura
					c.set_source(sparks)
					-- y relleno la silaba
					c.fill()
				else
					-- Configuracion de las Silabas NO Activa, segun el Sfurf del comienzo
					c.set_source_surface(fsurf, 0, 0)
					c.fill_preserve()
					-- Pinta el interior de las letras
					c.set_source_rgba(1, 1, 1, 1) --Se trabaja con ROJO-VERDE-AZUL-ALFA
					c.fill()
				end
				-- Configuración del tiempo de cada silaba
				sumdur = sumdur + syl.dur
			end
			
			-- FX de Fade con Blur en las lineas
			local final = surf
			if t < line.start_time or t > line.end_time then
				-- Comienzo del Fade de cada linea
				local invisibility
				if t < line.start_time then
					invisibility = (line.start_time - t) / fadetime
				else
					invisibility = (t - line.end_time) / fadetime
				end
				-- Se crea otro Surface
				final = cairo.image_surface_create(surf.get_width(), surf.get_height(), "argb32")
				local c = final.create_context()
				-- Pongo la linea en alpha
				c.set_source_surface(surf, 0, 0)
				c.paint_with_alpha(1-invisibility)
				-- y un poco de Blur
				raster.gaussian_blur(final, invisibility*15)
			end
		
			-- Funcion Final que hace sobreponerlo en el Video
			f.overlay_cairo_surface(final, 0, 0)			
		end
	end
end
