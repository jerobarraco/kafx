# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/d-gray-man-ed-1
"""
from libs import common
from libs.draw import advanced
from math import pi, sin

class FX1(common.Fx):
	def EnSilaba(self, diag):
		diag.actual.scale_x = diag.actual.scale_y = 1+((sin(pi*diag.progreso))/10)
		advanced.StartGroup()
		diag.Pintar()
		advanced.fGlow(6, 0.06)
		advanced.EndGroup()

	def EnSilabaMuerta(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.Pintar()


	def EnDialogoEntra(self, d):
		d.Fade(0, 1)
		d.actual.modo_relleno = d.P_DEG_VERT
		d.MoveFrom(-25, 0)
		d.Pintar()

	def EnDialogoSale(self, d):
		d.Fade(1, 0)
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.MoveTo(25, 0)
		d.Pintar()

	def EnSilabaDorm(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Pintar()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 700
		self.out_ms = 700
		self.fxs = (FX1(), FX1())