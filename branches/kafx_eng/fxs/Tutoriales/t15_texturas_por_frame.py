# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""

from libs import comun, video
from libs.draw import avanzado, extra

import random, cairo
from math import pi, sin, cos


textura1 = extra.CargarTextura('texturas/blanco3.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.CargarTextura('texturas/violeta1.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.CargarTextura('texturas/azul3.png', extend=cairo.EXTEND_REFLECT)



class FX1(comun.Fx):
	def EnDialogo(self, d):
		global textura6, textura5, textura3, textura4
		mitextura = comun.ElegirPorCuadro(0,91,textura1, textura1)
		mitextura = comun.ElegirPorCuadro(92,100,textura2, mitextura)
		mitextura = comun.ElegirPorCuadro(101,200,textura3, mitextura)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



class FxsGroup(comun.FxsGroup):
        def __init__(self):
			self.in_ms = 200
			self.out_ms = 200
			self.fxs = (FX1(),)