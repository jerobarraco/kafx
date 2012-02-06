# -*- coding: utf-8 -*-
from libs import common, physics, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin
t = extra.LoadTexture("texturas/uq7.png")

t3 = extra.LoadTexture('texturas/barra_gc.png') #entrada

#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.events = [Evento1()]
	def OnSyllableStarts(self, sil):
		global t
		#sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.parts = sil.CreateParticles(t, scale=0.1,alpha_min=0.4)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [advanced.cSprite(t, x +randint(-50, 50), y+randint(-50, 50), scale=random()*0.5 +0.5) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def OnSyllableSleep(self, sil):
		sil.PaintWithCache()
	def OnDialogueIn(self, d):
		global t3
		#d.MoveFrom((0+(comun.Interpolate(d.progress, -40,0, comun.i_b_backstart))) ,(0))
		mov = common.Interpolate(d.progress,1380, 3480)#el fx parece dar toda la vuelta... o ya no?
		extra.MoveTexture(t3, mov, 50)
		advanced.StartGroup()
		d.Paint()
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

class Evento1():
		def OnSyllable(self, sil):
			global world
			if sil.crear:
				sil.crear  = False
				for part in sil.parts:
					world.CreateSprite(part)
				for b in sil.bull:
					world.CreateSprite(b, False)
				sil.matar=True
			alpha = common.Interpolate(sil.progress, 1, -0.5)
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
					advanced.StartGroup()
					part.Paint()
					advanced.fGlow(2, 0.1+(sin(pi*sil.progress)/6.0))
					advanced.EndGroup()

					world.Resize(part, common.Interpolate(sil.progress, 0.1, 0.2))

		def SyllableTime(self, sil):
			return (sil._start, sil._end+500)



class FxsGroup(common.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto())
		world = physics.World(grav_y = 0)
		self.in_ms = 500

	def OnFrameStarts(self):
		global world
		world.Update(True)