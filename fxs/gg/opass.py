# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""
from libs import extra, cairo_basic, cairo_advanced, cairo_extra, avisynth
import random
from math import pi, sin, cos


class FX1(extra.Fx):


	def OnDialogoInicia(self, d):
	    d.CargarTextura('C:/Program Files/KickAss FX/stone2.png', parte=0)


	def OnDialogo(self, d):
	    cairo_advanced.GrupoInicio(True)

	    cairo_advanced.ModoPintado('overlay')
	    d.actual.borde = 0
	    d.Pintar()
	    cairo_advanced.ModoPintado('add')
	    d.actual.borde = 0
	    d.actual.color1.a = 0.3
	    d.Pintar()
	    d.actual.borde = 0
	    d.actual.color1.a = 0
	    cairo_advanced.ModoPintado('over')
	    d.actual.borde = 0.8

	    d.actual.color1.a = 0
	    d.Pintar()
	    cairo_advanced.GrupoFin(1.0)

	def OnDialogoEntra(self, d):
	    cairo_advanced.GrupoInicio(True)

	    cairo_advanced.ModoPintado('overlay')
	    d.actual.borde = 0
	    d.MoverDe(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    cairo_advanced.ModoPintado('add')
	    d.actual.borde = 0
	    d.actual.color1.a = 0.3
	    d.MoverDe(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    d.actual.borde = 0
	    d.actual.color1.a = 0
	    cairo_advanced.ModoPintado('over')
	    d.actual.borde = 0.8

	    d.actual.color1.a = 0
	    d.MoverDe(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    cairo_advanced.GrupoFin(extra.Interpolar(d.progreso, 0, 1))

	def OnDialogoSale(self, d):
	    cairo_advanced.GrupoInicio(True)

	    cairo_advanced.ModoPintado('overlay')
	    d.actual.borde = 0
	    d.MoverA(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    cairo_advanced.ModoPintado('add')
	    d.actual.borde = 0
	    d.actual.color1.a = 0.3
	    d.MoverA(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    d.actual.borde = 0
	    d.actual.color1.a = 0
	    cairo_advanced.ModoPintado('over')
	    d.actual.borde = 0.8

	    d.actual.color1.a = 0
	    d.MoverA(20, 0, extra.i_b_backstart)
	    d.Pintar()
	    cairo_advanced.GrupoFin(extra.Interpolar(d.progreso, 1, 0))
	    d.CargarTextura('C:/Program Files/KickAss FX/stone2.png', parte=1)
	    d.actual.borde = 0
	    d.actual.color1.a = extra.Interpolar(d.progreso, 0.5, 0)
	    d.MoverA(20, 0, extra.i_b_backstart)
	    d.Pintar()

	def OnSilaba(self, s):
	    s.CargarTextura('C:/Program Files/KickAss FX/stone2.png', parte=1)
	    cairo_advanced.GrupoInicio()
	    s.actual.borde = 0
	    s.actual.color1.a = 0.5
	    s.Pintar()
	    cairo_advanced.fGlow(2, ((sin(pi*s.progreso))/5))
	    cairo_advanced.GrupoFin()
	def OnSilabaMuerta(self, s):
	    s.CargarTextura('C:/Program Files/KickAss FX/stone2.png', parte=1)
	    s.actual.borde = 0
	    s.actual.color1.a = 0.5
	    s.Pintar()





class FxsGroup(extra.FxsGroup):
	def __init__(self):
		self.in_ms = 300
		self.out_ms = 300
		self.fxs = (FX1(), FX1())