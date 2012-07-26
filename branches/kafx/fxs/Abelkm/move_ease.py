# -*- coding: utf-8 -*-
#FX made by Abelkm. Use for learning only!
from libs import common
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


t1 = extra.LoadTexture('textures/blue_g22223.png', extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture('textures/g1.png', extend=cairo.EXTEND_REFLECT) #gold_1.png
t3 = extra.LoadTexture('textures/T_Negro22.png', extend=cairo.EXTEND_REFLECT)
class FX1(common.Fx):
	def __init__(self):
		self.events = [Evento1(),Evento1_b(), Evento1_c(),Evento2(),Evento3(), Evento2b()]
	def OnDialogueStarts(self, d):
		d.chars = []
		for silaba in d._syllables:
			silaba.SplitLetters()
			d.chars.extend(silaba._letters)


class Evento2():
		def AnimationIn(self, d, prog):
			d.progress = prog
   			d.actual.color1.a = 0
			d.textures[d.PART_BORDER] = t1
			d.actual.mode_border = d.P_TEXTURE
			d.actual.border = 4
			d.actual.color3.a = common.Interpolate(d.progress, 0, 1)
			advanced.StartGroup()
			d.Paint()
			advanced.fBlur1(2, 0.25)
			advanced.EndGroup()
			d.Restore()
			d.textures[d.PART_FILL] = t3
			d.actual.mode_fill = d.P_TEXTURE
			d.actual.color1.a = common.Interpolate(d.progress, 0, 1)
			d.actual.color3.a = common.Interpolate(d.progress, 0, 1)
			d.Paint()


		def OnDialogue(self, d):
			common.Chain(500, d.progress, d.chars, self.AnimationIn, 100)

		def DialogueTime(self, d):
			return (d._start-120, d._start+400)

class Evento2b():
		def OnSyllable(self, d):

   			d.actual.color1.a = 0
			d.textures[d.PART_BORDER] = t1
			d.actual.mode_border = d.P_TEXTURE
			d.actual.border = 4
			advanced.StartGroup()
			d.Paint()
			advanced.fBlur1(2, 0.25)
			advanced.EndGroup()
			d.Restore()
			d.textures[d.PART_FILL] = t3
			d.actual.mode_fill = d.P_TEXTURE
			d.Paint()

		def SyllableTime(self, sil):
			return (sil._parent._start+400, sil._parent._end-400)


class Evento3():
		def AnimationIn(self, d, prog):
			d.progress = prog
   			d.actual.color1.a = 0
			d.textures[d.PART_BORDER] = t1
			d.actual.mode_border = d.P_TEXTURE
			d.actual.border = 4
			d.actual.color3.a = common.Interpolate(d.progress, 1, 0)
			advanced.StartGroup()
			d.Paint()
			advanced.fBlur1(2, 0.25)
			advanced.EndGroup()
			d.Restore()
			d.textures[d.PART_FILL] = t3
			d.actual.mode_fill = d.P_TEXTURE
			d.actual.color1.a = common.Interpolate(d.progress, 1, 0)
			d.actual.color3.a = common.Interpolate(d.progress, 1, 0)
			d.Paint()



		def OnDialogue(self, d):
			common.Chain(500, d.progress, d.chars, self.AnimationIn, 100)

		def DialogueTime(self, d):
			return (d._end-400, d._end+100)




class Evento1():
		def OnLetter(self, l):
			global t2
			l.textures[l.PART_FILL] = t2
			l.actual.mode_fill = l.P_TEXTURE
			advanced.StartGroup()
			l.Paint()
			advanced.fBlur1(1, 0.10)
			advanced.fGlow(2, 0.10)

			advanced.EndGroup()

		def LetterTime(self, l):
			return (l._start, l._end)

class Evento1_b():
		def OnLetter(self, l):
			global t2
			l.textures[l.PART_FILL] = t2
			l.actual.mode_fill = l.P_TEXTURE
			advanced.StartGroup()
			l.Paint()
			advanced.fBlur1(1, 0.10)
			advanced.fGlow(2, 0.10)

			advanced.EndGroup(common.Interpolate(l.progress, 1, 0, common.i_b_ease_out))

		def LetterTime(self, l):
			#return (l._start, l._parent._end+90)
			sil_padre = l._parent
			if sil_padre._indice == len(sil_padre._parent._syllables)-1:
				vall = 90

			else:
   				vall = 400
   			return (l._end, l._end+vall)

class Evento1_c():
		def OnLetter(self, l):
			global t2
			l.textures[l.PART_FILL] = t2
			l.actual.mode_fill = l.P_TEXTURE
			advanced.StartGroup()
			l.Paint()
			advanced.fBlur1(1, 0.10)
			advanced.fGlow(2, 0.10)

			advanced.EndGroup(common.Interpolate(l.progress, 0, 1, common.i_b_ease_out))

		def LetterTime(self, l):
			return (l._start-100, l._start)


class FxsGroup(common.FxsGroup):
	def __init__(self):
		#self.in_ms = 300
		#self.out_ms = 100
		self.split_letters = True
		self.fxs = (FX1(), FX1())

