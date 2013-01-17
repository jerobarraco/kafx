# -*- coding: utf-8 -*-
from libs.draw import advanced, extra
from libs import common, video, audio
import cairo, random
from math import pi
#import gtk

class Efecto():
	def __init__(self):
		self.mwindow = float( min(video.vi.width, video.vi.height )	)
		self.centx = video.vi.width/2
		self.centy = video.vi.height/2
		self.startx = video.vi.width
		self.starty = video.vi.height

	def max_scale(self, picw, pich):
		wr = float(picw)/video.vi.width
		hr = float(pich)/video.vi.height
		rm = max(wr, hr)
		return 1.0/(rm or 1.0)

	def OnDialogueStarts(self, diag):
		text = extra.LoadTexture(diag._text)
		diag.pic = advanced.cSprite(text)
		#msize = max(diag.pic._width, diag.pic._height )
		diag.pic.max_scale = self.max_scale(diag.pic._width,diag.pic._height )#(self.mwindow/msize)
		diag.pic.min_scale = diag.pic.max_scale /4.0
		diag.pic.Scale(diag.pic.max_scale, diag.pic.max_scale)
		diag.pic.y = self.centy
		diag.off = 0.0

	def OnDialogueIn(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		advanced.StartGroup()
		#diag.pic.x = common.Interpolate(diag.progress, self.centx, 0, common.i_accel )
		#scale = common.Interpolate(diag.progress, diag.pic.max_scale, diag.pic.min_scale, common.i_accel)
		#diag.pic.Scale(scale, scale)
		diag.pic.color.a = common.Interpolate(diag.progress,0.0, 1.0, common.i_accel)
		diag.pic.Paint()
		tam = common.Interpolate(diag.progress, 20, 0, common.i_accel)
		advanced.fWave(diag.off, amplitude=tam,vertical=False )
		diag.off += 2
		advanced.EndGroup()

	def OnDialogue(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		diag.pic.color.a = 1
		diag.pic.angle = 0.0
		diag.pic.Paint()

	def OnDialogueOut(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		advanced.StartGroup()
		#diag.pic.x = common.Interpolate(diag.progress, self.centx, 0, common.i_accel )
		#scale = common.Interpolate(diag.progress, diag.pic.max_scale, diag.pic.min_scale, common.i_accel)
		#diag.pic.Scale(scale, scale)
		diag.pic.color.a = common.Interpolate(diag.progress, 1.0, 0.0, common.i_accel)
		diag.pic.Paint()
		tam = common.Interpolate(diag.progress, 0, 20, common.i_accel)
		advanced.fWave(diag.off, amplitude=tam )
		diag.off += 2
		advanced.EndGroup()

class Subtitulo():
	def OnDialogueIn(self, diag):
		diag.Fade(0, 1)
		diag.Paint()
		diag.PaintReflection()

	def OnDialogue(self, diag):
		diag.PaintWithCache()
		diag.PaintReflection()

t3 = extra.LoadTexture('textures/barra3.png', extend=cairo.EXTEND_REFLECT) #entrada
t4 = extra.LoadTexture('textures/barra4.png', extend=cairo.EXTEND_REFLECT)
class Sub2():
	def __init__(self):
		self.butter = advanced.cSprite("textures/butterfly.png")
		self.parts = advanced.cParticleSystem(png="textures/star3.png", max_life=3, emit_parts=7, scale_from=1.0, scale_to=0.3, mode=1, max_parts=5000)
		#Configuramos la ventana y el angulo
		self.parts.SetWindow(60, 4)
		self.parts.SetAngle(pi, 3, pi/4.0)

	def OnDialogueIn(self, d):
		d.actual.mode_fill = d.P_DEG_VERT
		mov = common.Interpolate(d.progress, 1380, 3480)
		extra.MoveTexture(t3, mov, 0)
		advanced.StartGroup()
		d.Paint()
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

		x = common.Interpolate(d.progress,-50, video.vi.width+50 )
		y = d.actual.pos_y - d.actual.org_y


		#butterfly
		self.butter.x = x
		self.butter.y = y
		
		self.parts.SetPosition(x-60, y)
		self.parts.Emit()
		self.butter.Paint()

	def OnDialogue(self, diag):
		diag.actual.mode_fill = diag.P_DEG_VERT
		diag.PaintWithCache()

	def OnDialogueOut(self, d):
		d.actual.mode_fill = d.P_DEG_VERT
		d.Fade(1,0)
		d.Paint()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 750
		self.out_ms = 750
		self.skip_frames = False
		self.fxs = (Efecto(), Subtitulo(), Sub2())

	def OnFrameEnds(self):
		advanced.StartGroup()
		self.fxs[2].parts.Paint()
		advanced.fGlow()
		advanced.EndGroup()