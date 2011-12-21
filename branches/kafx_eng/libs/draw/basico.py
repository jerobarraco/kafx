# -*- coding: utf-8 -*-
import cairo
from libs import video

#Las funciones S setean un surce
#NO OLIVDAR QUE LOS SOURCES SON RELATIVOS AL PUNTO DE POSICION DEL VECTOR!
def SSolido(obj, color, part):
	"""usa el color definido en obj.actual como source"""
	#Tambien podriamos usar cairo.SolidPattern(a.r, a.g, a.b, a.a) #tener en cuenta para crear un pattern de un ccairocolor
	video.cf.ctx.set_source_rgba(color.r, color.g, color.b, color.a)

def STextura(obj, mycolor, part):
	"""Setea el source, usa la textura (pattern) almacenada en obj.actual.source como source"""
	txt = obj.texturas[part]
	ctx = video.cf.ctx
	ctx.set_source(txt)
	if mycolor.a < 1:
		ctx.push_group()
		ctx.set_source(txt)
		#Esto es un truco, ya que paint with alpha no depende de el path activo
		#si esto llegase a cambiar, hay que cambiar todo el código, yay!
		ctx.paint_with_alpha(mycolor.a)
		ctx.pop_group_to_source()

def Linear(x,y,x1,y1,c1,c2):
	"""código repetido de las funciones de degradados"""
	lineal = cairo.LinearGradient(x,y, x1,y1)
	lineal.add_color_stop_rgba(0, c1.r, c1.g, c1.b, c1.a)
	lineal.add_color_stop_rgba(1, c2.r, c2.g, c2.b, c2.a)
	video.cf.ctx.set_source(lineal)

def SDegradadoVertical(obj, color, part):
	"""Setea el source como un dergadado lineal verticalmente, el alto del degradado es el alto de la linea,
	para que sea el mismo aun pintando diferentes sílabas por separado"""
	Linear(0, -obj.original._alto_linea, 0, 0, color, obj.actual.color2)

def SDegradadoHorizontal(obj, color, part):
	"""Setea el source como un degradado lineal horizontalmente"""
	Linear(0,0, obj.original._ancho,0, color, obj.actual.color2)

def SDegradadoDiagonal(obj, color, part):
	"""Setea el source con un degradado lineal en diagonal desde arriba a la izquierda a abajo a la derecha"""
	Linear(0, -obj.original._alto_linea, obj.original._ancho,0, color, obj.actual.color2)

def SDegradadoRadial(obj, color, part):
	"""Setea el source como un degradado radial con centro en el punto de origen"""
	a = obj.actual
	cx = a.org_x
	cy = a.org_y

	hasta = a.color2
	radial = cairo.RadialGradient(cx, cy, 0, cx, cy, obj.original._ancho/2.0)
	radial.add_color_stop_rgba(0, color.r, color.g, color.b, color.a)
	radial.add_color_stop_rgba(1, hasta.r, hasta.g, hasta.b, hasta.a)
	video.cf.ctx.set_source(radial)

def SDegradadoLinealAnimado(obj, color, part):
	"""Crea un degradado lineal a lo ancho, usando el progress para el punto medio, creando un barrido"""
	a = obj.actual
	hasta = a.color2
	lineal = cairo.LinearGradient(a.pos_x, a.pos_y,
		a.pos_x+ (obj.original._ancho*obj.progress)
		, a.pos_y + (obj.original._alto_linea*obj.progress))
	lineal.add_color_stop_rgba(obj.progress, color.r, color.g, color.b, color.a)
	lineal.add_color_stop_rgba(1, hasta.r, hasta.g, hasta.b, hasta.a)
	video.cf.ctx.set_source(lineal)

def SDegradadoRadialAnimado(obj, color, part):
	"""Un degradado radial que va creciendo con el progress)"""
	a = obj.actual
	cx = a.org_x
	cy = a.org_y
	rad = obj.original._ancho*2*obj.progress or 0.001

	r = cairo.RadialGradient(cx, cy, 0, cx, cy, rad)
	r.add_color_stop_rgba(0, color.r, color.g, color.b, color.a)
	r.add_color_stop_rgba(1, a.color2.r, a.color2.g, a.color2.b, a.color2.a)
	video.cf.ctx.set_source(r)

def SColorPattern(obj, color, part):
	txt = obj.texturas[part]
	ctx = video.cf.ctx
	ctx.set_source_rgba(color.r, color.g, color.b, color.a)
	ctx.push_group()
	ctx.mask(txt)
	ctx.set_source(txt)
	ctx.pop_group_to_source()

def SBevel(obj, color, part):
	#untested
	#Codigo contribuido por cairocool y ranma42 en #cairo@irc.freenode.net
	# ver http://code.google.com/p/cairocks/
	a = obj.actual
	ctx = video.cf.ctx
	ctx.push_group()
	ctx.set_source_rgba(color.r, color.g, color.b, color.a)
	ctx.fill_preserve()
	o = a.color2
	ctx.set_source_rgba(o.r, o.g, o.b, 0.25)

	for i in range(8, 0, -2):
		ctx.set_line_width(i)
		ctx.stroke_preserve()

	ctx.pop_group_to_source()

"""Este array define los posibles sources
Podes implementar los tuyos en tu efecto, sólo agregalos al array al final,
tu función debe tener 3 parametros
	obj -> el objeto (cDialogo, cSilaba o cVector)
	color -> el color sugerido (color para relleno, ocolor para borde, bcolor para sombra)
	part -> 0, 1 o 2 indicando borde, relleno o sombra respectivamente

para usarla sólo debes agregar el nombre de tu función al final  (recomiendo usar
	basico.sources.append(xxxxx)
desde tu script, nunca modifiques este archivo)

y poner el indice que corresponda al usar ModeRelleno/Borde/Shadow
ej: diag.ModeShadow(8)
"""
sources = [SSolido, STextura, SDegradadoVertical, SDegradadoHorizontal, SDegradadoDiagonal,
	SDegradadoRadial, SDegradadoLinealAnimado, SDegradadoRadialAnimado, SColorPattern, SBevel
	]
