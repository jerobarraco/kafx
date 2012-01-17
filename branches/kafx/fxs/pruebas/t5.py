# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun, video, audio

power = 0.0

class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		global power
		diag.actual.color1.Interpolar(power, diag.actual.color3) #Copiamos el color secundario al color primario,
		diag.actual.sombra = power*4
		diag.Pintar()# Pintamos la silaba en la pantalla

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.saltar_cuadros = False
		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), comun.Fx(), comun.Fx())
		self.audiodata = audio.Datos("fma.avi")
		self.paso = video.vi.width / float(self.audiodata.frameSize)

	def EnCuadroInicia(self):
		global power
		self.audiodata.leer()
		power = self.audiodata.rms()
		c = video.cf.ctx
		c.set_line_width(2)
		c.set_source_rgb(0.9, 0.5, 0.6)
		posx = 0
		posy = 40
		altura = 20.0 #altura máxima en píxeles
		c.move_to(posx, posy)

		for n in range(self.audiodata.frameSize):
			muestra = self.audiodata.muestra(n)
			c.line_to(posx, posy + (altura*muestra))
			posx += self.paso
		c.stroke()
