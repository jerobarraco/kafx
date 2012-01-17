# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun
from libs.draw import avanzado

class EfectoGenerico(comun.Fx):

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.Pintar()#Lo pintamos en la pantalla
		diag.PintarReflejo()

	def EnSilaba(self, sil):
		#Cuando la silaba sea cantada (activada)
		sil.actual.color1.CopiarDe(sil.actual.color2)
		sil.DeformarCompleto(self.deffunc)
		sil.Pintar()# Pintamos la silaba en la pantalla

	def EnSilabaMuerta(self, sil):
		#Cuando la silaba sea cantada (activada)
		sil.actual.color1.CopiarDe(sil.actual.color2)
		sil.PintarConCache()# Pintamos la silaba en la pantalla

	def deffunc(self, sil, vector):
		#lo convierto a lista para tomarle la longitud
		nv = list(vector)
		#calculamos la cantidad de puntos que vamos a usar dependiendo
		#del progreso
		cant_puntos = int(len(nv)*sil.progreso)
		#creamos un nuevo array con los puntos
		puntos = nv[:cant_puntos]
		return puntos
	
#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)

		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), EfectoGenerico())