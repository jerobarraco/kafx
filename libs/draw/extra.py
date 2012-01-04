# -*- coding: utf-8 -*-
import cairo
from math import ceil
from random import random

from libs import video, comun
import basico, avanzado

"""
Este modulo contiene todas las funciones que no hacen directamente a dibujar algo,
Sino que son ayuda o comandos basicos para las demas funciones.
"""
global debugi
debugi=-1
#TODO: eliminar los __S* de cvetor y modificar el resto de los scripts
def DebugCairo(carpeta="caps/"):
	global debugi
	debugi+=1
	video.cf.ctx.get_group_target().write_to_png(carpeta+str(debugi).zfill(5)+'.png')

def CargarSecuencia(carpeta, cantidad, digitos=3, extend=cairo.EXTEND_REPEAT):
	"""Carga una secuencia de texturas
	@carpeta : indica la carpeta donde estan las imagenes, si todas las imagenes empiezan con un prefijo
	(pej: imgxxx.png) también incluyan ese prefijo (e incluyan la "/")

	@cantidad : la cantidad de cuadros (imagenes)
					(notar que la secuencia comienza desde 0 y termia en cantidad-1)

	@digitos : cantidad de digitos que tiene la secuencia

	@extend: el extend default de la textura (default EXTEND_REPEAT)
			Para usar con cSprite el extend debe ser cairo.EXTEND_NONE
	"""
	#Esta es la forma corta
	#para el que no conozca se llama list comprehension
	return [
		CargarTextura(carpeta + str(i).zfill(digitos) + '.png', extend)
		for i in range(cantidad)
		]

	#Esta es la forma explicada
	"""
	#donde almacenaremos las texturas
	texturas = []
	for i in range (cantidad):
		#creamos un nombre de archivo a partir del numero
		#convertimos el numero en string y lo rellenamos con 0's hasta la cantidad de digitos
		num = str(i).zfill(digitos)
		imgname = carpeta + num + '.png'
		text = CargarTextura(imgname, extend)
		texturas.append(text)
	return texturas"""

def CargarTextura(archivo, extend=cairo.EXTEND_REPEAT):
	"""Devuelve una textura (SurfacePattern) de cairo, a partir de un archivo png.
	Para usar con set_source o lo que fuere
	@archivo: el nombre del archivo. Debe ser un PNG.

	@extend: el extend default de la textura (default EXTEND_REPEAT)
			Para usar con cSprite el extend debe ser cairo.EXTEND_NONE"""
	t = cairo.SurfacePattern(cairo.ImageSurface.create_from_png(archivo))
	t.set_extend(extend)
	return t
	"""
	try:
		t = cairo.SurfacePattern(cairo.ImageSurface.create_from_png(archivo))
		t.set_extend(extend)
	except:
		print "No se pudo cargar la textura en el archivo:", archivo
	return t"""

def SetEstilo(estilo):
	"""Prepara cairo con los estilos
	Antes de dibujar un texto, se puede llamar a esta funcion para que ponga las cosas basicas
	el estilo tiene que ser del tipo asslib.cPropiedades
	(y debe ser el original ya que requiere propiedades no animables)
	"""
	ctx = video.cf.ctx
	ctx.select_font_face(estilo._fuente, int(estilo._italica),  int(estilo._negrita))
	ctx.set_font_size(estilo._size)

def CrearMatriz(pos_x=0, pos_y=0, org_x=0, org_y=0, angle=0, scale_x=1, scale_y=1, inversa=False):
	"""Crea una matriz segun las transformaciones comunes
	pos_x, pos_y posicion x/y final
	org_x, org_y el punto de origen de la transformación
	angle angulo en radianes
	scale_x scale_y la escala
	inversa = False indica si es una matriz inversa (para patrones (puede fallar)) o normal, para contexto
	en caso de ser una matriz inversa, los scales deben estar invertidos o sea, 1.0/escala"""
	m = cairo.Matrix()

	#Evitamos errores de matrices no invertibles a costo de velocidad
	if scale_x == 0: scale_x = 0.00001
	if scale_y == 0: scale_y = 0.00001

	if inversa:
		#esto no está testeado asique ojo, sobretodo con el ultimo translate. puede ir sumado (o restado) con org
		#el punto de origen para la POSICION en los dialogos no es el mismo que el punto de origen, y esta siempre en el baseline,
		#por eso mismo. hay que sumarle el origen, esto no es "deseable" en las particulas pej, donde quermos que estén centradas.
		m.translate(org_x, org_y)
		m.rotate(angle)
		m.scale(scale_x, scale_y)
		m.translate(-pos_x, -pos_y)
	else:
		#para arreglar el problema aca estuve como 1 semana, hasta q empecé a escribir un mail al cairo list
		#al tipear "parece que la rotacion se aplica _despues_ de la posicion" me acordé que esto tiene el concepto de "inversa"
		#y dije, el orden es importante, quizas eso tamb está invertido... y asi resulto esto...
		#recuerden lean la doc y piensen las cosas
		m.translate(pos_x, pos_y)
		m.scale(scale_x, scale_y)
		m.rotate(-angle)
		m.translate(-org_x, -org_y)
	return m

#Clases
class cCairoColor():
	"""Clase para ayudar con los colores sólidos"""
	def __init__(self, numero=None, texto='', ccolor=None):
		"""
		3 formas
		@numero creado como con DesdeNumero, recibe un entero (0xAARRGGBB)
		@texto creado como con DesdeTexto, recibe un string ('AARRGGBB')
		@ccolor creado como con CopyFrom, recibe un objeto del tipo cCairoColor
		"""
		if texto:
			self.DesdeTexto(texto)
		elif ccolor:
			self.CopyFrom(ccolor)
		elif (numero is not None):
			self.DesdeNumero(numero)
		else:
			self.r= self.g= self.b= self.a=1.0

	def Pattern(self):
		"""Devuelve un pattern de cairo para que uses como source o en funciones que requieran un patrón
		si lo vas a usar de source es posible tambien poner directamente
		video.cf.ctx.set_source_rgba(a.r, a.g, a.b, a.a)"""
		return cairo.SolidPattern(self.r, self.g, self.b, self.a)

	def DesdeTexto(self, color):
		"""Crea un color desde otro
		color puede ser '&HAARRGGBB' o 'AARRGGBB'
		"""
		if (color[0]=='&'): 		color = color[1:]
		if color[0].lower()=='h': 	color = color[1:]

		color.zfill(8)#rellenamos con 0 a la izq si por alguna razon faltan
		self.a = (255-ord(color[:2].decode('hex')))/255.0 #alfa,
		self.b = ord(color[2:4].decode('hex'))/255.0 #blue
		self.g = ord(color[4:6].decode('hex'))/255.0#green y lo movemos a la izq
		self.r = ord(color[6:8].decode('hex'))/255.0 #red

	def DesdeNumero(self,  color):
		"""Crea un color desde otro
		color debe ser un entero: 31238231 o 0xAARRGGBB"""
		self.b = (color & 0xFF) /255.0 #hacemos un and de 255 = b11111111 ,(o sea, tomamos los ocho bits)
		color >>= 8 #Lo movemos ocho bits
		self.g = (color & 0xFF) /255.0 #lo mesmo
		color >>= 8
		self.r = (color & 0xFF) /255.0
		color >>= 8
		self.a = color /255.0
		"""
		self.b = (color % 256)/255.0
		color = color / 256
		self.g = (color % 256)/255.0
		color = color /256
		self.r = (color % 256.0)/255.0
		color = color / 256
		self.a = color / 255.0"""

	def CopyFrom(self, other):
		"""Copia un color desde otro
		@otro debe ser un objeto del tipo cCairoColor
		"""
		self.r=other.r
		self.g=other.g
		self.b=other.b
		self.a=other.a

	def Interpolate(self, progress, other, inter=comun.i_lineal):
		"""Interpola un color con otro, segun un progress
		La interpolacion es lineal, asique no esperen algo de croma ni nada por el estilo.

		@progress : indicador de progress de la interpolacion, es un valor entre 0 y 1
		@other : el color al cual se interpolará
		"""
		i = comun.Interpolate
		self.r = i(progress, self.r, other.r, inter)
		self.g = i(progress, self.g, other.g, inter)
		self.b = i(progress, self.b, other.b, inter)
		self.a = i(progress, self.a, other.a, inter)

class cVector():
	"""Clase basica de objetos de cairo.
	Incluye las cosas basicas de pintado de cairo
	basicamente puede ser instanciada,
	pasandole @texto o @figura al instanciarlo o llamando luego a
	CambiarTexto o CrearDesdeFigura respectivamente
	"""
	#Tipos de pintado
	#Esto ha de corresponderse con basico.sources, definido acá para comodidad del user.
	P_SOLIDO = 0
	P_TEXTURA = 1
	P_DEG_VERT = 2
	P_DEG_HOR = 3
	P_DEG_DIAG = 4
	P_DEG_RAD = 5
	P_AN_DEG_LIN = 6
	P_AN_DEG_RAD = 7
	P_PATRON_COLOREADO = 8
	PART_BORDER = 0
	PART_FILL = 1
	PART_SHADOW = 2
	PART_PARTICULA = 3

	def __init__(self, estilo=None, texto='', figura=None, parent=None):
		"""Parametros
		@estilo objeto del tipo cPropiedades del cual heredar
		@texto crea un objeto desde un texto
		@figura lo crea desde una figura ass
		@parent el objeto padre
		"""
		from libs import asslib
		self.progress = 0.0
		self._end = 0
		self._start = 0
		self._dur = 0
		self._indice = 0
		self._parent = parent
		self.efecto = 0
		self.texturas = [None, None, None, None] #border, fill, shadow, particulas
		#Es la matriz de transformación del vector
		self.matrix = cairo.Matrix()

		self.original = asslib.cPropiedades(estilo)
		self.actual = asslib.cPropiedades(estilo)
		self._texto = ""
		self.pointsw = None

		if figura :
			self.CrearDesdeFigura(figura)
		elif texto:
			self.CambiarTexto(texto)
		else:
			self._old_path = self.path = None

		#el pattern usado por PaintWithCache, si se quiere reestablecer se puede proceder a borrar esta variable (asignandole None, nunca con "del _pat")
		self._pat_cache = None

	def _SetTextVertPos(self):
		"""Actualiza la posicion vertical segun la alineación
		es mejor llamar a _SetTextProps
		"""
		props = self.original
		vert = ceil(props._alin/3.0) # 1=bottom, 2=mid, 3=top
		if vert == 1 : #bottom
			props.pos_y = video.vi.height - props._marginv #- props._descent
		elif vert == 2: #middle
			props.pos_y = (video.vi.height - props._alto_linea )/2 #- props._descent
		else: #top
			props.pos_y = props._marginv -props._y_bearing #+ props._alto_linea #- props._y_bearing
		return

	def _SetTextHorizPos(self):
		"""Actualiza la posicion horizontal segun la alineacion
		es mejor llamar a _SetTextProps
		 1=bottom, 2=mid, 3=top
		"""
		props = self.original
		horiz = props._alin % 3 #1 = left, 2 mid, 0 right

		if horiz == 1:
			props.pos_x = props._marginl
		elif horiz == 2:
			props.pos_x = ((video.vi.width - props._ancho) / 2.0)
		else:
			props.pos_x = video.vi.width - props._ancho - props._marginr

		return
		"""if props.angle and not self._parent:
				props.pos_x, props.pos_y = self.matrix.transform_distance(props.pos_x, props.pos_y)"""


	def _SetTextProps(self, lasts=None):
		"""Setea las propiedades de un objeto segun el texto,
		usado para la primer vez que se crea el texto
		(mayormente posicion y tamaño)
		@lasts -> tupla (x, y) con la coordenada donde se inicia el texto.
		@return -> tupla (x, y) con la coordenada donde se iniciria el texto siguiente.

		"""
		ctx = video.cf.ctx
		props = self.original
		SetEstilo(props)

		props._x_bearing, props._y_bearing, props._ancho, props._alto, props._x_advance, props._y_advance = ctx.text_extents(self._texto)
		props._ascent, props._descent, props._alto_linea, props._max_x_advance, props._max_y_advance = ctx.font_extents()

		if lasts:
			props.pos_x = lasts[0]
			props.pos_y = lasts[1]
		else:
			self._SetTextHorizPos()
			self._SetTextVertPos()

		if self._parent and props.angle:
			#con el self.__parent evitamos modificar el dialogo
			#fix porque cuando el origen esta en otro lado, calcula para el orto
			#para arreglar el tema de las silabas a partir de un texto con angle
			props.org_x = 0
			props.org_y = 0
			#self._UpdateMatrix()
			#calculamos donde quedaría el xadvance y el yadvance segun la matriz de la silaba
			#ojo que esto podria traer problemas si las silabas tienen diferentes transformaciones que el dialogo
			#tambien se podria usar self._parent.matrix
			props._x_advance, props._y_advance = self._parent.matrix.transform_distance(props._x_advance, props._y_advance)
		else:
			props.org_x = (props._ancho/2.0)
			props.org_y = -(props._alto_linea/2.0) + props._descent

		self.actual.CopyAllFrom(props)
		return (props.pos_x + props._x_advance, props.pos_y + props._y_advance)

	def _SetPathProps(self):
		"""Pone las propiedades de un path.
		Llamar al cambiar el path, el path tiene que ser el path activo
		"""
		o = self.original
		e = video.cf.ctx.path_extents()#x1,y2,x2,y2
		o._ancho = e[2]-e[0]
		o._alto  = o._alto_linea = (e[3]-e[1])
		#el descent es casi como el e[1]
		o._x_bearing = e[0]
		o._y_bearing = e[1]

		o.org_x = o._x_bearing + (o._ancho/2.0)
		o.org_y = -(o._alto/2.0)
		self.actual.CopyAllFrom(o)

	def ObtenerForma(self):
		"""
		A partir del path activo, genera uno de esos strings de ass con una "forma"
		Algo asi 'm 13 13 13 31 b 31 31 13 31'
		esto es para zheo, saben que odio ass asi que no usen esto para nada util,
		lo dejo como ejemplo para que entiendan mas de ass y cairo
		"""
		#para entender un poco mas podes ver el Deformar que lo que hace es un FOR a traves de los points del path
		#Para saber como obtener un "path" fijate en UpdateTextPath, que hace un ctx.copy_path
		figura = ''
		lp = '' # ultimo punto, porque el vsfilter se mea en la cama.
		mapa = ['m ', 'l ', 'b ', 'c ']
		"""esta es la correspondencia (aproximada) entre el tipo de punto de cairo y el tipo en ass
			teniendo en cuenta que
			move_to = 0 = 'm'
			line_to = 1 = 'l'
			curve_to = 2 = 'b' #o 's'
			close_path = 3 = 'c'
		"""

		if self._old_path:#si no generaste el path estamos en problemas (no deberia pasar)
			for t, p in self._old_path:
				figura += lp #de esta manera obviamos el ultimo punto
				if t < 3:
					lp = mapa[t] #agregamos el tipo de punto
					for coord in p:
						lp += str(int(round(coord))) + ' '
					mapa[0] = 'n '
				else:
					lp = ''
					mapa[0] = 'm '

				"""#oldcode, incompatible con vsfilter :B pero compatible con el import de esto
				figura += mapa[t] #agregamos el tipo de punto
				for coord in p:
					figura += str(int(round(coord))) + ' '
				if t==0:#si el ultimo tipo fue un 'm' cambiamos el m a n
					mapa[0] = 'n '
				if t==3:#si el ultimo fue c, reseteamos a m
					mapa[0] = 'm '"""
		return figura


	def CrearDesdeFigura(self, ass):
		"""LENTO
		Crea el vector desde una figura del tipo ASS"""
		arr = ass.lower().split(' ')
		ctx = video.cf.ctx
		ctx_funcs = ( #Este map está hecho para mapear los tipos de item en el path con su funcion, para entonces poder construir "paths" a mano ya que no podemos modificarlo directamente.
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to,
			ctx.close_path
		)

		def get(a, i):
			#this function returns an array with the ammount of items in i, all parsed as float, if there aren't enough items in a, then it fills with 0
			return [ float(a.pop(0) if a else 0.0) for x in xrange(i)]

		ctx.new_path()
		t='m'

		while arr:
			if arr[0] in 'mnlbsc':
				t = arr.pop(0)
			if (t =='m') or (t=='n'):
				ctx_funcs[0](*get(arr , 2))
			elif t == 'l':
				ctx_funcs[1](*get(arr , 2))
			elif (t=='b') or (t=='s'):
				ctx_funcs[2](*get(arr , 6))
			elif t == 'c':
				ctx_funcs[3]()
			if t == 'm':
				ctx_funcs[3]()
		self._old_path = self.path = ctx.copy_path() #el setPropiedades resetea
		self._SetPathProps()

	def _UpdateMatrix(self):
		#updates the transformation matrix for the vector with the current style
		a = self.actual
		self.matrix = CrearMatriz(a.pos_x+a.org_x, a.pos_y-a.org_y, a.org_x, a.org_y, a.angle, a.scale_x, a.scale_y, False)

	def _UpdateTextPath(self):
		#Creates the path from a text, the style must be already set, position is ignored
		SetEstilo(self.original)
		ctx = video.cf.ctx
		ctx.new_path()
		ctx.text_path(self._texto)
		self._old_path = self.path = ctx.copy_path()

	def CambiarTexto(self, texto, last_pos=None):
		"""LENTO
		Cambia el texto de un vector
		@texto es el texto a usar
		para la recreacion del texto se usaran las propiedades almacenadas en ORIGINAL y se recalcularán todos los valores de posicion, etc
		opcionales:
		@last_pos=None tupla (x,y) con la posicion final de la silaba anterior (como lo devuelve esta misma funcion)"""
		self._texto = texto
		last = self._SetTextProps(last_pos)
		self._UpdateTextPath()
		return last #por las dudas si a algun tarado se le ocurre cambiar silabas, proveemos esto tamb.

	def Deformar(self, func):
		"""Deforma el vector del objeto,
		@func debe ser una funcion que sera llamada por cada grupo de de points del vector, debe recibir los siguientes parametros
		self : el dialogo sobre el que se efectua el deformar
		tipo : entero especificando el tipo de punto (0=mover, 1=linea, 2=curva, 3=cerrar path (esto sale de unas constantes de cairo que no recuerdo como se llaman))
		points : un array con points de longitud: 2 para mover, 2 para linea, 6 para curva, 0 para cerrar
		debe devolver un array con los points (o sea, lo mismo q recibio pero modificado)
		"""
		ctx = video.cf.ctx
		ctx_funcs = ( #Este map está hecho para mapear los tipos de item en el path con su funcion, para entonces poder construir "paths" a mano ya que no podemos modificarlo directamente.
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to
		)
		ctx.new_path()
		for t, p in self._old_path:
			if t<3:
				p = func(self, t, p)
				ctx_funcs[t](*p)
			else:
				ctx.close_path()
		self.path = ctx.copy_path()

	def DeformarCompleto(self, func):
		"""Igual que deformar pero recibe un solo objeto, con un array de tuplas como las recibiria deformar, y se espera que devuelva un solo array de tuplas
		Esto te permite mayor control sobre los points, pudiendo quitar o agregar points a placer.
		"""
		ctx = video.cf.ctx
		ctx_funcs = (
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to
		)
		ctx.new_path()

		for t, p in func(self, self._old_path):
			if t<3:
				ctx_funcs[t](*p)
			else:
				ctx.close_path()
		self.path = ctx.copy_path()

	def Restore(self):
		"""Restaura el estilo de un vector"""
		self.actual.CopyFrom(self.original)
		self.path = self._old_path

	def PaintWithCache(self, conFondo=False, matriz=None):
		"""Pinta un vector utilizando cache... notar que solo se crea la pintura la primera vez que se llama, luego se pintara lo cacheado
		opcionales:
		@conFondo=False Booleano indica si se pasa el fondo al texto (GrupoInicio con fondo)
		@matriz=None la matriz de transformacion para el GrupoFin
		"""
		if self._pat_cache :
			ctx = video.cf.ctx
			ctx.set_source(self._pat_cache)
			ctx.paint()
		else:
			self._pat_cache = self.Paint(conFondo, matriz)
		return self._pat_cache

	def BorrarCache(self):
		#Elimina el cache de pintura, trivial, para facilitarte la vida.
		self._pat_cache = None

	def Paint(self, conFondo=False, matriz=None, matriz2=None):
		"""Pinta un vector utilizando el estilo actual
		opcionales:
		@conFondo=False Booleano indica si se pasa el fondo al texto (GrupoInicio con fondo)
		@matriz=None la matriz de transformacion del VECTOR
		@matriz2=None la matriz de transformación del GrupoFin
		"""
		a = self.actual
		ctx = video.cf.ctx
		#empezamos un grupo por la shadow
		avanzado.GrupoInicio(conFondo)

		if matriz:
			#para permitir el uso de matrices personalizadas para hacer
			#unas transforamciones bien cochinas (como shear pej)
			self.matrix = matriz
		else:
			#y sino usamos una matriz creada a partir de las propiedades animables
			self._UpdateMatrix()

		ctx.set_matrix(self.matrix)
		#tambien está el ctx.transform, pero creo q eso va multiplicando las matrices (o sea, suma las distorciones)
		ctx.new_path()
		ctx.append_path(self.path)
		#border
		if a.border:
			#Si HAY border hacemos toda la maniobra (esto acelera las cosas en caso que no se quieran bordes)
			ctx.set_line_width(a.border)
			#Ponemos el source usando la funcion para sources
			#asignada al border y lo mismo haremos para el resto de las partes
			basico.sources[a.mode_border](self, a.color3, 0)
			#self.__SBorder(self, a.color3, 0)
			ctx.stroke_preserve()

		#fill
		basico.sources[a.mode_fill](self, a.color1, 1)
		#self.__SFill(self, a.color1, 1)
		ctx.fill()

		#finalizamos el grupo y aplicamos la 2º matriz
		#notar que la 2º matriz se afecta ya sobre el pattern, o sea,
		#sobre el raster y no sobre el vector, eso trae consecuencias
		pat = avanzado.GrupoFin(0.0, matriz2)

		#shadow. notar que la cargamos antes de restaurar la matriz identidad,
		#para q sea concordante en caso de no ser solida, y que los points de control no sean un caso y sean iguales en todos los casos (border/fill)
		basico.sources[a.mode_shadow](self, a.color4, 2)
		#self.__SShadow(self, a.color4, 2)

		#Devolvemos el patron con la shadow integrada
		pat =  avanzado.Shadow(pat, a.shadow, a.shad_x, a.shad_y)
		ctx.identity_matrix()
		return pat

	def PaintReference(self, matriz=None):
		"""Pinta los points de referencia del vector, note que puede no estar sujeta a ciertas transformaciones"""
		ctx = video.cf.ctx
		if matriz:
			self.matrix = matriz
		else:
			self._UpdateMatrix()
		ctx.set_matrix(self.matrix)
		ctx.rectangle(*self.Box())
		#posicion
		"""x1, y1, x2, y2 = self.Box()
		#obtenemos los valores de ancho y alto
		x2 -= x1
		y2 -= y1
		ctx.rectangle(x1, y1, x2, y2)"""
		ctx.set_source_rgba(1,0,1,1)
		ctx.stroke()

		ctx.arc(0,0, 4, 0, 6.283)#Esto es posx/posy tamb el baseline del texto
		ctx.set_source_rgba(0,1,0,1)
		ctx.fill()

		#origen
		ctx.set_source_rgba(0,1,1, 1)
		a = self.actual
		ctx.arc(a.org_x, a.org_y, 3, 0, 6.283)
		#ctx.arc(self.actual.pos_x, self.actual.pos_y, 4, 0, 6.283)
		ctx.fill()
		ctx.identity_matrix ()

	def Box(self):
		"""Devuelve el bounding box como una tupla de 4 elementos (x0, y0, ancho, alto)
		relativo al punto 0,0 del vector, o sea el baseline
		Esto no es valido para paths deformados, en ese caso puede ser mejor usar ctx.path_extents
		"""
		o= self.original
		bord= self.actual.border
		#compatible con rectangle de cairo.....
		return (-o._x_bearing-bord, -o._alto-bord, o._x_bearing+o._ancho+(bord*2), o._alto+o._descent+(bord*2))
		#NO OLVIDAR QUE ES X, Y, ANCHO, ALTO

	def Centro(self):
		"""Devuelve el punto central de un vector relativo al punto de posicion"""
		"""o = self.original
		x = o._ancho/2.0
		props.org_y = -(props._alto_linea/2.0) + props._descent"""
		x = self.actual.pos_x +(self.original._ancho/2.0)
		y = self.actual.pos_y -(self.original._alto/2.0)
		return (x, y) #deberia cambiarlo para que use las cosas como en el box pero no se si da.

	def Mover(self, de, a, inter=comun.i_lineal):
		"""Anima el movimiento de posicion de un vector desde _de_ hasta _a_
		@de tupla (x,y)
		@a tupla (x,y)
		"""
		self.actual.pos_x = comun.Interpolate(self.progress, de[0], a[0], inter)
		self.actual.pos_y = comun.Interpolate(self.progress, de[1], a[1], inter)

	def MoverA(self, x, y, inter=comun.i_lineal):
		"""Anima el movimiento de un vector desde el punto indicado hasta su posicion original
		@x, y coordenada de punto inical relative to the original position
		"""
		org = self.original
		px = org.pos_x
		py = org.pos_y
		self.Mover( (px, py), (x+px, y+py), inter)

	def MoverDe(self, x, y, inter=comun.i_lineal):
		"""Anima el movimiento de un vector hasta el punto indicado desde su posicion original
		@x, y coordenada de punto final
		"""
		org = self.original
		px = org.pos_x
		py = org.pos_y
		self.Mover((px+x, py+y), (px, py), inter)

	def Desvanecer(self, desde, hasta, inter=comun.i_lineal):
		"""Anima el fade de un vector
		@desde float indicando el valor inicial
		@hasta float con el valor final
		ambos valores tienen un rango de 0 a 1
		"""
		self.Alpha(comun.Interpolate(self.progress, desde, hasta, inter))

	def Alpha(self, alpha):
		"""Especifica el alfa para todos los colores
		@alpha float con el valor del canal alfa, dentro del rango 0 a 1
		"""
		self.actual.color1.a = self.actual.color2.a = self.actual.color3.a = self.actual.color4.a = alpha

	def Girar(self, desde, hasta, inter=comun.i_lineal):
		"""Anima la rotacion de un vector
		@desde angle inical en radianes
		@hasta angle final en radianes
		"""
		self.actual.angle = comun.Interpolate(self.progress, desde, hasta, inter)

	def Escalar(self, desde, hasta, inter=comun.i_lineal):
		"""Anima el escalado de un vector
		@desde escala incial
		@hasa escala final
		ambos son float donde 1 es el valor normal >1 es mas grande y <1 es mas pequeño
		"""
		self.actual.scale_x = self.actual.scale_y = comun.Interpolate(self.progress, desde, hasta, inter)

	def Sacudir(self, amplitud=4):
		"""
		Anima la posición como un shake
		@amplitud = cantidad de pixels que se moverá
		"""
		self.actual.pos_x = self.original.pos_x + comun.Interpolate(self.progress, -amplitud, amplitud, comun.i_rand)
		self.actual.pos_y = self.original.pos_y +comun.Interpolate(self.progress, -amplitud, amplitud, comun.i_rand)

	def Wiggle(self, amplitud=4, frecuencia=2):
		"""
		Anima la posición como un movimiento entre points aleatorios
		@amplitud = cantidad de pixels que se moverá
		@frecuencia = cantidad de points a los que irá
		"""
		if self.pointsw == None:
			self.pointsw = []
			self.pointsw.append( (0, 0) )
			for i in range(frecuencia):
				randomx = comun.LERP(random(), -amplitud, amplitud)
				randomy = comun.LERP(random(), -amplitud, amplitud)
				self.pointsw.append( (randomx, randomy) )
				self.pointsw.append( (0, 0) )
		x, y = comun.RanmaBezier(self.progress, self.pointsw)
		self.actual.pos_x = self.original.pos_x +x
		self.actual.pos_y = self.original.pos_y +y
		return x, y

	def CargarTextura(self, archivo, part=PART_BORDER, extend=cairo.EXTEND_REPEAT):
		"""Esto carga la textura para todos los pintados, desde un archivo png
		@archivo path al archivo .png
		@part para que parte del texto se usará (0=border, 1=fill, 2=shadow, 3=particulas)
		(o usar .PART_BORDER .PART_FILL .PART_SHADOW o .PART_PARTICULAS)
		@extend tipo de extend de cairo default: cairo.EXTEND_REPEAT
		"""
		t = CargarTextura(archivo, extend)
		self.texturas[part] = t
		#esto es un fix para las texturas con otro extend.
		self.MoverTextura(pos_x = 0, pos_y=-self.original._ascent, part=part)
		a = self.actual
		o = self.original
		if part == self.PART_BORDER:
			o.mode_border = a.mode_border = self.P_TEXTURA
		elif part == self.PART_FILL:
			o.mode_fill = a.mode_fill = self.P_TEXTURA
		elif part == self.PART_SHADOW:
			o.mode_shadow = a.mode_shadow = self.P_TEXTURA
		elif part == self.PART_PARTICULA:
			o.mode_particula = a.mode_particula = self.P_TEXTURA

	def MoverTextura(self, pos_x, pos_y, org_x=0, org_y=0, angle=0, scale_x=1, scale_y=1, part=0):
		self.texturas[part].set_matrix(CrearMatriz(pos_x, pos_y, org_x, org_y, angle, scale_x, scale_y, inversa=True))

	def CrearParticulas(self, textura=None, escala=1.0, alpha_min=0.2, barrido_vertical=True, mode=0):
		"""Super Lento
		parametros:
		@textura -> pattern con la textura a usar
		opcionales:
		@escala=1.0 -> escala con la que se inicializarán todas las texturas
		@alpha_min=40 -> cualquier pixel que contenga un alpha menor a ese valor será ignorado (por lo tanto no generará partícula) (es de 0 a 255)
		@barrido_vertical=True -> True o False, indica si el barrido de pixels será vertical (True) u horizontal (False) esto influye en el orden en que serán creadas
		las partículas en el array, por lo tanto la forma en que se recorre
		@mode=0 -> el mode de las particulas
		"""
		if not textura:
			textura = self.texturas[3]

		#obtenemos el bounding box, y lo convertimos a todos a enteros
		x1, y1, x2, y2 = map(int, self.Box())
		a = self.actual
		#lo transportamos a las coordenadas absolutas (o relativas a la pantalla)
		x1 += int(a.pos_x-a.border)
		x2 += int(a.pos_x+a.border)
		y1 += int(a.pos_y-a.border)
		y2 += int(a.pos_y+a.border)

		box = (x1, y1, x2, y2)

		#Creamos un nuevo grupo para que no hayan cochinadas en el medio
		avanzado.GrupoInicio()
		#pintamos el vector/dialogo/silaba
		self.Paint()
		#creamos las particulas
		parts = avanzado.CrearParticulas(box, textura, escala, alpha_min, barrido_vertical, mode)
		avanzado.GrupoFin(opacidad=0.0)
		return parts

	def PaintReflection(self, alto = None):
		"""@alto : el alto en pixels para el degradado, o None para usar el default"""

		#cache
		posy = self.actual.pos_y
		alto_linea = self.original._alto_linea
		descent = self.original._descent
		alto = alto or self.original._alto

		avanzado.GrupoInicio()
		self.Paint()
		avanzado.fBlur()
		mt = CrearMatriz(org_y=posy-self.actual.org_y, pos_y=posy+alto_linea+descent, scale_y = -1)
		pat = avanzado.GrupoFin(0.0, matriz = mt)

		video.cf.ctx.set_source(pat)
		lineal = cairo.LinearGradient(0, posy+alto, 0, posy+(alto*2.0))
		lineal.add_color_stop_rgba(1, 0, 0, 0, 0)
		lineal.add_color_stop_rgba(0, 1, 1, 1, 1)
		video.cf.ctx.mask(lineal)

#los colores en cairo tiene alpha premultiplicado, en caso de necesitar demultiplicarlos pueden usar esto
#http://lists.freedesktop.org/archives/cairo/attachments/20050826/b24b464d/alpha_test.obj
def DemultiplicarAlpha(b,g,r,a):
	"""
	@b, g, r, a
	Todos los valores de 0 a 255"""
	r = Demult(r, a)
	g = Demult(g, a)
	b = Demult(b, a)
	return b, g, r, a

def D1(x):
	return x/255.0

def D2(x):
	return (x+0.5)/256.0

def Demult(x, a):
	from libs.comun import ClampB
	return ClampB( int( ((x*a)-1) /254 ) )

def DuplicarSurface(surface):
	vi = video.vi
	sfc2 = surface.create_similar(cairo.CONTENT_COLOR_ALPHA,  vi.width,  vi.height)
	ctx2 = cairo.Context(sfc2)
	ctx2.set_source_surface(surface)
	ctx2.set_operator(cairo.OPERATOR_SOURCE)
	ctx2.paint()
	return sfc2

def CopiarTarget():
	return DuplicarSurface(video.cf.ctx.get_group_target())
