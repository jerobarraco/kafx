# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""

from libs import comun, video
from libs.draw import avanzado, extra

import random, cairo
from math import pi, sin, cos

colora = extra.cCairoColor(0xFFA90FBF)

colorb = extra.cCairoColor(0xFF0FBF2F)

colorc = extra.cCairoColor(0xFFEEF7A7)

#los colores son html con FF (alpha) adelante.
class FX1():

        def OnDialogue(self, d):
			global colora, colorb, colorc
			d.actual.mode_fill = d.P_DEG_VERT
			micolor = comun.ChooseByFrame(0,91,colora, colora)
			micolor = comun.ChooseByFrame(92,100,colorb, micolor)
			micolor = comun.ChooseByFrame(101,200,colorc, micolor)
			d.actual.color1.CopyFrom(micolor)
			d.Paint()


class FxsGroup(comun.FxsGroup):
        def __init__(self):
			self.fxs = (FX1(),)