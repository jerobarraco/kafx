# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""


from libs import comun

class FX1(comun.Fx):
    def EnDialogo(self, d):
        d.FullWiggle(4)
        d.Pintar()

    def EnSilaba(self, d):
        d.actual.color1.CopiarDe(d.actual.color2)
        d.Pintar()

    def EnSilabaMuerta(self, d):
        d.actual.color1.CopiarDe(d.actual.color3)
        d.Pintar()

    def EnDialogoSale(self, d):
        d.actual.color1.CopiarDe(d.actual.color4)
        d.Pintar()

    def EnDialogoEntra(self, d):
        d.actual.color1.CopiarDe(d.actual.color4)
        d.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 500
		self.out_ms = 500
		self.fxs = (FX1(), FX1())
		self.reset_estilo = False
