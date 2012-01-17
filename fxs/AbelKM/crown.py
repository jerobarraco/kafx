# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra

t1 = extra.CargarTextura("texturas/spark3.png")

class Efecto():
	def __init__(self):
		self.world = physics.World()
		self.objs = []

	def EnSilabaInicia(self, sil):
		parts = sil.CrearParticulas(t1, escala=0.001 )
		sil.parts = [parts[pos] for pos in xrange(0, len(parts), 3) ] #tomamos 1 cada 100 parts
		sil.moving = False

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()

	def EnSilaba(self, sil):
		sil.PaintWithCache()
		for p in sil.parts:
			p.Paint()

	def EnSilabaSale(self, sil):
		if not sil.moving:
			sil.moving = True
			for p in sil.parts:
				self.world.CreateSprite(p)
				self.objs.append(p)

		for p in sil.parts [:]: #[:] para el remove
			p.Paint()
			#pintamos primero, porque hasta que no hagamos world.update no tomara los cambios
			p.color.a = comun.Interpolate(sil.progress, 1, 0.00)
			self.world.Resize(p, comun.Interpolate(sil.progress, 0.3, 0.001 ))
			if p.color.a <= 0.1:
				self.world.Destroy(p)
				sil.parts.remove(p)

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
		self.sil_out_ms = 500

	def EnCuadroInicia(self):
		self.fxs[0].world.Update(True) #esto actualiza las posiciones y rotaciones de losobjetos YA CREADOS