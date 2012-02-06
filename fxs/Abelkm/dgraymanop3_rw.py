# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""


from libs import common, video
from libs.draw import advanced, extra

import random, cairo
from math import pi, sin, cos

fondo = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/metal3.png', extend=cairo.EXTEND_REFLECT)
textura0 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/ror1.png', extend=cairo.EXTEND_REFLECT)
textura1 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/celeste1.png', extend=cairo.EXTEND_REFLECT)
textura2 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/rojo2.png', extend=cairo.EXTEND_REFLECT)
textura3 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/blanco3.png', extend=cairo.EXTEND_REFLECT)
textura4 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/violeta1.png', extend=cairo.EXTEND_REFLECT)
textura5 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/amarillo1.png', extend=cairo.EXTEND_REFLECT)
textura6 = extra.LoadTexture('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/textures/azul3.png', extend=cairo.EXTEND_REFLECT)



class FX1(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura0
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX2(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX3(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX4(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX5(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX6(common.Fx):
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
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX7(common.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX8(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX9(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.MoveFrom(0, -10, common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, -10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

#hasta aca son romajis, ahora empiezan los kanjis

class FX10(common.Fx):
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
		d.Fade(0,1)
		d.actual.pos_x = -100
		d.Move((-110, 214), (-100, 214), common.i_accel)

		d.Pintar()

	def EnSilaba(self, d):
		global textura0
		d.actual.pos_x = 20
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura0
		d.Fade(1,0)
		d.Move((-100, 214), (-110, 214), common.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX11(common.Fx):
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
		d.Fade(0,1)
		d.Move((-90, 214), (-80, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		mitextura = textura1
		d.actual.pos_x = 20
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Fade(1,0)
		d.Move((-80, 214), (-90, 214),  common.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX11b(common.Fx):
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
		d.Fade(0,1)
		d.Move((-140, 214), (-130, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura1
		d.actual.pos_x = 20
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura1
		d.Fade(1,0)
		d.Move((-130, 214), (-140, 214),  common.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX12(common.Fx):
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
		d.Fade(0,1)
		d.Move((-150, 214), (-139.5, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura2
		d.actual.pos_x = 20
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Fade(1,0)
		d.Move((-139.5, 214), (-150, 214),  common.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX13(common.Fx):
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
		d.Fade(0,1)
		d.Move((-110, 214), (-100, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		d.actual.pos_x = 20
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Fade(1,0)
		d.Move((-100, 214), (-110, 214),  common.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX13b(common.Fx):
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
		d.Fade(0,1)
		d.Move((-114, 214), (-104, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3
		d.actual.pos_x = 20
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3
		d.Fade(1,0)
		d.Move((-104, 214),(-114, 214), common.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX14(common.Fx):
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
		d.Fade(0,1)
		d.Move((-149, 214), (-139, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura4
		d.actual.pos_x = 20
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Fade(1,0)
		d.Move( (-139, 214), (-149, 214), common.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX15(common.Fx):
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
		d.Fade(0,1)
		d.Move( (-74, 214), (-64, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Fade(1,0)
		d.Move((-64, 214),  (-74, 214), common.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()
class FX15b(common.Fx):
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
		d.Fade(0,1)
		d.Move((-44, 214),  (-34, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Fade(1,0)
		d.Move( (-34, 214), (-44, 214), common.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX15c(common.Fx):
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
		d.Fade(0,1)
		d.Move( (-110, 214), (-100, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura5
		d.actual.pos_x = 20
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura5
		d.Fade(1,0)
		d.Move((-100, 214), (-110, 214),  common.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX16(common.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		d.actual.pos_x = -70
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.Move((-80, 214), (-70, 214),  common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura6, textura5
		d.actual.pos_x = 20
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.Move( (-70, 214), (-80, 214), common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX17(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		d.actual.pos_x = -80
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.Move( (-90, 214), (-80, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		d.actual.pos_x = 20
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.Move((-80, 214), (-90, 214),  common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX18(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		d.actual.pos_x = -135
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		global fondo
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Fade(0,1)
		d.Move( (-145, 214), (-135, 214), common.i_accel)
		d.Pintar()

	def EnSilaba(self, d):
		global textura3, textura4
		d.actual.pos_x = 20
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.actual.borde = 0
		advanced.StartGroup()
		d.Pintar()
		advanced.fGlow(1, 0.2+(sin(pi*d.progreso)/6.0))
		advanced.fBiDirBlur(random.randint(-4,4)/pi, 4*d.progreso, 0.25)
		advanced.EndGroup()

	def EnSilabaDorm(self, d):
		global fondo
		d.actual.pos_x = 20
		mitextura = fondo
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.Move( (-135, 214), (-145, 214), common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()
#hasta aca los kanjis, ahora la tradu T_______________________T no moar!!!


class FX19(common.Fx):
	def EnDialogo(self, d):
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura0
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura0
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura0
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX20(common.Fx):
	def EnDialogo(self, d):
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura1
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura1
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura1
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX21(common.Fx):
	def EnDialogo(self, d):
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura2
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura2
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura2
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX22(common.Fx):
	def EnDialogo(self, d):
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura3
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura3
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura3
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FX23(common.Fx):
	def EnDialogo(self, d):
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura4
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura4
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura4
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX24(common.Fx):
	def EnDialogo(self, d):
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura5
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura5
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		mitextura = textura5
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX25(common.Fx):
	def EnDialogo(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura6, textura5
		mitextura = common.ElegirPorCuadro(1202,1271,textura5, textura6)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX26(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1502,1561,textura3, textura4)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

class FX27(common.Fx):
	def EnDialogo(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()



	def EnDialogoEntra(self, d):
		d.Fade(0,1)
		d.MoveFrom(0, 10, common.i_accel)
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()

	def EnDialogoSale(self, d):
		global textura3, textura4
		mitextura = common.ElegirPorCuadro(1630,1704,textura4, textura3)
		d.texturas[d.PART_RELLENO] = mitextura
		d.Fade(1,0)
		d.MoveTo(0, 10, common.i_accel)
		d.texturas[d.PART_RELLENO] = mitextura
		d.actual.modo_relleno = d.P_TEXTURA
		d.Pintar()


class FxsGroup(common.FxsGroup):
        def __init__(self):
                self.movimiento = 0
                self.in_ms = 200
                self.out_ms = 200
                self.fxs = (FX1(),FX2(),FX3(),FX4(),FX5(),FX6(),FX7(),FX8(),FX9(),FX10(),FX11(),FX12(),FX13(),FX13b(),FX11b(),FX14(),FX15(),FX15b(),FX16(),FX17(),FX18(),FX15c(),FX19(),FX20(),FX21(),FX22(),FX23(),FX24(),FX25(),FX26(),FX27())

        def EnCuadroInicia(self):
                advanced.StartGroup()
        def EnCuadroFin(self):
                self.movimiento += 1
                advanced.fWave(self.movimiento, 0.025, 2,  False)
                advanced.fWave(self.movimiento, 0.02, 1,  True)
                advanced.EndGroup()