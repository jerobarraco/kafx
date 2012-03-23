# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos

t1 = extra.LoadTexture('textures/sangre3.png', extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture('textures/clouds2.png', extend=cairo.EXTEND_REFLECT)
class FX1(common.Fx):



	def OnDialogueOut(self, d):
		global t1
		d.actual.border = 0
		d.actual.color1.a = common.Interpolate(d.progress, 1,0, common.i_accel)
		d.actual.mode_fill = d.P_DEG_VERT
		d.Paint()
		d.Restore()
		d.textures[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.actual.border = 0.1
		d.actual.color1.a = 0
		d.actual.color3.a = common.Interpolate(d.progress, 1,0, common.i_accel)
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3+common.Interpolate(d.progress, 0,3, common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , 3+common.Interpolate(d.progress, 0,3, common.i_accel), 0.45)
		advanced.EndGroup(common.Interpolate(d.progress, 1,0, common.i_accel))

	def OnSyllableDead(self, d):
		global t1
		d.actual.border = 0
		d.actual.mode_fill = d.P_DEG_VERT
		d.Paint()
		d.Restore()
		d.textures[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.actual.border = 0.1
		d.actual.color1.a = 0
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3, 0.45)
		advanced.fDirBlur(pi*-1/2 , 3, 0.45)
		advanced.EndGroup()

	def OnSyllable(self, d):
		global t2, t1
		d.actual.border = 0
		d.actual.mode_fill = d.P_DEG_VERT
		d.actual.scale_x = d.actual.scale_y = 1+common.Interpolate(d.progress, 0, 0.25, common.i_b_boing)
		d.Paint()
		d.Restore()
		d.textures[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.actual.border = 0.1
		d.actual.color1.a = 0
		d.actual.scale_x = d.actual.scale_y = 1+common.Interpolate(d.progress, 0, 0.25, common.i_b_boing)
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3, 0.45)
		advanced.fDirBlur(pi*-1/2 , 3, 0.45)
		advanced.EndGroup(common.Interpolate(d.progress, 1,0, common.i_accel))
		d.Restore()
		d.textures[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.actual.border = 0.1
		d.actual.color1.a = 0
		d.actual.scale_x = d.actual.scale_y = 1+common.Interpolate(d.progress, 0, 0.25, common.i_b_boing)
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3, 0.45)
		advanced.fDirBlur(pi*-1/2 , 3, 0.45)
		advanced.EndGroup(common.Interpolate(d.progress, 0,1, common.i_accel))

	def OnSyllableSleep(self, d):
		global t2
		d.actual.border = 0
		d.actual.mode_fill = d.P_DEG_VERT
		d.Paint()
		d.Restore()
		d.textures[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURE
		advanced.StartGroup()
		d.actual.border = 0.1
		d.actual.color1.a = 0
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3, 0.45)
		advanced.fDirBlur(pi*-1/2 , 3, 0.45)
		advanced.EndGroup()


	def OnDialogueIn(self, d):
		global t2
		d.actual.border = 0
		d.actual.color1.a = common.Interpolate(d.progress, 0,1)
		d.actual.mode_fill = d.P_DEG_VERT
		d.Paint()
		d.Restore()
		d.textures[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURE
		d.actual.border = 0.1
		d.actual.color3.a = common.Interpolate(d.progress, 0,1, common.i_accel)
		d.actual.color1.a = 0
		advanced.StartGroup()
		d.Paint()
		advanced.fGlow(steps=3, opacity=0.10)
		advanced.fDirBlur(pi*1/2 , 3+common.Interpolate(d.progress, 3,0, common.i_accel), 0.45)
		advanced.fDirBlur(pi*-1/2 , 3+common.Interpolate(d.progress, 3,0, common.i_accel), 0.45)
		advanced.EndGroup()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 100
		self.out_ms = 100
		self.fxs = (FX1(), FX1())
		self.skip_frames = False

	def OnFrameStarts(self):
		advanced.StartGroup()
		advanced.fTimeBlur(0.25)

	def OnFrameEnds(self):

		advanced.EndGroup()
