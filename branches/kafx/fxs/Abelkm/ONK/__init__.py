# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos


textura1 = extra.CargarTextura('fxs/AbelKM/ONK/metala.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.CargarTextura('fxs/AbelKM/ONK/blanco3.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.CargarTextura('fxs/AbelKM/ONK/orange1.png', extend=cairo.EXTEND_REFLECT)


class FX1(comun.Fx):



	def EnDialogo(self, d):
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.15)
		avanzado.GrupoFin()
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
		avanzado.GrupoInicio()
		avanzado.ModoPintado('overlay')
		sil.Pintar()
		avanzado.fGlow(1, 0.1+(sin(pi*sil.progreso)/6.0))
		avanzado.fRotoZoom(8, 0.3+(sin(pi*sil.progreso)/8.0),  0.015, 0, sil.actual.pos_x+(comun.Interpolar(sil.progreso, -sil.actual.org_x*2,sil.actual.org_x*2)), sil.actual.pos_y)
		avanzado.GrupoFin(0.4)

	def EnSilabaDorm(self, d):
		global textura2
		d.actual.color3.a = 0
		d.texturas[d.PART_RELLENO] = textura2
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, diag):
		avanzado.GrupoInicio()
		diag.Desvanecer(1,0)
		diag.MoverA(0, 20, comun.i_accel)
		diag.Pintar()
		avanzado.fGlow(1, 0.15)
		avanzado.GrupoFin()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Desvanecer(1,0)
		diag.MoverA(0, 20, comun.i_accel)
		diag.Pintar()


	def EnDialogoEntra(self, d):
		avanzado.GrupoInicio()
		d.Desvanecer(0,1)
		d.MoverDe(0, 20, comun.i_accel)
		d.Pintar()
		avanzado.fGlow(1, 0.15)
		avanzado.GrupoFin()
		global textura3, textura1, textura2
		d.texturas[d.PART_RELLENO] = textura3
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = textura1
		d.actual.modo_borde = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, 20, comun.i_accel)
		d.Pintar()
		d.actual.color3.a = 0
		d.texturas[d.PART_RELLENO] = textura2
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.color1.a = comun.Interpolar(d.progreso,0, 1)
		d.MoverDe(0, 20, comun.i_accel)
		d.Pintar()




class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 350
		self.out_ms = 350
		self.fxs = (FX1(), FX1())