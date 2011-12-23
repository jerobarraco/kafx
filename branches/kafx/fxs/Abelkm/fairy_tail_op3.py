# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""
"""por alguna razón no anda D:"""

from libs import comun
from libs.draw import avanzado
from math import pi, sin, cos

class FX1(comun.Fx):
	def EnSilaba(self, d):

		d.CargarTextura('texturas/fire2.png', parte=d.PART_RELLENO)
		d.MoverTextura( 60*d.progreso, 60*d.progreso, parte = d.PART_RELLENO)
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(2, 0+((cos(pi*d.progreso))/4))
		avanzado.GrupoFin()

	def EnSilabaMuerta(self, d):

		d.CargarTextura('texturas/fire2.png', parte=d.PART_RELLENO)
		d.MoverTextura( -50*d.progreso, -50*d.progreso, parte=d.PART_RELLENO)
		d.Pintar()

	def EnDialogoSale(self, d):

		d.CargarTextura('texturas/fire2.png', parte=d.PART_RELLENO)
		d.MoverTextura( 70*d.progreso, 70*d.progreso, parte=d.PART_RELLENO)
		d.Desvanecer(1, 0)
		d.actual.scale_y  = 1+((d.progreso)/4.0)
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()


	def EnDialogoEntra(self, d):
		d.CargarTextura('texturas/stone2.png', parte=d.PART_RELLENO)
		d.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		d.actual.scale_y = (1)+(sin(pi*d.progreso))
		d.Pintar()
		avanzado.fBiDirBlur(pi/2.0, 7)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		d.CargarTextura('texturas/stone2.png', parte=d.PART_RELLENO)
		d.Pintar()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 170
		self.out_ms = 100
		self.fxs = (FX1(), FX1())