# -*- coding: utf-8 -*-
from libs import comun, formas
from libs.draw import extra


class Efecto():
	def __init__(self):
		self.forma = None

	def OnSyllableStarts(self, l):
		#creamos la forma aca apra copiar el estilo
		if not self.forma :
			l.actual.color1.CopyFrom(l.actual.color2)
			self.forma = extra.cVector(l.actual, figura= formas.SKULL1)

	def OnSyllableSleep(self, l):
		l.PaintWithCache()

	def OnSyllable(self, l):
		l.actual.color1.Interpolate(l.progress, l.actual.color2)
		l.Morph(self.forma)
		l.Paint()
	def OnSyllableOut(self, l):
		self.forma.actual.pos_x = comun.Interpolate(l.progress,l.original.pos_x, l.original.pos_x-50)
		self.forma.actual.pos_y = comun.Interpolate(l.progress,l.original.pos_y, l.original.pos_y-50)
		self.forma.Paint()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), comun.Fx(),comun.Fx())
		#no puedo crear dos efecto() porque intentaria crear dos mundos
		self.saltar_cuadros = False
		self.dividir_letras = True
		self.sil_out_ms = 200