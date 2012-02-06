# -*- coding: utf-8 -*-

from libs import common

class FX1(common.Fx):
	def EnDialogoEntra(self, d):
		d.MoveFrom(0, -50, common.i_b_boing)
		d.Pintar()

	def EnDialogoSale(self, d):
		d.MoveTo(0, 50, common.i_b_backstart)
		d.Pintar()

	def EnDialogo(self, d):
		d.Pintar()
		d.PintarReflejo()

	def EnSilaba(self, s):
		s.actual.color1.Interpolar(s.progreso, s.actual.color1, common.i_sin)
		s.Rotate(0, 6.29,  common.i_accel)
		s.Pintar()

class FxsGroup(common.FxsGroup):
  def __init__(self):
			self.in_ms = 350
			self.out_ms = 350
			self.fxs = [ FX1(), FX1()]