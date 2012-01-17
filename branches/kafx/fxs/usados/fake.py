# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado
from random import random

class FX1(comun.Fx):
	def EnSilaba(self, diag):
		#hacemos un borde que crezca hasta 6
		diag.actual.borde += (6*diag.progreso)
		#Comenzamos un grupo
		avanzado.GrupoInicio()
		#Lo pintamos
		diag.Pintar()
		#Y hacemos un glow que vaya creciendo con el progreso
		avanzado.fGlow(3,  diag.progreso*0.25)
		avanzado.GrupoFin()

	def EnSilabaEntra(self, diag):
		#cuando la silaba esta a punto de animarse, hacemos fade in
		diag.Desvanecer(0, 1)
		#La movemos desde unos 40 pixels a la der y 20 arriba
		diag.MoverDe(40, -20)
		#Cambiamos la escala, de 0.5 a 1.0 (50% a 100%)
		diag.Escalar(0.5, 1.0)
		#y finalmente la pintamos
		diag.Pintar()

	def EnSilabaSale(self, diag):
		#Luego que se anime la silaba
		#Hacemos fadeout
		diag.Desvanecer(1, 0)
		#Reducimos la escala
		diag.Escalar(1, 0.5)
		#La movemos unos 20 pixels a la izq y 20 arriba
		diag.MoverA(-20, -20)
		#Y la pintamos
		diag.Pintar()

class FX2(comun.Fx):
	def EnDialogo(self, diag):
		a = diag.actual
		#Elegimos una posicion aleatoria en -5/5 pixels de diferencia (para hacer un shake)
		a.pos_x = a.pos_x + comun.Interpolar(random(), -5, 5) #Lo mismo q poner a.pos_x += comun.....
		a.pos_y = a.pos_y + comun.Interpolar(random(), -5, 5)
		diag.Desvanecer(0.5, 0.5)

		avanzado.GrupoInicio()
		#Lo pintamos y le hacemos blur de 2 pasos
		diag.Pintar()
		avanzado.fBlur(2)
		avanzado.GrupoFin()

		#Reestablecemos la informacion de estilo, porque recien lo cambiamos
		diag.Restore()

		avanzado.GrupoInicio()
		#Lo volvemos a pintar como corresponde y le hacemos glow
		diag.Pintar()
		avanzado.fGlow(3, 0.06)
		avanzado.GrupoFin()

	def EnDialogoSale(self, diag):
		diag.Desvanecer(1,0)
		diag.MoverA(0, 20)
		diag.Escalar(1, 0.5)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		diag.MoverDe(40, -20)
		diag.Escalar(0.5, 1.0)
		diag.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Un effect si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (FX1(),  FX2())
