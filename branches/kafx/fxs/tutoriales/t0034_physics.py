# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra
#a este lo modifique y lo pise sin querer y justo el svn me lo cambiaron
class Efecto():
	def __init__(self):

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
		self.dividir_letras = True

	def EnCuadroInicia(self):
		self.fxs[0].world.Update(True)

	def EnCuadroFin(self):
		objs=self.fxs[0].objs
		dorm = self.fxs[0].dorm_objs
		world = self.fxs[0].world
		for p in dorm :
			p.Paint()

		for o in objs[:]:#[:]es para poder hacer remove
			#recordar que .a va decreciendo, asi que la interpolacion es al revez
			world.Resize(o, comun.Interpolate(o.color.a, 0.3, 0.7, comun.i_sin ))
			o.Paint()
			o.color.a -= 0.025
			if o.color.a <= 0.0:
				world.Destroy(o)
				objs.remove(o)