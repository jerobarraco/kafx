# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


t3 = extra.LoadTexture('textures/barra4.png', extend=cairo.EXTEND_REFLECT) #entrada

class FX1(common.Fx):


	def EnDialogo(self, d):
		d.MoveFrom((0+(common.Interpolate(d.progress, (random.randint(10, 10)),0, common.i_b_backstart))) ,(0))
		global t3#, t2
		#d.textures[d.PART_FILL] = t2
		#d.actual.modo_fill = d.P_TEXTURE
#		avanzado.StartGroup()
#		d.Paint()
#		texto = avanzado.EndGroup(0)
#		avanzado.StartGroup()
		d.texturas[d.PART_FILL] = t3
		d.actual.mode_fill = d.P_TEXTURA
		d.MoveTexture( common.Interpolate(d.progress,-3480, 3480) , 50, part = d.PART_FILL)
		d.texturas[d.PART_BORDER] = t3
		d.actual.mode_border = d.P_TEXTURA
		d.MoveTexture( common.Interpolate(d.progress,-3480, 3480) , 50, part = d.PART_BORDER)
		d.Paint()
#		mascara = avanzado.EndGroup(0)
#		video.cf.ctx.set_source(mascara)
#		video.cf.ctx.mask(texto)





class FxsGroup(common.FxsGroup):
	def __init__(self):
		#self.in_ms = 400
		#self.out_ms = 400
		self.fxs = (FX1(), FX1())