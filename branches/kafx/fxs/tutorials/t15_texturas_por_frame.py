# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""

from libs import common, video
from libs.draw import advanced, extra

import random, cairo
from math import pi, sin, cos


textura1 = extra.LoadTexture('textures/blanco3.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.LoadTexture('textures/violeta1.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.LoadTexture('textures/azul3.png', extend=cairo.EXTEND_REFLECT)



class FX1(common.Fx):
	def EnDialogo(self, d):
		global textura6, textura5, textura3, textura4
		mitextura = common.ElegirPorCuadro(0,91,textura1, textura1)
		mitextura = common.ElegirPorCuadro(92,100,textura2, mitextura)
		mitextura = common.ElegirPorCuadro(101,200,textura3, mitextura)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



class FxsGroup(common.FxsGroup):
        def __init__(self):
			self.in_ms = 200
			self.out_ms = 200
			self.fxs = (FX1(),)