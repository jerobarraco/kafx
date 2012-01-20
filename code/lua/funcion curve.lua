l = table.copy(line)
if sil() == ' ' then -- si no hay texto
l.text = "{}"
else -- si hay texto
maxi = 500
for j = 1, maxi do
tem1= line.start_time+syl.start_time -- tiempo 1
tem2= tem1+j*1+1 -- tiempo 2
tf= interpolate(j/maxi, tem1, tem2) -- inter pa los tiempos


Curve(j/maxi, 660, y, x+400, y-300, x-500, y+500, x, y) -- func de la curva
-- interva, x_in, y_ini, x_int1, y_int1, x_int2, y_int2, x_fin, y_fin

l.text = "{"..an(5)..pos(cur_x, cur_y)..be(2)..bord(0)..color(1,'FFDE93')..fscxy(350)..t(alpha('ff')..fscxy(0)..color(1, 'D5BF77')).."}"..p(1, Fpixel())
l.start_time= tf-maxi
l.end_time= tf-300
l.layer = 3
subs.append(l)    
end
end


--------
--------


l = table.copy(line)
if sil() == ' ' or sil() == '' then -- si no hay texto
l.text = "{}"
else -- si hay texto
maxi = 300
for j = 1, maxi do
tem1= line.start_time+syl.start_time -- tiempo 1
tem2= tem1+j*1+1 -- tiempo 2
tf= interpolate(j/maxi, tem1, tem2) -- inter pa los tiempos

if syl.i == 2 or syl.i == 4 or syl.i == 6 or syl.i == 8 or syl.i == 10 or syl.i == 12 or syl.i == 14 or syl.i == 16 or syl.i == 18 or syl.i == 20 or syl.i == 22 or syl.i == 24 or syl.i == 26 or syl.i == 28 or syl.i == 30 then
pxc = 200
pyc = 100
else
pxc = -200
pyc = -100
end
Curve(j/maxi, x-syl.width/2, y, x+pxc, y+pyc, x+80, y-100, x+syl.width/2, y) -- func de la curva
-- interva, x_in, y_ini, x_int1, y_int1, x_int2, y_int2, x_fin, y_fin

l.text = "{"..an(5)..pos(cur_x, cur_y)..bord(0.8)..blur(8)..shad(0)..color(3, 'ffffff')..color(1,'ffffff')..fscxy(110)..t(frx(360)..alpha('ff')..fscxy(0)).."}"..p(6, Fbrillo())
l.start_time= tf-maxi
l.end_time= tf+200
l.layer = 10
subs.append(l)    
end
end