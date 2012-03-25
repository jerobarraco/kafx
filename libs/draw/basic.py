# -*- coding: utf-8 -*-
"""
.. module:: libs.draw.basic
   :platform: Unix, Windows
   :synopsis:
				.. note::
						S* functions sets a `cairo.Source`
						DO -NOT- FORGET THE ORIGIN IS RELATIVE TO THE POSITION OF THE VECTOR! (cDialogue, cSyllable, etc )
.. moduleauthor:: Kafx team http://kafx.com.ar
"""
import cairo
from libs import video


def SSolid(obj, color, part):
	"""Uses the color from obj.actual"""#ACTUAL <- change that pretty much everywhere [[TO-DO]]
	#cairo.SolidPattern(a.r, a.g, a.b, a.a) is an alternative
	video.cf.ctx.set_source_rgba(color.r, color.g, color.b, color.a)

def SPattern(obj, mycolor, part):
	"""Uses the pattern in obj.actual.source"""
	txt = obj.textures[part]
	ctx = video.cf.ctx
	ctx.set_source(txt)
	if mycolor.a < 1:
		ctx.push_group()
		ctx.set_source(txt)
		#this is a workaround to avoid the active path
		#do not try to change this, you'd need to change everything else
		ctx.paint_with_alpha(mycolor.a)
		ctx.pop_group_to_source()

def Linear(x,y,x1,y1,c1,c2):
	"""Code for the gradient funcs"""
	lineal = cairo.LinearGradient(x,y, x1,y1)
	lineal.add_color_stop_rgba(0, c1.r, c1.g, c1.b, c1.a)
	lineal.add_color_stop_rgba(1, c2.r, c2.g, c2.b, c2.a)
	video.cf.ctx.set_source(lineal)

def SVerticalGradient(obj, color, part):
	"""Uses a vertical gradient, its height is the line's,
	for it to be the same for every syllable painted at the same time"""
	Linear(0, -obj.original._line_height, 0, 0, color, obj.actual.color2)

def SHorizontalGradient(obj, color, part):
	"""Uses a horizontal gradient"""
	Linear(0,0, obj.original._ancho,0, color, obj.actual.color2)

def SDiagonalGradient(obj, color, part):
	"""Uses a linear gradient, top-left to bottom-right"""
	Linear(0, -obj.original._line_height, obj.original._ancho,0, color, obj.actual.color2)

def SRadialGradient(obj, color, part):
	"""Uses a radial gradient, its center is the origin"""
	a = obj.actual
	cx = a.org_x
	cy = a.org_y

	hasta = a.color2
	radial = cairo.RadialGradient(cx, cy, 0, cx, cy, obj.original._ancho/2.0)
	radial.add_color_stop_rgba(0, color.r, color.g, color.b, color.a)
	radial.add_color_stop_rgba(1, hasta.r, hasta.g, hasta.b, hasta.a)
	video.cf.ctx.set_source(radial)

def SLinearAnimatedGradient(obj, color, part):
	"""Uses a linear horizontal gradient, animated through obj.progress"""
	a = obj.actual
	hasta = a.color2
	lineal = cairo.LinearGradient(a.pos_x, a.pos_y,
		a.pos_x+ (obj.original._ancho*obj.progress)
		, a.pos_y + (obj.original._line_height*obj.progress))
	lineal.add_color_stop_rgba(obj.progress, color.r, color.g, color.b, color.a)
	lineal.add_color_stop_rgba(1, hasta.r, hasta.g, hasta.b, hasta.a)
	video.cf.ctx.set_source(lineal)

def SRadialAnimatedGradient(obj, color, part):
	"""Uses a radial gradient, animated through obj.progress"""
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
	#Code by cairocool and ranma42 at #cairo@irc.freenode.net
	# more info: http://code.google.com/p/cairocks/
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

"""This array defines all the possible patterns,
you can create your own in your effect, either way...
your function must receive these parameters
	obj -> object (cDialogue, cSyllable or cVector)
	color -> suggested color (color1 for the fill color, color3 for the border, color4 for the shadow)
	part -> 0, 1 or 2 for fill, border and shadow respectively

you just have to append your function name  (it's strongly recommended to use
	basic.sources.append(yourFunction)
from your script, do -NEVER- modify this file)

and set the appropriate index for ModeFill/Border/Shadow
Example: diag.ModeShadow(8)
"""
sources = [SSolid, SPattern, SVerticalGradient, SHorizontalGradient, SDiagonalGradient,
	SRadialGradient, SLinearAnimatedGradient, SRadialAnimatedGradient, SColorPattern, SBevel
	]
