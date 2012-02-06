# -*- coding: utf-8 -*-
from libs import common, figures
from libs.draw import extra


class Efecto():
	def __init__(self):
		self.forma = None

	def OnSyllableStarts(self, l):
		#creamos la forma aca apra copiar el estilo
		#notar que lo guardamos en self. por eso hay UNa SOLA FORMA POR EFECTO (self es de effect)
		#por eso nos fijamos si ya la crearon
		if not self.forma :
			l.actual.color1.CopyFrom(l.actual.color2)
			self.forma = extra.cVector(l.actual, figure= figures.APPLE)

	def OnSyllableSleep(self, l):
		l.PaintWithCache()
	def OnSyllable(self, l):
		l.actual.color1.Interpolate(l.progress, l.actual.color2)
		l.Morph(self.forma)
		l.Paint()
	def OnSyllableOut(self, l):
		self.forma.actual.pos_x = common.Interpolate(l.progress,l.original.pos_x, l.original.pos_x-50)
		self.forma.actual.pos_y = common.Interpolate(l.progress,l.original.pos_y, l.original.pos_y-50)
		self.forma.Paint()


class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), common.Fx(),common.Fx())
		#no puedo crear dos effect() porque intentaria crear dos mundos
		self.skip_frames= False
		self.split_letters = True
		self.syl_out_ms = 200
		self.letter_in_ms = 200
		self.letter_out_ms= 200