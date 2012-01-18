# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado
import math, random, cairo
from math import pi, sin, cos

global pat
pat = None

class FX1(comun.Fx):
	def EnDialogoInicia(self, d):
		d.original.modo_relleno = d.P_TEXTURA


	def EnDialogo(self, d):
		global pat
		d.texturas[d.PART_RELLENO] = pat
		d.MoveTexture(-d.actual.pos_x, -d.actual.pos_y+d.original._y_bearing, parte = d.PART_RELLENO)
		avanzado.ModoPintado('color_burn')

		avanzado.StartGroup()
		d.Pintar()
		avanzado.EndGroup()
		avanzado.ModoPintado('over')
		d.Pintar()

	def EnDialogoEntra(self, d):
		global pat
		d.Fade(0, 1)
		d.MoveFrom(-30, 0, comun.i_b_backstart)
		d.texturas[d.PART_RELLENO] = pat
		d.MoveTexture(-d.actual.pos_x, -d.actual.pos_y, parte = d.PART_RELLENO)
		d.Pintar()

	def EnDialogoSale(self, d):
		global pat
		d.Fade(1, 0)
		d.MoveTo(30, 0, comun.i_b_backstart)
		d.texturas[d.PART_RELLENO] = pat
		d.MoveTexture(-d.actual.pos_x, -d.actual.pos_y, parte = d.PART_RELLENO)
		d.Pintar()


	def EnSilaba(self, d):
		d.Restore()
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/7.0))
		avanzado.EndGroup()
		d.actual.color1.CopiarDe(d.actual.color4)
		d.Pintar()


class FX2(comun.Fx):

	def EnDialogo(self, d):
		d.Pintar()

	def EnDialogoEntra(self, d):
		d.actual.color3.a = comun.Interpolar(d.progreso, 0, 1)
		d.MoveFrom(-30, 0, comun.i_b_backstart)
		d.Pintar()

	def EnDialogoSale(self, d):
		d.actual.color3.a = comun.Interpolar(d.progreso, 1, 0)
		d.MoveTo(30, 0, comun.i_b_backstart)
		d.Pintar()



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 250
		self.out_ms = 250
		self.fxs = (FX1(), FX2())

	def EnCuadroInicia(self):
		avanzado.StartGroup(True)
		avanzado.fGlow(2, 0.15)
		global pat
		pat = video.cf.ctx.pop_group()
		pat.set_extend(cairo.EXTEND_REFLECT)