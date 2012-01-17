# -*- coding: utf-8 -*-
from libs import comun, physics

class Efecto():
	def __init__(self):
		self.world  = physics.World()

	def EnSilabaInicia(self, sil):
		sil.moving = False
		sil.creada = False

	def EnSilaba(self, sil):
		sil.actual.color1.Interpolate(sil.progress, sil.actual.color2)
		sil.Paint()
		if not sil.moving:
			sil.moving = True
			self.world.CreateVector(sil)
			sil.creada = True

	def EnSilabaSale(self, s):
		s.Desvanecer(1, 0)
		escala = comun.Interpolate(s.progress, 1.0, 0.8)
		if s.creada:
			self.world.Resize(s, escala)
			self.world.UpdateVector(s)
			if s.progress >= 0.9:
				s.creada = False
				self.world.Destroy(s)

		s.Paint()


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
		#no puedo crear dos effect() porque intentaria crear dos mundos
		self.saltar_cuadros = False
		self.sil_out_ms = 1200
		self.reset_estilo = False #requerido para el world.Update(True)

	def EnCuadroInicia(self):
		self.fxs[0].world.Update(False)#le ponemos false porque vamos a updatear los elementos a mano
