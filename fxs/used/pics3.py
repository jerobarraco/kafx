# -*- coding: utf-8 -*-
from libs.draw import advanced, extra
from libs import common, video, audio
import cairo, random
from math import pi
#import gtk
t3 = extra.LoadTexture('textures/barra3.png', extend=cairo.EXTEND_REFLECT) #entrada
t4 = extra.LoadTexture('textures/barra4.png', extend=cairo.EXTEND_REFLECT)
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

	def OnDialogueIn(self, d):
		d.pic.x = self.centx
		d.pic.y = self.centy
		mov = common.Interpolate(d.progress, 1380, 3480)
		steps = round(common.Interpolate(d.progress, 4, 0), 0)
		extra.MoveTexture(t3, mov, 50)
		advanced.StartGroup()
		#d.pic.color.a = common.Interpolate(d.progress,0.0, 1.0, common.i_b_ease_in)
		d.pic.Paint()
		#advanced.fBiDirBlur(steps=steps)
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

	def OnDialogue(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		diag.pic.color.a = 1
		diag.pic.angle = 0.0
		diag.pic.Paint()

	def OnDialogueOut(self, d):
		d.pic.x = self.centx
		d.pic.y = self.centy
		mov = common.Interpolate(d.progress, 1380, 3480)
		steps = round(common.Interpolate(d.progress, 4, 0), 0)
		extra.MoveTexture(t4, mov, 50)
		advanced.StartGroup()
		d.pic.color.a = common.Interpolate(d.progress,1.0, 0.0, common.i_b_ease_in)
		d.pic.Paint()
		#advanced.fBiDirBlur(steps=steps)
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t4)

class Subtitulo():
	def OnDialogueIn(self, diag):
		diag.Fade(0, 1)
		diag.Paint()
		diag.PaintReflection()

	def OnDialogue(self, diag):
		diag.PaintWithCache()
		diag.PaintReflection()


class Sub2():
	def __init__(self):
		self.parts = advanced.cParticleSystem(png="textures/sakura3.png", max_life=4, emit_parts=1, scale_from=1.0, scale_to=0.3, mode=0)
		#Configuramos la ventana y el angulo
		self.parts.SetWindow(30, 4)
		#self.parts.SetGravity(3.0/4*pi,5 )
		self.parts.SetAngle((3*pi/2.0), 2, pi/2.0)

	def OnDialogueIn(self, d):
		d.actual.mode_fill = d.P_DEG_VERT
		d.Fade(0,1)
		d.MoveFrom(-50,0, common.i_b_boing)
		d.Paint()

	def OnDialogue(self, diag):
		diag.actual.mode_fill = diag.P_DEG_VERT
		diag.PaintWithCache()
		self.parts.SetWindow(diag.original._width, 4)
		self.parts.SetPosition(diag.actual.pos_x+diag.actual.org_x, diag.actual.pos_y+40)
		self.parts.Emit()

	def OnDialogueOut(self, d):
		d.actual.mode_fill = d.P_DEG_VERT
		d.Fade(1, 0)
		d.MoveTo(50, 0 , common.i_b_backstart)
		d.Paint()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 750
		self.out_ms = 750
		self.skip_frames = False
		self.fxs = (Efecto(), Subtitulo(), Sub2())

	def OnFrameEnds(self):
		#advanced.StartGroup()
		advanced.PaintMode("overlay")
		self.fxs[2].parts.Paint()
		advanced.PaintMode('over')
		#advanced.fGlow()
		#advanced.EndGroup()