# To change this template, choose Tools | Templates
# and open the template in the editor.


# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos

textura1 = extra.LoadTexture('C:/Users/Anibal/Documents/Everything is here/Software/KAFX/Cairo/textures/happy.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.LoadTexture('C:/Users/Anibal/Documents/Everything is here/Software/KAFX/Cairo/textures/blanco3.png', extend=cairo.EXTEND_REFLECT)

class FX1(comun.Fx):
	def __init__(self):
		self.events = [Evento1()]
	def EnDialogoInicia(self, d):
		d.mov2 = 0
	def EnDialogo(self, d):
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fGlow(1, 0.15)
		avanzado.EndGroup()
		global textura3, textura1
		d.texturas[d.PART_RELLENO] = textura3
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = textura1
		d.actual.modo_borde = d.P_TEXTURA
		d.Pintar()



	def EnDialogoSale(self, diag):
		avanzado.StartGroup()
		diag.Fade(1,0)
		diag.Pintar()
		avanzado.fWave( diag.mov2, 0.01, comun.Interpolar(diag.progreso, 0, 2, comun.i_accel),  True)
		avanzado.fWave( diag.mov2, 0.1, comun.Interpolar(diag.progreso, 0, 2, comun.i_accel),  False)
		avanzado.fGlow(1, 0.15)
		avanzado.EndGroup()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Fade(1,0)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fWave( diag.mov2, 0.01, comun.Interpolar(diag.progreso, 0, 2, comun.i_accel),  True)
		avanzado.fWave( diag.mov2, 0.1, comun.Interpolar(diag.progreso, 0, 2, comun.i_accel),  False)
		avanzado.EndGroup()
		diag.mov2 += 1

	def EnDialogoEntra(self, diag):
		avanzado.StartGroup()
		diag.Fade(0,1)
		diag.Pintar()
		avanzado.fWave( diag.mov2, 0.01, comun.Interpolar(diag.progreso, 2, 0, comun.i_accel),  True)
		avanzado.fWave( diag.mov2, 0.1, comun.Interpolar(diag.progreso, 2, 0, comun.i_accel),  False)
		avanzado.fGlow(1, 0.15)
		avanzado.EndGroup()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Fade(0,1)
		avanzado.StartGroup()
		diag.Pintar()
		avanzado.fWave( diag.mov2, 0.01, comun.Interpolar(diag.progreso, 2, 0, comun.i_accel),  True)
		avanzado.fWave( diag.mov2, 0.1, comun.Interpolar(diag.progreso, 2, 0, comun.i_accel),  False)
		avanzado.EndGroup()
		diag.mov2 += 1



class Evento1(comun.Event):
        def EnLetra(self, letra):
			global textura1
			letra.actual.color3.a = 0
			letra.actual.color1.a = 0.5
			letra.texturas[letra.PART_RELLENO] = textura1
			letra.actual.modo_relleno = letra.P_TEXTURA
			avanzado.StartGroup()
			avanzado.ModoPintado('color_burn')
			letra.Pintar()
			avanzado.fGlow(1, 0.1+(sin(pi*letra.progreso)/6.0))
			avanzado.EndGroup()
			letra.actual.color3.a = 0
			letra.actual.color1.a = 0.5
			avanzado.StartGroup()
			avanzado.ModoPintado('add')
			letra.Pintar()
			avanzado.fBlur1(4, 0.15)
			avanzado.EndGroup()

        def TiempoLetra(self, letra):
                return (letra._start, letra._end)

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 300
		self.out_ms = 300
		self.dividir_letras = True
		self.fxs = (FX1(), FX1())