# -*- coding: utf-8 -*-
#FX made by Abelkm. Use for learning only!
from libs import common
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


t1 = extra.LoadTexture('textures/cloud.png', extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture('textures/ror42.png', extend=cairo.EXTEND_REFLECT)
class FX1(common.Fx):
	def __init__(self):
		self.events = [Evento1(), Evento2()]

	def OnDialogue(self, d):
		global t1
		d.actual.border = 1
		d.Paint()
		d.actual.border = 0
		d.actual.color1.a = 0.6
		d.textures[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURE
		d.MoveTexture( common.Interpolate(d.progress, 90, 290), common.Interpolate(d.progress, 70, 150), part = d.PART_FILL)
		d.Paint()

	def OnDialogueIn(self, d):
		global t1
		d.actual.border = 1
		d.actual.color1.a = common.Interpolate(d.progress, 0, 1)
		d.actual.color3.a = common.Interpolate(d.progress, 0, 1)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(pi*1/2 , common.Interpolate(d.progress, 5,0,common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , common.Interpolate(d.progress, 5,0,common.i_accel), 0.45)
		advanced.EndGroup()
		d.actual.border = 0
		d.actual.color1.a = common.Interpolate(d.progress, 0, 0.6)
		d.actual.color3.a = common.Interpolate(d.progress, 0, 1)
		d.textures[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURE
		d.MoveTexture( common.Interpolate(d.progress, 80, 90), common.Interpolate(d.progress, 60, 70), part = d.PART_FILL)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(pi*1/2 , common.Interpolate(d.progress, 5,0,common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , common.Interpolate(d.progress, 5,0,common.i_accel), 0.45)
		advanced.EndGroup()

	def OnDialogueOut(self, d):
		global t1
		d.actual.border = 1
		d.actual.color1.a = common.Interpolate(d.progress, 1, 0)
		d.actual.color3.a = common.Interpolate(d.progress, 1, 0)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(pi*1/2 , common.Interpolate(d.progress, 0,5,common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , common.Interpolate(d.progress, 0,5,common.i_accel), 0.45)
		advanced.EndGroup()

		d.actual.border = 0
		d.actual.color1.a = common.Interpolate(d.progress, 0.6, 0)
		d.actual.color3.a = common.Interpolate(d.progress, 1, 0)
		d.textures[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURE
		d.MoveTexture( common.Interpolate(d.progress,290, 300), common.Interpolate(d.progress, 150, 160), part = d.PART_FILL)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(pi*1/2 , common.Interpolate(d.progress, 0,5,common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , common.Interpolate(d.progress, 0,5,common.i_accel), 0.45)
		advanced.EndGroup()



class Evento1():
		def OnLetter(self, l):

			global t2
			l.textures[l.PART_FILL] = t2
			l.actual.mode_fill = l.P_TEXTURE
			l.textures[l.PART_BORDER] = t2
			l.actual.mode_border = l.P_TEXTURE
			#advanced.StartGroup()
			l.Fade(0, 1, common.i_b_backstart)
			l.Paint()
			#advanced.fBlur1(1, ((sin(pi*sil.progress))/10.0))
			#advanced.fGlow(1, ((sin(pi*sil.progress))/8.0))
			#advanced.EndGroup(common.Interpolate(sil.progress, 0,1,common.i_accel))

		def LetterTime(self, l):
  			return (l._start-90, l._start)
class Evento2():
		def OnLetter(self, l):
			global t2
			l.textures[l.PART_FILL] = t2
			l.actual.mode_fill = l.P_TEXTURE
			l.textures[l.PART_BORDER] = t2
			l.actual.mode_border = l.P_TEXTURE
			l.actual.border = 1
			advanced.StartGroup()
			l.Paint()
			advanced.fBlur1(1, ((sin(pi*l.progress))/10.0))
			advanced.fGlow(1, ((sin(pi*l.progress))/8.0))
			advanced.EndGroup(common.Interpolate(l.progress, 1,0,common.i_accel))
		def LetterTime(self, l):
			vall = common.Interpolate(l.progress, 600,0)
			return (l._start, l._end+vall)
class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 100
		self.out_ms = 100
		self.split_letters = True
		self.fxs = (FX1(), FX1())

