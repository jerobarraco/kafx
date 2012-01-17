# -*- coding: utf8 -*-
from libs.draw import extra, avanzado
from libs import comun
import random

#--ACÁ SON LOS FX DEL KARAOKE--
class ef1(comun.Fx):
	def __init__(self):
		#cuando inicie el efecto
		#creamos un sistema de particulas, con un color definido
		p = avanzado.cParticleSystem(png="texturas/sakura.png", emitir_parts=3,
			color=extra.cCairoColor(0xFFFF0000))
		#Le ponemos un angulo para que salgan las particulas
		p.DarAngulo(5, 2, 0)
		#5 radianes, 2 pixels por cuadro, 0 de desviacion
		#y una gravedad
		p.DarGravedad(90, 3)
		#90 grados y una velocidad de 3 pixels
		#y lo guardamos en self (el efecto)
		self.parts = p

	def EnDialogoInicia(self, diag):
		#Cuando el dialogo inice, lo configuramos para que este relleno con degradado
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnSilabaInicia(self, s):
		#igual q arriba
		s.original.modo_relleno = s.P_DEG_VERT
		
	def EnDialogo(self, diag):
		#Al mostrar el dialogo, lo vamos haciendo un fadein
		diag.Desvanecer(0, 1)
		diag.Pintar()

	def EnDialogoSale(self, d):
		#Mientras el dialogo se va, Fade out y pintamos
		d.Desvanecer(1, 0)
		d.Pintar()

	def EnSilabaSale(self, d):
		#Cuando la silaba termina su accion
		d.Desvanecer(1, 0)
		d.Pintar()

	def EnSilaba(self, d):
		#Cuando la silaba esta activa
		#fadeout
		d.Desvanecer(0, 1)

		#creamos un grupo
		avanzado.GrupoInicio()
		#lo pintamos
		d.Pintar()
		#y le hacemos un glow
		avanzado.fGlow(3, d.progreso*0.25)


		#lo movemos en 3 pixels random para arriba o abajo
		d.actual.pos_x += random.randint(-3, 3)
		d.actual.pos_y += random.randint(-3, 3)
		#y lo pintamos
		d.Pintar()
		#y un blur de 1 paso
		avanzado.fBlur(1)
		avanzado.GrupoFin()
		#cambiamos la ventana de las particulas por el ancho de la silaba
		self.parts.DarVentana(d.original._ancho, 5)
		#Ponemos una posicion al emisor que va pasando por toda la silaba
		self.parts.DarPosicion(
			d.actual.pos_x+(d.original._ancho*d.progreso),
			d.actual.pos_y-d.actual.org_y
		)
		#Emitimos
		self.parts.Emitir()

class ef2(comun.Fx):
	#Efecto dos, me da fiaca comentarlo
	def EnDialogoInicia(self, d):
		d.original.modo_relleno = d.P_DEG_VERT

	def EnDialogo(self, d):
		d.Desvanecer(0, 1)
		d.Pintar()

	def EnSilabaInicia(self, d):
		d.original.modo_relleno = d.P_DEG_VERT

	def EnSilabaSale(self, d):
		d.Desvanecer(1, 0)
		d.Pintar()

	def EnSilaba(self, d):
		d.Desvanecer(0, 1)
		avanzado.GrupoInicio()
		d.Pintar()

		d.actual.pos_x += random.randint(-3,3)
		d.actual.pos_y += random.randint(-3, 3)
		avanzado.fGlow(3, d.progreso*0.25)
		
		d.Pintar()
		avanzado.fBlur( 1)
		avanzado.GrupoFin()

	def EnDialogoSale(self, d):
		d.Desvanecer(1, 0)
		d.Pintar()

class FxsGroup(comun.FxsGroup):
	def EnCuadroFin(self):
		self.fxs[0].parts.Pintar()

	def __init__(self):
		#necesario para las particulas
		self.saltar_cuadros = False

		self.in_ms = 100 #Milisegundos para la animacion de entrada
		self.out_ms = 350 #MS para animacion d salida
		self.sil_in_ms = 100 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
				
		#Funciones (grupo de efectos) que se provee
		self.fxs = (ef1(),  ef2())