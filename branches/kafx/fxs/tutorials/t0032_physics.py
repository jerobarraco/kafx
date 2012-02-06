# -*- coding: utf-8 -*-
from libs import common, physics
from libs.draw import extra

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

t1 = extra.LoadTexture("textures/uq7.png")

class Efecto():
	def __init__(self):
		self.world = physics.World()
		self.objs = []

	def EnSilabaInicia(self, sil):
		parts = sil.CreateParticles(t1, scale=0.3 )
		sil.parts = [parts[pos] for pos in xrange(0, len(parts), 2) ] #tomamos 1 cada 100 parts
		sil.moving = False

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()

	def EnSilaba(self, sil):
		if not sil.moving:
			sil.moving = True
			for p in sil.parts:
				self.world.CreateSprite(p)
				self.objs.append(p)

class Efecto2():
	def EnDialogo(self, d):
		d.PaintWithCache()

	def EnSilaba(self, s):
		s.actual.color1.CopyFrom(s.actual.color2)
		s.PaintWithCache()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), Efecto2(), Efecto2())
		#no puedo crear dos effect() porque intentaria crear dos mundos
		self.saltar_cuadros = False

	def EnCuadroInicia(self):
		self.fxs[0].world.Update(True)

	def EnCuadroFin(self):
		objs=self.fxs[0].objs
		world = self.fxs[0].world

		for o in objs[:]:#[:]es para poder hacer remove
			o.Paint()
			o.color.a -= 0.005
			if o.color.a <0.0:
				world.Destroy(o)
				objs.remove(o)