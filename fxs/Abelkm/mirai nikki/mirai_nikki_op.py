# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos


t1 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/T_Negro22.png', extend=cairo.EXTEND_REFLECT)
t2 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/T_Blanco2.png', extend=cairo.EXTEND_REFLECT)
t3 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/KAFX/branches/kafx_eng/textures/sangre3.png', extend=cairo.EXTEND_REFLECT)



class FX2():
	def __init__(self):
		self.eventos = [Evento7(), Evento8(), Evento9(), Evento11(), Evento12()]



	def EnDialogo(self, d):
		d.actual.color1.a = 0
		d.actual.color3.a = 0
		d.FullWiggle(14, 15)
		d.Paint()

	def EnDialogoSale(self, d):
		global t1, t2

		d.texturas[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveTo(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(1, 0, common.i_accel)
		d.Paint()



	def EnDialogoEntra(self, d):
		global t1, t2


		d.texturas[d.PART_FILL] = t2
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveFrom(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(0, 1, common.i_accel)
		d.Paint()

class Evento11():
        def EnLetra(self, letra):
			global t1, t2
			letra.texturas[letra.PART_FILL] = t1
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t2
			letra.actual.mode_border = letra.P_TEXTURA
			advanced.CapasActivar(10)
			letra.Paint()

        def TiempoLetra(self, letra):
			return (letra._parent._end, letra._parent._parent._end)
class Evento12():
        def EnLetra(self, letra):
			global t1, t2
			letra.texturas[letra.PART_FILL] = t2
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t1
			letra.actual.mode_border = letra.P_TEXTURA
			advanced.CapasActivar(11)
			letra.Paint()

        def TiempoLetra(self, letra):
			return (letra._parent._parent._start, letra._parent._end)

class Evento7():
		def EnSilaba(self, sil):
						global t3, p
						sil.actual.color3.a = 0
						sil.actual.color1.a = 0.5
						sil.texturas[sil.PART_FILL] = t3
						sil.actual.mode_fill = sil.P_TEXTURA
						advanced.CapasActivar(12)
						advanced.StartGroup()

						sil.Paint()
						advanced.fGlow(1, 0.15+(common.Interpolate(sil.progress, 0, 0.15, common.i_b_boing)))
						advanced.EndGroup()
						sil.actual.color3.a = 0
						sil.actual.color1.a = 0.5
						sil.texturas[sil.PART_FILL] = t3
						sil.actual.mode_fill = sil.P_TEXTURA
						sil.Scale(1, 1.1, common.i_accel)
						advanced.CapasActivar(13)
						advanced.StartGroup()

						sil.Paint()
						advanced.fGlow(2, 0.12+(common.Interpolate(sil.progress, 0, 0.14, common.i_b_boing)))
						advanced.EndGroup()


		def TiempoSilaba(self, sil):
                        return (sil._start, sil._end)


class Evento8():
        def EnLetra(self, sil):
						global t3
						sil.actual.color3.a = 0
						sil.actual.color1.a = common.Interpolate(sil.progress, 0, 0.5)
						sil.texturas[sil.PART_FILL] = t3
						sil.actual.mode_fill = sil.P_TEXTURA
						advanced.CapasActivar(14)
						advanced.StartGroup()

						sil.Paint()
						advanced.fGlow(2, 0.1)
						advanced.EndGroup()
						sil.actual.color3.a = 0
						sil.actual.color1.a = common.Interpolate(sil.progress, 0, 0.5)
						advanced.CapasActivar(15)
						sil.Paint()

        def TiempoLetra(self, sil):
                        return (sil._start - 15, sil._start)


class Evento9():
        def EnSilaba(self, sil):
						global t3
						sil.actual.color3.a = 0
						sil.actual.color1.a = common.Interpolate(sil.progress, 0.5, 0)
						sil.texturas[sil.PART_FILL] = t3
						sil.actual.mode_fill = sil.P_TEXTURA
						advanced.CapasActivar(16)
						advanced.StartGroup()

						sil.Paint()
						advanced.fGlow(1, 0.15+(common.Interpolate(sil.progress, 0.15, 0, common.i_accel)))
						advanced.EndGroup()
						sil.actual.color3.a = 0
						sil.actual.color1.a = common.Interpolate(sil.progress, 0.5, 0)
						sil.texturas[sil.PART_FILL] = t3
						sil.actual.mode_fill = sil.P_TEXTURA
						sil.Scale(1.1, 1, common.i_accel)
						advanced.CapasActivar(17)
						advanced.StartGroup()
						sil.Paint()
						advanced.fGlow(2, 0.12+(common.Interpolate(sil.progress, 0.15, 0, common.i_accel)))
						advanced.EndGroup()

        def TiempoSilaba(self, sil):
                        return (sil._end, sil._end+150)



class FX3():
        def __init__(self):
                self.eventos = [Evento1(), Evento2(), Evento3(), Evento13(), Evento14()]




	def EnDialogo(self, d):
		d.actual.color1.a = 0
		d.actual.color3.a = 0
		d.FullWiggle(20, 15)
		d.Paint()



	def EnDialogoSale(self, d):
		global t1, t2

		d.texturas[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveTo(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(1, 0, common.i_accel)
		d.Paint()



	def EnDialogoEntra(self, d):
		global t1, t2


		d.texturas[d.PART_FILL] = t2
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveFrom(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(0, 1, common.i_accel)
		d.Paint()

class Evento13():
        def EnLetra(self, letra):
			global t1, t2
			letra.texturas[letra.PART_FILL] = t1
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t2
			letra.actual.mode_border = letra.P_TEXTURA
			advanced.CapasActivar(18)
			letra.Paint()

        def TiempoLetra(self, letra):
			return (letra._start, letra._parent._parent._end)
class Evento14():
        def EnLetra(self, letra):
			global t1, t2
			letra.texturas[letra.PART_FILL] = t2
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t1
			letra.actual.mode_border = letra.P_TEXTURA
			advanced.CapasActivar(19)
			letra.Paint()

        def TiempoLetra(self, letra):
			return (letra._parent._parent._start, letra._start)

class Evento1():
                def EnLetra(self, letra):
						global t3
						letra.actual.color3.a = 0
						letra.actual.color1.a = 0.5
						letra.texturas[letra.PART_FILL] = t3
						letra.actual.mode_fill = letra.P_TEXTURA
						advanced.CapasActivar(20)
						advanced.StartGroup()
						letra.Paint()
						advanced.fGlow(1, 0.15+(common.Interpolate(letra.progress, 0, 0.15, common.i_b_boing)))
						advanced.EndGroup()
						letra.actual.color3.a = 0
						letra.actual.color1.a = 0.5
						letra.texturas[letra.PART_FILL] = t3
						letra.actual.mode_fill = letra.P_TEXTURA
						letra.Scale(1, 1.1, common.i_accel)
						advanced.CapasActivar(21)
						advanced.StartGroup()
						letra.Paint()
						advanced.fGlow(2, 0.15+(common.Interpolate(letra.progress, 0, 0.15, common.i_b_boing)))
						advanced.EndGroup()


                def TiempoLetra(self, letra):
                        return (letra._start, letra._end)


class Evento2():
        def EnLetra(self, letra):
						global t3
						letra.actual.color3.a = 0
						letra.actual.color1.a = common.Interpolate(letra.progress, 0, 0.5, common.i_accel)
						letra.texturas[letra.PART_FILL] = t3
						letra.actual.mode_fill = letra.P_TEXTURA
						advanced.CapasActivar(22)
						advanced.StartGroup()
						letra.Paint()
						advanced.fGlow(2, 0.1)
						advanced.EndGroup()
						letra.actual.color3.a = 0
						letra.actual.color1.a = common.Interpolate(letra.progress, 0, 0.5,  common.i_accel)
						advanced.CapasActivar(23)
						letra.Paint()

        def TiempoLetra(self, letra):
                        return (letra._start - 15, letra._start)


class Evento3():
        def EnLetra(self, letra):
						global t3
						letra.actual.color3.a = 0
						letra.actual.color1.a = common.Interpolate(letra.progress, 0.5, 0, common.i_accel)
						letra.texturas[letra.PART_FILL] = t3
						letra.actual.mode_fill = letra.P_TEXTURA
						advanced.CapasActivar(24)
						advanced.StartGroup()
						letra.Paint()
						advanced.fGlow(1, 0.15+(common.Interpolate(letra.progress, 0.15, 0, common.i_accel)))
						advanced.EndGroup()
						letra.actual.color3.a = 0
						letra.actual.color1.a = common.Interpolate(letra.progress, 0.5, 0, common.i_accel)
						letra.texturas[letra.PART_FILL] = t3
						letra.actual.mode_fill = letra.P_TEXTURA
						letra.Scale(1.1, 1, common.i_accel)
						advanced.StartGroup()
						letra.Paint()
						advanced.fGlow(2, 0.15+(common.Interpolate(letra.progress, 0.15, 0, common.i_accel)))
						advanced.EndGroup()

        def TiempoLetra(self, letra):
                        return (letra._end, letra._end+400)





class FX1():
	def __init__(self):
		self.t = extra.LoadTexture("textures/sangre2.png")
		self.eventos = [Evento4(), Evento5(), Evento6(), Evento10()]

	def EnLetraInicia(self, letra):
		letra.actual.shadow = 0
		letra.actual.border = 0
		letra.parts = letra.CreateParticles(self.t, 0.1, mode = 1)
		for p in letra.parts:
			p.inix = p.x
			p.iniy = p.y
			p.movx = p.inix + random.randint(-20, 20) - random.randint(-10, 10) - random.randint(-10, 10)
			p.movy = p.iniy + random.randint(-20, 20) - random.randint(-10, 10) - random.randint(-10, 10)
			p.movx2 = p.inix + random.randint(-0, 40)
			p.movy3 = p.iniy + random.randint(-10, 10)
			p.movx3 = p.inix + random.randint(-40, 0)
			p.esc = 0.1
			p.maxx = random.randint(1, 30)
			p.maxy = random.randint(1, 30)



	def EnSilabaMuerta(self, d):
		global t1, t2
		advanced.CapasActivar(4)

		d.texturas[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURA
		d.Paint()


	def EnDialogoSale(self, d):
		global t1, t2
		advanced.CapasActivar(2)
		d.texturas[d.PART_FILL] = t1
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t2
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveTo(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(1, 0, common.i_accel)
		d.Paint()



	def EnDialogoEntra(self, d):
		global t1, t2
		advanced.CapasActivar(1)

		d.texturas[d.PART_FILL] = t2
		d.actual.mode_fill = d.P_TEXTURA
		d.texturas[d.PART_BORDER] = t1
		d.actual.mode_border = d.P_TEXTURA
		d.Wiggle(10, 6)
		d.MoveFrom(random.randint(-20, 10),random.randint(-20, 10))
		d.Fade(0, 1, common.i_accel)
		d.Paint()



class Evento4():
        def EnLetra(self, letra):

			for p in letra.parts:
				p.color.a = common.Interpolate(letra.progress, 1, 0, common.i_accel)
				p.y += random.random()*2
				advanced.CapasActivar(6)
				p.Paint()

        def TiempoLetra(self, letra):
			return (letra._start, letra._end+500)

class Evento5():
        def EnLetra(self, letra):

			advanced.CapasActivar(8)
			for p in letra.parts:

				p.color.a = common.Interpolate(letra.progress, 0, 1, common.i_accel)
				p.Paint()

        def TiempoLetra(self, letra):
			return (letra._start, letra._end)


class Evento6():
        def EnLetra(self, letra):
			global t1, t2
			advanced.CapasActivar(5)

			letra.texturas[letra.PART_FILL] = t1
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t2
			letra.actual.mode_border = letra.P_TEXTURA
			letra.Paint()


        def TiempoLetra(self, letra):
			return (letra._start, letra._parent._end)

class Evento10():
        def EnLetra(self, letra):
			global t1, t2
			letra.texturas[letra.PART_FILL] = t2
			letra.actual.mode_fill = letra.P_TEXTURA
			letra.texturas[letra.PART_BORDER] = t1
			letra.actual.mode_border = letra.P_TEXTURA
			advanced.CapasActivar(3)
			letra.Paint()


        def TiempoLetra(self, letra):
			return (letra._parent._parent._start, letra._parent._end)

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 200
		self.out_ms = 200
		self.dividir_letras = True
		self.fxs = (FX1(), FX2(), FX3())


	def EnCuadroInicia(self):
		advanced.CapasInicia()
	def EnCuadroFin(self):
		advanced.CapasFin()