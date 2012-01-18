# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""

from libs import comun
from libs.draw import avanzado, extra
from math import pi, sin

class FX1(comun.Fx):
	def EnDialogoEntra(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Fade(0, 1)
		d.Pintar()

	def EnSilabaDorm(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.PintarConCache()

	def EnSilabaInicia(self, d):
		d.LoadTexture('textures/green2.png', parte=d.PART_RELLENO)


	def EnSilabaMuerta(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Fade(1,  0.6)
		d.Pintar()

	def EnDialogoSale(self,  d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Fade(0.6,  0)
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fRotoZoom(6, 0.7*d.progreso,  0.01, 0, d.actual.pos_x+d.actual.org_x, d.actual.pos_y+d.actual.org_y)
		avanzado.EndGroup()

	def EnSilaba(self, d):
		d.MoveTexture( 120*d.progreso, 120*d.progreso, parte = d.PART_RELLENO)
		d.actual.modo_relleno = d.P_TEXTURA
		d.PintarConCache()
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fGlow(6, sin(pi*d.progreso)/11.0)
		avanzado.EndGroup()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 200
		self.out_ms = 350
		self.fxs = (FX1(),)
