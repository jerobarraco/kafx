# -*- coding: utf-8 -*-
#Importamos las funciones del KAFX~
from libs import comun
from math import cos, pi, sin

#Definimos un efecto
class Fx1(comun.Fx):
	def Char(self, c, prog):
		#Esta es la función que se llamará por cada silaba activa
		#ver EnSilaba

		#Como esta funcion es llamada por Encadenar, el progreso es un parametro
		#lo copiamos al progreso (no es necesario para este efecto pero tenganlo en cuenta)
		c.progress = prog
		#interpolamos los colores
		#Esto anima el color de relleno con el color secundario
		c.actual.color1.Interpolate(prog, c.original.color2)
		c.Paint()

	def EnSilaba(self, s):
		#Cuando la silaba está activa animamos sus caracteres con la
		#funcion self.Char (de ahi arriba),
		#como s._dur son frames, la duracion por char la pongo en cuadros (el 6 ese)
		#Esa duracion la podria obviar
		s.Encadenar(self.Char, 6)
		#Esta es la mejor forma de animar por caracteres (para principiantes)

	def EnDialogoInicia(self, d):
		#Cuando el dialogo inicia hacemos una lista con todos los caracteres de
		#todas las silabas
		d.chars = [] #copiamos los chars acá
		#por cada silaba
		for silaba in d._silabas:
			#computamos los caracteres
			silaba.DividirLetras()
			#y los metemos en el array de chars
			d.chars.extend(silaba._letras)

	def AnimacionEntrada(self, c, prog):
		#Esta animacion se llama cuando el DIALOGO entra
		#como es llamada por el Encadenar, nos pasa el caracter y el progreso
		#Al progreso lo copiamos aunque no es necesario
		c.progress = prog
		#hacemos un scale_y de -cos de 0 a 180º (vean la grafica para saber los valores :B)
		c.actual.scale_y = -cos(pi*prog)
		c.Paint()

	def EnDialogoEntra(self, d):
		#Cuando el dialogo entra
		"""
		#notar que llamamos a comun.Encadenar,
		si llamaramos a d.Encadenar eso encadenaria las silabas
		(aunque desde ahi podriamos llamar s.Encadenar pero me parece muy complejo
		para un ejemplo)
		el primer tiempo es la duracion total de la animacion (la puse en ms)
		luego va el progreso maestro (q es el progreso del dialogo)
		luego los objetos a encadenar (las letras q coleccionamos en el EnDialogoInicia)
		luego la funcion encargada de animar (self.AnimacionEntrada)
		luego el tiempo de animacion de cada objeto (caracter)
		como el tiempo total está en ms la duracion de cada caracter tamb la puse en ms
		"""
		comun.Encadenar(500, d.progress, d.chars, self.AnimacionEntrada, 100)

	def AnimacionSalida(self, c, prog):
		#Esta animacion se llama cuando el DIALOGO sale
		c.progress = prog
		c.actual.pos_y += sin(pi*prog)*30
		#Notar que para que el desvanecer (y demás funciones del c.) funcione bien
		#hay que copiar el progreso a c.progreso
		c.Desvanecer(1, 0)
		c.Paint()

	def EnDialogoSale(self, d):
		#lo mismo q la otra
		comun.Encadenar(500, d.progress, d.chars, self.AnimacionSalida, 100)

	def EnDialogo(self, d):
		d.Paint()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 300 #Milisegundos para la animacion de entrada
		self.out_ms = 300 #MS para animacion d salida
		self.sil_in_ms = 150 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#El segundo efecto es una instancia de comun.Fx q como está vacia no va a mostrar el otro efecto
		self.fxs = (Fx1(), comun.Fx())