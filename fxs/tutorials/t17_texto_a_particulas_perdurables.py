# -*- coding: utf-8 -*-
"""
Tutorial de como crear partículas a partir de un texto.
"""
from libs import common
from libs.draw import extra
from random import randint

class Fxpart (common.Fx):
	def __init__(self):
		self.t = extra.LoadTexture("textures/snowflake2.png")
		self.parts_a_pintar = []

	def EnLetraInicia(self, le):
		le.actual.modo_relleno = le.P_DEG_VERT
		le.parts = le.CreateParticles(self.t, 0.2)
		for p in le.parts:
			p.movx = randint(-10, 10)
			p.movy = randint(-10, 10)
			p.esc = 0.2

	def EnLetra(self, le):
		self.parts_a_pintar.extend(
			le.parts
		)
		le.parts = []

	def EnDialogo(self, d):d.PintarConCache()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart()]
		self.saltar_cuadros = False
		self.dividir_letras = True

	def EnCuadroFin(self):
		for p in self.fxs[0].parts_a_pintar[:]:
			p.color.a -= 0.08
			p.x += p.movx
			p.y += p.movy
			p.esc += 0.01
			p.Scale(p.esc, p.esc)
			p.Pintar()

			if p.color.a <= 0:
				self.fxs[0].parts_a_pintar.remove(p)
