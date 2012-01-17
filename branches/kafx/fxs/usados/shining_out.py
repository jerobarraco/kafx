# -*- coding: utf8 -*-
from libs.draw import extra, avanzado
from libs import comun, audio
from math import pi

#formato viejo, reescribir... quizas funcione, no lo se. #le faltan cambiar varias cosas...
#El test.bpm se lo piden a Zheo porque yo no lo tengo xD

class FX1(comun.Fx):
	## FX01 BPM DETECTION CON GLOW
	def __init__(self):
		self.audio  = audio.BPM("test.bpm")

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogo(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 0.8, 1)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 0.9, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(1, self.audio.RevBPM()/5.0)
		avanzado.GrupoFin()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.MoverA(-3, 0)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnSilaba(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 1, 0.6)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 1, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.GrupoFin()


class FX2(comun.Fx):
	## FX02 GLOW CON DEGRADO
	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, sil):
		sil.original.modo_relleno = sil.P_DEG_VERT

	def EnDialogo(self, diag):
		diag.actual.color1.Interpolar(diag.progreso, diag.original.color2)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(2,0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.MoverA(-3,0)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnSilaba(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 1, 0.6)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 1, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.GrupoFin()


class FX3(comun.Fx):
	## FX03 SHAKE CON GLOW
	def __init__(self):
		self.audio  = audio.BPM("test.bpm")

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, sil):
		sil.original.modo_relleno = sil.P_DEG_VERT

	def EnDialogo(self, diag):
		#for silaba in diag.silabas:
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 0.8, 1)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 0.9, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		diag.Sacudir(2)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(1, 0.08*diag.progreso)
		avanzado.fBlur(2, self.audio.RevBPM()/5.0)
		avanzado.GrupoFin()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.MoverA(-3,0)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnSilaba(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 1, 0.6)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 1, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		diag.Desvanecer(1, 0)
		diag.Sacudir(2)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

## FX04 GLOW Y PARTICULA
class FX4(comun.Fx):
	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, sil):
		sil.original.modo_relleno = sil.P_DEG_VERT

	def __init__(self):
		self.audio  = audio.BPM("test.bpm")
		self.parts = avanzado.cParticleSystem(png="texturas/star3.png",
			color=extra.cCairoColor(0xFFBCD8EA))
		self.parts.DarVentana(3, 3)
		self.parts.DarAngulo(pi, 3, pi)

	def EnDialogo(self, diag):
		#for silaba in diag.silabas:
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 0.8, 1)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 0.9, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(1, self.audio.RevBPM()/5.0)
		avanzado.GrupoFin()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.MoverA(-3, 0)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnSilaba(self, diag):
		if diag._texto.strip() =="":
			return
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 1, 0.6)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 1, 1)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 1, 1)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(1,self.audio.RevBPM()/5.0)
		self.parts.DarPosicion(diag.actual.pos_x+diag.progreso*diag.original._ancho, diag.actual.pos_y)
		self.parts.Emitir()
		avanzado.GrupoFin()

## FX05 TRADUCCION
class FX5(comun.Fx):
	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, sil):
		sil.original.modo_relleno = sil.P_DEG_VERT

	def EnDialogo(self, diag):
		avanzado.GrupoInicio()
		diag.PintarConCache()
		avanzado.fGlow(2, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.Desvanecer(1,0)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0,1)
		diag.Pintar()


## FX KANJIS
class FX6(comun.Fx):
	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, sil):
		sil.original.modo_relleno = sil.P_DEG_VERT

	def EnDialogo(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 0.8, 1)
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 0.9, 1)
		diag.actual.color1.b = 1
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(1,0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.MoverA(-3, 0)
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fBlur(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

	def EnSilaba(self, diag):
		diag.actual.color1.r = comun.Interpolar(diag.progreso, 1, 0.6)
		diag.actual.color1.g = 1
		diag.actual.color1.b = 1
		diag.Desvanecer(1, 0)
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.GrupoFin()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.saltar_frames= False
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 150 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#~~~~~
		self.fxs = (FX1(), FX2(), FX3(), FX4(), FX5(), FX6())

	def EnCuadroFin(self):
			self.fxs[3].parts.Pintar()
