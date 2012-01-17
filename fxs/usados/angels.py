# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado
from random import random
from math import pi, cos, sin

class Romanji(comun.Fx):
	def EnSilabaInicia(self, d):
		#Por cada silaba que inicia
		#Elegimos un angulo random,
		#usamos Interpolar porque me resulta comodo para elegir un valor entre 2 valores
		ang = comun.Interpolar(4, 5, random())
		#Una distancia máxima, dividiendo la duracion obtenemos una velocidad similar para todas las silabas, dependiendo de su duracion
		dist = d._dur/30.0 #milisegundos de duracion /15, a 30fps son como 2px por frame...
		#una linda forma de hacer una veloicdad constante (remember vel = dist/time solo puedes cambiar 1 por vez)
		d.mov_x = cos(ang)*dist
		d.mov_y = sin(ang)*-dist
		
	def EnDialogoEntra(self, d):
		#como el org modifica la transformacion del texto (posicion, escala, rotacion) 
		#le ponemos como parámetro que no transforme, es una limitacion actual
		#porque como los degradados usan tambien el origen, solo podemos cambiar 
		#o el degradado o la transformacion. (aunque en realidad solo afecta cuando realizamos escalado y/o rotacion)
		a = d.actual
		#alpha del color secundario actual a 0
		a.color2.a = 0.0
		a.modo_relleno = d.P_AN_DEG_LIN
		a.modo_borde = d.P_AN_DEG_LIN
		d.Pintar()
				
	def EnSilaba(self, diag):
		#Cuando la silaba esta activa
		#(cacheamos diag.actual)
		a = diag.actual
		#Copiamos el color del borde al color primario
		a.color1.CopiarDe(a.color3)
		#Lo movemos hacia la posicion que calculamos en el EnSilabaInicia
		diag.MoverA(diag.mov_x, diag.mov_y)
		#y hacemos que se escale de 1 a 0.5
		a.scale_x = a.scale_y = comun.Interpolar(diag.progreso, 1, 0.5)
		#Lo desvanecemos y lo pintamos
		diag.Desvanecer(1, 0)
		diag.Pintar()
		
	def EnSilabaDorm(self, d):
		#Las sílabas inactivas...
		d.Pintar()

class tradu(comun.Fx):
	def EnDialogo(self, d):
		d.PintarConCache()

	def EnDialogoEntra(self, d):
		#Calculamos el desplazamiento con la funcion seno, para q parezca tener aceleacion
		desp = sin(pi*d.progreso)*15 #aumentará hasta 20 px, en una acelearcion como una curva. q va d 0 a 1  y de nuevo a 0 (porque el angulo del seno es de 0 a 180º
		#lo movemos en las Y (verticalmente)
		d.actual.pos_y -= desp
		d.Desvanecer(0, 1)
		d.Pintar()
		
	def EnDialogoSale(self, d):
		desp = sin(pi*d.progreso)*15
		d.actual.pos_y += desp
		d.Desvanecer(1,0)
		d.Pintar()

class cred(comun.Fx):
	def EnDialogo(self, d):
		#Usando alpha podemos elegir un valor de alpha manualmente,
		#Entonces puedo usar la funcion seno que me dara valores de 0 a 1 en una forma mas suave
		d.Alpha(sin(pi*d.progreso))
		#Esto tambien es posible usando Desvanecer y especificando otro interpolador (comun.i_sin) pero eso es mas avanzado :B
		d.Pintar()
		
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		#Un effect si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 500 #Milisegundos para la animacion de entrada
		self.out_ms = 500 #MS para animacion d salida
		self.syl_in_ms = 250 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = ( Romanji(), tradu(), cred())
		
	def EnCuadroInicia(self): #Cuando el cuadro inicie
		avanzado.StartGroup() #Empezamos un grupo de pintura
		 
	def EnCuadroFin(self):#Cuando termine el cuadro
		#cerramos el grupo y guardamos lo que se pinto en un patron
		pat = avanzado.EndGroup()
		#Iniciamos otro grupo
		avanzado.StartGroup()
		#Ponemos el color a blanco
		video.cf.ctx.set_source_rgba(1,1,1,1)
		#Pintamos la sombra de lo que había en el patron
		avanzado.Sombra(pat, 3)
		avanzado.fGlow(2, 0.02)#Hacemos un glow a todo lo que se dibujó
		avanzado.EndGroup()#Y cerramos el grupo

		#De esta manera la sombra no se superpone por cada silaba
