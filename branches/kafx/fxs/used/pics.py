# -*- coding: utf-8 -*-
from libs.draw import advanced
from libs import common, video, audio
power = 0.0
class Efecto():
	def __init__(self):
		self.mwindow = float( min(video.vi.width, video.vi.height )	)
		self.centx = video.vi.width/2
		self.centy = video.vi.height/2
		self.startx = video.vi.width
		self.starty = video.vi.height

	def OnDialogueStarts(self, diag):
		#texture =extra.LoadTexture(diag._text)
		diag.pic = advanced.cSprite(diag._text)
		msize = max(diag.pic._width,diag.pic._height )
		diag.pic.max_scale = (self.mwindow/msize)
		diag.pic.min_scale = diag.pic.max_scale /4.0
		diag.pic.Scale(diag.pic.max_scale,diag.pic.max_scale)
		diag.pic.y = self.centy

	def OnDialogueIn(self, diag):
		diag.pic.x = common.Interpolate(diag.progress, self.startx, self.centx, common.i_deccel )
		diag.pic.color.a = common.Interpolate(diag.progress, 0.0, 1.0, common.i_deccel)
		scale = common.Interpolate(diag.progress, diag.pic.min_scale, diag.pic.max_scale, common.i_deccel)
		diag.pic.Scale(scale, scale)
		diag.pic.angle = common.Interpolate(diag.progress, 3.14*2, 0.0, common.i_deccel)
		diag.pic.Paint()

	def OnDialogue(self, diag):
		diag.pic.x = self.centx
		diag.pic.y = self.centy
		diag.pic.color.a = 1
		diag.pic.angle = 0.0
		diag.pic.Paint()

	def OnDialogueOut(self, diag):
		diag.pic.x = common.Interpolate(diag.progress, self.centx, 0, common.i_accel )
		scale = common.Interpolate(diag.progress, diag.pic.max_scale, diag.pic.min_scale, common.i_accel)
		diag.pic.Scale(scale, scale)
		diag.pic.color.a = common.Interpolate(diag.progress, 1.0, 0.0, common.i_accel)
		diag.pic.Paint()

class Subtitulo():
	def OnDialogueIn(self, diag):
		diag.Fade(0,1)
		diag.Paint()
	def OnDialogue(self, diag):
		global power
		advanced.StartGroup()
		diag.PaintWithCache()
		advanced.fGlow(opacity=0.3*power)
		advanced.EndGroup()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 500
		self.out_ms = 500
		self.skip_frames = False
		self.fxs = (Efecto(), Subtitulo())
		self.audiodata = audio.Data("in.avi")
		self.paso = video.vi.width / float(self.audiodata.frameSize)

	def OnFrameStarts(self):
		#En cada cuadro
		global power
		#leemos una "linea" de audio (un grupo de muestras para un cuadro de video)
		#very important , mantiene la sincronia del audio con el video
		self.audiodata.read()

		advanced.StartGroup()
		c = video.cf.ctx
		c.set_line_width(2)
		c.set_source_rgb(75/255.0, 0, 130/255.0)
		posx = 0
		posy_base = 40
		posy = posy_base
		altura = 40.0 #altura máxima en píxeles

		c.move_to(posx, posy)
		power = self.audiodata.rms()
		#iteramos cada una de las muestras para este cuadro de video
		for n in range(self.audiodata.frameSize):
			#obtenemos el valor de la muestra numero n
			muestra = self.audiodata.sample(n)
			posy = posy_base + (altura*muestra)
			#y dibujamos una linea, cuya altura depende del valor de la muestra
			c.line_to(posx, posy)
			#y vamos avanzando horizontalmente
			posx += self.paso
		#y pintamos la linea
		c.stroke()
		advanced.fGlow()
		advanced.EndGroup()
