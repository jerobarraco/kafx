# -*- coding: utf-8 -*-
"""
Tutorial de como crear partículas a partir de un texto.
"""
from libs import common
from libs.draw import extra
from random import randint

class FXPart (common.Fx):
	def __init__(self):
		self.textura  = extra.LoadTexture("textures/sakura.png")

	def EnSilabaInicia(self, sil):
		sil.actual.color1.CopiarDe(sil.original.color2)
		sil.actual.modo_relleno = sil.P_DEG_VERT
		sil.parts = sil.CreateParticles(self.textura, 0.1)
		for p in sil.parts:
			p.movx = randint(-10, 10)
			p.movy = randint(-10, 10)
			p.esc = 0.1

	def EnSilaba(self, sil):
		for p in sil.parts:
			p.x += p.movx
			p.y += p.movy
			p.angulo = common.Interpolar(sil.progreso, 0, 6.28, common.i_b_boing)
			p.color.a -= 0.1
			p.esc += 0.05
			p.Scale(p.esc, p.esc)
			p.Pintar()

	def EnDialogo(self, d):
		d.PintarConCache()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = [FXPart()]
		self.saltar_cuadros = False