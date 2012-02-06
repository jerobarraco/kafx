# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


t1 = extra.LoadTexture("textures/snowflake2.png", extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture("textures/snowflake2.png", extend=cairo.EXTEND_REFLECT)
t3 = extra.LoadTexture("textures/snowflake2.png", extend=cairo.EXTEND_REFLECT)



class FX1(common.Fx):
	def __init__(self):
		self.events = [Evento1(), Evento2(), Evento3()]
	def EnSilaba(self, sil):
		sil.FullWiggle(20,4)
		sil.Paint()
	def EnDialogoSale(self, d):
		global t1, t2
		d.texturas[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURA
		d.Fade(1,0, common.i_b_ease_out)
		advanced.StartGroup()
		d.Paint()
		advanced.fBlur1(3, common.Interpolate(d.progress, 0, 0.15, common.i_b_ease_in))
		advanced.EndGroup()


        def EnDialogoEntra(self, d):
                global t1, t2
                d.texturas[d.PART_FILL] = t1
                d.actual.mode_fill = d.P_TEXTURA
                d.texturas[d.PART_BORDER] = t2
                d.actual.mode_border = d.P_TEXTURA
                d.Fade(0,1, common.i_b_ease_in)
                advanced.StartGroup()
                d.Paint()
                advanced.fBlur1(3, common.Interpolate(d.progress, 0.15, 0, common.i_b_ease_in))
                advanced.EndGroup()



class Evento1(common.Event):
                def EnLetra(self, letra):
                        global t3, p
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = 0.5
                        letra.texturas[letra.PART_FILL] = t3
                        letra.actual.mode_fill = letra.P_TEXTURA
                        advanced.StartGroup()
                        letra.Paint()
                        advanced.fGlow(1, 0.15+(common.Interpolate(letra.progress, 0, 0.15, common.i_b_boing)))
                        advanced.EndGroup()
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = 0.5
                        letra.texturas[letra.PART_FILL] = t3
                        letra.actual.mode_fill = letra.P_TEXTURA
                        #letra.Scale(1, 1.1, comun.i_accel)
                        advanced.StartGroup()
                        letra.Paint()
                        advanced.fGlow(2, 0.15+(common.Interpolate(letra.progress, 0, 0.15, common.i_b_boing)))
                        advanced.EndGroup()


                def TiempoLetra(self, letra):
                        return (letra._start, letra._end)


class Evento2(common.Event):
        def EnLetra(self, letra):
                        global t3
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = common.Interpolate(letra.progress, 0, 0.5,  common.i_b_ease_in)
                        letra.texturas[letra.PART_FILL] = t3
                        letra.actual.mode_fill = letra.P_TEXTURA
                        advanced.StartGroup()
                        letra.Paint()
                        advanced.fGlow(2, 0.1)
                        advanced.EndGroup()
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = common.Interpolate(letra.progress, 0, 0.5,  common.i_b_ease_in)
                        letra.Paint()

        def TiempoLetra(self, letra):
                        return (letra._start - 5, letra._start)


class Evento3(common.Event):
        def EnLetra(self, letra):
                        global t3
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = common.Interpolate(letra.progress, 0.5, 0, common.i_accel)
                        letra.texturas[letra.PART_FILL] = t3
                        letra.actual.mode_fill = letra.P_TEXTURA
                        advanced.StartGroup()
                        letra.Paint()
                        advanced.fGlow(1, 0.15+(common.Interpolate(letra.progress, 0.15, 0, common.i_accel)))
                        advanced.EndGroup()
                        letra.actual.color3.a = 0
                        letra.actual.color1.a = common.Interpolate(letra.progress, 0.5, 0, common.i_accel)
                        letra.texturas[letra.PART_FILL] = t3
                        letra.actual.mode_fill = letra.P_TEXTURA
                        #letra.Scale(1.1, 1, comun.i_accel)
                        advanced.StartGroup()
                        letra.Paint()
                        advanced.fGlow(2, 0.15+(common.Interpolate(letra.progress, 0.15, 0, common.i_accel)))
                        advanced.EndGroup()

        def TiempoLetra(self, letra):
                        return (letra._end, letra._end+400)

class FxsGroup(common.FxsGroup):

        def __init__(self):
                        self.in_ms = 200
                        self.out_ms = 400
                        self.dividir_letras = True
                        self.fxs = (FX1(), FX1())