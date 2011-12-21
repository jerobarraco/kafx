# -*- coding: utf-8 -*-
"""
Hecho por Abelkm
http://my.opera.com/Abelkm/blog/
reemplazar las imágenes por otras para probarlo, no las voy a subir al svn
"""


from libs import comun
from libs.draw import avanzado
from math import pi, sin, cos

class FX1(comun.Fx):

	def EnSilaba(self, d):
		d.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/glass3.png', parte = d.PART_RELLENO)
		d.MoverTextura( 60*d.progreso, 60*d.progreso, parte = d.PART_RELLENO)
		d.actual.color1.a = 0.6
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fGlow(2, ((sin(pi*d.progreso))/6.0))
		avanzado.GrupoFin()




	def EnSilabaMuerta(self, d):
		d.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/glass3.png', parte=d.PART_RELLENO)
		d.actual.color1.a = 0.6
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.ModoPintado('add')
		avanzado.GrupoFin()


	def EnDialogoSale(self, d):
		d.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/glass3.png', parte=d.PART_RELLENO)
		d.actual.color1.a = comun.Interpolar(d.progreso, 0.6, 0)
		d.actual.color3.a = comun.Interpolar(d.progreso, 1, 0)
		d.actual.borde = comun.Interpolar(d.progreso, 1, 0)
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fBiDirBlur(pi, (sin(pi*d.progreso)*5.0))
		avanzado.ModoPintado('add')
		avanzado.GrupoFin()

	def EnDialogoEntra(self, d):
		d.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/glass1.png', parte=d.PART_RELLENO)
		d.actual.color1.a = comun.Interpolar(d.progreso, 0, 0.6)
		d.actual.color3.a = comun.Interpolar(d.progreso, 0, 1)
		d.actual.borde = comun.Interpolar(d.progreso, 0, 1)
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fBiDirBlur(pi, (sin(pi*d.progreso)*5.0))
		avanzado.ModoPintado('add')
		avanzado.GrupoFin()


	def EnSilabaDorm(self, d):
		d.CargarTextura('E:/Documents and Settings/Administrador/Escritorio/Nueva carpeta/texturas/glass1.png', parte=d.PART_RELLENO)
		d.actual.color1.a = 0.6
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.ModoPintado('add')
		avanzado.GrupoFin()


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 240
		self.out_ms = 300
		self.fxs = (FX1(), FX1())
