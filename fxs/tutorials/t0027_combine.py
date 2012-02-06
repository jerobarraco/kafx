# -*- coding: utf-8 -*-
from libs import common

class EfectoGenerico(common.Fx):
		def EnDialogo(self, diag):
			diag.Paint()

		def EnSilaba(self, diag):
				diag.actual.color1.CopyFrom(diag.actual.color2)
				diag.Paint()

class Efecto2(common.Fx):
		def EnLetra(self, let):
				let.Pintar()



class Compuesto (EfectoGenerico, Efecto2):
		pass

class FxsGroup(common.FxsGroup):
	def __init__(self):
        self.fxs = (EfectoGenerico(), Efecto2(), Compuesto())