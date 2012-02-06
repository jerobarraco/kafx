# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import common, video, audio
from libs.draw import advanced


class EfectoGenerico(common.Fx):
	#def EnDialogo(self, diag):
	#	#Cuando el dialogo sea mostrado
	#	diag.PintarConCache()#Lo pintamos en la pantalla

	def EnSilaba(self, diag):
		advanced.CapasActivar(2)
		diag.MoveTo(0,0)
		diag.Pintar()# Pintamos la silaba en la pantalla

		#Podemos activar cualquier capa en cualquier momento, tantas veces como queramos
		#(de hecho cambiar de capa no consume muchos recursos) (no digo que sea instantaneo pero es bastante rapido)
		#Tengan en cuenta que al activar una capa QUEDA ACTIVADA HASTA EL PROXIMO CUADRO!!! (o hasta que activen otra)
		advanced.CapasActivar(1)
		diag.MoveTo(10, 10)
		diag.actual.color1.r = 1.0
		diag.Pintar()

		#Notar que el 2º pintar es llamado DESPUES (en cuanto a tiempo real)
		#Pero es pintado "antes" en cuanto a posicion de capas...
		#eso es porque esta pintado luego de activar la capa 1, porque es la que está mas abajo (se ordenan por nombre)
		

class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (EfectoGenerico(),)

	def EnCuadroInicia(self):
		advanced.CapasInicia()
		#no importa el orden de creado, es más, pueden crearlas dinamicamente en otro momento
		#(siempre entre CapasInicia y CapasFin) (no recomiendo crearlas despues, eso es cosa de cochino)
		advanced.CapasCrear(2, 0.5, 'add')
		advanced.CapasCrear(1)
		#El nombre con que se crean (el 1º parametro) es el nombre con el cual se activan luego
		#ADEMAS define el orden en que eran pintadas, (segun como se ordenan (alfabeticamente o numericamente)
		#los otros dos parametros son opcionales
		
	def EnCuadroFin(self):
		advanced.CapasFin()