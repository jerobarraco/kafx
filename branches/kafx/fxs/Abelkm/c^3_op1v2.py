# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin, cos
import random
import cairo

t1 = extra.LoadTexture('textures/barra_c31.png') #entrada
t2 = extra.LoadTexture('textures/barra_c32.png') #salida

ca = extra.cCairoColor(0xFFE88CE0)#rosita
cb = extra.cCairoColor(0xFF7390AB)#gris
#lo empeore...
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

		def OnDialogue(self, diag):
			global ca, cb, t1
			diag.actual.color1.CopyFrom(diag.actual.color4)
			diag.actual.color2.CopyFrom(diag.actual.color3)
			diag.actual.mode_fill = diag.P_DEG_VERT
			mov = common.Interpolate(diag.progress,1380, 3480)
			extra.MoveTexture(t1, mov, 50)
			advanced.StartGroup()
			diag.Paint()
			texto = advanced.EndGroup(0)
			video.cf.ctx.set_source(texto)
			video.cf.ctx.mask(t1) #empieza 556 y se ve 560

		def DialogueTime(self, diag):
			return (diag._start-100, diag._start+600)





class Evento1b():
		def OnSyllable(self, sil):

			global ca, cb
			sil.actual.color1.CopyFrom(sil.actual.color4)
			sil.actual.color2.CopyFrom(sil.actual.color3)
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._parent._start+600, sil._start)

class Evento2():
		def OnSyllable(self, sil):
			global ca, cb
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._end, sil._parent._end-700)

class Evento2b():
		def OnDialogue(self, diag):
			global ca, cb, t2
			diag.actual.mode_fill = diag.P_DEG_VERT
			mov = common.Interpolate(diag.progress,1380, 3480)#(diag.progress,1380, 3480)
			extra.MoveTexture(t2, mov, 50)
			advanced.StartGroup()
			diag.Paint()
			texto = advanced.EndGroup(0)
			video.cf.ctx.set_source(texto)
			video.cf.ctx.mask(t2)

		def DialogueTime(self, diag):
			return (diag._end-700, diag._end+100)

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

