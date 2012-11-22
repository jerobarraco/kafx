# -*- coding: utf-8 -*-

from libs import common

class FX1(common.Fx):
    def OnDialogue(self, d):
        #d.actual.color1.Interpolate(d.progress*4,  d.actual.color2, common.i_lincycle)
        d.Paint()



class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(), FX1())
