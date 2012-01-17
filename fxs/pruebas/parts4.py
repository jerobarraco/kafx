# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import extra
import random

class Fxpart (comun.Fx):
	def __init__(self):
		self.t = extra.CargarTextura("texturas/star1.png")

	def EnSilabaEntra(self, sil):
		for p in sil.parts:
			p.color.a = comun.Interpolar (sil.progreso, 0, 1)
			p.x = comun.Interpolar(sil.progreso, p.movx, p.inix)
			p.y = comun.Interpolar(sil.progreso, p.movy, p.iniy)
			p.Pintar()

	def EnSilabaSale(self, sil):
		for p in sil.parts:
			p.color.a = comun.Interpolar (sil.progreso, 1,0)
			p.x = comun.Interpolar(sil.progreso, p.inix, p.movx2)
			p.y = comun.Interpolar(sil.progreso, p.iniy, p.movy)
			p.Pintar()

	def EnSilabaInicia(self, sil):
		sil.parts = sil.CrearParticulas(self.t, 0.1)
		for p in sil.parts:
			p.inix = p.x
			p.iniy = p.y
			p.movx = p.inix + random.randint(-0, 40)
			p.movy = p.iniy + random.randint(-10, 10)
			p.movx2 = p.inix + random.randint(-40, 0)
			p.esc = 0.1

	def EnSilaba(self, sil):
		sil.PintarConCache()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart()]
		self.saltar_cuadros = False
		self.syl_in_ms = 400
		self.syl_out_ms = 400