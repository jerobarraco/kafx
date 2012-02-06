# -*- coding: utf-8 -*-
from libs import common, physics
from libs.draw import extra, advanced
from random import randint
t = extra.LoadTexture("textures/T_NEGRO2.png")
#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
class Efecto():
	def __init__(self):
		self.world = physics.World(grav_y = 0)

	def EnSilabaInicia(self, sil):
		global t
		sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.parts = sil.CreateParticles(t, scale=0.2)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [advanced.cSprite(t, x +randint(-10, 10), y+randint(-10,10) ) for i in range(5)] #para que desordenen, pero no las vamos a pintar

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()
	def EnSilaba(self, sil):
		sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.PaintWithCache()

	def EnSilabaSale(self, sil):
		if sil.crear:
			sil.crear  = False
			for part in sil.parts:
				self.world.CreateSprite(part)
			for b in sil.bull:
				self.world.CreateSprite(b, False)
			sil.matar=True

		for part in sil.parts[:]:
			part.Paint()
			part.color.a -=0.05
			if part.color.a <0.0:
				self.world.DestroySprite(part)
				sil.parts.remove(part)

class Efecto2():
	def EnDialogo(self, d):
		d.PaintWithCache()

	def EnSilaba(self, s):
		s.Paint()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), Efecto2())
		self.syl_out_ms = 1200


	def EnCuadroInicia(self):
		self.fxs[0].world.Update()