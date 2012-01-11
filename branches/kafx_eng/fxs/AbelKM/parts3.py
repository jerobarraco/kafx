# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra, avanzado
from random import randint
t = extra.CargarTextura("texturas/uq7.png")
#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
class Efecto():
	def __init__(self):
		self.eventos = [Evento1()]
	def EnSilabaInicia(self, sil):
		global t
		sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.parts = sil.CrearParticulas(t, escala=0.1)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [avanzado.cSprite(t, x +randint(-50, 50), y+randint(-50, 50) ) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()


class Evento1():
		def EnSilaba(self, sil):
			global world
			if sil.crear:
				sil.crear  = False
				for part in sil.parts:
					world.CreateSprite(part)
				for b in sil.bull:
					world.CreateSprite(b, False)
				sil.matar=True

			for part in sil.parts[:]:
				part.Paint()
				world.Resize(part, comun.Interpolate(sil.progress, 0.1, 0.2))
				part.color.a = comun.Interpolate(sil.progress, 1, 0.00)
				#part.color.a -=0.07
				if part.color.a <0.0:
					world.DestroySprite(part)
					sil.parts.remove(part)

		def TiempoSilaba(self, sil):
                        return (sil._start, sil._end+500)

class Efecto2():
	def EnDialogo(self, d):
		d.PaintWithCache()

	def EnSilaba(self, s):
		s.Paint()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(), Efecto2())
		world = physics.World(grav_y = 0)
		#self.sil_out_ms = 1200


	def EnCuadroInicia(self):
		global world
		world.Update(True)