# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
vil copia del tuto de nande! pero a mi estilo xD
"""


from libs import common

class FX1(common.Fx):

	def DialogoQueEntra(self, s, p):
		#acá se ponen todos los efectos de la entrada del diálogo
		s.progress = p
		s.Fade(0, 1)
		s.Paint()

	def OnDialogueIn(self, d):
		#acá se encadena y se le da una duración para cada sílaba entrante, así no se la de el kafx automáticamente
		d.Chain(self.DialogoQueEntra, duration=150)



	def DialogoQueSale(self, s, p):
		#lo mismo que antes, efectos
		s.progress = p
		s.Fade(1, 0)
		s.Paint()

	def OnDialogueOut(self, d):
		#acá también es lo mismo, encadenar y poner tiempo, sólo que con la salida del diálogo
		d.Chain(self.DialogoQueSale, duration=40)


	def OnDialogue(self, d):
		#diálogo for the lulz
		d.Paint()



class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(),)
		self.in_ms = 300 #duración entrada del diálogo
		self.out_ms = 300 #duración salida del diálogo

