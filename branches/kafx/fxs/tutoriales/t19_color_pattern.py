# -*- coding: utf-8 -*-
"""Como utilizar los datos de audio de un archivo externo"""
from libs import comun, video, audio

power = 0.0

class EfectoGenerico(comun.Fx):
	def EnDialogoInicia(self, diag):
		diag.CargarTextura('texturas/T_Negro2.png', diag.PART_RELLENO)
		diag.original.modo_relleno = diag.P_PATRON_COLOREADO
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.Pintar()#Lo pintamos en la pantalla
	def EnSilabaInicia(self, sil):
		sil.CargarTextura('texturas/T_Negro2.png', sil.PART_RELLENO)
		sil.original.modo_relleno = sil.P_PATRON_COLOREADO
		
	def EnSilaba(self, diag):
		diag.actual.color1.Interpolar(diag.progreso, diag.actual.color2)
		diag.Pintar()

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.saltar_cuadros = False
		#Un efecto si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), EfectoGenerico(), EfectoGenerico())
		#hasta aca deberian saber que es
		