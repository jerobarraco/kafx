# -*- coding: utf-8 -*-
from libs import common, figures
from libs.draw import extra

import kafx_main
class Efecto():
	def __init__(self):
		self.forma = None

	def OnDialogueStarts(self, l):
		#creamos la forma aca apra copiar el estilo
		#notar que lo guardamos en self. por eso hay UNa SOLA FORMA POR EFECTO (self es de effect)
		#por eso nos fijamos si ya la crearon

		if not self.forma :
			l.actual.color1.CopyFrom(l.actual.color2)
			self.forma = extra.cVector(l.actual, figure= figures.APPLE)

	def OnDialogue(self, l):
		l.PaintWithCache()

	def OnSyllable(self, l):
		l.actual.color1.Interpolate(l.progress, l.actual.color2)
		l.Paint()
	def OnDialogueOut(self, l):
		otroi = l._indice+1
		otrodiag = kafx_main.ass.dialogos[otroi]

		l.Morph(otrodiag)
		l.actual.pos_x= common.Interpolate(l.progress, l.actual.pos_x, otrodiag.actual.pos_x)
		l.actual.pos_y= common.Interpolate(l.progress, l.actual.pos_y, otrodiag.actual.pos_y)
		l.Paint()


class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), common.Fx(),common.Fx())
		#no puedo crear dos effect() porque intentaria crear dos mundos
		self.skip_frames= False
		self.split_letters = True
		self.out_ms = 300