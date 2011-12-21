# -*- coding: utf-8 -*-
from libs import comun
from math import pi, sin

class FX1(comun.Fx):
		#Entrada: sea por silabas y con fadein
		def EnSilabaEntra(self, s):
			s.Desvanecer(0, 1)#fadein
			s.Pintar()

		#Estatico: solo color
		#Las silabas que no son animadas las pintamos aparte
		def EnSilabaDorm(self, s):
			s.Pintar() #Tal cual como vienen

		#FX Sil: un escalado a 150 y que vuelva a 100
		#Las que se estan animando
		def EnSilaba(self, s):
			#La escala está dada por scale_x y scale_y, 1 = 100% , 0.5 = 50% , 1.5 = 150% , 2 = 200% se entiende? (-1 es como dado vuelta)
			#para que crezca y decrezca usaré la funcion sin, q vos le das un angulo entre 0 y 2*pi y va de 0 a 1 y de nuevo a 0 de forma bastante suave. (es un circulo)
			s.actual.scale_x = s.actual.scale_y = 1.5 * sin(2*pi*s.progreso)
			s.actual.color1.CopiarDe(s.original.color2)#Copiamos el color del color secundario
			s.Pintar()
		#Las que ya fueron animadas las pintamos con el otro color
		def EnSilabaMuerta(self, s):
			s.actual.color1.CopiarDe(s.original.color2)#Copiamos el color del color secundario
			s.Pintar()

		#Salida: un fadeout x silaba
		def EnSilabaSale(self, s):
			s.Desvanecer(1, 0)#fadeout
			s.Pintar()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 150 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#ponemos el FX1 dos veces porque el script ass default usa 2 efectos, asique los dos efectos serán iguaels
		self.fxs = (FX1(), FX1())

