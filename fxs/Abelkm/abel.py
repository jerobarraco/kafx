# -*- coding: utf-8 -*-


from libs import common, video
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


class FX1(common.Fx):
		def EnSilabaInicia(self, d):
			d.LoadTexture('textures/blast.png', parte=0)
		def EnDialogo(self, d):
			advanced.StartGroup()
			advanced.ModoPintado('color_burn')
			d.actual.color1.a = 0
			d.actual.color3.a = 2.5
			d.Pintar()
			advanced.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.Pintar()
			d.actual.color1.a = 1
			advanced.ModoPintado('over')
			d.actual.color3.a = 1.3
			advanced.fBlur(2)
			d.Pintar()
			advanced.EndGroup(1.0)

		def EnSilaba(self, d):
			advanced.StartGroup()
			d.Pintar()
			advanced.fGlow(2, 0+((sin(pi*d.progreso))/6))
			advanced.EndGroup()

		def EnDialogoEntra(self, d):
			advanced.StartGroup()
			advanced.ModoPintado('color_burn')
			d.actual.color.a = 0
			d.actual.color3.a = 2.5
			d.MoveFrom(30, 0, common.i_b_backstart)
			d.Pintar()
			advanced.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.MoveFrom(30, 0, common.i_b_backstart)
			d.Pintar()
			d.actual.color.a = 1
			advanced.ModoPintado('over')
			d.actual.color3.a = 1.3
			advanced.fBlur(2)
			d.MoveFrom(30, 0, common.i_b_backstart)
			d.Pintar()
			advanced.EndGroup(common.Interpolar(d.progreso, 0, 1, common.i_accel))

		def EnDialogoSale(self, d):
			advanced.StartGroup()
			advanced.ModoPintado('color_burn')
			d.actual.color1.a = 0
			d.actual.color3.a = 2.5
			d.MoveTo(30, 0, common.i_b_backstart)
			d.Pintar()
			advanced.ModoPintado('add')
			d.actual.color3.a = 0
			d.actual.color1.a = 0.3
			d.MoveTo(30, 0, common.i_b_backstart)
			d.Pintar()
			d.actual.color1.a = 1
			advanced.ModoPintado('over')
			d.actual.color3.a = 1.3
			advanced.fBlur(2)
			d.MoveTo(30, 0, common.i_b_backstart)
			d.Pintar()
			advanced.EndGroup(common.Interpolar(d.progreso, 1, 0, common.i_accel))

class FxsGroup(common.FxsGroup):
        def __init__(self):
			self.in_ms = 500
			self.out_ms = 500
			self.fxs = (FX1(), FX1())