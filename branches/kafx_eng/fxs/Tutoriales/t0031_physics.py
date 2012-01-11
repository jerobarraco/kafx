# -*- coding: utf-8 -*-
from libs import comun, physics

class Efecto():
	def __init__(self):
		self.world  = physics.World()
		self.objs = []

	def EnSilabaInicia(self, sil):
		sil.moving = False
		sil.creada = False

	def EnSilaba(self, sil):
		if not sil.moving:
			sil.moving = True
			self.world.CreateVector(sil, square=True)
			sil.creada = True
			self.objs.append(sil)

	def EnDialogo(self, diag):
		diag.PaintWithCache()


class Efecto2():
	def EnDialogo(self, d):
		d.PaintWithCache()

	def EnSilaba(self, s):
		s.actual.color1.CopyFrom(s.actual.color2)
		s.PaintWithCache()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), Efecto2(), Efecto2())
		#no puedo crear dos efecto() porque intentaria crear dos mundos
		self.saltar_cuadros = False

	def EnCuadroInicia(self):
		self.fxs[0].world.Update(True)

	def EnCuadroFin(self):
		for s in self.fxs[0].objs[:]:
			s.actual.color1.CopyFrom(s.actual.color2)
			s.Paint()
			escala = comun.Interpolate(s.actual.color2.a, 4.0, 1.0)
			self.fxs[0].world.Resize(s, escala)
			s.original.color2.a -= 0.01
			if s.original.color2.a <= 0.0:
				self.fxs[0].objs.remove(s)
				self.fxs[0].world.Destroy(s)