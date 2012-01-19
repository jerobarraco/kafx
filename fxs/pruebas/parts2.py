# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado, extra
import math, random, cairo
from math import pi, sin, cos
from random import randint


parts_a_pintar = []
parts_a_pintar2 = []
class Evento1(comun.Event):
        def EnSilaba(self, sil):
                global parts_a_pintar
                parts_a_pintar.extend(
                        sil.parts1
                )
                sil.parts1 = []

        def TiempoSilaba(self, sil):
                return (sil._start-400, sil._start)

class Evento2(comun.Event):
        def EnSilaba(self, sil):
                global parts_a_pintar2
                parts_a_pintar2.extend(
                        sil.parts2
                )
                sil.parts2 = []

        def TiempoSilaba(self, sil):
                return (sil._end, sil._end+400)

class Fxpart (comun.Fx):

        def __init__(self):
			self.events = [Evento1(), Evento2()]
			self.t = extra.LoadTexture("textures/star1.png")

        def EnSilabaInicia(self, sil):
			sil.parts1 = sil.CreateParticles(self.t, 0.1 )
			for p in sil.parts1:
				p.inix = p.x
				p.iniy = p.y
				p.movx = p.inix + random.randint(-10, 10)
				p.movy = p.iniy + random.randint(-10, 10)
				p.esc = 0.01
				p.vida1 = 0

			sil.parts2 = sil.CreateParticles(self.t, 0.1 )
			for p in sil.parts2:
				p.inix = p.x
				p.iniy = p.y
				p.movx = p.inix + random.randint(-10, 10)
				p.movy = p.iniy + random.randint(-10, 10)
				p.esc = 0.01
				p.vida2 = 0

        def EnSilaba(self, sil):
			sil.Pintar()

class FxsGroup(comun.FxsGroup):
        def __init__(self):
                self.fxs = [Fxpart()]
                self.saltar_cuadros = False

        def EnCuadroFin(self):
			global parts_a_pintar, parts_a_pintar2
			for p in parts_a_pintar[:]:
				p.color.a += 0.05
				p.x = comun.Interpolar(p.vida1, p.movx, p.inix)
				p.y = comun.Interpolar(p.vida1, p.movy, p.iniy)
				#p.esc -= 0.001
				#p.Scale(p.esc, p.esc)
				p.Pintar()
				p.vida1 += 0.1
				if p.vida1>1:
					parts_a_pintar.remove(p)


			for p in parts_a_pintar2[:]:
				p.color.a -= 0.08
				p.x = comun.Interpolar(p.vida2, p.inix, p.movx)
				p.y = comun.Interpolar(p.vida2, p.iniy, p.movy)
				#p.esc += 0.0005
				#p.Scale(p.esc, p.esc)
				p.Pintar()
				p.vida2 += 0.1
				if p.vida2>1:
					parts_a_pintar2.remove(p)