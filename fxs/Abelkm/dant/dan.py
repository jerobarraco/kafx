# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos


t2 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/plata1.png', extend=cairo.EXTEND_REFLECT)
t1 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/silver2.png', extend=cairo.EXTEND_REFLECT)
t3 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/win3.png', extend=cairo.EXTEND_REFLECT)

class FX1(comun.Fx):

	def __init__(self):
		self.events = [Evento1(), Evento2(), Evento3()]

	def EnDialogo(self, d):
		global t1, t2
		d.texturas[d.PART_RELLENO] = t1
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = t2
		d.actual.modo_borde = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global t1, t2
		d.texturas[d.PART_RELLENO] = t1
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = t2
		d.actual.modo_borde = d.P_TEXTURA
		d.Desvanecer(1,0)
		d.MoverA(random.randint(0, 30), 0)
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fBlur1(3, comun.Interpolar(d.progreso, 0, 0.15, comun.i_b_ease_in))
		avanzado.EndGroup()


	def EnDialogoEntra(self, d):
		global t1, t2
		d.texturas[d.PART_RELLENO] = t1
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = t2
		d.actual.modo_borde = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(random.randint(-30, 0), 0)
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fBlur1(3, comun.Interpolar(d.progreso, 0.15, 0, comun.i_b_ease_in))
		avanzado.EndGroup()



class Evento1(comun.Evento):
		def __init__(self):
			p = avanzado.cParticleSystem(png="texturas/win3.png", emit_parts=40,
				modo = 0, max_parts=80, rotation= 0.1, scale_from=0.05, scale_to= 0.05,max_life=1)
			p.DarAngulo(10, 2, 10)
			p.DarGravedad(0, 1)
			self.parts = p

		def EnLetra(self, letra):
			global t3
			letra.actual.color3.a = 0
			letra.actual.color1.a = 0.5
			letra.texturas[letra.PART_RELLENO] = t3
			letra.actual.modo_relleno = letra.P_TEXTURA
			avanzado.StartGroup()
			letra.Pintar()
			avanzado.fGlow(1, 0.1+(sin(pi*letra.progreso)/6.0))
			avanzado.EndGroup()
			self.parts.DarVentana(letra.original._ancho+1, 1)
			self.parts.DarPosicion(
				letra.actual.pos_x+random.randint(-2,3)+(letra.original._ancho*(letra.progreso)/4),
            	(random.randint(1,17)+letra.actual.pos_y)
			)

			if letra._texto.strip()<>"":
				self.parts.Emitir()

		def TiempoLetra(self, letra):
			return (letra._start, letra._end)

class Evento2(comun.Evento):
        def EnLetra(self, letra):
			global t3
			letra.actual.color3.a = 0
			letra.actual.color1.a = comun.Interpolar(letra.progreso, 0, 0.5,  comun.i_b_ease_in)
			letra.texturas[letra.PART_RELLENO] = t3
			letra.actual.modo_relleno = letra.P_TEXTURA
			avanzado.StartGroup()
			letra.Pintar()
			avanzado.fGlow(2, 0.1)
			avanzado.EndGroup()
			letra.actual.color3.a = 0
			letra.actual.color1.a = comun.Interpolar(letra.progreso, 0, 0.5,  comun.i_b_ease_in)
			letra.Pintar()

        def TiempoLetra(self, letra):
                return (letra._start - 5, letra._start)

class Evento3(comun.Evento):
        def EnLetra(self, letra):
			global t3
			letra.actual.color3.a = 0
			letra.actual.color1.a = comun.Interpolar(letra.progreso, 0.5, 0,  comun.i_b_ease_out)
			letra.texturas[letra.PART_RELLENO] = t3
			letra.actual.modo_relleno = letra.P_TEXTURA
			avanzado.StartGroup()
			letra.Pintar()
			avanzado.fGlow(2, 0.1)
			avanzado.EndGroup()
			letra.actual.color3.a = 0
			letra.actual.color1.a = comun.Interpolar(letra.progreso, 0.5, 0,  comun.i_b_ease_out)
			letra.Pintar()

        def TiempoLetra(self, letra):
                return (letra._end, letra._end + 5)



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 250
		self.out_ms = 250
		self.dividir_letras = True
		self.saltar_cuadros = False
		self.fxs = (FX1(), FX1())