# -*- coding: utf8 -*-
from libs.draw import advanced
from libs import common, audio
from math import pi, sin, cos

class FX1(common.Fx):
	def __init__(self):
		#Cuando se cree el effect
		#Creamos las particulas
		self.parts = advanced.cParticleSystem(png="textures/star3.png", max_life=3, emit_parts=2, scale_from= 0.8, scale_to=0.3, modo=1)
		#Configuramos la ventana y el angulo
		self.parts.DarVentana(6, 2)
		self.parts.DarAngulo(pi, 3, pi/4.0)
		#Pi/4.0 ==45º eso espero

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, s):
		s.original.modo_relleno = s.P_DEG_VERT

	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		diag.Pintar()

	def EnSilaba(self, diag):
		#Cuando toca la silaba
		#si la silaba no tiene letras (un espacio o vacia) salimos
		if diag._texto.strip() =="":
			return

		#cambiamos la posicion del emitter de particulas
		self.parts.DarPosicion(
			diag.actual.pos_x + diag.progreso*diag.original._ancho,
			diag.actual.pos_y - (diag.actual.org_y)
		)
		self.parts.Emitir()
		diag.actual.color4.r=diag.actual.color4.g=diag.actual.color4.b=0.8
		diag.Fade(1, 0)
		diag.Pintar()

	def EnSilabaDorm(self, diag):
		diag.PintarConCache()

#El otro effect
class FX2(common.Fx):
	def EnDialogoInicia(self, diag):
		#abrimos el bpm
		self.audio = audio.BPM("fxs/Usados/gogo.bpm")

	def EnDialogo(self, diag):
		#En el dialogo
		#Calculamos un valor, que va a ser mayor a uno
		#y en funcion de seno, desde el bpm
		som = 1+sin(self.audio.RevBPM())*6
		advanced.StartGroup()
		diag.actual.sombra = som #y hacemos una sombra de ese tamaño
		diag.Pintar()
		#lo pintamos y le hacemos un glow con una opacidad que depende tamb del valor anterior
		advanced.fGlow(opacity=som/200.0)
		advanced.EndGroup()

	def EnDialogoEntra(self, diag):
		#Entra con una scale creciente, con una onda como seno
		sc = 1+0.25*sin(pi*diag.progreso/2.0)
		diag.Scale(sc, sc)
		diag.Pintar()

	def EnDialogoSale(self, diag):
		#Sale con una scale decreciente
		diag.actual.scale_y  = 1.01-diag.progreso
		diag.Fade(1,0)
		diag.Pintar()

class FX3(common.Fx):
	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogo(self, diag):
		angulo = 2*pi*diag.progreso
		advanced.StartGroup()
		diag.Alpha(sin(angulo))
		diag.actual.pos_x += (cos(angulo)*120)# Esto depende de reset_style
		#diag.MoveTo(diag.actual.pos_x+, 0)
		diag.Pintar()
		advanced.fGlow(opacity=0.025)
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
		self.fxs = (FX1(), FX2(), FX3())

	def EnCuadroFin(self):
		#Pintamos las partículas con un modo aditivo
		advanced.ModoPintado('add')
		self.fxs[0].parts.Pintar()
		advanced.ModoPintado('over')
