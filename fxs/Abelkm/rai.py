# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


textura1 = extra.LoadTexture('C:\Users\Riis\Videos\kafx\ONK\metala.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.LoadTexture('C:\Users\Riis\Videos\kafx\ONK\blanco3.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.LoadTexture('C:\Users\Riis\Videos\kafx\ONK\orange1.png', extend=cairo.EXTEND_REFLECT)


class FX1(common.Fx):



	def EnDialogo(self, d):
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1
		d.texturas[d.PART_RELLENO] = textura3
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = textura1
		d.actual.modo_borde = d.P_TEXTURA
		d.Pintar()

	def EnSilaba(self, sil):
		global textura3
		sil.actual.color3.a = 0
		sil.texturas[sil.PART_RELLENO] = textura3
		sil.actual.modo_relleno = sil.P_TEXTURA
		advanced.StartGroup()
		advanced.ModoPintado('overlay')
		sil.Pintar()
		advanced.fGlow(1, 0.1+(sin(pi*sil.progreso)/6.0))
		advanced.fRotoZoom(8, 0.3+(sin(pi*sil.progreso)/8.0),  0.015, 0, sil.actual.pos_x+(common.Interpolar(sil.progreso, -sil.actual.org_x*2,sil.actual.org_x*2)), sil.actual.pos_y)
		advanced.EndGroup(0.4)

	def EnSilabaDorm(self, d):
		global textura2
		d.actual.color3.a = 0
		d.texturas[d.PART_RELLENO] = textura2
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, diag):
		advanced.StartGroup()
		diag.Fade(1,0)
		diag.MoveTo(0, 20, common.i_accel)
		diag.Pintar()
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Fade(1,0)
		diag.MoveTo(0, 20, common.i_accel)
		diag.Pintar()


	def EnDialogoEntra(self, d):
		advanced.StartGroup()
		d.Fade(0,1)
		d.MoveFrom(0, 20, common.i_accel)
		d.Pintar()
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1, textura2
		d.texturas[d.PART_RELLENO] = textura3
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = textura1
		d.actual.modo_borde = d.P_TEXTURA
		d.Fade(0,1)
		d.MoveFrom(0, 20, common.i_accel)
		d.Pintar()
		d.actual.color3.a = 0
		d.texturas[d.PART_RELLENO] = textura2
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.color1.a = common.Interpolar(d.progreso,0, 1)
		d.MoveFrom(0, 20, common.i_accel)
		d.Pintar()




class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 350
		self.out_ms = 350
		self.fxs = (FX1(), FX1())