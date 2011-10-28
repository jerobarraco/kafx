# -*- coding: utf-8 -*-

from libs import comun

class FX1(comun.Fx):
	def EnDialogoEntra(self, d):
		d.MoverDe(0, -50, comun.i_b_boing)
		d.Pintar()

	def EnDialogoSale(self, d):
		d.MoverA(0, 50, comun.i_b_backstart)
		d.Pintar()

	def EnDialogo(self, d):
		d.Pintar()
		d.PintarReflejo()

	def EnSilaba(self, s):
		s.actual.color1.Interpolar(s.progreso, s.actual.color1, comun.i_sin)
		s.Girar(0, 6.29,  comun.i_accel)
		s.Pintar()

class FxsGroup(comun.FxsGroup):
  def __init__(self):
			self.in_ms = 350
			self.out_ms = 350
			self.fxs = [ FX1(), FX1()]