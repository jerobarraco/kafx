
-- This script is given to the public domain.
-- You can use and modify the effect freely, also without credit, although I would appreciate some.
-- http://my.opera.com/alkoon/blog/
-- al-koon-11@hotmail.com

include("karaskel.lua")
include("zheolib.lua") 
include("formaslib.lua")

script_name = "Curve FX"
script_description = "Fx Lu.4"
script_author = "Alkoon"
script_version = "1.0"

function fx_Curve(subs)
	aegisub.progress.task("Getting header data...")
	local meta, styles = karaskel.collect_head(subs)
	aegisub.progress.task("Applying effect...")
	local i, ai, maxi, maxai = 1, 1, #subs, #subs
	while i <= maxi do 
		aegisub.progress.task(string.format("Applying effect (%d/%d)...", ai, maxai))
		aegisub.progress.set((ai-1)/maxai*100)
		local l = subs[i]
		if l.class == "dialogue" and not l.comment then
			karaskel.preproc_line(subs, meta, styles, l)
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
		local x=syl.center + line.left
		local y=line.middle	
		line.fx = table.copy(line)

line.fx.text = "{"..an(5)..bord(1)..fad(100,0)..pos(x,y)..c(1,'HFFFFFF').."}"..syl.text
line.fx.start_time=line.fx.start_time - 1000+syl.i*40
line.fx.end_time = line.start_time+syl.i*40
line.fx.layer = 4 
subs.append(line.fx)

line.fx.text = "{"..an(5)..bord(1)..pos(x,y)..c(1,'HFFFFFF').."}"..syl.text
line.fx.start_time = line.start_time+syl.i*40
line.fx.end_time = line.start_time+syl.start_time
subs.append(line.fx)




    if syl.inline_fx == "1" then --# {\k50\-1} in ass file

	l = table.copy(line)
	local maxi = 340
	for j = 1, maxi do
	tiem_1= line.start_time+syl.start_time -1500
	tiem_2= line.start_time+syl.start_time+j*1   
	tf= interpolate(j/maxi,tiem_1,tiem_2)
	Curve(j/maxi,300,57,x+140,y-35,x-40,y-100,x-7,y-10)
	l.text = "{"..an(5)..move(cur_x,cur_y,cur_x,cur_y)..bord(0)..fscxy(440)..fad(0,0)..be(2)..blur(3)..t(fscxy(100)..blur(1))..t(color(1,'H96B0E0'))..t(color(1,'H104CB5'))..t(color(1,'H8AAADE')).."}"..p(1,Fpixel())
	l.start_time= tf-maxi   +20
	l.end_time= tf    
	l.layer=2
	subs.append(l)
	end
 

	l = table.copy(line)
	l.text = "{"..an(5)..bord(1)..frz(10)..t(frz(20))..move(x,y,x,y+10)..clip(1,0,639,56)..t(tt(0,300)..color(1,'99ACE0')).."}"..syl.text
	l.start_time = line.start_time + syl.start_time
	l.end_time = l.start_time + syl.duration +100
	l.layer=1
	subs.append(l)
	l = table.copy(line)
	l.text = "{"..an(5)..bord(1)..frz(20)..move(x,y+10,x-300,y+26)..clip(1,0,639,56)..t(tt(0,300)..color(1,'99ACE0')).."}"..syl.text
	l.start_time=line.start_time+syl.start_time + syl.duration +100
	l.end_time=l.start_time+1500
	l.layer=1
	subs.append(l)


    elseif syl.inline_fx == "2"  then  --# {\k50\-2} in ass file
 
	l = table.copy(line)
	local maxi = 340
	for j = 1, maxi do
	tiem_1= line.start_time+syl.start_time -1500
	tiem_2= line.start_time+syl.start_time+j*1   
	tf= interpolate(j/maxi,tiem_1,tiem_2)
	Curve(j/maxi,300,5,x+140,y+35,x-40,y+100,x-7,y+10)
	l.text = "{"..an(5)..move(cur_x,cur_y,cur_x,cur_y)..bord(0)..fscxy(440)..fad(0,0)..be(2)..blur(3)..t(fscxy(100)..blur(1))..t(color(1,'H96B0E0'))..t(color(1,'H104CB5'))..t(color(1,'H8AAADE')).."}"..p(1,Fpixel())
	l.start_time= tf-maxi   +20
	l.end_time= tf    
	l.layer=2
	subs.append(l)					
	end
 
	l = table.copy(line)
	l.text = "{"..an(5)..bord(1)..frz(-10)..t(frz(-20))..move(x,y,x,y+10)..clip(1,0,639,56)..t(tt(0,300)..color(1,'99ACE0')).."}"..syl.text
	l.start_time = line.start_time + syl.start_time
	l.end_time = l.start_time + syl.duration +100
	l.layer=1
	subs.append(l)
	l = table.copy(line)
	l.text = "{"..an(5)..bord(1)..frz(-20)..move(x,y+10,x-300,y+26)..clip(1,0,639,56)..t(tt(0,300)..color(1,'99ACE0')).."}"..syl.text
	l.start_time=line.start_time+syl.start_time + syl.duration +100
	l.end_time=l.start_time+1500
	l.layer=1
	subs.append(l)
    end




function genre_circulo(rad,centrox,centroy,angulo,moveminto)
                      posx=centrox + rad*math.cos(angulo)
                      posy=centroy + rad*math.sin(angulo)
 
   if not moveminto then
   return posx,posy
    else
                      posx1=centrox + (rad+moveminto)*math.cos(angulo)
                      posy1=centroy + (rad+moveminto)*math.sin(angulo)
   return posx,posy,posx1,posy1
   end
end

                                         local color={"&HD2DCF8&","&H4B76E3&","&HBFCEED&","&H1558DE&"}
                                         local pcolor=color[math.random(1,4)]
                                         local maxi =   100,math.ceil(syl.duration/10*15)
                                         for i  =   0, maxi  do  
                                         if i ==  0 then 
                                         mov =40  
                                         end
                                         angulo=math.rad(mov) 
                                         genre_circulo(5,x,y,mov,25)
                                         l.text = string.format("{\\p1\\fad(50,200)\\be0\\an5\\bord1\\blur2\\3c&HE3EBFB&\\move(%d,%d,%d,%d)\\fscx100\\fscy100\\1c%s\\t(\\1c&HF8DFCE&\\b2)}m 0 0 l 0 1 1 1 1 0{\\p0}",posx,posy,posx1,posy1,pcolor)
                                         l.start_time=line.start_time+ syl.start_time + (i/maxi)*syl.duration  
                                         l.end_time=l.start_time+syl.duration 
                                         l.layer = 0
                                         subs.append(l)
                                         mov=mov+40 + (i/maxi)
                                         end

end
end

 
aegisub.register_macro("Curve", "~ALKOON~", fx_Curve)
aegisub.register_filter("Curve", "~ALKOON~", 2000, fx_Curve)