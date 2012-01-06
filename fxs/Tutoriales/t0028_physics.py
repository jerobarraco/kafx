# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra
from libs.draw import avanzado

t = extra.CargarTextura("texturas/snowflake2.png")

class Efecto():
	def EnSilabaInicia(self, sil):
		global t
		sil.parts = sil.CrearParticulas(t)
		sil.crear = True
		
	def EnSilaba(self, sil):
		global t
		if sil.crear:
			for part in sil.parts:
				physics.CreateSprite(part)
		for part in sil.parts:
			physics.UpdateSprite(part)
			part.Paint()
		
			
	def EnDialogo(self, diag):
		diag.PaintWithCache()				
					

class Efecto2():
	def EnDialogo(self, d):
		d.PaintWithCache()
		
	def EnSilaba(self, s):
		s.Paint()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global t
		physics.Create()
		self.fxs = (Efecto(), Efecto2())
		
		
	def EnCuadroInicia(self):
		physics.Update()