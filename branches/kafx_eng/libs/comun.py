# -*- coding: utf-8 -*-
"""
Módulo con funciones varias
teóricamente no dependen de nada raro como cairo o ass
"""
import math
import random

from libs import video

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def ClampB(x):
	"Recorta un número (entero) al rango entre 0 y 255"
	if x > 255: x = 255
	if x < 0: x = 0
	return x

def Clamp(num):
	"Recorta un número flotante al rango entre 0.0 y 1.0"
	if num < 0.0 : return 0.0
	if num > 1.0 : return 1.0
	return num

def ElegirPorCuadro(cuadro_ini, cuadro_fin, active, inactive=None ):
	"""frame_ini tiene el cuadro en que inicia
	frame_Fin el cuadro donde termina
	inactive es lo que devuelve cuando el cuadro actual no esta entre frame_ini ni frame_fin
	active es lo que te devuelve si estas dentro del frame
	ejemplo
	d.actual.pos_x = ElegirPorFrame(100, 200, 0, 20)
	esto hara que la posicion_x del dialogo sea 20 SOLAMENTE entre el frame 100 y el 200, y luego vuelva a 0
	tambien pueden usarse otros objetos como:
	d.actual.color1.CopyFrom(ElegirPorFrame(100, 400, d.actual.color2, d.actual.color3)
	"""

	if cuadro_ini <= video.cf.framen  <= cuadro_fin:
		return active
	else:
		return inactive #el else no es necesario pero es para que entiendas
	#tambien podria usar esto perque quedaria muy criptico, lo dejo para el lulz
	#return ( (cuadro_ini <= video.cf.framen) and active) or inactive

def Elegir(progress, vector):
	#Segun un progress (de 0.0 a 1.0) devuelve un item de un vector (array o lista) de elementos
	progress = Clamp(progress)#el clamp es importante sino dara access error
	l = len(vector)
	i = int(l*progress)
	if i == l: i = l-1
	return vector[i]

#funciones para interpolar
#dado un valor de 0-1 devuelven otro valor de 0-1, (algunas permiten otro rango de numeros
def i_lineal(p): return float(p)
def i_sin(p): return math.sin(math.pi*p)
def i_cos(p): return math.cos(math.pi*p)
#en caso de querer hacer cosas "circulares"
def i_full_sin(p): return math.sin(2*math.pi*p)
def i_full_cos(p): return math.cos(2*math.pi*p)

def i_accel(p): return math.sin(math.pi*p*0.5)**2 #pi/2 = 90º
def i_deccel(p): return 1-i_accel(p)
def i_rand(p): return random.random()
def i_log(p):
	#usar con cuidado, numeros menores a 1 da error
	return math.log((p*2)+1)

#http://www.the-art-of-web.com/css/timing-function/ <<
#esto es lo que yo queria hacer con beziers hace raaaaaaaaaaaaaaaaato pero no me daba
#los mismos resultados, igual la idea es hacerlo con splines, aunque creo que no vale la pena
def i_b_default(p):
	return PointBezier(p, 0, 0, 0.25, 0.1, 0.25, 1, 1, 1)[1]

def i_b_ease_in(p):
	return PointBezier(p, 0, 0, 0.42, 0.0, 1, 1, 1, 1)[1]

def i_b_ease_out(p):
	return PointBezier(p, 0, 0, 0, 0, 0.58, 1, 1, 1)[1]

def i_b_ease_in_out(p):
	return PointBezier(p, 0, 0, 0.42, 0.0, 0.58, 1, 1, 1)[1]

def i_b_cubic(p):
	return PointBezier(p, 0, 0, 0, 1.0, 1.0, 0, 1, 1)[1]

def i_b_backstart(p):
	return PointBezier(p, 0, 0,
		0.2, -0.3, 0.6, 0.26,
		1, 1)[1]

def i_b_boing(p):
	return PointBezier(p,
	0, 0,
	0.42, 0.0,
	0.58, 1.5,
	1, 1
	)[1]

def Interpolate(progress, de, hasta, function=i_lineal):
	"""
	devuelve un número flotante entre 2 valores, el número devuelto corresponde a una cantidad indicada por el primer valor
	@progress indicador de que tan cerca del inico o fin debe estar el valor devuelto, debe ser un número entre 0 y 1 (aunque otros valores funcionan)
	@de valor inicial, o comienzo del rango
	@hasta valor final, o final del rango
	@funcion funcion personal que devuelva un valor entre 0 y 1 (siempre float) dado un valor de progress entre 0 y 1
	(puede usar las funciones que comienzan por i_)
	"""
	#http://es.wikipedia.org/wiki/Interpolación
	return (function(progress) * (hasta-de))+de

def LERP(progress, de, hasta):
	"""
	devuelve un número flotante entre 2 valores, el número devuelto corresponde a una cantidad indicada por el primer valor
	@progress indicador de que tan cerca del inico o fin debe estar el valor devuelto, debe ser un número entre 0 y 1 (aunque otros valores funcionan)
	@de valor inicial, o comienzo del rango
	@hasta valor final, o final del rango
	Esta funcion es lo mismo que interpolar lineal, pero un poco mas rapida,
	solo para funciones que requieran unicamente interpolacion lineal
	"""
	return de+(float(progress)*(hasta-de))

def RanmaBezier(progress, points):
	"""
	Devuelve un punto (x, y) sobre una curva bezier dado el avance en la misma
	Admite curvas biezer de cualquier orden
	@progress como en interpolar, normalmente un numero entre 0 y 1 indicando el avance de sobre la curva
	@points : array de points -> [ [0, 0], [1, 1], [2, 2] ]
	es como PointBezier pero permite curvas de cualquier cantidad de points de control (de 1 a (teoricamente) infinito))
	es algo mas lento que PointBezier para curvas de la misma cantidad de points
	escrito por Ranma42 @ irc.freenode.net/#cairo
	"""

	while len(points)>1:
		points2 = []
		for i in range(len(points) - 1):
			px0,py0 = points[i]
			px1,py1 = points[i+1]
			p = (Interpolate(progress, px0, px1), LERP(progress, py0, py1))
			points2.append(p)
		points = points2
	return points[0]

def PointBezier(progress, x_ini, y_ini,  x_int1, y_int1, x_int2, y_int2, x_fin, y_fin):
	"""
	Devuelve un punto (x, y) sobre una curva bezier dado el avance en la misma
	@x_ini, y_ini : punto inicial de la curva
	@x_int1, y_int1 : 1º punto de control de la curva
	@x_int2, y_int2 : 2º punto de control de la curva
	@x_fin, y_fin : punto final de la curva
	@progress : avance sobre la curva (0 a 1)
	Esta funcion es igual que Bezier pero es algo más rápida, además,
	Está limitada a:
	1 Punto de inicio
	2 points de control
	1 Punto final
	y todos los points son pasados por parámetro secuencialmente.
	#with help of ranma42!
	"""

	curvx1 = LERP(progress, x_ini, x_int1)
	curvx2 = LERP(progress, x_int1, x_int2)
	curvx3 = LERP(progress, x_int2, x_fin)

	curvx4 = LERP(progress, curvx1, curvx2)
	curvx5 = LERP(progress, curvx2, curvx3)

	curvx6 = LERP(progress, curvx4, curvx5)

	curvy1 = LERP(progress, y_ini, y_int1)
	curvy2 = LERP(progress, y_int1, y_int2)
	curvy3 = LERP(progress, y_int2, y_fin)

	curvy4 = LERP(progress, curvy1, curvy2)
	curvy5 = LERP(progress, curvy2, curvy3)

	curvy6 = LERP(progress, curvy4, curvy5)
	return curvx6, curvy6

def Encadenar(duracion, progress, objetos, function, tiempo=None):
	"""Realiza una animación en cadena.
	dado una duración maestra y un progress maestro aplicados a
	un array de objetos y un tiempo de animacion por objeto
	se calcula el progress para cada objeto y se llama a la funcion pasada por parametro para cada uno.

	La idea es poder animar sílabas según el diálogo, o letras según la sílaba,
	pero aun así lo pongo acá para que pueda ser usado de otras formas

	@duración Duración del tiempo maestro
	@progress float de rango 0 a 1 que dice el progress maestro
	@objetos array de objetos a ser animados en cadena.
		serán pasados a la función func. (sólo debe implementar len y ser iterables (string y array funcionan))

	@función debe ser una funcion
	será llamada progresivamente vez por cada objeto en orden de aparición con los siguientes parámetros:
		objeto, progress

	@tiempo define el tiempo que dura la animación de cada objeto
		si el tiempo es mayor a la duración/len(objetos)
		entonces las aniamciones se superpondran.
		si el tiempo es None (o no se especifica) las animaciones se dan
		una atrás de la otra, o sea el tiempo es = duración/len(objetos)
		si es menor no sé.
	"""
	duracion = float(duracion)
	slen = len(objetos)
	if slen == 0 : return
	tsil = duracion/slen#Tiempo por sílaba en progress constante

	if not tiempo:
		tiempo = tsil
	#El progress va a ser calculado de atrás para adelante. o sea, que terminen cuando les corresponda.
	#Pero van a empezar cuando convenga para ajustarse al tiempo de animación.

	#Cuanto del progress del diálogo le corresponde
	#a cada sílaba
	#Para eso el calculo de las sílabas debe ser secuencial y en orden
	finacum = tsil#Acumula los tiempos d fin (en que finaliza cada sílaba(respecto del diálogo))
	tactualdiag=(progress*duracion)
	for obj in objetos:
		tini = finacum - tiempo
		tactualsilaba = (tactualdiag - tini)
		if tactualsilaba <= 0:# No se anima aún (si es menor a 0 entonces tini es mayor que tactual)
			prog = 0.0
		elif tactualsilaba >= tiempo:#Si el tiempo en la sílaba es mayor al tiempo que tiene que estar
			prog = 1.0
		else:
			prog = tactualsilaba/tiempo

		function(obj, prog)#This is magic!
		finacum += tsil

def SafeGetFloat(dicc, prop, default=0.0):
	"""
	Devuelve una propiedad un diccionario convertido a float, o un valor default
	@dict diccionario
	@prop propiedad del diccionario a devolver
	@default opcional, valor por default 0.0, es el valor que se devolverá en caso de haber algun error al convertir la propiedad del diccionario
	"""
	try:
		return float(dicc[prop]) #porque en algunos lados se puede pasar algo que devuelve un string no valido como float, lo tenemos que poner dentro del try, así evitamos cosas
	except:
		return default

class FxsGroup():
	"""Clase de la que desciende un grupo de efectos"""

	"""
	Decidí pasar los elementos acá para para evitar tener que explicar el __init__ en las instancias
	me baso en esto:

	"All variables at the class method (irrespective of mutability -- lists and dicts are mutable) are shared.
	With immutable objects, the sharing isn't interesting. With mutable objects (lists and dicts) the sharing is significant.
	– S.Lott Oct 8 '09 at 11:58 @stackoverflow.com"


	el único problema sería con el array de fxs pero mientras no usen append o cosa así todo estará bien
	además que no van a crear dos instancias de un descendiente de FxsGroup al mismo tiempo
	"""
	in_ms = 0
	#Milisegundos para la animación de entrada
	out_ms = 0
	#MS para animación d salida
	sil_in_ms = 0
	#ms para la animación de entrada de cada sílaba sin animar (en el diálogo actual)
	sil_out_ms = 0
	#ms para la animación de cada sílaba muerta (en el diálogo actual)
	letra_in_ms = 0
	#ms para la animación de cada letra dormida (en la silaba actual)
	letra_out_ms = 0
	#ms para la animación de cada letra muerta (en la silaba actual)
	saltar_cuadros = True
	#Indica si vas a usar todos los cuadros del video, incluso aquellos en que no aparecen diálogos o sílabas.
	reset_estilo = True
	#esto indica si se resetea el estilo (se vuelve al original) tras cada cuadro para cada sílaba.
	dividir_letras = False
	#Esto indica si se van a dividir las letras de las silabas al cargar

	fxs = []
	#A diferencia de los anteriores ésta es la única propiedad que hay que definir sí o sí.
	#Esta propiedad contiene los diferentes efectos que harás. Por ejemplo, para un video si tenes una línea de kanjis,
	#una con la traducción y una con la letra; podés crear un efecto para cada tipo.

	tipo_blur = 0
	#Esto es para elegir el tipo de blur, es experimental y avanzado (y poco útil)

	def EnCuadroInicia(self):
		#Esto se ejecuta justo cuando empieza el cuadro. Antes que cualquier diálogo.
		pass

	def EnCuadroFin(self):
		#Esto se ejecuta al terminar el cuadro. Luego de todos los diálogos.
		pass

class Fx():
	"""Clase de la que desciende un efecto"""
	eventos = []
	#Un array con eventos personalizados, debe contener instancias de la clase Evento

	def EnDialogo(self, *args):
		pass
	def EnSilaba(self, *args):
		pass
	def EnLetra(self, *args):
		pass


	def EnSilabaMuerta(self, *args):
		pass
	def EnSilabaDorm(self, *args):
		#Sílaba dormida común (el progress es igual para todas las sílabas dormidas del mismo diálogo)
		pass

	#Hasta aca son las animaciones normales
	def EnDialogoEntra(self, *args):
		pass
	def EnSilabaEntra(self, *args):
		pass
	def EnLetraEntra(self, *args):
		pass

	def EnDialogoSale(self, *args):
		pass
	def EnSilabaSale(self, *args):
		pass
	def EnLetraSale(self, *args):
		pass

	def EnDialogoInicia(self, *args):
		pass
	def EnSilabaInicia(self, *args):
		pass
	def EnLetraInicia(self, *args):
		pass

class Evento():
	def EnSilaba(self, sil):
		pass
	def EnDialogo(self, diag):
		pass
	def EnLetra(self, let):
		pass

	def TiempoSilaba(self, sil):
		return (0, 0)
	def TiempoDialogo(self, diag):
		return (0, 0)
	def TiempoLetra(self, let):
		return (0, 0)


####Cosas mas bien internas

def MyImport(name):
	#función interna que uso para cargar un modulo a partir de un string separado por points, no recomiendo que lo usen
	mod = __import__(name)
	components = name.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod
