# -*- coding: utf-8 -*-


from libs import comun, video
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos


class FX1(comun.Fx):
		def EnSilabaInicia(self, d):
			d.LoadTexture('textures/blast.png', parte=0)
		def EnDialogo(self, d):
			avanzado.StartGroup()
			avanzado.ModoPintado('color_burn')
			d.actual.color1.a = 0
			d.actual.color3.a = 2.5
			d.Pintar()
			avanzado.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.Pintar()
			d.actual.color1.a = 1
			avanzado.ModoPintado('over')
			d.actual.color3.a = 1.3
			avanzado.fBlur(2)
			d.Pintar()
			avanzado.EndGroup(1.0)

		def EnSilaba(self, d):
			avanzado.StartGroup()
			d.Pintar()
			avanzado.fGlow(2, 0+((sin(pi*d.progreso))/6))
			avanzado.EndGroup()

		def EnDialogoEntra(self, d):
			avanzado.StartGroup()
			avanzado.ModoPintado('color_burn')
			d.actual.color.a = 0
			d.actual.color3.a = 2.5
			d.MoveFrom(30, 0, comun.i_b_backstart)
			d.Pintar()
			avanzado.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.MoveFrom(30, 0, comun.i_b_backstart)
			d.Pintar()
			d.actual.color.a = 1
			avanzado.ModoPintado('over')
			d.actual.color3.a = 1.3
			avanzado.fBlur(2)
			d.MoveFrom(30, 0, comun.i_b_backstart)
			d.Pintar()
			avanzado.EndGroup(comun.Interpolar(d.progreso, 0, 1, comun.i_accel))

		def EnDialogoSale(self, d):
			avanzado.StartGroup()
			avanzado.ModoPintado('color_burn')
			d.actual.color1.a = 0
			d.actual.color3.a = 2.5
			d.MoveTo(30, 0, comun.i_b_backstart)
			d.Pintar()
			avanzado.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.MoveTo(30, 0, comun.i_b_backstart)
			d.Pintar()
			d.actual.color1.a = 1
			avanzado.ModoPintado('over')
			d.actual.color3.a = 1.3
			avanzado.fBlur(2)
			d.MoveTo(30, 0, comun.i_b_backstart)
			d.Pintar()
			avanzado.EndGroup(comun.Interpolar(d.progreso, 1, 0, comun.i_accel))

class FxsGroup(comun.FxsGroup):
        def __init__(self):
			self.in_ms = 500
			self.out_ms = 500
			self.fxs = (FX1(), FX1())