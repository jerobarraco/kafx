# -*- coding: utf-8 -*-
from libs import comun, physics, video
from libs.draw import extra, avanzado

from random import randint, random

import cairo



t = extra.CargarTextura("texturas/uq7.png")

t3 = extra.CargarTextura('texturas/barra_gc.png') #entrada

#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.eventos = [Evento1()]
	def EnSilabaInicia(self, sil):
		global t
		#sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.parts = sil.CrearParticulas(t, escala=0.1)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [avanzado.cSprite(t, x +randint(-50, 50), y+randint(-50, 50), escala=random()*0.5 +0.5) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()
	def EnDialogoEntra(self, d):
		global t3
		#d.MoverDe((0+(comun.Interpolate(d.progress, -40,0, comun.i_b_backstart))) ,(0))
		mov = comun.Interpolate(d.progress,1380, 3480)#el fx parece dar toda la vuelta... o ya no?
		extra.MoveTexture(t3, mov, 50)
		avanzado.GrupoInicio()
		d.Paint()
		texto = avanzado.GrupoFin(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

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
			alpha = comun.Interpolate(sil.progress, 1, -0.5)
			if alpha < 0.0:
				for part in sil.parts:
						world.DestroySprite(part)
				sil.parts = [] #borramos las parts
				for b in sil.bull:
					world.DestroySprite(b)
				sil.bull = []
			else:
				for part in sil.parts[:]:
					part.color.a = alpha
					part.Paint()
					world.Resize(part, comun.Interpolate(sil.progress, 0.1, 0.2))

		def TiempoSilaba(self, sil):
                        return (sil._start, sil._end+500)



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto())
		world = physics.World(grav_y = 0)
		self.in_ms = 500


	def EnCuadroInicia(self):
		global world
		world.Update(True)