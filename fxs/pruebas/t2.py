# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun, video
from libs.draw import avanzado, extra
import wave, audioop

audio = wave.open('out.wav', 'r')

"""conf"""
vidfps = 29.976
channels, sampwidth, framerate, nframes, comptype, compname = audio.getparams()
print "Channels %s, Width %s, SampleRate %s, Samples %s, CompType %s, CompName %s" %(channels, sampwidth, framerate, nframes, comptype, compname)

audioFrameSize = int(framerate / vidfps)
color = extra.cCairoColor(numero=0xFFFFFFFF)
maxint = float(2**31)
maxintb= float(2**29)
p = 0.0
frames = ""


class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		global p, color
		diag.actual.color1.Interpolar(p, color)

		diag.Pintar()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		global p, color
		diag.actual.color3.Interpolar(p, color) #Copiamos el color secundario al color primario,
		diag.actual.sombra = 8*p
		diag.Pintar()# Pintamos la silaba en la pantalla

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.saltar_cuadros = False
		#Un efecto si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), comun.Fx(), comun.Fx())
		self.paso = video.vi.width/ float(audioFrameSize)


	def EnCuadroInicia(self):
		global audio, audioFrameSize, maxint, p, sampwidth, paso, maxintb, frames

		frames = audio.readframes(audioFrameSize)
		p = audioop.rms(frames, sampwidth)/maxint
		avanzado.GrupoInicio()

	def EnCuadroFin(self):
		#con esto pintamos el wave
		#cacheamos el contexto
		if not frames: return
 		c = video.cf.ctx

		c.set_line_width(2)
		c.set_source_rgb(1, 0.3, 0.3)
		posx = 0
		posy = 40
		altura = 10.0 #altura máxima en píxeles
 		c.move_to(posx, posy)

		for f in range(audioFrameSize):
			frame = audioop.getsample(frames, sampwidth, f)/maxint
			c.line_to(posx, posy + (altura*frame))
			posx += self.paso

		avanzado.ModoPintado("atop")
		c.stroke()
		avanzado.ModoPintado("over")
		avanzado.GrupoFin()