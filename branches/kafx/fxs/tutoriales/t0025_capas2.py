# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun, video, audio
from libs.draw import avanzado


class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		avanzado.CapasActivar('2 puede ser un nombre tambien pero es mas largo y lento')
		diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		#esto es al pedo pero es para mostrar que una capa se puede activar muchas veces.
		avanzado.CapasActivar('2 puede ser un nombre tambien pero es mas largo y lento')
		diag.MoveTo(0, 0)
		diag.Pintar()# Pintamos la silaba en la pantalla

		#Asi demostramos como pintar una silaba por debajo del dialogo.. aunque esto podria ser hecho de otra manera
		avanzado.CapasActivar('1 moviendose')
		diag.MoveTo(10, 10)
		diag.actual.color1.r = 1.0
		diag.Pintar()

		#Notar que el 2º pintar es llamado DESPUES (en cuanto a tiempo real)
		#Pero es pintado "antes" en cuanto a posicion de capas...
		#eso es porque esta pintado luego de activar la capa 1, porque es la que está mas abajo (se ordenan por nombre)
		

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (EfectoGenerico(),)

	def EnCuadroInicia(self):
		avanzado.CapasInicia()
		#Las capas se pintan segun el orden de su nombre
		#1Moviendose se pinta antes que 2puedes.....
		avanzado.CapasCrear('1 moviendose', 0.5)
		avanzado.CapasCrear('2 puede ser un nombre tambien pero es mas largo y lento', 1.0 , 'add')
		
		
	def EnCuadroFin(self):
		avanzado.CapasFin()