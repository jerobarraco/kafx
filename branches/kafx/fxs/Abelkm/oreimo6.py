# To change this template, choose Tools | Templates
# and open the template in the editor.


# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos

textura1 = extra.LoadTexture('C:/Users/Anibal/Documents/Everything is here/Software/KAFX/Cairo/textures/happy.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.LoadTexture('C:/Users/Anibal/Documents/Everything is here/Software/KAFX/Cairo/textures/blanco3.png', extend=cairo.EXTEND_REFLECT)

class FX1(common.Fx):
	def __init__(self):
		self.events = [Evento1()]
	def EnDialogoInicia(self, d):
		d.mov2 = 0
	def EnDialogo(self, d):
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1
		d.texturas[d.PART_RELLENO] = textura3
		d.actual.modo_relleno = d.P_TEXTURA
		d.texturas[d.PART_BORDE] = textura1
		d.actual.modo_borde = d.P_TEXTURA
		d.Pintar()



	def EnDialogoSale(self, diag):
		advanced.StartGroup()
		diag.Fade(1,0)
		diag.Pintar()
		advanced.fWave( diag.mov2, 0.01, common.Interpolar(diag.progreso, 0, 2, common.i_accel),  True)
		advanced.fWave( diag.mov2, 0.1, common.Interpolar(diag.progreso, 0, 2, common.i_accel),  False)
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Fade(1,0)
		advanced.StartGroup()
		diag.Pintar()
		advanced.fWave( diag.mov2, 0.01, common.Interpolar(diag.progreso, 0, 2, common.i_accel),  True)
		advanced.fWave( diag.mov2, 0.1, common.Interpolar(diag.progreso, 0, 2, common.i_accel),  False)
		advanced.EndGroup()
		diag.mov2 += 1

	def EnDialogoEntra(self, diag):
		advanced.StartGroup()
		diag.Fade(0,1)
		diag.Pintar()
		advanced.fWave( diag.mov2, 0.01, common.Interpolar(diag.progreso, 2, 0, common.i_accel),  True)
		advanced.fWave( diag.mov2, 0.1, common.Interpolar(diag.progreso, 2, 0, common.i_accel),  False)
		advanced.fGlow(1, 0.15)
		advanced.EndGroup()
		global textura3, textura1
		diag.texturas[diag.PART_RELLENO] = textura3
		diag.actual.modo_relleno = diag.P_TEXTURA
		diag.texturas[diag.PART_BORDE] = textura1
		diag.actual.modo_borde = diag.P_TEXTURA
		diag.Fade(0,1)
		advanced.StartGroup()
		diag.Pintar()
		advanced.fWave( diag.mov2, 0.01, common.Interpolar(diag.progreso, 2, 0, common.i_accel),  True)
		advanced.fWave( diag.mov2, 0.1, common.Interpolar(diag.progreso, 2, 0, common.i_accel),  False)
		advanced.EndGroup()
		diag.mov2 += 1



class Evento1(common.Event):
        def EnLetra(self, letra):
			global textura1
			letra.actual.color3.a = 0
			letra.actual.color1.a = 0.5
			letra.texturas[letra.PART_RELLENO] = textura1
			letra.actual.modo_relleno = letra.P_TEXTURA
			advanced.StartGroup()
			advanced.ModoPintado('color_burn')
			letra.Pintar()
			advanced.fGlow(1, 0.1+(sin(pi*letra.progreso)/6.0))
			advanced.EndGroup()
			letra.actual.color3.a = 0
			letra.actual.color1.a = 0.5
			advanced.StartGroup()
			advanced.ModoPintado('add')
			letra.Pintar()
			advanced.fBlur1(4, 0.15)
			advanced.EndGroup()

        def TiempoLetra(self, letra):
                return (letra._start, letra._end)

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 300
		self.out_ms = 300
		self.dividir_letras = True
		self.fxs = (FX1(), FX1())