# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import common

class EfectoGenerico(common.Fx):
	def EnDialogoInicia(self, diag):
		diag.LoadTexture("textures/cloud3.png", diag.PART_RELLENO)
		diag.original.modo_relleno = diag.P_PATRON_COLOREADO

	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.actual.color1.Interpolar(diag.progreso, diag.original.color2)
		diag.Pintar()#Lo pintamos en la pantalla


#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)

		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), EfectoGenerico())