# -*- coding: utf-8 -*-
#FX made by Abelkm. Use for learning only!
from libs import common
from libs.draw import advanced, extra, basic
import math, random, cairo
from math import pi, sin, cos



class FX1():
	def __init__(self):
		self.events = [Event1(),Event2(),Event3()]
	def OnDialogueStarts(self, d):
		d.chars = []
		for silaba in d._syllables:
			silaba.SplitLetters()
			d.chars.extend(silaba._letters)

	def OnSyllable(self, sil):

		sil.actual.color1.r = 0
		sil.actual.color1.b = 0
		sil.actual.color1.g = 0

		sil.Scale(1, common.Interpolate(sil.progress, 1.5, 1), common.i_accel)
		sil.actual.pos_x = sil.actual.pos_x + random.randint(-2,2)
		sil.actual.pos_y = sil.actual.pos_y + random.randint(-2,2)
		sil.actual.border = 0

		advanced.StartGroup()
		advanced.PaintMode('overlay')
		sil.Paint()
		advanced.fBlur1(1, 0.35)
		advanced.fGlow(1, 0.05)

		advanced.EndGroup(common.Interpolate(sil.progress, 0.8, 0.4, common.i_b_ease_out))


		sil.actual.mode_fill = sil.P_DEG_RAD
		sil.actual.color1.r = 0.9
		sil.actual.color1.b = 0.3
		sil.actual.color1.g = 0.3
		sil.actual.color2.r = 0.7
		sil.actual.color2.b = 0.7
		sil.actual.color2.g = 0.7
		sil.Scale(1, common.Interpolate(sil.progress, 1.5, 1), common.i_accel)
		sil.actual.pos_x = sil.actual.pos_x + random.randint(-2,2)
		sil.actual.pos_y = sil.actual.pos_y + random.randint(-2,2)

		advanced.StartGroup()
		advanced.PaintMode('over')
		sil.Paint()
		advanced.fBlur1(1, 0.35)
		advanced.fGlow(1, 0.05)

		advanced.EndGroup(common.Interpolate(sil.progress, 1, 0.4, common.i_b_ease_out))


class Event2():
	def AnimationIn(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.Scale(1.5, 1 )
		d.Fade(0,0.85)
		d.Paint()

	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationIn, 50)

	def DialogueTime(self, d):
		return (d._start-100, d._start+400)

class Event1():
	def AnimationD(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.Alpha(0.85)

		d.Paint()



	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationD, 50)

	def DialogueTime(self, d):
		return (d._start+400, d._end-400)
class Event3():
	def AnimationOut(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.Scale(1, 1.5 )
		d.Fade(0.85,0)
		d.Paint()



	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationOut, 50)

	def DialogueTime(self, d):
		return (d._end-400, d._end+300)

class FX2():
	def __init__(self):
		self.events = [Event1(),Event2(),Event3()]
	def OnDialogueStarts(self, d):
		d.chars = []
		for silaba in d._syllables:
			silaba.SplitLetters()
			d.chars.extend(silaba._letters)

	def OnSyllable(self, sil):

		sil.actual.color1.r = 1
		sil.actual.color1.b = 1
		sil.actual.color1.g = 1
		sil.actual.scale_y = common.Interpolate(sil.progress, 1, 1.55, common.i_b_boing)
		sil.actual.scale_x = common.Interpolate(sil.progress, 1, 1.55, common.i_b_boing)
		
		sil.actual.pos_x = sil.actual.pos_x + random.randint(-2,2)
		sil.actual.pos_y = sil.actual.pos_y + random.randint(-2,2)
		sil.actual.border = 0

		advanced.StartGroup()
		advanced.PaintMode('overlay')
		sil.Paint()
		advanced.fBlur1(1, 0.35)
		advanced.fGlow(1, 0.05)

		advanced.EndGroup(common.Interpolate(sil.progress, 0.8, 0.4, common.i_b_ease_out))


		sil.actual.mode_fill = sil.P_DEG_RAD
		sil.actual.color1.r = 0.4
		sil.actual.color1.b = 0.9
		sil.actual.color1.g = 0.6
		sil.actual.color2.r = 1
		sil.actual.color2.b = 1
		sil.actual.color2.g = 1
		sil.actual.scale_y = common.Interpolate(sil.progress, 1, 1.55, common.i_b_boing)
		sil.actual.scale_x = common.Interpolate(sil.progress, 1, 1.55, common.i_b_boing)
		sil.actual.pos_x = sil.actual.pos_x + random.randint(-2,2)
		sil.actual.pos_y = sil.actual.pos_y + random.randint(-2,2)

		advanced.StartGroup()
		advanced.PaintMode('over')
		sil.Paint()
		advanced.fBlur1(1, 0.35)
		advanced.fGlow(1, 0.05)

		advanced.EndGroup(common.Interpolate(sil.progress, 0.8, 0.4, common.i_b_ease_out))


class Event2():
	def AnimationIn(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.actual.scale_y = common.Interpolate(d.progress, 1.5, 1, common.i_b_ease_in)
		d.actual.scale_x = common.Interpolate(d.progress, 1.5, 1, common.i_b_ease_in)
		d.Fade(0,0.85)
		d.Paint()

	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationIn, 150)

	def DialogueTime(self, d):
		return (d._start-100, d._start+400)

class Event1():
	def AnimationD(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.Alpha(0.85)

		d.Paint()



	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationD, 150)

	def DialogueTime(self, d):
		return (d._start+400, d._end-400)
class Event3():
	def AnimationOut(self, d, prog):
		d.progress = prog
		d.actual.mode_fill = d.P_DEG_VERT
		d.actual.scale_y = common.Interpolate(d.progress, 1, 1.5, common.i_b_ease_out)
		d.actual.scale_x = common.Interpolate(d.progress, 1, 1.5, common.i_b_ease_out)
		d.Fade(0.85,0)
		d.Paint()



	def OnDialogue(self, d):
		common.Chain(500, d.progress, d.chars, self.AnimationOut, 150)

	def DialogueTime(self, d):
		return (d._end-400, d._end+300)




class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.split_letters = True
		skip_frames = False
		self.fxs = (FX1(), FX2())

	def OnFrameStarts(self):
		advanced.StartGroup()
		advanced.fTimeBlurStart(0.5)

	def OnFrameEnds(self):
		advanced.fTimeBlurEnd()
		advanced.EndGroup()