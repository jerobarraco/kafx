# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""


from libs import comun, video
from libs.draw import avanzado, extra

import random, cairo
from math import pi, sin, cos

fondo = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/metal3.png', extend=cairo.EXTEND_REFLECT)
textura0 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/ror1.png', extend=cairo.EXTEND_REFLECT)
textura1 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/celeste1.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/rojo2.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/blanco3.png', extend=cairo.EXTEND_REFLECT)
textura4 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/violeta1.png', extend=cairo.EXTEND_REFLECT)
textura5 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/amarillo1.png', extend=cairo.EXTEND_REFLECT)
textura6 = extra.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/azul3.png', extend=cairo.EXTEND_REFLECT)



class FX1(comun.Fx):
	def EnDialogo(self, d):
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura0
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX2(comun.Fx):
	def EnDialogo(self, d):
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX3(comun.Fx):
	def EnDialogo(self, d):
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX4(comun.Fx):
	def EnDialogo(self, d):
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX5(comun.Fx):
	def EnDialogo(self, d):
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX6(comun.Fx):
	def EnDialogo(self, d):
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX7(comun.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX8(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX9(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.MoverDe(0, -10, comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, -10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

#hasta aca son romajis, ahora empiezan los kanjis

class FX10(comun.Fx):
	def EnDialogo(self, d):
		global textura0
		d.actual.pos_x = -100
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.actual.pos_x = -100
		d.Mover((-110, 214), (-100, 214), comun.i_accel)

		d.Pintar()

	def EnSilaba(self, d):
		global textura0
		d.actual.pos_x = 20
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura0
		d.Desvanecer(1,0)
		d.Mover((-100, 214), (-110, 214), comun.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX11(comun.Fx):
	def EnDialogo(self, d):
		global textura1
		d.actual.pos_x = -80
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-90, 214), (-80, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		mitextura = textura1
		d.actual.pos_x = 20
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Desvanecer(1,0)
		d.Mover((-80, 214), (-90, 214),  comun.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX11b(comun.Fx):
	def EnDialogo(self, d):
		global textura1
		d.actual.pos_x = -130
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-140, 214), (-130, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		d.actual.pos_x = 20
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Desvanecer(1,0)
		d.Mover((-130, 214), (-140, 214),  comun.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX12(comun.Fx):
	def EnDialogo(self, d):
		global textura2
		d.actual.pos_x = -139.5
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-150, 214), (-139.5, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura2
		d.actual.pos_x = 20
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Desvanecer(1,0)
		d.Mover((-139.5, 214), (-150, 214),  comun.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX13(comun.Fx):
	def EnDialogo(self, d):
		global textura3
		d.actual.pos_x = -100
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-110, 214), (-100, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		d.actual.pos_x = 20
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Desvanecer(1,0)
		d.Mover((-100, 214), (-110, 214),  comun.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX13b(comun.Fx):
	def EnDialogo(self, d):
		global textura3
		d.actual.pos_x = -104
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-114, 214), (-104, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		d.actual.pos_x = 20
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Desvanecer(1,0)
		d.Mover((-104, 214),(-114, 214), comun.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX14(comun.Fx):
	def EnDialogo(self, d):
		global textura4
		d.actual.pos_x = -139
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-149, 214), (-139, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura4
		d.actual.pos_x = 20
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Desvanecer(1,0)
		d.Mover( (-139, 214), (-149, 214), comun.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX15(comun.Fx):
	def EnDialogo(self, d):
		global textura5
		d.actual.pos_x = -64
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover( (-74, 214), (-64, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Desvanecer(1,0)
		d.Mover((-64, 214),  (-74, 214), comun.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()
class FX15b(comun.Fx):
	def EnDialogo(self, d):
		global textura5
		d.actual.pos_x = -34
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-44, 214),  (-34, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Desvanecer(1,0)
		d.Mover( (-34, 214), (-44, 214), comun.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX15c(comun.Fx):
	def EnDialogo(self, d):
		global textura5
		d.actual.pos_x = -100
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover( (-110, 214), (-100, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Desvanecer(1,0)
		d.Mover((-100, 214), (-110, 214),  comun.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX16(comun.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		d.actual.pos_x = -70
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover((-80, 214), (-70, 214),  comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura6, textura5
		d.actual.pos_x = 20
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.Mover( (-70, 214), (-80, 214), comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX17(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		d.actual.pos_x = -80
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover( (-90, 214), (-80, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		d.actual.pos_x = 20
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.Mover((-80, 214), (-90, 214),  comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX18(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		d.actual.pos_x = -135
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Desvanecer(0,1)
		d.Mover( (-145, 214), (-135, 214), comun.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		d.actual.pos_x = 20
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		avanzado.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		avanzado.GrupoFin()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.Mover( (-135, 214), (-145, 214), comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()
#hasta aca los kanjis, ahora la tradu T_______________________T no moar!!!


class FX19(comun.Fx):
	def EnDialogo(self, d):
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura0
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX20(comun.Fx):
	def EnDialogo(self, d):
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura1
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX21(comun.Fx):
	def EnDialogo(self, d):
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX22(comun.Fx):
	def EnDialogo(self, d):
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura3
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX23(comun.Fx):
	def EnDialogo(self, d):
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX24(comun.Fx):
	def EnDialogo(self, d):
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura5
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX25(comun.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = comun.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX26(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX27(comun.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Desvanecer(0,1)
		d.MoverDe(0, 10, comun.i_accel)
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = comun.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Desvanecer(1,0)
		d.MoverA(0, 10, comun.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FxsGroup(comun.FxsGroup):
        def __init__(self):
                self.movimiento = 0
                self.in_ms = 200
                self.out_ms = 200
                self.fxs = (FX1(),FX2(),FX3(),FX4(),FX5(),FX6(),FX7(),FX8(),FX9(),FX10(),FX11(),FX12(),FX13(),FX13b(),FX11b(),FX14(),FX15(),FX15b(),FX16(),FX17(),FX18(),FX15c(),FX19(),FX20(),FX21(),FX22(),FX23(),FX24(),FX25(),FX26(),FX27())

        def EnCuadroInicia(self):
                avanzado.GrupoInicio()
        def EnCuadroFin(self):
                self.movimiento += 1
                avanzado.fOnda(self.movimiento, 0.025, 2,  False)
                avanzado.fOnda(self.movimiento, 0.02, 1,  True)
                avanzado.GrupoFin()