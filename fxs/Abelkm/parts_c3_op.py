# -*- coding: utf-8 -*-
from libs import common
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin

import cairo



t = extra.LoadTexture("textures/sakura3.png")

class FX1():

	def __init__(self):
		self.events = [Evento1()]
		p = advanced.cParticleSystem(png="textures/sakura3.png", emit_parts=40, mode = 0, max_parts=80, rotation= 0.1, scale_from=0.05, scale_to= 0.05,max_life=1)
		p.SetAngle(10, 2, 10)
		p.SetGravity(0, 1)
		self.parts = p

	def OnSyllable(self, sil):
		sil.Paint()




class Evento1():
		def OnSyllable(self, sil):
			sil.Paint()
			self.parts.SetWindow(letter.original._width+1, 1)
			self.parts.SetPosition(
				letter.actual.pos_x+random.randint(-2,3)+(letter.original._width*(letter.progress)/4),
            	(random.randint(1,17)+letter.actual.pos_y))

			if letter._text.strip()<>"":
				self.parts.Emit()


		def SyllableTime(self, sil):
			return (sil._start, sil._end)




class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.out_ms = 250
		self.in_ms = 250
		self.skip_frames= False
		self.fxs = (FX1(),)
