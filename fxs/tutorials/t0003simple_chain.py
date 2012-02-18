# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
vil copia del tuto de nande! pero a mi estilo xD
"""


from libs import common

class FX1(common.Fx):

	def DialogoQueEntra(self, s, p):
		#here all the fxs for the dialoguein
		s.progress = p
		s.Fade(0, 1)
		s.Paint()

	def OnDialogueIn(self, d):
		#and here we give it the time using a chain
		d.Chain(self.DialogoQueEntra, duration=150)



	def DialogoQueSale(self, s, p):
		#same as before, effects
		s.progress = p
		s.Fade(1, 0)
		s.Paint()

	def OnDialogueOut(self, d):
		#and so here, chain
		d.Chain(self.DialogoQueSale, duration=40)


	def OnDialogue(self, d):
		#dialogue for the lulz
		d.Paint()



class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(),)
		self.in_ms = 300 #duración entrada del diálogo
		self.out_ms = 300 #duración salida del diálogo

