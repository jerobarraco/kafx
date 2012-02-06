# -*- coding: utf-8 -*-
from libs import common, figures
from libs.draw import extra

import kafx_main
class Efecto():
	def __init__(self):
		self.forma = None

	def OnDialogue(self, l):
		l.PaintWithCache()

	def OnSyllable(self, l):
		l.actual.color1.Interpolate(l.progress, l.actual.color2)
		l.Paint()
	def deform(self, diag, path):
		points = list(path)#lo convertimos
		print points
		cant_max = len(points)/2.0
		cant= int(cant_max*diag.progress)
		topoints = points[:cant]
		topoints.extend(points[-cant:])
		return topoints
	def OnDialogueOut(self, l):
		l.CompleteDeform(self.deform)
		l.Paint()


class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), common.Fx(),common.Fx())
		#no puedo crear dos effect() porque intentaria crear dos mundos
		self.skip_frames= False
		self.split_letters = True
		self.out_ms = 300