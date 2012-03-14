# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""


from libs import common

from libs.draw import advanced, extra

class FX1(common.Fx):


    def OnSyllable(self, d):
		advanced.StartGroup()
		d.MoveTo(10, 10)
		d.Paint()
		advanced.fTimeBlur(opacidad=0.60)
		advanced.EndGroup()




class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 500
		self.out_ms = 500
		self.fxs = (FX1(), FX1())
