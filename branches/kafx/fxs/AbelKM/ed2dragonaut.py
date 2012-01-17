# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""
from libs import comun
from libs.draw import avanzado
import random
from math import pi, sin


class FX1(comun.Fx):
	def EnSilaba(self, diag):
		diag.actual.modo_relleno = diag.P_DEG_VERT
		diag.actual.scale_x = diag.actual.scale_y = 1+((sin(pi*diag.progreso))/15)
		diag.actual.color1.Interpolar(diag.progreso, diag.actual.color3)
		avanzado.GrupoInicio()
		diag.actual.pos_x += random.randint(-1, 1)
		diag.actual.pos_y += random.randint(-1, 1)
		diag.Pintar()
		avanzado.fGlow(5, 0+((sin(pi*diag.progreso))/10))
		avanzado.GrupoFin()

	def EnSilabaMuerta(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.Pintar()


	def EnDialogoEntra(self, di):
		di.Desvanecer(0, 1)
		di.actual.modo_relleno = di.P_DEG_VERT
		avanzado.GrupoInicio()
		di.actual.scale_y = (1.5)+(sin(pi*di.progreso))
		di.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()

	def EnDialogoSale(self, di):
		di.Desvanecer(1, 0)
		di.actual.modo_relleno = di.P_DEG_VERT
		di.actual.color1.CopiarDe(di.actual.color3)
		di.actual.scale_y  = 1+di.progreso
		avanzado.GrupoInicio()
		di.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Pintar()

class FX2(comun.Fx):
	def EnSilaba(self, diag):
		diag.actual.modo_relleno = diag.P_DEG_VERT
		diag.actual.scale_x = diag.actual.scale_y = 1+((sin(pi*diag.progreso))/4)
		diag.actual.color1.Interpolar(diag.progreso, diag.actual.color3)
		avanzado.GrupoInicio()
		diag.actual.pos_x += random.randint(-2, 2)
		diag.actual.pos_y += random.randint(-2, 2)
		diag.Pintar()
		avanzado.fGlow(5, 0+((sin(pi*diag.progreso))/10))
		avanzado.GrupoFin()

	def EnSilabaMuerta(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.actual.color1.CopiarDe(d.actual.color3)
		d.Pintar()


	def EnDialogoEntra(self, di):
		di.Desvanecer(0, 1)
		di.actual.modo_relleno = di.P_DEG_VERT
		avanzado.GrupoInicio()
		di.actual.scale_y = (1.5)+(sin(pi*di.progreso))
		di.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()

	def EnDialogoSale(self, di):
		di.Desvanecer(1, 0)
		di.actual.modo_relleno = di.P_DEG_VERT
		di.actual.color1.CopiarDe(di.actual.color3)
		di.actual.scale_y  = 1+di.progreso
		avanzado.GrupoInicio()
		di.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		d.actual.modo_relleno = d.P_DEG_VERT
		d.Pintar()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 250
		self.out_ms = 150
		self.fxs = (FX1(), FX2())