# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin, cos
import random
import cairo



ca = extra.cCairoColor(0xFFE88CE0)#rosita
cb = extra.cCairoColor(0xFF7390AB)#gris

class Efecto():
	def __init__(self):
		self.events = [Evento1(),Evento1b(),Evento2(),Evento2b(),Evento3()]

	def OnSyllableStarts(self, sil):
		global ca, cb
		sil.actual.mode_fill = sil.P_DEG_VERT

class Evento3():
		def OnSyllable(self, sil):

			global ca, cb

			sil.actual.mode_fill = sil.P_DEG_VERT
			advanced.StartGroup()
			sil.Paint()
			advanced.fBlur1(1, ((sin(pi*sil.progress))/10.0))
			advanced.fGlow(1, ((sin(pi*sil.progress))/8.0))
			advanced.EndGroup()

		def SyllableTime(self, sil):
			return (sil._start, sil._end)#sil._start+((sil._end-sil._start)/2.0)

class Evento1():
		def OnSy1(self, s, pro):

			global ca, cb
			s.progress = pro
			s.actual.color1.CopyFrom(s.actual.color4)
			s.actual.color2.CopyFrom(s.actual.color3)
			s.actual.mode_fill = s.P_DEG_VERT
			s.Fade(0, 1)
			s.Paint()

		def OnSyllable(self, sil):
			sil.Chain(self.OnSy1, duration = 150)

		def SyllableTime(self, sil):
			return (sil._parent._start-600, sil._parent._start-200)





class Evento1b():
		def OnSyllable(self, sil):

			global ca, cb
			sil.actual.color1.CopyFrom(sil.actual.color4)
			sil.actual.color2.CopyFrom(sil.actual.color3)
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._parent._start-200, sil._start)

class Evento2():
		def OnSyllable(self, sil):

			global ca, cb
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._end, sil._parent._end-200)

class Evento2b():
		def OnSyllable(self, sil):

			global ca, cb
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.Fade(1, 0)
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._parent._end-200, sil._parent._end+200)

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Efecto(),Efecto())

	def OnFrameStarts(self):
		advanced.StartGroup()



	def OnFrameEnds(self):
		micolor = extra.cCairoColor()
		factual = video.cf.framen
		if factual<=1072:
			micolor.CopyFrom(ca)
		elif 1073<=factual<=1256:
			micolor.CopyFrom(cb)


		elif 1257<=factual<=1330:
			micolor.CopyFrom(ca)
			micolor.Interpolate((1330-factual)/float(1330-1257), cb)

		elif 1331<=factual<= 2159:
			micolor.CopyFrom(ca)


		pat = advanced.EndGroup()
		ctx = video.cf.ctx
		ctx.set_source_rgba(micolor.r, micolor.g, micolor.b ,micolor.a)
		ctx.rectangle(0,0, video.vi.width, video.vi.height)
		advanced.PaintMode("screen")
		ctx.mask(pat)

		advanced.PaintMode("over")

