# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos


t3 = extra.CargarTextura('texturas/barra4.png', extend=cairo.EXTEND_REFLECT) #entrada

class FX1(comun.Fx):


	def EnDialogo(self, d):
		d.MoverDe((0+(comun.Interpolate(d.progress, (random.randint(10, 10)),0, comun.i_b_backstart))) ,(0))
		global t3#, t2
		#d.texturas[d.PART_FILL] = t2
		#d.actual.modo_fill = d.P_TEXTURA
		avanzado.GrupoInicio()
		d.Paint()
		texto = avanzado.GrupoFin(0)
		avanzado.GrupoInicio()
		d.texturas[d.PART_FILL] = t3
		d.actual.modo_fill = d.P_TEXTURA
		d.MoverTextura( comun.Interpolate(d.progress,-3480, 3480) , 50, part = d.PART_FILL)
		d.texturas[d.PART_BORDER] = t3
		d.actual.modo_border = d.P_TEXTURA
		d.MoverTextura( comun.Interpolate(d.progress,-3480, 3480) , 50, part = d.PART_BORDER)
		d.Paint()
		mascara = avanzado.GrupoFin(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(mascara)





class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#self.in_ms = 400
		#self.out_ms = 400
		self.fxs = (FX1(), FX1())