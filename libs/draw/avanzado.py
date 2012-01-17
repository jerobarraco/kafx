# -*- coding: utf-8 -*-
import cairo
from random import random
from math import cos, sin, pi

import extra
from libs import video

"""Estos son los efectos "Avanzados"
Mas que nada son efectos que trabajan a nivel imagen.
O sea, mas que nada filtros y cosas similares.
"""

"""
Esto es para AbelKM dada su alta participacion con KAFX.
pero no recomiendo (yo, nande) para nada su utilizacion.
Usarlos es aceptar que estas haciendo algo que no esta
del todo bien, y que probablemente hay otra forma correcta
de hacerlo y que probablemente no buscaste como hacerlo.
recuerden que pueden preguntar en el irc.
"""
_capas = {}
class Capa:
	"""Clase interna para cada capa, no tocar :D"""
	def __init__(self,  opacidad=1.0, mode='over'):
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
		self.alpha = opacidad

def CapasInicia():
	"""Llamar en cada OnFrameStarts"""
	global _capas
	_capas = {}

	if not ('base' in _capas):
		base = Capa()
		base.ctx = video.cf.ctx
		_capas['base'] = base

#TODO antialias
#TODO problema de stride
#TODO Orden en eventos
def CapasActivar(capa=0, opacity=1.0, mode='over'):
	"""Activa una capa.
	todo lo que se pinte luego de esto se pintará sobre la capa activada.
	@capa Nombre de la capa a activar, igual que se uso en CapasCrear
		la capa de nombre "base" es una capa especial, la capa del video, sobre la que se pinta todo.

	Si no existe la crea, y ahi se usan los parametros adicionales
	@capa
		nombre de la capa. Puede ser un numero o un texto, Esto define el orden en que se pintan
		las capas. Siempre se pintaran segun el orden de su nombre (1,2,3) ('a','b','c') etc
	@opacidad=1.0
		opacidad de la capa. Valor entre 0.0 y 1.0
	@mode='over'
		mode de pintado de la capa. un texto. igual que en ModePainted.
		(Ver valores posibles en avanzado.OPERATORS)
	"""
	global _capas
	if not capa in _capas:
		_capas[capa] = Capa(opacity, mode)
	video.cf.ctx = _capas[capa].ctx

def CapasFin():
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
	'over', #draw source layer on top of destination layer (bounded)
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

def fBlur1(pasos=4, opacidad=0.15):
	"""
		El blur por excelencia, el mas rápido, mas visible, sin errores (casi)
		opcionales:
		@pasos=4 cantidad de pasos del blur
		@opacidad=0.15 opacidad de cada paso
	"""
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	#creamos un pattern porque parece q tiene un minimo overhead menor al surface además no tenemos el dilema del "al pintar d nuevo cambia el source con la pintada anterior"
	ctx.set_source(pat) #lo ponemos como source
	m=cairo.Matrix()#creamos una matriz de transformación para el pat
	for a in xrange(1, int(pasos+1)):
		a1 = -a #optimizacion  (???)
		a2 = a*2
		for x in (a1, a2):
			m.translate(x, 0) #cairo permite transformaciones "progresivas"
			#por eso hacemos -a, a*2, lo movemos a la izq, y para ponerlo a la derecha tenemos que moverlo dos veces a la derecha (y luego una vez mas a la izq para centrarlo)
			for y in (a1, a2):
				m.translate(0, y)
				pat.set_matrix(m)
				ctx.paint_with_alpha(opacidad)
			m.translate(0,a1)#center
		m.translate(a1,0)#center

def fBlur1b(pasos=6,  opacidad=0.25):
	"""El viejo blur..."""
	ctx = video.cf.ctx
	sfc=extra.CopiarTarget()
	for a in xrange(1, int(pasos+1)):
		for x in (-a, a):
			for y in (-a, a):
				ctx.set_source_surface(sfc, x, y)
				ctx.paint_with_alpha(opacidad)

def fBlur2(pasos=3, opacidad=0.8):
	#This blur (seems to) have a decreasing opacity, it looks more "real" more round and more soft, but needs more opacity
	#also doesnt seem to work well with big sizes
	#por alguna razon se va abajo y el blur1 no
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	ctx.set_source(pat)
	acumop = float(opacidad)/pasos
	pasos+=1
	for i in xrange(1, int(pasos)):
		m=cairo.Matrix()
		m.translate(0, -i)#0,-1 #up
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacidad)

		m.translate(-i, i)#-1,0 #left
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacidad)

		m.translate(i, i)#0,1 #down
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacidad)

		m.translate(i, -i)#1,0 #right
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacidad)
		opacidad-=acumop

def fBlur3(pasos=3, opacidad=None):
	"""Blur usando pil, verdadero blur gausiano.. el parametro de opacidad no hace effect
	asquerosamente lento,

	"""
	import Image, ImageFilter, array #code ripped form cairo somewhere in the weird web
	ctx = video.cf.ctx

	im = ctx.get_group_target()
	w = im.get_width()
	h = im.get_height()
	#Cuidado con esto, si no convirtieron el frame de avisynth a rgba (rgb32) es posible que de errores.... para eso habria que checkear video.cf y el tipo de datos, pero no da
	im1 = Image.frombuffer("RGBA", (w,h ), im.get_data(), "raw", "RGBA", 0, 1)
	for i in xrange(int(pasos)):
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

def fBlur4(pasos=0, opacidad=0):
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
"""Si se desea cambiar el tipo de blur pueden hacerlo seteando la variable tipo_blur en tu clase FxsGroup
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
	GrupoInicio()
	if size > 0 :
		#recordar de setear el source ANTES de llamar
		ctx.set_matrix(extra.CrearMatriz(offx, offy))
		ctx.mask(pattern)
		ctx.identity_matrix()
		fBlur(size)
	ctx.set_source(pattern)
	ctx.paint()
	op = 0.0
	if paint : op = 1.0

	return GrupoFin(opacidad=op)

def fDirBlur(angle=0, pasos=1,  opacidad=0.25):
	"""
		Blur Direccional
	opcionales:
	@angle=0 angulo en radianes de la dirección
	@pasos=1 cantidad de pixels y pasos que tendrá el blur
	@opacidad=0.25 opacidad de cada paso
	"""
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	#creamos un pattern porque parece q tiene un minimo overhead menor al surface además no tenemos el dilema del "al pintar d nuevo cambia el source con la pintada anterior"
	ctx.set_source(pat) #lo ponemos como source
	m = cairo.Matrix()#creamos una matriz de transformación para el pat
	xi = cos(angle)
	yi = sin(angle)

	for a in range(1, int(pasos+1)):
		m.translate(xi, yi)
		pat.set_matrix(m)
		ctx.paint_with_alpha(opacidad)

def fDirBlurB(angle=0, pasos=1, opacidad=0.25):
	"""blur direccional usando surface"""
	ctx = video.cf.ctx
	sfc=ctx.get_group_target()
	x= xi = cos(angle)
	y= yi = sin(angle)

	for a in range(1, pasos+1):
		ctx.set_source_surface(sfc,  x, y)
		ctx.paint_with_alpha(opacidad)
		x+=xi
		y+=yi

def fBiDirBlur(angle=0, pasos=1, opacidad=0.25):
	"""Blur bidireccional
	opcionales:
	opcionales:
	@angle=0 angulo en radianes de la dirección
	@pasos=1 cantidad de pixels y pasos que tendrá el blur
	@opacidad=0.25 opacidad de cada paso
	"""
	fDirBlur(angle, pasos, opacidad)
	fDirBlur(angle+pi, pasos, opacidad)

def fGlow(pasos=3, opacidad=0.05):
	"""
	Hace un effect de brillo
	opcionales:
	@pasos cantidad de pasos
	@opacidad opacidad de cada paso
	"""
	video.cf.ctx.set_operator(cairo.OPERATOR_ADD)
	fBlur(pasos, opacidad)
	ModePainted()

def GrupoInicio(copiarFondo=False):
	"""Comienza un grupo de pintado.
	es como un encapsulamiento
	todo lo que pintes dentro de un grupo no sera afectado por lo que tiene el de afuera.
	opcional
	@copiarFondo=False indica si el nuevo grupo contiene la informacion del grupo anterior
	"""
	if copiarFondo:
		ctx = video.cf.ctx
		#si esto da algun tipo de "error" (como cuando la textura se repite o si da error o algo raro)
		#activar la siguiente linea y comentar la otra
		sfc = extra.CopiarTarget() #esto es mas lento pero quizas de menos problemas
		#sfc = ctx.get_group_target()#esto es mas rapido pero puede traer problemas ademas no esta admitido legalemente por cairo, asi que se puede romper en cualquier momento
		ctx.push_group()
		ctx.set_source_surface(sfc, 0, 0)
		ctx.paint()
	else:
		video.cf.ctx.push_group()

def GrupoFin(opacidad=1.0, matriz=None):
	"""
	Finaliza un grupo,
	opcionales:
	@paint Indica si al finalizar el grupo se pinta el contenido
	@matriz Matriz del tipo cairo.matrix con la transformacion sobre el grupo anterior
	@return devuelve un pattern con el resultado del grupo
	"""
	ctx= video.cf.ctx
	pat= ctx.pop_group()
	if matriz:
		pat.set_matrix(matriz)
	#if opacidad>0:
	ctx.set_source(pat)
	ctx.paint_with_alpha(opacidad)
	return pat

"""
#todo probar esto pero usando  extra.CopiarTarget
_time_blur_pat = None
def fTimeBlur(opacidad=0.15):
	global _time_blur_pat
	ctx = video.cf.ctx
	if _time_blur_pat:
		ctx.set_source_surface(_time_blur_pat)
		ctx.paint_with_alpha(opacidad)
	_time_blur_pat = ctx.get_group_target()
"""

def fRotoZoom(pasos=4, opacidad=0.25, escala=1, angle=0, org_x=0, org_y=0):
	"""Realiza un effect de rotacion y zoom progresivos sobre todo el contenido del cuadro
	@pasos : cantidad de pasos
	@opacidad : opacidad de cada paso
	@escala : incremento de escala por paso
	@angle : incremento del ángulo por paso, en radianes
	@org_x, org_y : el origen sobre el que se realizan las transformaciones
	"""
	ctx = video.cf.ctx
	sfc = ctx.get_group_target()
	pat = cairo.SurfacePattern(sfc)
	#creamos un pattern porque parece q tiene un minimo overhead menor al surface además no tenemos el dilema del "al pintar d nuevo cambia el source con la pintada anterior"
	ctx.set_source(pat) #lo ponemos como source
	fangle = angle

	for a in xrange(int(pasos)):
		fescala = 1.0/(1.0+(a*escala)) #1/a*2
		fangle += angle
		pat.set_matrix(
			extra.CrearMatriz(org_x, org_y, org_x, org_y, fangle, fescala, fescala, inversa=True)
		)
		ctx.paint_with_alpha(opacidad)

def fOnda( inicio,  delta=0.1,  amplitud = 10,  vertical=True,  borrar=True):
	"""Realiza un effect de ondulacion sobre la imagen activa.
	@inicio : un offset del angle de inicio (si se quiere animar esto se debe modificar)
	@delta = 0.1 : el delta que indica cuanto cambiará la onda de pixel a pixel (es como el ancho de la onda (en vertical)) (mientras mas pequeño, la onda es mas ancha) (esto es lo mismo que frecuencia)
	@amplitud = 10 : cuan fuerte es la deformacion (el alto de la onda (en vertical))
	@vertical = True : True si se quiere hacer una onda vertical, False si se la quiere horizontal
	@borrar = True : True si se desea eliminar lo dibujado anteriormente, o False si se desea redibujar lo deformado encima de lo anterior
	"""
	ctx = video.cf.ctx
	vi = video.vi

	sfc = extra.CopiarTarget()

	if borrar:
		ctx.set_operator(cairo.OPERATOR_CLEAR)
		ctx.paint()
		ModePainted()

	x1,  x2,  y1,  y2 = 0,  vi.width,  0,  vi.height
	if vertical :
		alto = y2
		ancho = 1
		min = x1
		max = x2
	else:
		alto = 1
		ancho = x2
		min = y1
		max = y2

	for i in xrange(min,  max):
		dif = delta*(i+inicio)
		if vertical:
			x1 = i
			mx = 0
			my =  sin(pi*dif)*amplitud
		else:
			y1 = i
			mx = sin(pi*dif)*amplitud
			my = 0

		ctx.set_source_surface(sfc,  mx,  my)
		ctx.rectangle(x1, y1, ancho,  alto)
		ctx.fill()

class cSprite():
	#Implementación basica de una imagen estática
	#Para animar cambien las propiedades
	def __init__(self, text=None, x = 0, y = 0, angle=0, color=None, mode=1, escala=1.0):
		"""
		@text : pattern que se usará como textura
			(se puede cargar con extra.CargarTextura("archivo.png") o simplemente pasar el nombre de archivo "archivo.png")
		@mode =1: 1-> textura solida, 0-> un solo color y mascara
		@center =False: If true, then the sprite will be moved to be centered at the x/y (works better with squared textures)
		"""
		if text == None:
			text = cairo.SurfacePattern(cairo.ImageSurface.create_from_png("texturas/sakura.png"))
		text.set_extend(cairo.EXTEND_NONE)
		self._pat = text
		self._s = text.get_surface()

		self._ancho = (self._s.get_width())
		self._alto = (self._s.get_height())
		self.org_x = (self._ancho/2.0)
		self.org_y = (self._alto/2.0)
		self.angle = angle
		self.color = color or extra.cCairoColor()
		self.mode = mode
		self.x = x
		self.y = y
		self.Escalar(escala, escala)

	def Escalar(self, x, y):
		"""se puede hacer directamente accediendo a scale_x y scale_y,
		pero esta para facilitar el tema de la division,
		si usás escalas predivididas, es más rápido asignarlas directamente a scale_x y scale_y"""
		self.scale_x = 1.0/(x or 1.0)
		self.scale_y = 1.0/(y or 1.0)

	def Paint(self):
		"""Pinta la imagen sobre el cuadro según las propiedades
		"""
		"""mat = cairo.Matrix()
		mat.translate(self.org_x, self.org_y)
		mat.rotate(self.angle)
		mat.scale(self.sx, self.sy)
		mat.translate(-self.x, -self.y)
		self.pat.set_matrix(mat)"""

		self._pat.set_matrix(extra.CrearMatriz(self.x, self.y, self.org_x, self.org_y, self.angle, self.scale_x, self.scale_y, True))
		ctx = video.cf.ctx
		if self.mode:
			ctx.set_source(self._pat)
			ctx.paint_with_alpha(self.color.a)
		else:
			ctx.set_source_rgba(self.color.r, self.color.g, self.color.b, self.color.a)
			ctx.mask(self._pat)

class cParticleSystem():
	class cEmisor():
		x = y = angle = vel = mapertura = xg = yg = mw = mh = 0.0

	class cParticula():
		def __init__(self, i=0):
			self.indice = i
			self.Reset()

		def Reset(self, activa=False, x=300, y=300, life=1, color=None, xi=0, yi=0, sc1=1, sc2=1, xg=0, yg=0, rotacion=0.1):
			"""Llamado por el sistema de particulas para "crear" una particula nueva"""
			self.activa = activa #indica si la particula está activa o muerta
			self.life = 0 #indica cuanta vida tiene (como el progress d 0 a 1) (1=muerta)
			self.escala = sc1
			self.fade = ((random()/10)+0.1) /life
			#esto indica la velocidad con que muere, al tener /life ahi, el valor de esa variable, puede ser sumada a life y life pasa a funcionar como el progress de los dialogues..
			#aumentando el valor de life aumenta la cantidad d animaciones requeridas para morir.
			#considerable como "paso" de animacion (step)

			self.color = color

			#posicion
			self.x = x
			self.y = y
			#incremento de las posiciones (aka velocidad+direccion)
			self.xi = xi
			self.yi = yi

			#angle
			self.angle = random()*2*pi
			#incremento del angle aka animacion de la rotacon
			self.anglei = random()*rotacion
			#incremento de la escala.
			self.sci = (sc2-sc1)*self.fade
			#gravedad
			self.xg = xg
			self.yg = yg

		def AnimadorBase(self):
			"""Animador default
			  puedes llamar a este animador para que haga las cosas normales, movimiento, rotacion, escala
			  tambien podes definir el tuyo y pasarlo por parametro al instanciar el sistema de particulas
			  asegurate de modificar el valor de activa
			"""
			self.angle += self.anglei
			self.y += self.yi
			self.x += self.xi
			self.escala += self.sci
			self.color.a -= self.fade
			self.xi += self.xg
			self.yi += self.yg
			self.life += self.fade
			self.activa = (self.life<1) #mas rapido (??) acuerdense que aca adentro estamos si p.active == True

	def __init__(self, png="texturas/blast.png", emitir_parts=5, max_parts=500, max_life=2, mode=None, color=None, escala_de=1.0, escala_a=2.0, rotacion= 0.1, animador=None):
		"""
		todos los valores son opcionales

		png archivo png usado como textura/mascara
		max_parts total de particulas posibles en todo momento
		emitir_parts maxima cantidad de particulas que se crearan por vez que se llama a Emitir
		color = None -> Color random, o instancia de cCairoColor
		max_life entero con el máximo de vida de cada particula
		mode = 0-> textura, 1->mascara con color solido, 2-> mascara tomando el color del punto sobre el que cae
			Para mejor funcionamiento, no especificar color si se usará el mode 0
		escala_de valor de escala inical para cada particula
		escala_a valor de escala final para cada particula
		animador una función que se llama por cada particula, por cada cuadro, que recibe como parametro la particula en cuestion
		"""
		self.parts = [self.cParticula(i=i) for i in xrange(max_parts)]
		self.ppc = emitir_parts
		self.life = max_life or 1 #0 daría ZeroDivide en part.Reset
		if mode == None:
			if color == None:
				mode = 0
			else:
				mode = 1

		self.mode = mode
		self.color = color
		self.sfc = cairo.ImageSurface.create_from_png(png)

		#predividimos por 1.0 para mayor velocidad.
		self.sc1 = 1.0/escala_de
		self.sc2 = 1.0/escala_a
		self.pat = cairo.SurfacePattern(self.sfc)
		self.centx = (self.sfc.get_width()/2)
		self.centy = (self.sfc.get_height()/2)
		self.w = self.sfc.get_width()
		self.h = self.sfc.get_height()
		self.anglei = rotacion
		self.emisor = self.cEmisor()
		self.Animar = animador or self.cParticula.AnimadorBase
		#notar q hacemos referencia a AnimadorBase de la CLASE cParticula, no de una INSTANCIA, por lo q hay q poner explicitamente el primer parámetro
		#con esto y la liena self.Animar(p) solucionamos problemas del "self" (q psicoloco q suena)

	def Emit(self):
		"""Cuando se llama a esta función se le indica al sistema se emiten particulas
		Cada vez que se llama, se crearán un máximo de "emitir_parts".
		Se lo puede llamar varias veces en el mismo cuadro,
		cambiando las propiedades del emisor entre las diferentes llamadas
		"""
		newparts = 0
		e=self.emisor
		for p in self.parts:
			if newparts > self.ppc: return
			if not p.activa:
				x = -(e.x + ((random()*e.mw*2)- e.mw))
				y = -(e.y + ((random()*e.mh*2)- e.mh))
				if self.color:
					c = extra.cCairoColor(ccolor=self.color)
				else:
					c = extra.cCairoColor()
					if self.mode==2:
						im = video.cf.ctx.get_group_target()
						stride = im.get_stride() #Normalmente es w*4 (4 bytes por pixels)
						#El tipo de esto es un buffer, altamente eficiente (supuestamente) es como un vector de c
						pixels = im.get_data()
						pos = -((int(y))*stride) + ((int(x))*4)
						#el int por separado es porque la "alineacion" es importante si el numero es flotante, la pos nos puede dar en medio de los 4bytes
						#el - es porque las coordenadas estan invertidas
						try:
							b,g,r,a = map(ord, pixels[pos:pos+4])
						except:
							b=g=r=a = 0
						#c.a = a/256.0
						c.r = r/256.0
						c.g = g/256.0
						c.b = b/256.0
					else:
						c.r = random()
						c.g = random()
						c.b = random()
						c.a = 1
				xi = -cos(e.angle+e.mapertura-(e.mapertura*2.0*random()))*e.vel
				yi = sin(e.angle+e.mapertura-(e.mapertura*2.0*random()))*e.vel
				p.Reset(True, x=x, y=y, life=self.life, color=c, xi=xi, yi=yi,
					sc1=self.sc1, sc2=self.sc2, xg=e.xg, yg=e.yg, rotacion=self.anglei)
				newparts+=1

	def SetPosition(self, x, y):
		"""Para cambiar la posicion del emisor
		@x, y : Posición en pixels"""
		self.emisor.x=x
		self.emisor.y=y

	def SetAngle(self, angle, velocidad, apertura=0):
		"""Para cambiar el angle de emision
		@angle : el ángulo en radianes de la emisión
		@velocidad : la velocidad de la emisión, en pixels por cuadro
		@apertura : angulo en radianes para el ángulo de apertura máxima de emisión"""
		e = self.emisor
		e.angle = angle
		e.vel = velocidad
		e.mapertura = apertura/2.0

	def SetGravity(self, angle, velocidad ):
		"""para cambiar la gravedad del sistema de partículas
		@angle : angulo en radianes de la gravedad
		@velocidad : la velocidad de ACELEARCION de la gravedad en pixels por cuadro
		"""
		self.emisor.xg = -cos(angle)*velocidad
		self.emisor.yg = sin(angle)*velocidad
		#para la gravedad si lo guardamos como coordenada.
		#porque no da para ir calculando el seno y eso cada cuadro,
		#además como que la gravedad no cambia igual python es tan versatil ;)
		#q si queres podes cambiarlo con part.emisor.xg=xxx

	def SetWindow(self, ancho, alto):
		"""para cambiar la ventana de creacion de particulas
		@ancho, alto : indican el tamaño de la ventana donde pueden aparecer
		partículas
		"""
		self.emisor.mw = ancho/2.0
		self.emisor.mh = alto/2.0

	def Paint(self):
		"""Cada vez que se llama a esta funcion se pintan todas las particulas vivas, se calcula su nueva posicion, y si estan vivas
		o no.
		Se crean particulas nuevas si se llamó a Emitir
		"""
		ctx = video.cf.ctx
		for p in self.parts: #Por cada particula
			if p.activa:#Si está viva
				mat = cairo.Matrix()
				mat.translate(self.centx, self.centy)
				mat.rotate(p.angle)
				mat.scale(p.escala, p.escala)
				mat.translate(p.x, p.y)
				self.pat.set_matrix(mat)

				"""
				#PAra crear una matriz para un pattern ha de ser una matriz inversa... es mucho mas lenta sobretodo
				#porque hay que andar dividiendo el scale por 1
				#Además para velocidad, x,y , xi, yi están premultiplicados por -1 (o sea, cambiados de signos)
				#eso se hace una sola vez al crear la particula
				self.pat.set_matrix(
					extra.CrearMatriz( p.x, p.y, self.centx, self.centy, p.angle, p.escala, p.escala, True)
				)"""
				if self.mode:
					ctx.set_source_rgba(p.color.r, p.color.g, p.color.b, p.color.a)
					ctx.mask(self.pat)
				else:
					ctx.set_source(self.pat)
					ctx.paint_with_alpha(p.color.a)
				#Este es el animador de la particula, puede ser uno personalizado
				self.Animar(p)

def CrearParticulas(box, textura, escala=1.0, alpha_min=0.2, barrido_vertical=True, mode=0 ):
		"""Super Lento
		parametros:
		@box -> tupla con las coordenadas de donde buscar (x0, y0, ancho, alto) (todos los items DEBEN ser enteros (int)))
		@textura -> pattern que se usará como textura
		opcionales:
		@escala=1.0 -> escala con la que se inicializarán todas las texturas
		@alpha_min=0.2 -> cualquier pixel que contenga un alpha menor a ese valor será ignorado (por lo tanto no generará partícula) (es de 0 a 255)
		@barrido_vertical=True -> True o False, indica si el barrido de pixels será vertical (True) u horizontal (False) esto influye en el orden en que serán creadas
				las partículas en el array, por lo tanto la forma en que se recorre
		@mode=0 -> el mode de las particulas
		"""

		#creamos un array de particulas
		parts = []

		#obtenemos el contenido del grupo, y sus datos
		im = video.cf.ctx.get_group_target()

		#estos no los necesito
		width = im.get_width()
		height = im.get_height()
		if hasattr(im, 'get_stride'):
			stride = im.get_stride() #Normalmente es w*4 (4 bytes por pixels)
			#esto esta mas que nada para soportar el raro caso en que el stride sea
			#mayor al w*4 , porque si usaramos 3 bytes por pixel, fallaria horriblemente
		else:
			stride = video.vi.width* 4


		#El tipo de esto es un buffer, altamente eficiente (supuestamente) es como un vector de c
		pixels = im.get_data()
		#obtenemos el bounding box, y lo convertimos a todos a enteros
		x1, y1, x2, y2 = box

		#Haciendo esta cochinada evitamos usar una funcion extra, esperemos que sea mas rapido asi.
		if barrido_vertical:
			i1, i2 = x1, x2
			j1, j2 = y1, y2
		else:
			i1, i2 = y1, y2
			j1, j2 = x1, x2

		#recorremos lo pixels
		for i in xrange(i1, i2):
			for j in xrange(j1, j2):
				if barrido_vertical:
					x = i
					y = j
				else:
					y = i
					x = j
				#si el stdout dice que faltan mas valores para unpack, entonces hay que cambiar el > por >=
				if x <0 or x>=width:
					continue
				if y <0 or y>=height:
					continue

				pos = (y*stride) + (x*4)

				try:#la posicion puede estar fuera de rango.
					#obtenemos el pixel
					#OJO, me entere que si el micro es BigEnding o SmallEnding (byte shit) el orden cambia

					b, g, r, a = map(extra.D1, map(ord, pixels[pos:pos+4]))
					"""
					para demultiplicar .. (algo que parece inservible dentro de cairo)
					b,g,r,a = map(extra.d1, extra.DemultiplicarAlpha(*map(ord, pixels[pos:pos+4])))
					b,g,r,a = map(extra.d2, extra.DemultiplicarAlpha(*map(ord, pixels[pos:pos+4])))
					"""
					#ignoramos pixels con menos opacidad que la pedida
					if a<(alpha_min): continue

					#Creamos un color con los datos
					c = extra.cCairoColor()
					c.r = r
					c.a = a
					c.g = g
					c.b = b
					#y creamos una "particula"
					parts.append(cSprite(text= textura, x=x+0.5, y=y+0.5, escala=escala, color=c, mode=mode))
				except:
					import traceback
					print "Error al crear las particulas", traceback.print_exc()
		return parts
