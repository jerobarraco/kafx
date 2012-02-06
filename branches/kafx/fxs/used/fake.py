# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced
from random import random

class FX1(common.Fx):
	def EnSilaba(self, diag):
		#hacemos un borde que crezca hasta 6
		diag.actual.borde += (6*diag.progreso)
		#Comenzamos un grupo
		advanced.StartGroup()
		#Lo pintamos
		diag.Pintar()
		#Y hacemos un glow que vaya creciendo con el progreso
		advanced.fGlow(3,  diag.progreso*0.25)
		advanced.EndGroup()

	def EnSilabaEntra(self, diag):
		#cuando la silaba esta a punto de animarse, hacemos fade in
		diag.Fade(0, 1)
		#La movemos desde unos 40 pixels a la der y 20 arriba
		diag.MoveFrom(40, -20)
		#Cambiamos la scale, de 0.5 a 1.0 (50% a 100%)
		diag.Scale(0.5, 1.0)
		#y finalmente la pintamos
		diag.Pintar()

	def EnSilabaSale(self, diag):
		#Luego que se anime la silaba
		#Hacemos fadeout
		diag.Fade(1, 0)
		#Reducimos la scale
		diag.Scale(1, 0.5)
		#La movemos unos 20 pixels a la izq y 20 arriba
		diag.MoveTo(-20, -20)
		#Y la pintamos
		diag.Pintar()

class FX2(common.Fx):
	def EnDialogo(self, diag):
		a = diag.actual
		#Elegimos una posicion aleatoria en -5/5 pixels de diferencia (para hacer un shake)
		a.pos_x = a.pos_x + common.Interpolar(random(), -5, 5) #Lo mismo q poner a.pos_x += comun.....
		a.pos_y = a.pos_y + common.Interpolar(random(), -5, 5)
		diag.Fade(0.5, 0.5)

		advanced.StartGroup()
		#Lo pintamos y le hacemos blur de 2 pasos
		diag.Pintar()
		advanced.fBlur(2)
		advanced.EndGroup()

		#Reestablecemos la informacion de estilo, porque recien lo cambiamos
		diag.Restore()

		advanced.StartGroup()
		#Lo volvemos a pintar como corresponde y le hacemos glow
		diag.Pintar()
		advanced.fGlow(3, 0.06)
		advanced.EndGroup()

	def EnDialogoSale(self, diag):
		diag.Fade(1,0)
		diag.MoveTo(0, 20)
		diag.Scale(1, 0.5)
		diag.Pintar()

	def EnDialogoEntra(self, diag):
		diag.Fade(0, 1)
		diag.MoveFrom(40, -20)
		diag.Scale(0.5, 1.0)
		diag.Pintar()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Un effect si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (FX1(),  FX2())
