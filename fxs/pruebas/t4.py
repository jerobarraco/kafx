# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import common, video
from libs.draw import advanced, extra
import audioop, cairo
import subprocess as s

"""conf"""
vidfps = 29.970
videof  = "tos open2.avi"
#channels, sampwidth, framerate, nframes, comptype, compname = audio.getparams()
sampwidth= 4
framerate = 44100
#print "Channels %s, Width %s, SampleRate %s, Samples %s, CompType %s, CompName %s" %(channels, sampwidth, framerate, nframes, comptype, compname)

audioFrameSize = int(framerate / vidfps) #4bytes
color = extra.cCairoColor(numero=0xFFFFFFFF)
maxint = float(2**31)
maxintb= float(2**29)
frames = ""
power = 0.0
args = [
	#video to decode
	'ffmpeg',  '-i', videof,
	#pipe data
	'-vn',  '-acodec', 'pcm_s32le', '-ac', '1', '-ar' , str(framerate), '-ab', '32', '-f', 'wav',
	'-y', '-' #-y IS important
	]

p=s.Popen(args, bufsize=audioFrameSize*sampwidth, stdout=s.PIPE, stdin=open("fakein.txt"),  stderr=open('audioerr.txt', 'w'))

class EfectoGenerico(common.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		global power
		diag.actual.color3.Interpolar(power, diag.actual.color1) #Copiamos el color secundario al color primario,
		diag.actual.sombra = power*4
		diag.Pintar()# Pintamos la silaba en la pantalla

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.saltar_cuadros = False
		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), common.Fx(), common.Fx())
		self.paso = video.vi.width / float(audioFrameSize)
		#self.paso = 1.0


	def EnCuadroInicia(self):
		global audio, audioFrameSize, maxintb, sampwidth, power
		#frames = audio.readframes(audioFrameSize)
		frames = p.stdout.read(audioFrameSize*sampwidth)
		power = audioop.rms(frames, sampwidth)/maxintb
		if frames:
			c = video.cf.ctx
			c.set_line_width(2)
			c.set_source_rgb(0.9, 0.5, 0.6)
			posx = 0
			posy = 40
			altura = 20.0 #altura máxima en píxeles
	 		c.move_to(posx, posy)

			for f in range(audioFrameSize):
				frame = audioop.getsample(frames, sampwidth, f)/maxint
				c.line_to(posx, posy + (altura*frame))
				posx += self.paso
			c.stroke()
