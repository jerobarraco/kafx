# -*- coding: utf8 -*-
from libs.draw  import extra, advanced
from libs import common
from math import pi, sin

class Kara2(common.Fx):
	def __init__(self):
		#Creamos el sistema d particulas que usaremos en dos dialogues
		self.parts = advanced.cParticleSystem(png="textures/snowflake1.png",
			max_life=2, max_parts=30, emit_parts=2, scale_from=0.2, scale_to=0.03,
			color=extra.cCairoColor(0x88FFFFFF), modo=1)
		#Le damos una direccion de 90º, 2 pixels por cuadro y 0.5 radianes de diferencia posible
		self.parts.DarAngulo(pi/2.0, 2, 0.5)
		
	def EnSilabaInicia(self, s):
		s.ModoRelleno(s.P_DEG_VERT)

	def EnDialogoEntra(self, diag):
		diag.ModoRelleno(diag.P_DEG_VERT)
		diag.Fade(0, 1)
		diag.Pintar()
		#Lo restauramos para los demás EnDialogo*
		diag.ModoRelleno(diag.P_SOLIDO)

	#Dado que EnSilabaDorm y EnSilabaMuerta no hacen modificaciones al texto
	#podemos usar PintarConCache en ambas

	def EnSilabaDorm(self, diag):
		diag.PintarConCache()

	def EnSilabaMuerta(self, diag):
		diag.PintarConCache()

	def EnSilaba(self, diag):
		if diag._texto.strip() =="":
			return
		#Calculamos la posicion de forma que vaya recorriendo desde arriba hasta abajo de la silaba
		x = diag.actual.pos_x+(diag.original._ancho/2.0)
		y = (diag.progreso*diag.original._alto)+ diag.actual.pos_y-diag.original._alto
		#y le damos esa posicion al emitter
		self.parts.DarPosicion(x, y)
		#y le decimos que tenga una ventana maxima del ancho de las silabas
		self.parts.DarVentana(diag.original._ancho, 2)
		self.parts.Emitir()
		
class Kara1(common.Fx):
	def __init__(self):
		#angulo de rotacion
		self.ang = pi /3.0
		#angulo maximo de la funcion seno
		self.ang2 = 2.0*pi

	def EnSilaba(self, diag):
		#cambiamos el angulo segun el angulo máximo,
		#por la funcion seno del otro angulo modificado por el progreso
		diag.actual.angulo = self.ang*sin(diag.progreso*self.ang2)
		diag.Pintar()
		
	def EnSilabaMuerta(self, diag):
		diag.PintarConCache()
		
	def EnSilabaDorm(self, diag):
		diag.PintarConCache()

	def EnDialogoSale(self, diag):
		diag.Fade(1, 0)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		diag.Pintar()

class Cred(common.Fx):
	def EnDialogo(self, diag):
		diag.PintarConCache()

	def EnDialogoSale(self, diag):
		diag.Fade(1, 0)
		diag.MoveTo(0, 30)
		diag.Pintar()
		
	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		diag.MoveFrom(0, 30)
		diag.Pintar()

class Trad(common.Fx):
	def EnDialogo(self, diag):
		diag.PintarConCache()

	def EnDialogoSale(self, diag):
		diag.Fade(1, 0)
		#una scale que va a ir de 1 a 2 (0<=progreso<=1)
		diag.actual.scale_y  = 1+diag.progreso
		advanced.StartGroup()
		diag.Pintar()
		advanced.fBiDirBlur(pi/2.0, 5)
		advanced.EndGroup()

	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		advanced.StartGroup()
		#una scale que va a ir de 2 a 1
		diag.actual.scale_y = 2 -diag.progreso
		diag.Pintar()
		advanced.fBiDirBlur(pi/2.0, 5)
		advanced.EndGroup()

class Kanji(common.Fx):
	def EnDialogo(self, diag):
		diag.Pintar()

	def EnDialogoSale(self, diag):
		diag.Fade(1, 0)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		advanced.StartGroup()
		diag.Pintar()
		advanced.fBiDirBlur(pi/2.0, 5)
		advanced.EndGroup()
			
class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.saltar_cuadros = False
		self.in_ms = 300 #Milisegundos para la animacion de entrada
		self.out_ms = 300 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#~~~~~
		self.fxs = (Cred(), Kara1(), Trad(), Kanji(), Kara2())

	def EnCuadroInicia(self):
		advanced.StartGroup()

	def EnCuadroFin(self):
		self.fxs[4].parts.Pintar()
		advanced.fGlow(3, 0.04)
		advanced.EndGroup()
