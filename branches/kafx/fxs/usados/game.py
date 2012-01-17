# -*- coding: utf8 -*-
from libs import comun
from libs.draw import avanzado
import random

#Primer effect
class FX1(comun.Fx):
	def EnDialogo(self, diag):
		#Mientras el dialogo se muestre
		#Hacemos un grupo (para que el glow no afecte el video)
		avanzado.GrupoInicio()
		diag.Pintar()
		#Pintamos y hacemos un glow con una opacidad random
		avanzado.fGlow(4, random.random()/30.0)
		avanzado.GrupoFin()

	#Hacemos que aparezca y desaparezca con fade
	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		diag.Pintar()

	def EnDialogoSale(self, diag):
		diag.Desvanecer(1, 0)
		diag.Pintar()

	def EnSilaba(self, diag):
		#Hacemos que el color varie de una forma rara
		diag.actual.color1.g = comun.Interpolar(diag.progreso, 0.5, 0)
		diag.actual.color1.b = comun.Interpolar(diag.progreso, 0.5, 0)
		#Y lo pintamos y le hacemos un glow que va a ir creciendo con el progreso
		avanzado.GrupoInicio()
		diag.Pintar()
		avanzado.fGlow(5, 0.08*diag.progreso)
		avanzado.GrupoFin()

#Efecto 2
class FX2(comun.Fx):
	def EnDialogo(self, diag):
		#Simplemente lo pintamos cuando aparezca
		diag.PintarConCache()

	#Y que entre y se vaya con fade y un movimiento hacia la izq
	def EnDialogoSale(self, diag):
		diag.MoverA(-5, 0)
		diag.Desvanecer(1, 0)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.MoverDe(5, 0)
		diag.Desvanecer(0, 1)
		diag.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#~~~~~
		self.fxs = (FX1(), FX2())
