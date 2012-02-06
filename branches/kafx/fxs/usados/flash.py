# -*- coding: utf8 -*-
from libs import comun, audio
from libs.draw import avanzado

## FX01 BPM DETECTION CON GLOW
class FX1(comun.Fx):
	def EnDialogoInicia(self, diag):
		#Cargamos el bpm
		self.audio = audio.BPM('fxs/Usados/flash.bpm')
		#Elegimos el modo de relleno Degradado Vertical
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogo(self, diag):
		#Cuando se muestre el dialogo
		#Comenzamos un grupo
		avanzado.StartGroup()
		#Pintamos el dialogo
		diag.Pintar()
		#Hacemos un glow a todo lo que esté en la pantalla
		avanzado.fGlow(1, self.audio.RevBPM()/5.0)
		#Cerramos el grupo
		avanzado.EndGroup()

	def EnDialogoEntra(self, diag):
		#Cuando el dialogo entre
		#Hacemos un fade-in
		diag.Fade(0, 1)
		#Creamos un grupo
		avanzado.StartGroup()
		#Pintamos el dialogo
		diag.Pintar()
		#Hacemos un glow que vaya creciendo con el progreso
		avanzado.fBlur(5, 0.08*diag.progreso)
		#Cerramos el dialogo
		avanzado.EndGroup()

	def EnDialogoSale(self, diag):
		#Cuando el dialogo sale
		#Lo movemos 3 pixels a la izq
		diag.MoveTo(-3, 0)
		#Hacemos un fade-out
		diag.Fade(1, 0)
		#Grupo-Pintamos-Blur-Cerramos
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnSilaba(self, diag):
		#Cuando se muestre la silaba
		#Hacemos un fade out
		diag.Fade(1, 0)
		#Grupo-Pintamos-Glow-Cerramos
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.EndGroup()

## FX02 GLOW CON DEGRADO
class FX2(comun.Fx):
	def EnDialogoInicia(self, diag):
		self.audio = audio.BPM('fxs/Usados/flash.bpm')
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogo(self, diag):
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fGlow(1,self.audio.RevBPM()/5.0)
		avanzado.EndGroup()

	def EnDialogoEntra(self, diag):
		diag.Fade(0,1)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnDialogoSale(self, diag):
		diag.MoveTo(-3,0)
		diag.Fade(1,0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnSilaba(self, diag):
		diag.actual.color1.r = 0.8
		diag.actual.color1.g = 0.6
		diag.actual.color1.b = 0.5
		diag.Fade(1,0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.EndGroup()

## FX03  GLOW
class FX3(comun.Fx):
	def EnDialogoInicia(self, diag):
		self.audio = audio.BPM('fxs/Usados/flash.bpm')

	def EnDialogo(self, diag):
		avanzado.StartGroup()
		diag.PintarDegradadoL()
		avanzado.fGlow(1, 0.08*diag.progreso)
		avanzado.fBlur(2, self.audio.RevBPM()/5.0)
		avanzado.EndGroup()

	def EnDialogoEntra(self, diag):
		diag.Fade(1,0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnDialogoSale(self, diag):
		diag.MoveTo(-3,0)
		diag.Devanecer(1,0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnSilaba(self, diag):
		diag.actual.color1.r = 0.9
		diag.actual.color1.g = 0.7
		diag.actual.color1.b = 0.5
		diag.Fade(1, 0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.EndGroup()

## FX04 TRADU
class FX4(comun.Fx):
	def EnDialogo(self, diag):
		avanzado.StartGroup()
		diag.original.modo_relleno = diag.P_DEG_VERT
		diag.Pintar()
		avanzado.fGlow(2, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnDialogoEntra(self, diag):
		diag.Fade(0.0, 1.0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()

	def EnDialogoSale(self, diag):
		diag.MoveTo(-3, 0)
		diag.Fade(1.0, 0.0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.EndGroup()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.saltar_cuadros = False
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 150 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#~~~~~
		self.fxs = (FX1(), FX2(), FX3(), FX4())

	def EnCuadroInicia(self):
		avanzado.StartGroup()

	def EnCuadroFin(self):
		avanzado.fGlow(1, 0.04)
		avanzado.EndGroup()
