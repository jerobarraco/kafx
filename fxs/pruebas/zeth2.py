# -*- coding: utf-8 -*-
from libs.draw import extra, advanced, basic
from libs import common
from math import cos, pi, sin
import math, random

class FX1(common.Fx):
	def __init__(self):
		self.movimiento=0

	def EnDialogoEntra(self, d):
		advanced.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(0, 1)
		d.Pintar()
		advanced.fWave(self.movimiento, 0.030, 2, True)
		advanced.fWave(self.movimiento, 0.040, 2, False)
		advanced.EndGroup()

	def EnDialogo(self,  d):
		advanced.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Pintar()
		advanced.fWave(self.movimiento, 0.030, 2, True)
		advanced.fWave(self.movimiento, 0.040, 2, False)
		advanced.EndGroup()

	def EnSilaba(self, d):
		d.Fade(1, 0)
		advanced.StartGroup()
		d.Pintar()
		advanced.fWave(self.movimiento, 0.030, 2, True)
		advanced.fWave(self.movimiento, 0.040, 2, False)
		advanced.fGlow(3, d.progreso*0.15)
		advanced.EndGroup()

	def EnDialogoSale(self, d):
		advanced.StartGroup()
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(1, 0)
		d.Pintar()
		advanced.fWave(self.movimiento, 0.030, 2,  True)
		advanced.fWave(self.movimiento, 0.040, 2,  False)
		advanced.EndGroup()

class FX2(common.Fx):
	def __init__(self):
		self.parts = advanced.cParticleSystem(png="textures/spark.png", color = extra.cCairoColor(0xFFAFAFAF), max_life=3, emit_parts=2, scale_from= 0.4, scale_to=0.1, modo=1)
		self.parts.DarVentana(6, 2)
		self.parts.DarAngulo(pi, 5, pi/4.2)
		self.posx= 0
		self.posy= 0

	def EnDialogoInicia(self, d):
		d.chars = []
		for silaba in d._silabas:
			silaba.DividirLetras()
			d.chars.extend(silaba._letras)

	def EnDialogoEntra(self, d):
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(0, 1)
		d.Pintar()

	def EnDialogo(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT
		diag.actual.pos_x += self.posx
		diag.actual.pos_y += self.posy
		diag.Pintar()

	def EnSilaba(self, s):
		if not s._texto.strip():
			return #nunca pongas un return adentro de un grupo (o sea antes de grupofin)
		s.Fade(1, 0)
		s.actual.pos_x += self.posx
		s.actual.pos_y += self.posy
		advanced.StartGroup()
		s.Pintar()
		advanced.fGlow(5, 0.08*s.progreso)
		advanced.EndGroup()
		
		valor= random.randint(0,1)
		if valor == "1":
			ZethPRO= common.Interpolar(random.random(), -15, 10)
		else:
			ZethPRO= common.Interpolar(random.random(), 10, 15)
		self.parts.DarPosicion( s.actual.pos_x + s.progreso*s.original._ancho, s.actual.pos_y + ZethPRO)
		self.parts.Emitir()

	def EnDialogoSale(self, d):
		d.original.modo_relleno = d.P_DEG_VERT
		d.Fade(1, 0)
		d.Pintar()
		
class traduANDkanji(common.Fx):
	def EnDialogo(self, d):
		d.PintarConCache()

	def EnDialogoEntra(self, d):
		desp = sin(pi*d.progreso)*15
		ZethRandom= random.randint(0,1)
		if ZethRandom == 0:
			d.actual.pos_x -= desp
		else:
			d.actual.pos_x += desp
		d.Fade(0, 1)
		d.Pintar()

	def EnDialogoSale(self, d):
		desp = sin(pi*d.progreso)*15
		ZethRandom= random.randint(0,1)
		if ZethRandom == 0:
			d.actual.pos_x -= desp
		else:
			d.actual.pos_x += desp
		d.Fade(1,0)
		d.Pintar()
		

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.saltar_cuadros = False
		self.in_ms = 250
		self.out_ms = 250
		self.syl_in_ms = 500
		self.syl_out_ms = 200
		self.fxs = (FX1(), FX2(), traduANDkanji(),)
	def EnCuadroInicia(self):
		advanced.StartGroup()
	def EnCuadroFin(self):
		advanced.fGlow(2, 0.06)
		advanced.EndGroup()
		advanced.ModoPintado('add')
		self.fxs[1].parts.Pintar()
		advanced.ModoPintado('over')
		self.fxs[0].movimiento +=1
		self.fxs[1].posx= random.random()*6
		self.fxs[1].posy= random.random()*6.5