# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
"""


from libs import comun
from libs.draw import avanzado, extra

import random, cairo
from math import pi, sin, cos

textura = extra.CargarTextura('spiral/metal6.png', extend=cairo.EXTEND_REPEAT)
textura2 = extra.CargarTextura('spiral/metal5.png', extend=cairo.EXTEND_REPEAT)
textura3 = extra.CargarTextura('spiral/metal6.png', extend=cairo.EXTEND_REPEAT)

class FX1(comun.Fx):
    def EnDialogo(self, diag):
        global textura
        global textura2
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.MoverTextura( 60*diag.progreso, 60*diag.progreso, diag.actual.org_x, diag.actual.org_y, 0, diag.actual.scale_x, diag.actual.scale_y, diag.PART_RELLENO)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(0.2)
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore() #el restore pone el modo relleno en el normal
        diag.texturas[diag.PART_RELLENO] = textura2
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()

    def EnDialogoEntra(self, diag):
        global textura
        global textura2
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.Desvanecer(0,1)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(comun.Interpolar(diag.progreso, 0, 0.2))
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore()
        diag.texturas[diag.PART_RELLENO] = textura2
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Desvanecer(0,1)
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.fBiDirBlur(pi, (sin(pi*diag.progreso)*5.0))
        avanzado.GrupoFin()

    def EnSilaba(self, sil):
        global textura3
        sil.texturas[sil.PART_RELLENO] = textura3
        sil.actual.modo_relleno = sil.P_TEXTURA
        sil.actual.color1.r = comun.Interpolar(sil.progreso, 0.8, 1)
        sil.actual.color1.g = comun.Interpolar(sil.progreso, 0.9, 1)
        sil.actual.color1.b = comun.Interpolar(sil.progreso, 1, 1)
        sil.Alpha(comun.Interpolar(sil.progreso, 1, 0.5))
        avanzado.GrupoInicio()
        sil.Pintar()
        avanzado.fGlow(1, comun.Interpolar(sil.progreso, 0.1, 0)+((sin(pi*sil.progreso))/6.0))
        avanzado.fBiDirBlur(random.randint(-2,2)/pi, 4*sil.progreso, 0.25)
        avanzado.GrupoFin()

    def EnSilabaMuerta(self, sil):
        global textura3
        sil.texturas[sil.PART_RELLENO] = textura3
        sil.actual.modo_relleno = sil.P_TEXTURA
        sil.Pintar()

    def EnDialogoSale(self, diag):
        global textura
        global textura3
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.Desvanecer(1,0)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(comun.Interpolar(diag.progreso, 0.2, 0))
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore()
        diag.texturas[diag.PART_RELLENO] = textura3
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Desvanecer(1,0)
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.fBiDirBlur(pi, (sin(pi*diag.progreso)*5.0))
        avanzado.GrupoFin()


class FX2(comun.Fx):
    def EnDialogo(self, diag):
        global textura
        global textura2
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.MoverTextura( 60*diag.progreso, 60*diag.progreso, diag.actual.org_x, diag.actual.org_y, 0, diag.actual.scale_x, diag.actual.scale_y, diag.PART_RELLENO)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(0.2)
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore()
        diag.texturas[diag.PART_RELLENO] = textura2
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()

    def EnDialogoEntra(self, diag):
        global textura
        global textura2
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.Desvanecer(0,1)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(comun.Interpolar(diag.progreso, 0, 0.2))
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore()
        diag.texturas[diag.PART_RELLENO] = textura2
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Desvanecer(0,1)
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.fBiDirBlur(pi, (sin(pi*diag.progreso)*5.0))
        avanzado.GrupoFin()

    def EnDialogoSale(self, diag):
        global textura
        global textura2
        diag.texturas[diag.PART_RELLENO] = textura
        diag.actual.modo_relleno = diag.P_TEXTURA
        diag.Desvanecer(1,0)
        diag.Pintar()
        avanzado.GrupoInicio()
        diag.Alpha(comun.Interpolar(diag.progreso, 0.2, 0))
        diag.Pintar()
        avanzado.fBiDirBlur(2/pi, 6, 0.15)
        avanzado.fRotoZoom(1, 0.25, 1, 0, org_x=0, org_y=0)
        avanzado.fGlow(5, 0.005)
        avanzado.GrupoFin()
        diag.Restore()
        diag.texturas[diag.PART_RELLENO] = textura2
        diag.actual.modo_relleno = diag.P_TEXTURA
        avanzado.GrupoInicio()
        diag.Desvanecer(1,0)
        diag.Pintar()
        avanzado.fGlow(5, 0.005)
        avanzado.fBiDirBlur(pi, (sin(pi*diag.progreso)*5.0))
        avanzado.GrupoFin()



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 200
		self.out_ms = 200
		self.fxs = (FX1(), FX2())
