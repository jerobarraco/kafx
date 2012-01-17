# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun, video
from libs.draw import avanzado, extra
import wave, audioop, cairo

audio = wave.open('out.wav', 'r')

"""conf"""
vidfps = 29.976
channels, sampwidth, framerate, nframes, comptype, compname = audio.getparams()
print "Channels %s, Width %s, SampleRate %s, Samples %s, CompType %s, CompName %s" %(channels, sampwidth, framerate, nframes, comptype, compname)

audioFrameSize = int(framerate / vidfps)
color = extra.cCairoColor(numero=0xFFFFFFFF)
maxint = float(2**31)
maxintb= float(2**29)
frames = ""


class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)

		diag.actual.color3.Interpolar(diag.progreso, diag.actual.color1) #Copiamos el color secundario al color primario,
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
		#self.paso = video.vi.width / float(audioFrameSize)
		self.paso = 1.0


	def EnCuadroInicia(self):
		avanzado.GrupoInicio()
		pass

	def EnCuadroFin(self):
		global audio, audioFrameSize, maxint, sampwidth
		frames = audio.readframes(audioFrameSize)
 		if not frames: return
 		c = video.cf.ctx
		#con esto pintamos el wave
		#cacheamos el contexto
		self.paso = video.vi.width /float(audioFrameSize)

		delta = 10.0 #altura máxima en píxeles
		sfc = extra.CopiarTarget()
		c.set_operator(cairo.OPERATOR_CLEAR)
		c.paint()
		avanzado.ModoPintado()
		posx = 0
		for f in range(audioFrameSize):
			frame = audioop.getsample(frames, sampwidth, f)/maxint
			c.set_source_surface(sfc,  0,  frame*delta)
			c.rectangle(posx, 0, 1,  video.vi.height)
			c.fill()
			posx += self.paso
		avanzado.GrupoFin()