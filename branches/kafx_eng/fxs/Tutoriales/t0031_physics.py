# -*- coding: utf-8 -*-
from libs import comun, physics

objs = []
class Efecto():
	def EnSilabaInicia(self, sil):
		sil.moving = False

	def EnSilaba(self, sil):
		if not sil.moving:
			physics.CreateVector(sil)
			sil.moving = True
			objs.append(sil)
			
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
		physics.Create()
		self.fxs = (Efecto(), Efecto(), Efecto2())
		self.saltar_cuadros = False
		
	def EnCuadroInicia(self):
		physics.Update()
		
	def EnCuadroFin(self):
		global objs
		for o in objs:
			o.actual.color1.CopyFrom(o.actual.color2)
			physics.UpdateVector(o)
			o.Paint()
			"""if o.body.IsSleeping():
				physics.Destroy(o)
				objs.remove(o)"""