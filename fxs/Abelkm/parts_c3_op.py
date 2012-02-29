# -*- coding: utf-8 -*-
from libs import common
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin
import random
import cairo



#metodo 1, menos cochino, globales
p = advanced.cParticleSystem(png="textures/sakura3.png", emit_parts=40, mode = 0, max_parts=80, rotation= 0.1, scale_from=0.60, scale_to= 0.9,max_life=1.6)
p.SetAngle(10, 2, 10)
p.SetGravity(0, -1)
class FX1():
	def __init__(self):
		self.events = [Evento1()]
		self.parts = p
	def OnSyllable(self, sil):
		sil.Paint()




class Evento1():
		def OnSyllable(self, sil):
			global p
			sil.Paint()

			p.SetWindow(sil.original._width+1, 1)
			p.SetPosition(
				sil.actual.pos_x+random.randint(8,12)-(random.randint(-2,3)+(sil.original._width*(sil.progress)/4)),
            	(random.randint(1,20)+sil.actual.pos_y))

			if sil._text.strip()<>"":
				p.Emit()


		def SyllableTime(self, sil):
			return (sil._start, sil._end)




class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.out_ms = 250
		self.in_ms = 250
		self.skip_frames= False
		self.fxs = (FX1(),)

	def OnFrameEnds(self):
		global p
		advanced.StartGroup()
		p.Paint()
		advanced.fGlow(1, 0.05)
		advanced.fBlur1(1, 0.05)

		advanced.EndGroup()