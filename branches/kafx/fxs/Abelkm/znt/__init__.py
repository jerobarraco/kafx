# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos

t1 = extra.CargarTextura('texturas/pink_g.png', extend=cairo.EXTEND_REFLECT)

t3 = extra.CargarTextura('texturas/blue_g2.png', extend=cairo.EXTEND_REPEAT)
class FX1(comun.Fx):
	def __init__(self):
		self.eventos = [Evento1(), Evento2()]


	def EnSilaba(self, sil):
		global t3, t1
		sil.actual.sombra = 1
		sil.actual.borde = 0
		sil.Escalar(1, comun.Interpolar(sil.progreso, 1.30, 1, comun.i_b_boing))
		sil.Pintar()
		sil.texturas[sil.PART_RELLENO] = t1
		sil.actual.modo_relleno = sil.P_TEXTURA
		avanzado.GrupoInicio()
		sil.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*sil.progreso)/10.0))
		avanzado.GrupoFin(comun.Interpolar(sil.progreso, 1, 0, comun.i_accel))
		sil.actual.borde = 0
		sil.texturas[sil.PART_RELLENO] = t3
		sil.actual.modo_relleno = sil.P_TEXTURA
		avanzado.GrupoInicio()
		sil.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*sil.progreso)/6.0))
		avanzado.GrupoFin(comun.Interpolar(sil.progreso, 0, 1, comun.i_accel))

class Evento1(comun.Evento):
	def EnSilaba(self, sil2):
		global t3
		sil2.Desvanecer(1,0)
		sil2.texturas[sil2.PART_RELLENO] = t3
		sil2.actual.modo_relleno = sil2.P_TEXTURA
		sil2.actual.color3.a = comun.Interpolar(sil2.progreso, 0.6, 0)
		sil2.Pintar()

	def TiempoSilaba(self, sil2):
		return (sil2._end, sil2._parent._end +300)

class Evento2(comun.Evento):
	def EnSilaba(self, sil3):
		global t1
		sil3.Desvanecer(0,1)
		sil3.texturas[sil3.PART_RELLENO] = t1
		sil3.actual.modo_relleno = sil3.P_TEXTURA
		sil3.actual.color3.a = comun.Interpolar(sil3.progreso, 0, 0.6)
		sil3.Pintar()#Este es el que se come todo el cpu mas que nada por la sombra 

	def TiempoSilaba(self, sil3):
		return (sil3._parent._start - 300, sil3._start)

#@Type FxsGroup comun.FxsGroup
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(), FX1())