local line = lines[1]
local l = line
local time_end = (lines[2].start_time)

if line.i ~= #lines then
	--Create path with character shifted points
	local function create_path(destination, char)
		if char.text ~= " " then
			local char_path = GetPath(line.styleref, char.text)
			for pi, point in ipairs(char_path) do
				point.x = point.x + math.floor((char.left - line.left) * 8)
			end
			table.insert(destination, char_path)
		end
	end
	--Fix tables to equal number of elements (minimal table size: 3)
	local function equal_size(path_a, path_b)
		local path_diff = math.abs(#path_a - #path_b)
		if path_diff > 0 then
			local small_path
			if #path_a > #path_b then
				small_path = path_b
			else
				small_path = path_a
			end
			for i=1, path_diff do
				local index = math.random(2, #small_path-1)
				local tab = table.copy(small_path[index])
				table.insert(small_path, index, tab)
			end
		end
	end
	--Current character paths
	local cur_path = {}
	for ci, char in ipairs(line.chars) do
		create_path(cur_path, char)
	end
	--Destination character paths
	local next_path = {}
	for ci, char in ipairs(lines[line.i+1].chars) do
		create_path(next_path, char)
	end
	--Equal character paths number
	equal_size(cur_path, next_path)
	--Animate (line-to-line morphing)
	for s, e, i, n in frames(line.end_time, time_end +1500 , 41.71) do
		for ci=1, #cur_path do
			equal_size(cur_path[ci], next_path[ci])
			l.start_time = s
			l.end_time = e
			local pct = i / n
			local function morph(x, y, p_pct)
				local index = math.ceil(p_pct * #cur_path[ci])
				local new_x = x + math.floor(pct * (next_path[ci][index].x - x))
				local new_y = y + math.floor(pct * (next_path[ci][index].y - y))
				return new_x, new_y
			end
			local line_shape = BuildPath(cur_path[ci], morph)
			l.text = string.format("{\\an7\\pos(%.3f,%.3f)\\p4}%s", line.left, line.top, line_shape)
			Output(l)
		end
	end
end