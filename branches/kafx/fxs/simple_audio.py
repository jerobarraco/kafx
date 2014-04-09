# -*- coding: utf-8 -*-
"""Como utilizar los datos de audio de un archivo externo"""
from libs import common, video, audio

power = 0.0

class EfectoGenerico(common.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		global power #Tomamos el power del sonido (es una variable global)
		#Copiamos el color secundario al color primario,
		#usamos el power como modificador del avance del effect
		diag.actual.color3.Interpolar(power, diag.actual.color1)
		#y ponemos una sombra que dependa del power
		#(esto es lo mismo que poner)
		#diag.actual.sombra = comun.Interpolar(power, 0, 4)
		diag.actual.sombra = power*5
		diag.Pintar()# Pintamos la silaba en la pantalla

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(common.FxsGroup):
	def __init__(self):
	
		self.skip_frames = False
		
		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), EfectoGenerico(), EfectoGenerico())
		#hasta aca deberian saber que es

		#Creamos un objeto audiodata, para manejar el audio
		#le pasamos por parametro el nombre de archivo de donde tomaremos el audio
		fname = "audio.mp3" 
		try:
			import __main__
			if __main__.conf_module:
				print ('loading data from main module')
				if __main__.conf_module.audio_in:
					fname =__main__.conf_module.audio_in
				else:
					fname =__main__.conf_module.video_in
		except:
			pass
		
		self.audiodata = audio.Data(fname)
		#calculamos el espacio entre punto y punto en el video
		
		#self.audiodata.frameSize indica la cantidad de muestras que el audio para un cuadro de video
		self.paso = video.vi.width / float(self.audiodata.frameSize)

	def OnFrameStarts(self):
		#leemos una "linea" de audio (un grupo de muestras para un cuadro de video)
		#very important , mantiene la sincronia del audio con el video
		self.audiodata.read()
		#calculamos el power (RMS) del audio
		power = self.audiodata.rms()

		c = video.cf.ctx
		c.set_line_width(3)
		#c.set_source_rgb(0.29411765, 0., 0.50980392)
		c.set_source_rgb(0.43529412, 0., 0.999999999)
		posx = 0
		posy = 360
		altura = 200.0 #altura máxima en píxeles
		
		c.move_to(posx, posy)
		#iteramos cada una de las muestras para este cuadro de video
		for n in range(self.audiodata.frameSize):
			#obtenemos el valor de la muestra numero n
			muestra = self.audiodata.sample(n)
			#y dibujamos una linea, cuya altura depende del valor de la muestra
			c.line_to(posx, posy + (altura*muestra))
			#y vamos avanzando horizontalmente
			posx += self.paso
		#y pintamos la linea
		c.stroke()