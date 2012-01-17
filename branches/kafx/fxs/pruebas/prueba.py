# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun
from libs.draw import avanzado
import kafx_ogl

class EfectoGenerico(comun.Fx):
	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.Pintar()#Lo pintamos en la pantalla
		
	def EnSilabaMuerta(self, diag):
		diag.PintarConCache()
	def EnSilaba(self, diag):
		#Cuando la silaba sea cantada (activada)
		diag.actual.color1.Interpolar(diag.progreso, diag.actual.color2) #Copiamos el color secundario al color primario,
		c1 = diag.actual.color1 #cacheo del nombre
		c = [c1.r, c1.g, c1.b, c1.a]
		kafx_ogl.drawText(diag._texto, diag.actual.pos_x, diag.actual.pos_y, ry=diag.progreso, color=c)
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
		self.fxs = (EfectoGenerico(), EfectoGenerico())


	def EnCuadroInicia1(self):
		#Cuando inicia el cuadro (antes de cualquier dialogo o silaba)
		#Comenzamos un grupo
		avanzado.StartGroup()

	def EnCuadroFin1(self):
		#Cuando termina el cuadro (luego de todas las sibalas y dialogues)
		#Hacemos un glow con lo que habia
		#avanzado.fGlow()
		#Y cerramos el grupo
		avanzado.fBlur()
		avanzado.EndGroup()