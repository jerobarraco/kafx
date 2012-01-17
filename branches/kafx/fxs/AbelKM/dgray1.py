# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/d-gray-man-ed-1
"""
from libs import comun
from libs.draw import avanzado
from math import pi, sin

class FX1(comun.Fx):
	def EnSilaba(self, diag):
		diag.actual.scale_x = diag.actual.scale_y = 1+((sin(pi*diag.progreso))/10)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(6, 0.06)
		avanzado.GrupoFin()

	def EnSilabaMuerta(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.Pintar()


	def EnDialogoEntra(self, d):
		d.Desvanecer(0, 1)
		d.actual.modo_relleno = d.P_DEG_VERT
		d.MoverDe(-25, 0)
		d.Pintar()

	def EnDialogoSale(self, d):
		d.Desvanecer(1, 0)
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.MoverA(25, 0)
		d.Pintar()

	def EnSilabaDorm(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 700
		self.out_ms = 700
		self.fxs = (FX1(), FX1())