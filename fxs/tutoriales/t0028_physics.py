# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra

t = extra.LoadTexture("texturas/snowflake2.png")
#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
class Efecto():
	def __init__(self):
		self.world = physics.World(grav_y = 100)

	def OnSyllableStarts(self, sil):
		global t
		sil.parts = sil.CreateParticles(t, scale=0.2)
		sil.crear = True

	def OnSyllable(self, sil):
		if sil.crear:
			sil.crear  = False

			for part in sil.parts:
				self.world.CreateSprite(part)
			sil.matar=True

		for part in sil.parts:
			part.Paint()

	def OnSyllableOut(self, sil):
		if sil.matar :
			sil.matar = False
			for p in sil.parts:
				self.world.DestroySprite(p)

	def OnDialogue(self, diag):
		diag.PaintWithCache()


class Efecto2():
	def OnDialogue(self, d):
		d.PaintWithCache()

	def OnSyllable(self, s):
		s.Paint()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(), Efecto2())


	def OnFrameStarts(self):
		self.fxs[0].world.Update()