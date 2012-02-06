﻿# -*- coding: utf-8 -*-
from libs import comun

class EfectoGenerico(comun.Fx):
		def EnDialogo(self, diag):
			diag.Paint()

		def EnSilaba(self, diag):
				diag.actual.color1.CopyFrom(diag.actual.color2)
				diag.Paint()

class Efecto2(comun.Fx):
		def EnLetra(self, let):
				let.Pintar()



class Compuesto (EfectoGenerico, Efecto2):
		pass

class FxsGroup(comun.FxsGroup):
	def __init__(self):
        self.fxs = (EfectoGenerico(), Efecto2(), Compuesto())