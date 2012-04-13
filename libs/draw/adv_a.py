# -*- coding: utf-8 -*-
"""
.. module:: libs.draw.advanced
   :platform: Unix, Windows
   :synopsis:
				These are the "Advanced" effects
				Basically these are effects that working at image level.
				In other words, filters and similar things.

.. moduleauthor:: Kafx team http://kafx.com.ar
"""
import cairo
from random import random
from math import cos, sin, pi

import extra
from libs import video

_capas = {}
class Layer:
	"""Clase interna para cada capa, no tocar :D"""
	def __init__(self,  opacity=1.0, mode='over'):
		#todo copiar capa
		#Esto me suena a que va a ser super costoso... pero bueno, me lo han pedido taaaaaaaaaaaaaaanto...
		global OPERATORS

		vi = video.vi
		"""sfc = video.cf.ctx.get_target().create_similar(cairo.CONTENT_COLOR_ALPHA,  vi.width,  vi.height)
		self.ctx = cairo.Context(sfc)
		self.ctx.set_operator(cairo.OPERATOR_CLEAR)
		self.ctx.paint()
		self.ctx.set_operator(cairo.OPERATOR_OVER)"""
		self.ctx = cairo.Context(cairo.ImageSurface(vi.modo, vi.width, vi.height))#habia cambiado modo por mode, pero me tiro error para las capas asi que lo deje como estaba :D
		self.ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
		#cairo.ANTIALIAS_SUBPIXEL
		#cairo.ANTIALIAS_NONE
		#cairo.ANTIALIAS_GRAY
		fop = cairo.FontOptions()
		fop.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
		self.ctx.set_font_options(fop)
		self.ctx.set_line_join(cairo.LINE_JOIN_ROUND)
		self.ctx.set_line_cap(cairo.LINE_CAP_ROUND)

		if mode not in OPERATORS :
			mode = 'over'

		self.mode = OPERATORS.index(mode)
		self.alpha = opacity

def LayerStarts():
	"""Llamar en cada OnFrameStarts"""
	global _capas
	_capas = {}

	if not ('base' in _capas):
		base = Layer()
		base.ctx = video.cf.ctx
		_capas['base'] = base

#TODO problema de stride
def LayerActivate(layer=0, opacity=1.0, mode='over'):
	"""
	Activates a layer.
		todo lo que se pinte luego de esto se pintará sobre la capa activada.

	.. note::
		Layers are for Abelkm because his high participation in KAFX.
		But I (`Nande!`) don't recommend its use.
		To use it, you are agree that the things you make are bad, and probably
		you didn't search how to make it better, remember there is a forum, doc, and IRC channel.


	:param layer:
		Nombre de la capa a activar, igual que se uso en CapasCrear
		la capa de nombre "base" es una capa especial, la capa del video, sobre la que se pinta todo.
		Si no existe la crea, y ahi se usan los parametros adicionales
	:type layer:
		Puede ser un numero o un texto, Esto define el orden en que se pintan
		las capas. Siempre se pintaran segun el orden de su nombre (1,2,3) ('a','b','c') etc
	:param opacity: Layer opacity
	:type opacity: double. Between 0.0 and 1.0
	:param mode: 	mode de pintado de la capa. un texto. igual que en PaintMode.
	:type mode: string. (Ver valores posibles en `OPERATORS`)

	"""
	global _capas
	if not layer in _capas:
		_capas[layer] = Layer(opacity, mode)
	video.cf.ctx = _capas[layer].ctx

def LayerEnd():
	"""Llamar en cada OnFrameEnds"""
	global _capas
	video.cf.ctx = _capas['base'].ctx
	ctx = video.cf.ctx

	nombres = _capas.keys()
	nombres.sort()
	nombres.remove('base')
	for nombre in nombres:
		#@Type capa Capa
		capa = _capas[nombre]
		ctx.set_source_surface(capa.ctx.get_target())
		ctx.set_operator(capa.mode)
		ctx.paint_with_alpha(capa.alpha)
	_capas = {}

"""Notes
set_source toma un pattern
set_source_surface toma un surface
pop_group devuelve un pattern
pop_group_to_source ... lo pone en source
get_group_target da un surface que es a donde se pinta
"""

#Estos son los tipos de operadores, solo se necesita cambiar esto en caso que cairo saque algo nuevo.. cosa q dudo , pero gracias a dios paso
#http://cairographics.org/manual-1.10.0/cairo-cairo-t.html#cairo-operator-t

OPERATORS = [
	'clear',#clear destination layer (bounded)

	'source', #replace destination layer (bounded)
	'over', #(default mode) draw source layer on top of destination layer (bounded)
	'in', #draw source where there was destination content (unbounded)
	'out', #draw source where there was no destination content (unbounded)
	'atop', #draw source on top of destination content and only there

	'dest', #ignore the source
	'dest_over', #draw destination on top of source
	'dest_in', #leave destination only where there was source content (unbounded)
	'dest_out', #leave destination only where there was no source content
	'dest_atop',#leave destination on top of source content and only there (unbounded)

	'xor',#source and destination are shown where there is only one of them
	'add',#source and destination layers are accumulated
	'saturate',#like over, but assuming source and dest are disjoint geometries

	#Pequeño hack para poder usar estas constantes con pycairo 1.8 (ya que estas constantes se declararon en cairo>1.9, pero como gkt2 trae cairo 1.10...)
	'multiply',
	'screen',
	'overlay',
	'darken',
	'lighten',
	'color_dodge',
	'color_burn',
	'hard_light',
	'soft_light',
	'difference',
	'exclusion',
	'hsl_hue',
	'hsl_saturation',
	'hsl_color',
	'hsl_luminosity'
]

#El tipo de operacion de pintado default es over
paint_operator = cairo.OPERATOR_OVER

def PaintMode(op=None):
	"""
	Cambia el mode de pintado comun,
	@op : opcional ha de ser un string con el nombre del mode de pintado tal cual esta en el array OPERATORS
	Si no se especifica la operacion, se restaura al ultimo mode que se usó, util porque algunas funciones cambiarán el mode de pintado de manera temporal,
	de esta manera se puede hacer poner un mode global e intercambiarlo para funciones especificas, como glow"""
	ctx = video.cf.ctx
	global OPERATORS, paint_operator
	if op in OPERATORS:
		paint_operator = OPERATORS.index(op)
	ctx.set_operator(paint_operator)

def fBlur1(steps=4, opacity=0.15):
	"""
		El blur por excelencia, el mas rápido, mas visible, sin errores (casi)
		opcionales:
		@steps=4 cantidad de steps del blur
		@opacity=0.15 opacity de cada paso
	"""
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	#creamos un pattern porque parece q tiene un minimo overhead menor al surface además no tenemos el dilema del "al pintar d nuevo cambia el source con la pintada anterior"
	ctx.set_source(pat) #lo ponemos como source
	m=cairo.Matrix()#creamos una matriz de transformación para el pat
	for a in xrange(1, int(steps+1)):
		a1 = -a #optimizacion  (???)
		a2 = a*2
		for x in (a1, a2):
			m.translate(x, 0) #cairo permite transformaciones "progresivas"
			#por eso hacemos -a, a*2, lo movemos a la izq, y para ponerlo a la derecha tenemos que moverlo dos veces a la derecha (y luego una vez mas a la izq para centrarlo)
			for y in (a1, a2):
				m.translate(0, y)
				pat.set_matrix(m)
				ctx.paint_with_alpha(opacity)
			m.translate(0,a1)#center
		m.translate(a1,0)#center

def fBlur1b(steps=6,  opacity=0.25):
	"""El viejo blur..."""
	ctx = video.cf.ctx
	sfc=extra.CopyTarget()
	for a in xrange(1, int(steps+1)):
		for x in (-a, a):
			for y in (-a, a):
				ctx.set_source_surface(sfc, x, y)
				ctx.paint_with_alpha(opacity)

def fBlur2(steps=3, opacity=0.8):
	#This blur (seems to) have a decreasing opacity, it looks more "real" more round and more soft, but needs more opacity
	#also doesnt seem to work well with big sizes
	#por alguna razon se va abajo y el blur1 no
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	ctx.set_source(pat)
	acumop = float(opacity)/steps
	steps+=1
	for i in xrange(1, int(steps)):
		m=cairo.Matrix()
		m.translate(0, -i)#0,-1 #up
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacity)

		m.translate(-i, i)#-1,0 #left
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacity)

		m.translate(i, i)#0,1 #down
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacity)

		m.translate(i, -i)#1,0 #right
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacity)
		opacity-=acumop

def fBlur3(steps=3, opacity=None):
	"""Blur usando pil, verdadero blur gausiano.. el parametro de opacity no hace effect
	asquerosamente lento,

	"""
	import Image, ImageFilter, array #code ripped form cairo somewhere in the weird web
	ctx = video.cf.ctx

	im = ctx.get_group_target()
	w = im.get_width()
	h = im.get_height()
	#Cuidado con esto, si no convirtieron el frame de avisynth a rgba (rgb32) es posible que de errores.... para eso habria que checkear video.cf y el tipo de datos, pero no da
	im1 = Image.frombuffer("RGBA", (w,h ), im.get_data(), "raw", "RGBA", 0, 1)
	for i in xrange(int(steps)):
		im1 = im1.filter(ImageFilter.BLUR)
	#this will also allows to use convolution kernel filters if you didn't noticed :D
	im1 = im1.filter(ImageFilter.SMOOTH_MORE)

	#imgd = im1.tostring("raw","RGBA",0,1)
	imgd = im1.tostring()
	a = array.array('B', imgd)
	surface = cairo.ImageSurface.create_for_data (a, cairo.FORMAT_ARGB32, w, h, video.vi.fake_stride)
	#ctx.rectangle(0,0, w,h)
	ctx.set_source_surface(surface)
	#ctx.fill()
	ctx.paint()

def fBlur4(steps=0, opacity=0):
	"""Ejemplo de como implementar un filter kernel
	es tambien un ejemplo de como pasar un surface de cairo a otras cosas como pil o ogl"""
	import Image, ImageFilter, array
	ctx = video.cf.ctx
	im = ctx.get_group_target()
	w = im.get_width()
	h = im.get_height()
	im1 = Image.frombuffer("RGBA", (w,h), im.get_data(), "raw", "RGBA", 0, 1)
	#laplace kernel
	#k = (-1, -1, -1, 1, 1,  -1, -1, -1, -1, 1,  2, 0, -1, -1, 1,  4, 2, -1, -1, -1,  1,1,1,-1,-1)
	#s = (5,5)
	#detect edges
	#k = (0,1,0, 1,-3,1, 0,1,0)
	#s=(3,3)
	#m=0
	#convolution
	#k = (0.5, 1, 0.5, 1, 0, 1, 0.5, 1, 0.5)
	#s=(3,3)
	#m=3
	#lines
	"""m=1
	s=(5,5)
	k = (	-1, -1, -1, -1, -1,
			 0,  0,  0,  0,  0,
			 1,  1,  1,  1,  1,
			 0,  0,  0,  0,  0,
			 -1, -1, -1, -1, -1)
	im1 = im1.filter(ImageFilter.Kernel( s, k ,m) )"""
	im1 = im1.filter(ImageFilter.MaxFilter)
	#im1 = im1.filter(ImageFilter.BLUR)
	#im1 = im1.filter(ImageFilter.SMOOTH_MORE)

	a = array.array('B', im1.tostring())
	surface = cairo.ImageSurface.create_for_data (a, cairo.FORMAT_ARGB32, w, h, video.vi.fake_stride)
	ctx.set_source_surface(surface)
	ctx.paint()

#este array define los tipos de blurs disponibles
fBlurs = [fBlur1, fBlur1b, fBlur2, fBlur3, fBlur4]
#esta variable es el tipo de blur usado, default el primero
fBlur = fBlurs[0]
"""Si se desea cambiar el tipo de blur pueden hacerlo seteando la variable blur_type en tu clase FxsGroup
o de la misma manera que acá arriba desde el script de effect obvio, no modifiquen este archivo por un effect.
"""

def Shadow(pattern, size=5, offx=0, offy=0, paint=True):
	"""
	@pattern es el patron usado como máscara. (o sea, el relleno de la sombra)
	opcionales:
	@size el tamaño del blur (cantidad de pasos y pixels)
	@offx, offy desplazamiento de la sombra sobre x e y respectivamente.
	@paint booleano indicando si se debe pintar o solo devolver el patron
	@return devuelve lo que se pinto como patron
	"""
	ctx = video.cf.ctx
	StartGroup()
	if size > 0 :
		#recordar de setear el source ANTES de llamar
		ctx.set_matrix(extra.CreateMatrix(offx, offy))
		ctx.mask(pattern)
		ctx.identity_matrix()
		fBlur(size)
	ctx.set_source(pattern)
	ctx.paint()
	op = 0.0
	if paint : op = 1.0

	return EndGroup(opacity=op)

def fDirBlur(angle=0, steps=1,  opacity=0.25):
	"""
	Blur Direccional

	opcionales:
	@angle=0 angulo en radianes de la dirección
	@steps=1 cantidad de pixels y steps que tendrá el blur
	@opacity=0.25 opacity de cada paso
	"""
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	#creamos un pattern porque parece q tiene un minimo overhead menor al surface además no tenemos el dilema del "al pintar d nuevo cambia el source con la pintada anterior"
	ctx.set_source(pat) #lo ponemos como source
	m = cairo.Matrix()#creamos una matriz de transformación para el pat
	xi = cos(angle)
	yi = sin(angle)

	for a in range(1, int(steps+1)):
		m.translate(xi, yi)
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacity)

def fDirBlurB(angle=0, steps=1, opacity=0.25):
	"""blur direccional usando surface"""
	ctx = video.cf.ctx
	sfc=ctx.get_group_target()
	x= xi = cos(angle)
	y= yi = sin(angle)

	for a in range(1, steps+1):
		ctx.set_source_surface(sfc,  x, y)
		ctx.paint_with_alpha(opacity)
		x+=xi
		y+=yi

def fBiDirBlur(angle=0, steps=1, opacity=0.25):
	"""Blur bidireccional

	opcionales:
	@angle=0 angulo en radianes de la dirección
	@steps=1 cantidad de pixels y steps que tendrá el blur
	@opacity=0.25 opacity de cada paso
	"""
	fDirBlur(angle, steps, opacity)
	fDirBlur(angle+pi, steps, opacity)

def fGlow(steps=3, opacity=0.05):
	"""
	Hace un effect de brillo
	opcionales:
	@steps cantidad de steps
	@opacity opacity de cada paso
	"""
	video.cf.ctx.set_operator(cairo.OPERATOR_ADD)
	fBlur(steps, opacity)
	PaintMode()

def StartGroup(copy_background=False):
	"""Comienza un grupo de pintado.
	es como un encapsulamiento
	todo lo que pintes dentro de un grupo no sera afectado por lo que tiene el de afuera.
	opcional
	@copy_background=False indica si el nuevo grupo contiene la informacion del grupo anterior
	"""
	if copy_background:
		ctx = video.cf.ctx
		#si esto da algun tipo de "error" (como cuando la textura se repite o si da error o algo raro)
		#activar la siguiente linea y comentar la otra
		sfc = extra.CopyTarget() #esto es mas lento pero quizas de menos problemas
		#sfc = ctx.get_group_target()#esto es mas rapido pero puede traer problemas ademas no esta admitido legalemente por cairo, asi que se puede romper en cualquier momento
		ctx.push_group()
		ctx.set_source_surface(sfc, 0, 0)
		ctx.paint()
	else:
		video.cf.ctx.push_group()

def EndGroup(opacity=1.0, matrix=None):
	"""
	Closes a Group. Every Opened group MUST be closed. Group are like parenthesis.
	The last opened group is the first to get closed.

	:param opacity: The opacity used for painting the resultant group. It can be 0.0 or False.
	:param matrix: Matrix for distortion of the whole group
	:type opacity: double
	:type matrix: :class:`cairo.Matrix`

	:Returns:
		a newly created :class:`cairo.SurfacePattern` containing the results
		of all drawing operations performed to the group.

	"""
	ctx= video.cf.ctx
	pat= ctx.pop_group()
	if matrix:
		pat.set_matrix(matrix)
	#if opacity>0:
	ctx.set_source(pat)
	ctx.paint_with_alpha(opacity)
	return pat


#todo probar esto pero usando  extra.CopyTarget
_time_blur_pat = None
def fTimeBlur(opacidad=0.15):
	global _time_blur_pat
	ctx = video.cf.ctx
	if _time_blur_pat:
		ctx.set_source_surface(_time_blur_pat)
		ctx.paint_with_alpha(opacidad)
	_time_blur_pat = ctx.get_group_target()
