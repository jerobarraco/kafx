from libs.draw import avanzado, extra
from libs import comun, video, audio
from math import pi, cos, sin

import numpy
class Fxpart (comun.Fx):
	def EnSilaba(self, sil): sil.PintarConCache()
	EnDialogo = EnSilaba

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart(), ]
		self.saltar_cuadros = False
		self.syl_in_ms = 400
		self.syl_out_ms = 400
		self.psys =  avanzado.cParticleSystem( png="textures/T_Negro2.png",
			max_life=1, max_parts=2000, emit_parts=4, scale_from= 0.6, scale_to=1, modo=1, rotation=0,
			color=extra.cCairoColor(numero=0xFFA060F0))
		self.psys.DarAngulo(pi, 0.0, pi/2.0)
		self.psys.DarVentana(0, 0)
		self.psys.DarGravedad(pi, 00)#1.5=3/2
		self.audiodata = audio.Datos("fma.avi")

	def EnCuadroInicia(self):
		self.audiodata.leer()
		rms = self.audiodata.rms()
		rad = 50+(rms * 100)
		for i in range(30):
			x = 250 + cos(pi/15.0*i)*rad
			y = 250 + sin(pi/15.0*i)*rad
			self.psys.DarPosicion(x, y)
			self.psys.Emitir()
		self.psys.Pintar()

		frames = numpy.fromstring(self.audiodata.frames, numpy.int32)
		fft = numpy.log10(numpy.absolute(numpy.fft.fft(frames)))
		x = 0
		c = video.cf.ctx
		c.set_line_width(1)
		c.set_source_rgb(0.9, 0.5, 0.6)
		for i in fft[:len(fft)/2]:
			c.line_to(x, 300-(i*20.0))
			x+=0.50
		c.stroke()
