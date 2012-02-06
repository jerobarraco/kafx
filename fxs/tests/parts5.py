# -*- coding: utf-8 -*-
from libs import common
from libs.draw import extra
import random
from math import pi, cos, sin, hypot, atan2

class Fxpart (common.Fx):
	def __init__(self):
		self.t = extra.LoadTexture("textures/star1.png")

	def EnSilabaEntra(self, sil):
		for p in sil.parts:
			p.color.a = common.Interpolar (sil.progreso, 0, 1)
			p.x = common.Interpolar(sil.progreso, p.movx, p.inix)
			p.y = common.Interpolar(sil.progreso, p.movy, p.iniy)
			p.Pintar()

	def EnSilabaSale(self, sil):
		for p in sil.parts:
			angulo = common.Interpolar(sil.progreso, p.ang, p.mang)
			p.color.a = common.Interpolar (sil.progreso, 1, 0)
			p.x = sil.centx- cos(angulo)*p.rad
			p.y = sil.centy+ sin(angulo)*p.rad
			#p.y = p.iniy
			p.Pintar()

	def EnSilabaInicia(self, sil):
		sil.parts = sil.CreateParticles(self.t, 0.1)
		sil.centx = sil.actual.pos_x +sil.actual.org_x
		sil.centy = sil.actual.pos_y -sil.actual.org_y
		print sil.actual.pos_x, sil.centx, sil.actual.pos_y, sil.centy
		for p in sil.parts:
			p.inix = p.x
			p.iniy = p.y
			p.difx = p.x - sil.centx
			p.dify = p.y - sil.centy
			p.rad = hypot(p.difx, p.dify)
			p.ang = atan2(p.difx, p.dify)	+ pi/4.0
			p.mang = p.ang + pi*p.rad/10.0
			p.movx = p.inix + random.randint(-0, 40)
			p.movy = p.iniy + random.randint(-10, 10)
			p.movx2 = p.inix + random.randint(-40, 0)
			
			p.esc = 0.1

	def EnSilaba(self, sil):
		for p in sil.parts:
			p.x = p.inix
			p.y = p.iniy
			p.Pintar()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = [Fxpart(), common.Fx()]
		self.saltar_cuadros = False
		self.syl_in_ms = 400
		self.syl_out_ms = 400