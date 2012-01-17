# -*- coding: utf-8 -*-
from libs import comun, audio, video
from libs.draw import extra, avanzado
import random
from math import pi, cos, sin, hypot, atan2

power = 0.0
class Fxpart (comun.Fx):
	def EnSilaba(self, sil): sil.PintarConCache()
	EnDialogo = EnSilaba

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart(), comun.Fx()]
		self.saltar_cuadros = False
		self.syl_in_ms = 400
		self.syl_out_ms = 400
		self.psys =  avanzado.cParticleSystem(png="texturas/star2.png",
		max_life=2, max_parts=2000, emitir_parts=1, escala_de= 0.4, escala_a=1, modo=1, rotacion=0)
		self.psys.DarAngulo(2*pi, 0.5, 2*pi)
		self.psys.DarVentana(2, 2)
		self.psys.DarGravedad(pi*1.5, 0)#1.5=3/2
		
		self.audiodata = audio.Datos("fma.avi")
		#calculamos el espacio entre punto y punto en el video
		#self.audiodata.frameSize indica la cantidad de muestras que el audio para un cuadro de video
		self.paso = video.vi.width / float(self.audiodata.frameSize)
		
	def EnCuadroInicia(self):
		#En cada cuadro
		global power
		#leemos una "linea" de audio (un grupo de muestras para un cuadro de video)
		#very important , mantiene la sincronia del audio con el video
		self.audiodata.leer()

		c = video.cf.ctx
		c.set_line_width(2)
		c.set_source_rgb(0.9, 0.5, 0.6)
		posx = 0
		posy_base = 40
		posy = posy_base
		altura = 20.0 #altura máxima en píxeles

		c.move_to(posx, posy)
		#iteramos cada una de las muestras para este cuadro de video
		for n in range(self.audiodata.frameSize):
			#obtenemos el valor de la muestra numero n
			muestra = self.audiodata.muestra(n)
			posy = posy_base + (altura*muestra)
			if (abs(muestra)) > 0.85:
				self.psys.DarPosicion(posx, posy)
				self.psys.Emitir()

			#y dibujamos una linea, cuya altura depende del valor de la muestra
			c.line_to(posx, posy)
			#y vamos avanzando horizontalmente
			posx += self.paso
		#y pintamos la linea
		c.stroke()
		avanzado.GrupoInicio()
		self.psys.Pintar()
		avanzado.fGlow()
		avanzado.GrupoFin()