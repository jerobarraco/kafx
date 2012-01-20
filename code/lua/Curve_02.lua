
--# This script is given to the public domain.
--# You can use and modify the effect freely, also without credit, although I would appreciate some.
--#  http://my.opera.com/alkoon/blog/
--#  al-koon-11@hotmail.com
--# Use VSFilterMod

include("karaskel.lua")
include("zheolib.lua")

script_name = "Curve FX"
script_description = "Bezeir Curve FX ~"
script_author = "ALKOON"
script_version = "1.2"

function fx_Curve(subs)
	aegisub.progress.task("Getting header data...")
	local meta, styles = karaskel.collect_head(subs)
	aegisub.progress.task("Applying effect...")
	local i, ai, maxi, maxai = 1, 1, #subs, #subs
	while i <= maxi do 
		aegisub.progress.task(string.format("Applying effect (%d,%d)...", ai, maxai))
		aegisub.progress.set((ai-1)/maxai*100)
		local l = subs[i]
		if l.class == "dialogue" and not l.comment then karaskel.preproc_line(subs, meta, styles, l)
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
     for i = 1, line.kara.n do
		local syl = line.kara[i]
		local x, y =syl.center + line.left, line.middle
		local l = table.copy(line)
		if i == 1 then universe = -300
		end

		l.text = string.format("{\\an5\\org(%d,%d)\\bord0\\be2\\move(%d,%d,%d,%d)\\fad(150,0)\\1c&HD2F1CB&\\3c&H000000&\\frz100\\frx60\\t(\\fscx60\\fscy60\\frx100\\fry100\\frz300)\\t(\\1vc(H1D700A,H176D04,H48BD2D,H77D661)\\fscx100\\fscy100\\bord1\\be2\\frx0\\fry0\\frz0)}%s",x,y+60,x+70,0, x, y-10,syl.text)
		l.start_time=l.start_time - 700+syl.i*30+ universe
		l.end_time = line.start_time+syl.i*30
		l.layer=1
		subs.append(l)
		l.text = string.format("{\\an5\\org(%d,%d)\\bord0\\be2\\move(%d,%d,%d,%d)\\fad(150,0)\\1c&HD2F1CB&\\3c&H000000&\\frz100\\frx60\\t(\\fscx60\\fscy60\\frx100\\fry100\\frz-300)\\t(\\1vc(H1D700A,H176D04,H48BD2D,H77D661)\\fscx100\\fscy100\\bord1\\be2\\frx0\\fry0\\frz0)}%s",x,y-60,x+70,0, x, y-10,syl.text)
		l.start_time=l.start_time - 700+syl.i*30+ universe
		l.end_time = line.start_time+syl.i*30
		l.layer=1
		subs.append(l)		

		l.text = string.format("{\\an5\\bord0\\pos(%d,%d)\\1c&H10CE23&\\1vc(H1D700A,H176D04,H48BD2D,H77D661)\\jitter(2,2,2,2,0,0)\\3c&H000000&\\bord1}%s" ,x,y,syl.text)
		l.start_time=line.start_time+syl.i*30
		l.end_time = line.start_time + syl.start_time
		l.layer=1
		subs.append(l)
 


    if syl.inline_fx == "1" then 

		l = table.copy(line)
		local maxi = 380
		for j = 1, maxi do
		tiem_1= line.start_time+syl.start_time -500
		tiem_2= line.start_time+syl.start_time+j*1   
		tf= interpolate(j/maxi,tiem_1,tiem_2)
		Curve(j/maxi,450,57,x+140,y-35,x-40,y-100,x-7,y-10)
		l.text = string.format("{\\p1\\an5\\pos(%d,%d)\\fscx360\\fad(0,70)\\fscy360\\bord0\\blur2\\shad1\\4c&H61F5B2&\\1c&H0A9D19&\\t(\\1c&H1CAD2E&\\fscx250\\fscy250\\4c&H1AFEC6&)\\t(\\blur2\\fscx100\\fscy100\\fad(0,50))\\t(\\1c&HCFFFD4&\\4c&HB4FEED&)}m 0 0 l 0 0 l 1 0 l 1 1 l 0 1 {\\p0}" ,cur_x,cur_y)
		l.start_time= tf-maxi    
		l.end_time= tf    + 100
		l.layer=2
		subs.append(l)
		end
 
		l = table.copy(line)
		l.text = "{"..an(5)..bord(1)..frz(10)..fad(0,60)..t(frz(320))..move(x,y,x+10,y+50)..color(1,'10CE23')..t(color(1,'H49A93A')).."}"..syl.text
		l.start_time = line.start_time + syl.start_time
		l.end_time = l.start_time + syl.duration /2 + 50
		l.layer=1
		subs.append(l)


    elseif syl.inline_fx == "2"  then  

		l = table.copy(line)
		local maxi = 380
		for j = 1, maxi do
		tiem_1= line.start_time+syl.start_time -500
		tiem_2= line.start_time+syl.start_time+j*1   
		tf= interpolate(j/maxi,tiem_1,tiem_2)
		Curve(j/maxi,450,5,x+140,y+35,x-40,y+100,x-7,y+10)
		l.text = string.format("{\\p1\\an5\\pos(%d,%d)\\fscx360\\fad(0,70)\\fscy360\\bord0\\blur2\\shad1\\4c&H61F5B2&\\1c&H277B1A&\\t(\\1c&H40A031&\\fscx250\\fscy250\\4c&H1AFEC6&)\\t(\\blur1\\fscx100\\fscy100)\\t(\\1c&HCFFFD4&\\4c&HB4FEED&)}m 0 0 l 0 0 l 1 0 l 1 1 l 0 1 {\\p0}" ,cur_x,cur_y)
		l.start_time= tf-maxi    
		l.end_time= tf   + 100
		l.layer=2
		subs.append(l)					
		end
 
		l = table.copy(line)
		l.text = "{"..an(5)..bord(1)..frz(-10)..fad(0,60)..t(frz(-320))..move(x,y,x+10,y-50)..color(1,'10CE23')..t(color(1,'H49A93A')).."}"..syl.text
		l.start_time = line.start_time + syl.start_time
		l.end_time = l.start_time + syl.duration /2 + 50
		l.layer=1
		subs.append(l)

       end
    end
end

aegisub.register_macro("Curve_fx", "~ALKOON~", fx_Curve)
aegisub.register_filter("Curve_fx", "~ALKOON~", 2000, fx_Curve)