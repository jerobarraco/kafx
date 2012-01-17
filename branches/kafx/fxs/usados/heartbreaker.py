# -*- coding: utf-8 -*-
import cairo
from random import random

#Importamos las funciones del KAFX~
from libs.draw import extra, avanzado
from libs import video, comun
from math import sin


class FX1(comun.Fx):
	def __init__(self):
		#Cargamos una textura, notar que la textura queda almacenada en el self (o sea en FX1)
		self.textura = comun.CargarTextura('texturas/scan.png')

	def EnSilabaInicia(self, d):
		#Cuando la silaba inicializa
		#cacheamos algunas propiedades
		l= d.original._capa
		t= d._texto
		p= d.original.pos_x
		#creamos una matriz y la guardamos en d (nuestra silaba)
		#esto es porque es mas rapido crear una sola vez la matriz y usarla muchas veces
		d.mat = extra.CrearMatriz(pos_x = random()*-300, pos_y = int(random()*100)*4)
		#*4: para q las lineas horizontales concuerden
		if l ==1:
			#el heart original
			if t =='HEART':		self.pheart = p
			elif t =='Ji' :		self.pji = p
			elif t =='geut':	self.pgeut = p
			elif t =='STILL':	self.pstill = p
			elif t =='BREA':	self.pbrea = p
			elif t =='KER':		self.pker = p
		elif l==2:#hay 2 geuts diferentes
			if t =='Ppi':		self.ppi = p
			if t =='geut':		self.pgeut2 = p
		#estas son copias
		elif l==10:
			#el heart copia
			if t == 'HEART':	d.original.pos_x = self.pheart
			elif t =='Ji' :		d.original.pos_x = self.pji
			elif t =='geut':	d.original.pos_x = self.pgeut
			elif t =='STILL':	d.original.pos_x = self.pstill
			elif t =='BREA':	d.original.pos_x = self.pbrea
			elif t =='KER':		d.original.pos_x = self.pker
		elif l==11:
			if t =='Ppi':		d.original.pos_x = self.ppi
			elif t =='geut':	d.original.pos_x = self.pgeut2

	def EnDialogoSale(self, d):
		if d.original._capa>1 : return
		d.actual.color1.CopiarDe(d.actual.color2)
		d.Desvanecer(1,0)
		d.Pintar()

	def EnDialogoEntra(self, d):
		#obviamos de pintar ciertos dialogos que se repiten
		if d.original._capa>5: return
		d.Desvanecer(0,1)
		d.Pintar()

	def EnSilabaMuerta(self, d):
		if d.original._capa>5: return

		d.actual.color1.CopiarDe(d.actual.color2)
		d.Pintar()

	def EnSilabaDorm(self, d):
		#para el piguettae necesito que se pinten las muertas
		#if d.original._capa>5: return
		d.PintarConCache()

	def EnSilaba(self,d):
		if not d._texto: return
		a = d.actual
		cx = a.org_x
		cy = a.org_y

		#Creamos un patron con degradado radial
		#Con centro en el centro del dialogo
		t = cairo.RadialGradient(cx, cy, 0, cx, cy, d.original._ancho*2)
		t.add_color_stop_rgba(0, a.scolor.r, a.scolor.g, a.scolor.b, a.scolor.a)
		#y que va creciendo con el progreso de la silaba
		t.add_color_stop_rgba(d.progreso, a.color.r, a.color.g, a.color.b, a.color.a)

		#Elegimos el modo de relleno Textura
		d.actual.modo_relleno = d.P_TEXTURA
		#asignamos el degradado a la textura del relleno
		d.texturas[1] = t
		#pintamos y guardamos lo que se pintó en un patron
		pat = d.Pintar()
		
		#escalamos el source para que no quede deformado el noise, asi conservamos un ruido con calidad
		pat.set_matrix(extra.CrearMatriz(pos_x = random()*-5))
		self.textura.set_matrix(d.mat)

		#Si quisieramos que la textura de la mascara se vaya moviendo podriamos hacer esto
		#x = comun.Interpolar(random(), -20, 20)
		#self.textura.set_matrix(extra.CrearMatriz( pos_x=x, pos_y=x))

		avanzado.GrupoInicio()
		#asignamos la textura en pat como source
		video.cf.ctx.set_source(pat)
		#llamamos a máscara usando la textura (ruidosa) como máscara
		video.cf.ctx.mask(self.textura)
		avanzado.fGlow(3,0.1)
		avanzado.GrupoFin()

class FX2(comun.Fx):
	def EnDialogoInicia(self,d):
		#desplazamos la sombra un pixel a la derecha y abajo
		d.original.shad_x = 1
		d.original.shad_y = 1
		d.original.modo_borde = d.P_DEG_VERT

	def EnDialogoEntra(self,d):
		d.Desvanecer(0,1)
		#hacemos que se vaya moviendo hacia abajo con velocidad en seno
		d.actual.pos_y += sin(d.progreso*3.14)*10
		d.Pintar()

	def EnDialogo(self,d):
		d.PintarConCache()

	def EnDialogoSale(self,d):
		d.Desvanecer(1,0)
		#hacemos que se vaya moviendo hacia arriba con velocidad en seno
		d.actual.pos_y -= sin(d.progreso*3.14)*10
		d.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 150 #MS para animacion d salida
		self.sil_in_ms = 0 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 0 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (FX1(), FX2())

