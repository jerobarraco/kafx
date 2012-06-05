# -*- coding: utf-8 -*-
from libs.draw import advanced, extra
from libs import common, video, audio
import cairo, random
from math import pi
from math import ceil
#import gtk
t3 = extra.LoadTexture('textures/barra3.png', extend=cairo.EXTEND_REFLECT) #entrada
t4 = extra.LoadTexture('textures/barra4.png', extend=cairo.EXTEND_REFLECT)
box = extra.LoadTexture('textures/T_Negro05.png', extend=cairo.EXTEND_NONE)
class Efecto():
	def __init__(self):
		self.mwindow = float( min(video.vi.width, video.vi.height )	)
		self.centx = video.vi.width/2
		self.centy = video.vi.height/2
		self.startx = video.vi.width
		self.starty = video.vi.height
		self.rows = int(ceil(video.vi.height /50.0))
		self.cols = int(ceil(video.vi.width /50.0))

	def max_scale(self, picw, pich):
		wr = float(picw)/video.vi.width
		hr = float(pich)/video.vi.height
		rm = max(wr, hr)
		return 1.0/(rm or 1.0)

	def OnDialogueStarts(self, diag):
		text = extra.LoadTexture(diag._text)
		diag.pic = advanced.cSprite(text)
		diag.pic.max_scale = self.max_scale(diag.pic._width,diag.pic._height )#(self.mwindow/msize)
		diag.pic.min_scale = diag.pic.max_scale /4.0
		diag.pic.Scale(diag.pic.max_scale, diag.pic.max_scale)
		diag.pic.y = self.centy
		diag.off = 0.0

	def OnDialogueIn(self, d):
		d.pic.x = self.centx
		d.pic.y = self.centy
		d.pic.color.a = common.Interpolate(d.progress, 0.0, 1.0, common.i_accel)
		for r in range (self.rows):
			for c in range (self.cols):
				posx = c*50
				posy = r*50
				offx = common.Interpolate(d.progress, c*50, 0, common.i_b_ease_in )
				offy = common.Interpolate(d.progress, r*50, 0, common.i_b_ease_in )

				extra.MoveTexture(box, posx+offx, posy+offy)
				d.pic.x = self.centx+offx
				d.pic.y = self.centy+offy
				advanced.StartGroup()
				d.pic.Paint()
				texto = advanced.EndGroup(0)
				video.cf.ctx.set_source(texto)
				video.cf.ctx.mask(box)

	def OnDialogue(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		diag.pic.color.a = 1
		diag.pic.angle = 0.0
		diag.pic.Paint()

	def OnDialogueOut(self, d):
		d.pic.x = self.centx
		d.pic.y = self.centy
		steps = round(common.Interpolate(d.progress, 2, 5), 0)
		advanced.StartGroup()
		d.pic.color.a = common.Interpolate(d.progress, 1.0, 0.0, common.i_b_ease_in)
		d.pic.Paint()
		#d.pic.Scale(xscale, d.pic.max_scale)
		advanced.fGlow(steps, 0.1)
		advanced.EndGroup()

class Subtitulo():
	def OnDialogueIn(self, diag):
		diag.Fade(0, 1)
		diag.Paint()
		diag.PaintReflection()

	def OnDialogue(self, diag):
		diag.PaintWithCache()
		diag.PaintReflection()

class Sub2():
	def OnDialogueIn(self, d):
		d.actual.mode_fill = d.P_DEG_VERT
		d.Fade(0,1)
		d.MoveFrom(-50,0, common.i_b_boing)
		d.Paint()

	def OnDialogue(self, diag):
		diag.actual.mode_fill = diag.P_DEG_VERT
		diag.PaintWithCache()

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

