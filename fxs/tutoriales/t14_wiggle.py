# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun

class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.FullWiggle(10, 5)
		diag.Pintar()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		diag.actual.color1.CopiarDe(diag.actual.color2) #Copiamos el color secundario al color primario,
		diag.Pintar()# Pintamos la silaba en la pantalla


class Efecto2(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.Pintar()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		diag.actual.color1.CopiarDe(diag.actual.color2) #Copiamos el color secundario al color primario,
		diag.Wiggle(10, 5)
		diag.Pintar()# Pintamos la silaba en la pantalla

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
		self.fxs = (EfectoGenerico(), Efecto2())


		"""Como se definenen los efectos?
			Basicamente contamos con una variable llamada fxs, esta tiene que llamarse asi porque la usara directamente el kafx_main
			fxs es un array, cada item representa un Efecto del archivo Ass,
			que se define en cada linea de dialogo... (Columna Effect)
			(generalmente ass lo usa para poner cosas como "karaoke" "scroll" acá usaremos un numero,
			0 para el primer effect, 1 para el siguiente y asi)"""