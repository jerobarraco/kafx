# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado
from random import random

class Romanji(comun.Fx):
	#Este effect se aplica al romanji o sea el karaoke
	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		diag.Pintar()
		#Entra con fade_in 
		
	def EnDialogoSale(self, diag):
		diag.Desvanecer(1, 0)
		diag.Pintar()
		#se va con fade_out
		
	def EnDialogo(self, diag):
		diag.PintarConCache()
		#por cada cuadro pintamos el dialogo completo tal cual
		
	def EnSilaba(self, diag):
		#por cad asilaba
		#diag.actual.color = diag.actual.scolor Esto funciona pero mejor si evitamos usarl
		a = diag.actual
		#cacheamos el estilo actual para no escribir tanto (y esperando q python sea mas rapido asi)
		a.color4.CopiarDe(a.color1)
		#copiamos el color primario al color del borde.
		a.sombra = 2
		#le asignamos una sombra de 2pxs
		a.color1.CopiarDe(a.color2)
		#copiamos el color secundario al color primario
		diag.Desvanecer(0, 1, comun.i_sin)
		#diag.Alpha(sin(pi*diag.progreso))
		#le ponemos un alfa de el seno de pi por el progreso (la curva es la grafica de seno de 0 a 180, o sea, sube a 1, y baja a 0 de nuevo)
		avanzado.GrupoInicio()
		#hacemos un grupo para el glow
		diag.Pintar()
		#pintamos
		avanzado.fGlow(4, 0.1)
		#brillo
		avanzado.GrupoFin()
		#fin del grupo.
		"""este effect se podia hacer de 3 formas
		variando el primer parametro del glow, la cantidad de pasos.
		a menos pasos el encoding es mas rapido, pero la cantidad de pasos es siempre entera
		asique se veria como entrecortado el effect.
		otra forma era cambiar el segundo parametro del glow, la fuerza.
		esta hubiese funcionado bastante bien, y es lo que uso normalmente... aunque
		el glow tiene el problema que valores muy bajos de fuerza no lo toma bien.
		
		y la forma que yo use, fue cambiar la opacidad de lo que pinto y el glow usa eso
		esto logra un effect igual a lo demás, con la ventaja que se forma un effect raro
		que el texto se ve a travez del glow en ciertos casos.
		"""

class Kanji(comun.Fx):
	#Para el kanji
	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0,1)
		diag.Pintar()
		
	def EnDialogoSale(self, diag):
		diag.Desvanecer(1,0)
		diag.Pintar()		
		
	def EnDialogo(self, diag):
		diag.PintarConCache()
	#Entra desvaneciendo, sale desvaneciendo, y lo pintamos con una nueva funcion que cachea lo que pintamos
	#que lleva el kafx a 15fps 
	
class Creditos(comun.Fx):
	#los creditos
	def EnDialogo(self, diag):
		#durante el dialogo
		avanzado.GrupoInicio()
		diag.Desvanecer(0, 1, comun.i_sin)
		#diag.Alpha(sin(pi*diag.progreso))
		#un effect de alpha con la misma curva que antes, 0 a 1 a 0, con la forma de un seno...
		diag.Pintar()
		avanzado.fGlow(10, 0.005 + (random()*0.005))
		#hacemos un glow, con un minimo de fuerza de 0.005 y un maximo de .01 para q de esa senzacion de interferencia
		#el defecto de esta tecnica (random) es que no hay interpolacion entre los cuadros, o sea, el glow del cuadro 
		#anterior es completamente individual del glow del cuadro siguiente, asique ciertos efectos asi no se hacen
		avanzado.GrupoFin()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		#Un effect si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 350 #Milisegundos para la animacion de entrada
		self.out_ms = 300 #MS para animacion d salida
		self.syl_in_ms = 5 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		#le puse 5 ms porque como no uso animaciones de silabas, queria probar si con un numero bajo iba mas rapido
		#la conclusion es... nidea.
		self.syl_out_ms = 2 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#same
		
		self.fxs = (Romanji(), Kanji(), Creditos())
