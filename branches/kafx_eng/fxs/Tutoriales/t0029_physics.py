	# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra
from libs.draw import avanzado

t = extra.CargarTextura("texturas/snowflake2.png")
parts = []
world = None
class Efecto():
	def EnSilabaInicia(self, sil):
		global parts
		sil.parts = []
		sil.creadas  = False

	def EnSilaba(self, sil):
		global t, parts,world
		if not sil.creadas:
			sil.parts = []
			sil.creadas = True
			for i in range(5):
				nx = comun.LERP(i/5.0, sil.actual.pos_x, sil.actual.pos_x + sil.original._ancho)
				ny = sil.actual.pos_y + sil.actual.org_y
				np = avanzado.cSprite(t, x = nx, y= ny)
				sil.parts.append(np)
				world.CreateSprite(np)

		for part in sil.parts[:]:
			parts.append(part)
			sil.parts.remove(part)

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
		global world
		world.Create()
		self.fxs = (Efecto(), Efecto2())
		self.saltar_cuadros = False

	def EnCuadroInicia(self):
		physics.Update(True)

	def EnCuadroFin(self):
		global parts
		for part in parts:
			part.Paint()