
include("karaskel.lua")
script_name = "Test_Colors_Curve"
script_author = "Esmaeel sddeq almansoori (ALKOON) "

function Fx_Curve_Colors(subs)
	local meta, styles = karaskel.collect_head(subs)
	local i, ai, maxi, maxai = 1, 1, #subs, #subs
	while i <= maxi do 
		aegisub.progress.task(string.format("Applying effect (%d/%d)...", ai, maxai))
		aegisub.progress.set((ai-1)/maxai*100)
		local l = subs[i]
		if l.class == "dialogue"  then karaskel.preproc_line(subs, meta, styles, l)
		do_fx(subs, meta, l)
		maxi = maxi - 1
		subs.delete(i)
		else
		i = i + 1
		end
		ai = ai + 1
	end
end

function do_fx(subs, meta, line)
     for i = 1,  line.kara.n  do
	local syl = line.kara[i]
	local x, y =syl.center + line.left, line.middle
	local l = table.copy(line) 


if i == 1 then alkoon = -200
end

 
	l.text = string.format("{\\an5\\bord1\\fad(200,0)\\pos(%d,%d)\\3a&H000000&\\1c%s\\3a&H22&\\be1}%s",x,y,ass_color(HSV_to_RGB(500*(syl.i/line.kara.n),1,1)),syl.text)		
	l.start_time = line.start_time -250 + syl.i*40 +alkoon 
	l.end_time = line.start_time +syl.start_time
	subs.append(l)

	l.text = string.format("{\\an5\\bord1\\be2\\fad(0,50)\\pos(%d,%d)\\1c%s\\3c&H000000&\\t(\\3c%s\\blur6\\fscx150\\fscy150)}%s",x,y,ass_color(HSV_to_RGB(500*(syl.i/line.kara.n),1,1)),ass_color(HSV_to_RGB(500*(syl.i/line.kara.n),1,1)),syl.text)		
	l.start_time = line.start_time+syl.start_time
	l.end_time = l.start_time +syl.duration
	subs.append(l)

	--# Make this function  David Pineda (Zheo) #--
 
 	function Curve(intpol, x_ini, y_ini,  x_int1, y_int1, x_int2, y_int2, x_fin, y_fin)
	curvx1 = interpolate(intpol, x_ini, x_int1)
	curvx2 = interpolate(intpol, curvx1, x_int2)
	curvx3 = interpolate(intpol, curvx2, x_fin)
	curvy1 = interpolate(intpol, y_ini, y_int1)
	curvy2 = interpolate(intpol, curvy1, y_int2)
	curvy3 = interpolate(intpol, curvy2, y_fin)
	curv_x, curv_y = curvx3, curvy3 
	return curv_x, curv_y
	end
 
	local maxi = 350 
         	for j = 1, maxi   do
 
	local durations = syl.end_time
	tiem_1= line.start_time+syl.start_time -1500
	tiem_2= line.start_time+syl.start_time   + j*1
	tf= interpolate(maxi/j,tiem_1,tiem_2)
	Curve(j/maxi,300,57,x+140,y-35,x-40,y-100,x,y)
	l.text = string.format("{\\p1\\an5\\bord0\\be1\\blur2\\bord0.9\\shad1\\4c&HFFFFFF&\\fad(0,50)\\pos(%d,%d)\\3c%s\\fscx250\\fscy250\\t(\\fscx30\\fscy30)\\t(0,100,\\1c%s)\\t(100,%d,\\fscx0\\fscy0)}m 0 0 l 0 0 l 1 0 l 1 1 l 0 1 {\\p0}",curv_x,curv_y ,ass_color(HSV_to_RGB(500*(syl.i/line.kara.n),1,1)),ass_color(HSV_to_RGB(300*(syl.i/20),1,1)),durations )		
	l.start_time= tf-maxi   
	l.end_time= tf    -100
	l.layer=2
	subs.append(l)
	end
	 
     end
end

 
aegisub.register_macro("Fx_Curve_Colors", "Applying Effect", Fx_Curve_Colors)
aegisub.register_filter("Fx_Curve_Colors", "Applying Effect", 2010, Fx_Curve_Colors)