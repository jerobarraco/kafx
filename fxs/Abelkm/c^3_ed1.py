# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin
import cairo, random

t3 = extra.LoadTexture('textures/blue_g2.png', extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture('textures/blue_g222.png', extend=cairo.EXTEND_REFLECT)
t1 = extra.LoadTexture('textures/blue_g2.png', extend=cairo.EXTEND_REPEAT)
t0 = extra.LoadTexture('textures/blue_g22223.png', extend=cairo.EXTEND_REPEAT)

p = advanced.cParticleSystem(png="textures/blue-ball.png", emit_parts=5, mode = 0, max_parts=10, rotation= 0.1, scale_from=0.015, scale_to= 0.03,max_life=1.6)
p.SetAngle(10, 2, 10)
p.SetGravity(0, 1)

class FX1():
	def __init__(self):
		self.events = [Evento1()]
		self.parts = p


	def OnDialogueStarts(self, d):
		d.mov1 = 0
		d.mov2 = 0

	def OnSyllable(self, sil):
		global t3, t1, t2
		sil.textures[sil.PART_FILL] = t2
		sil.actual.mode_fill = sil.P_TEXTURE
		sil.textures[sil.PART_BORDER] = t1
		sil.actual.mode_border = sil.P_TEXTURE
		sil.Paint()
		sil.Restore()
		sil.textures[sil.PART_FILL] = t3
		sil.actual.mode_fill = sil.P_TEXTURE
		advanced.StartGroup()
		sil.Paint()
		advanced.fBlur1(1, ((sin(pi*sil.progress))/6.0))
		advanced.fGlow(2, ((sin(pi*sil.progress))/6.0))
		advanced.EndGroup(common.Interpolate(sil.progress, 1.0, 0.0))
	def OnSyllableSleep(self, sil):
		global t3, t0
		sil.textures[sil.PART_BORDER] = t0
		sil.actual.mode_border = sil.P_TEXTURE
		sil.textures[sil.PART_FILL] = t3
		sil.actual.mode_fill = sil.P_TEXTURE
		sil.Paint()

	def OnSyllableDead(self, sil):
		global t2, t1
		sil.textures[sil.PART_FILL] = t2
		sil.actual.mode_fill = sil.P_TEXTURE
		sil.textures[sil.PART_BORDER] = t1
		sil.actual.mode_border = sil.P_TEXTURE
		sil.Paint()

	def OnDialogueIn(self, d):
		global t3, t0
		d.textures[d.PART_FILL] = t3
		d.actual.mode_fill = d.P_TEXTURE
		d.textures[d.PART_BORDER] = t0
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.Paint()
		advanced.fWave( d.mov2, 0.05, common.Interpolate(d.progress, 2, 0, common.i_accel),  True)
		advanced.fWave( d.mov2, 0.1, common.Interpolate(d.progress, 2, 0, common.i_accel),  False)
		advanced.EndGroup(common.Interpolate(d.progress, 0, 1))
		d.mov1 += 1
	def OnDialogueOut(self, d):
		global t2, t1
		d.textures[d.PART_FILL] = t2
		d.actual.mode_fill = d.P_TEXTURE
		d.textures[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.Paint()
		advanced.fWave( d.mov2, 0.05, common.Interpolate(d.progress, 0, 2, common.i_accel),  True)
		advanced.fWave( d.mov2, 0.1, common.Interpolate(d.progress, 0, 2, common.i_accel),  False)
		advanced.EndGroup(common.Interpolate(d.progress, 1, 0))
		d.mov2 += 1


class Evento1():
		def OnSyllable(self, sil):
			global p
			p.SetWindow(sil.original._width+1, 1)
			p.SetPosition(
				sil.actual.pos_x+random.randint(8,12)-(random.randint(-2,3)+(sil.original._width*(sil.progress)/4)),
            	(random.randint(1,20)+sil.actual.pos_y)+random.randint(-4,5))

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
		advanced.fBlur1(1, 0.10)

		advanced.EndGroup()