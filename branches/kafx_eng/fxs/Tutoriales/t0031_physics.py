# -*- coding: utf-8 -*-
from libs import comun, physics

class Efecto():
	def __init__(self):
		self.world  = physics.World()
		self.objs = []
		
	def EnSilabaInicia(self, sil):
		sil.moving = False

	def EnSilaba(self, sil):
		if not sil.moving:
			self.world.CreateVector(sil)
			sil.moving = True
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
		for o in self.fxs[0].objs:
			o.actual.color1.CopyFrom(o.actual.color2)
			o.Paint()
			"""if o.body.IsSleeping():
				physics.Destroy(o)
				objs.remove(o)"""