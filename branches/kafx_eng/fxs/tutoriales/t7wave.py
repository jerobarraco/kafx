# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado

class FX1(comun.Fx):
	def EnDialogoInicia(self, d):
		d.movimiento = 0#creamos una variable para que vaya animandose el movimiento

	def EnDialogo(self,  d):
		#Como Onda es un "f" modifica TODA la pantalla, para que modifique solamente
		#el dialogo, creamos un grupo y lo pintamos ahi dentro
		avanzado.GrupoInicio()
		d.Pintar()
		#Hacemos una onda de movimiento = a d.movimiento
		#con una frecuencia en 0.01
		#y con una amplitud de 4
		#y le indicamos que es vertical con True
		avanzado.fOnda( d.movimiento, 0.01, 4,  True)
		#ahora hacemos otra onda, con desplazamiento d.movimiento
		#con una frecuencia en 0.1
		#con una amplitud de 4
		#y le indicamos que no es vertical (o sea, es horizontal)
		avanzado.fOnda( d.movimiento, 0.1, 3,  False)
		avanzado.GrupoFin()
		#y aumentamos el movimiento para que se vea animado.
		d.movimiento += 1

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(), FX1())
