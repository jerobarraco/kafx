# -*- coding: utf-8 -*-
from libs import common
from math import pi, sin

class FX1(common.Fx):
		#Entrada: sea por silabas y con fadein
		def OnDialogueIn(self, s):
			s.Fade(0, 1)#fadein
			s.Paint()

		#Estatico: solo color
		#Las silabas que no son animadas las pintamos aparte
		def OnSyllableSleep(self, s):
			s.Paint() #Tal cual como vienen

		#FX Sil: un escalado a 150 y que vuelva a 100
		#Las que se estan animando
		def OnSyllable(self, s):
			#La scale está dada por scale_x y scale_y, 1 = 100% , 0.5 = 50% , 1.5 = 150% , 2 = 200% se entiende? (-1 es como dado vuelta)
			#para que crezca y decrezca usaré la funcion sin, q vos le das un angulo entre 0 y 2*pi y va de 0 a 1 y de nuevo a 0 de forma bastante suave. (es un circulo)
			s.actual.scale_x = s.actual.scale_y = 0.5 * sin(pi*s.progress) + 1 # tambien se puede hacer asi: common.Interpolate(s.progress, 1, 1.5, common.i_sin)
			s.actual.color1.CopyFrom(s.original.color2)#Copiamos el color del color secundario
			s.Paint()
		#Las que ya fueron animadas las pintamos con el otro color
		def OnSyllableDead(self, s):
			s.actual.color1.CopyFrom(s.original.color2)#Copiamos el color del color secundario
			s.Paint()

		#Salida: un fadeout x silaba
		def OnDialogueOut(self, s):
			s.Fade(1, 0)#fadeout
			s.Paint()


class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 150 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#ponemos el FX1 dos veces porque el script ass default usa 2 efectos, asique los dos efectos serán iguaels
		self.fxs = (FX1(), FX1())

