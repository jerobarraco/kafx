# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import extra
import random


parts_a_pintar = []
parts_a_pintar2 = []

class Fxpart (comun.Fx):
	def __init__(self):
		self.t = extra.CargarTextura("texturas/star1.png")

	def EnSilabaEntra(self, sil):
		global parts_a_pintar
		parts_a_pintar.extend( sil.parts1 )
		sil.parts1 = []

	def EnSilabaSale(self, sil):
		global parts_a_pintar2
		parts_a_pintar2.extend( sil.parts2  )
		sil.parts2 = []

	def EnSilabaInicia(self, sil):
		sil.parts1 = sil.CrearParticulas(self.t, 0.1)
		for p in sil.parts1:
			p.inix = p.x
			p.iniy = p.y
			p.movx = p.inix + random.randint(-0, 40)
			p.movy = p.iniy + random.randint(-10, 10)
			p.esc = 0.1
			p.vida = 0.0

		sil.parts2 = sil.CrearParticulas(self.t, 0.1 )
		for p in sil.parts2:
			p.inix = p.x
			p.iniy = p.y
			p.movx = p.inix + random.randint(-40, 0)
			p.movy = p.iniy + random.randint(-10, 10)
			p.esc = 0.1
			p.vida = 0.0

	def EnSilaba(self, sil):
		sil.PintarConCache()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart()]
		self.saltar_cuadros = False
		self.sil_in_ms = 400
		self.sil_out_ms = 400

	def EnCuadroFin(self):
		global parts_a_pintar, parts_a_pintar2
		for p in parts_a_pintar[:]:
			p.color.a += comun.Interpolar(p.vida, 0, 1)
			p.x = comun.Interpolar(p.vida, p.movx, p.inix)
			p.y = comun.Interpolar(p.vida, p.movy, p.iniy)
			p.Pintar()

			p.vida += 0.06
			if p.vida>1:
				parts_a_pintar.remove(p)


		for p in parts_a_pintar2[:]:
			p.color.a = comun.Interpolar(p.vida, 1, 0)
			p.x = comun.Interpolar(p.vida, p.inix, p.movx )
			p.y = comun.Interpolar(p.vida, p.iniy, p.movy)
			p.Pintar()

			p.vida += 0.06
			if p.vida>1:
				parts_a_pintar2.remove(p)