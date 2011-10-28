# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun
from libs.draw import avanzado
from math import pi

class EfectoGenerico(comun.Fx):
	def __init__(self):
		#Cuando se cree el efecto
		#Creamos las particulas
		self.parts = avanzado.cParticleSystem(png="texturas/spark5.png",
		max_life=3, max_parts=10000, emitir_parts=10, escala_de= 0.05, escala_a=0.5, modo=1, rotacion=0)
		#Configuramos la ventana y el angulo
		self.parts.DarVentana(0, 0)
		#self.parts.DarGravedad(pi/2.0, 0.01)
		self.parts.DarAngulo(pi/2,0.5,  pi)

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT
		diag.original.modo_borde = diag.P_DEG_VERT

	def EnSilabaInicia(self, d):
		d.original.modo_relleno = d.P_DEG_VERT

	def deform(self, sil, vector):
		pos_x = sil.actual.pos_x
		pos_y = sil.actual.pos_y + 20
		last = (0, 0)
		for t, p in vector:
			l = len(p)
			if (l == 2) or (l == 6):
				if l ==2:
					px = comun.LERP(sil.progreso, last[0], p[0])
					py = comun.LERP(sil.progreso, last[1], p[1])
					last = p
				else:
					px, py = comun.PuntoBezier(
						sil.progreso, last[0], last[1], p[0], p[1], p[2], p[3], p[4], p[5])
					last = p[4:]
				self.parts.DarPosicion(pos_x+px, pos_y+py)
				self.parts.Emitir()
		return vector

	def EnSilaba(self, d):
		d.actual.color1.Interpolar(d.progreso, d.actual.color2)
		d.Pintar()
		d.DeformarCompleto(self.deform)

	def EnDialogo(self, d):
		#Cuando el dialogo sea mostrado
		d.PintarReflejo()
		d.Pintar()


	def chainin(self, s, p):
		s.progreso = p
		s.Desvanecer(0,1)
		s.PintarReflejo()
		s.Pintar()


	def EnDialogoEntra(self, d):
		d.Encadenar(self.chainin)

	def chainout(self, s, p):
		s.progreso = p
		s.Desvanecer(1, 0)
		s.PintarReflejo()
		s.Pintar()


	def EnDialogoSale(self, d):
		d.Encadenar(self.chainout)

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
		self.fxs = (EfectoGenerico(), EfectoGenerico())

	def EnCuadroFin(self):
		#Pintamos las partículas con un modo aditivo
		avanzado.ModoPintado('add')
		self.fxs[0].parts.Pintar()
		avanzado.ModoPintado('over')