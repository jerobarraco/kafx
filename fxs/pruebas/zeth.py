# -*- coding: utf-8 -*-
from libs.draw import extra, avanzado, basico
from libs import comun
from math import cos, pi, sin
import math, random

class FX1(comun.Fx):
	def __init__(self):
		self.movimiento=0

	def EnDialogoEntra(self, d):
		avanzado.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(0, 1)
		d.Pintar()
		avanzado.fWave(self.movimiento, 0.030, 2, True)
		avanzado.fWave(self.movimiento, 0.040, 2, False)
		avanzado.EndGroup()

	def EnDialogo(self,  d):
		avanzado.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Pintar()
		avanzado.fWave(self.movimiento, 0.030, 2, True)
		avanzado.fWave(self.movimiento, 0.040, 2, False)
		avanzado.EndGroup()

	def EnSilaba(self, d):
		d.Fade(1, 0)
		avanzado.StartGroup()
		d.Pintar()#el pintar va antes del wave, sino el wave no le afecta :D
		avanzado.fWave(self.movimiento, 0.030, 2, True)
		avanzado.fWave(self.movimiento, 0.040, 2, False)
		avanzado.fGlow(3, d.progreso*0.35)
		avanzado.EndGroup()

	def EnDialogoSale(self, d):
		avanzado.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(1, 0)
		d.Pintar()
		avanzado.fWave( self.movimiento, 0.030, 2,  True)
		avanzado.fWave( self.movimiento, 0.040, 2,  False)
		avanzado.EndGroup()

class FX2(comun.Fx):

	def __init__(self):
		self.parts = avanzado.cParticleSystem(png="textures/spark.png", color = extra.cCairoColor(0xFFAFAFAF), max_life=3, emit_parts=2, scale_from= 0.4, scale_to=0.1, modo=1)
		self.parts.DarVentana(6, 2)
		self.parts.DarAngulo(pi, 5, pi/4.2)

	def EnDialogoInicia(self, d):
		d.chars = []
		for silaba in d._silabas:
			silaba.DividirLetras()
			d.chars.extend(silaba._letras)

	def Entrada(self, c, prog):
		c.progreso = prog
		otro_interpolado= comun.Interpolar(prog, 0, 1)
		c.Fade(0, otro_interpolado)
		#c.actual.scale_x = c.actual.scale_y= otro_interpolado
		c.Pintar()

	def Salida(self, c, prog):
		c.progreso = prog
		#otro_interpolado= comun.Interpolar(prog, 1, 0)
		c.Fade(1,0)
		#c.actual.scale_x = c.actual.scale_y= otro_interpolado
		c.Pintar()

	def EnDialogoEntra(self, d):
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(0, 1)
		d.Pintar()
		#d.original.modo_relleno = d.P_DEG_VERT
		#comun.Encadenar(450, d.progreso, d.chars, self.Entrada, 200)

	def EnDialogo(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT
		#diag.actual.pos_x += random.randint(-3,3)
		#diag.actual.pos_y += random.randint(-3,3)
		diag.actual.pos_x += random.randint(-1,1)
		diag.actual.pos_y += random.randint(-1,1)
		diag.Pintar()

	def EnSilaba(self, s):
		if not s._texto.strip():
			return #nunca pongas un return adentro de un grupo (o sea antes de grupofin)
		s.Fade(1, 0)
		avanzado.StartGroup()
		s.Pintar()
		avanzado.fGlow(5, 0.08*s.progreso)
		avanzado.EndGroup()
		
		valor= random.randint(0,1)
		if valor == "1":
			ZethPRO= comun.Interpolar(random.random(), -15, 10)
		else:
			ZethPRO= comun.Interpolar(random.random(), 10, 15)
		self.parts.DarPosicion( s.actual.pos_x + s.progreso*s.original._ancho, s.actual.pos_y + ZethPRO)
		self.parts.Emitir()

	def EnDialogoSale(self, d):
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(1, 0)
		d.Pintar()
		#d.original.modo_relleno = d.P_DEG_VERT
		#comun.Encadenar(450, d.progreso, d.chars, self.Salida, 200)

class tradu(comun.Fx):
	def EnDialogo(self, d):
		d.PintarConCache()

	def EnDialogoEntra(self, d):
		desp = sin(pi*d.progreso)*15
		d.actual.pos_x -= desp
		d.Fade(0, 1)
		d.Pintar()

	def EnDialogoSale(self, d):
		desp = sin(pi*d.progreso)*15
		d.actual.pos_x += desp
		d.Fade(1,0)
		d.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.saltar_cuadros = False
		self.in_ms = 250
		self.out_ms = 250
		self.syl_in_ms = 500
		self.syl_out_ms = 200
		self.fxs = (FX1(), FX2(), tradu())

	def EnCuadroInicia(self):
		avanzado.StartGroup()
	def EnCuadroFin(self):
		avanzado.fGlow(2, 0.06)
		avanzado.EndGroup()
		avanzado.ModoPintado('add')
		self.fxs[1].parts.Pintar()
		self.fxs[0].movimiento +=1
		avanzado.ModoPintado('over')