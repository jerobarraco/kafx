# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced
from random import random
from math import pi, cos, sin

class Romanji(common.Fx):
	def OnSyllableStarts(self, d):
		#Por cada silaba que inicia
		#Elegimos un angulo random,
		#usamos Interpolar porque me resulta comodo para elegir un valor entre 2 valores
		ang = common.Interpolate(4, 5, random())
		#Una distancia máxima, dividiendo la duracion obtenemos una velocidad similar para todas las silabas, dependiendo de su duracion
		dist = d._dur/30.0 #milisegundos de duracion /15, a 30fps son como 2px por frame...
		#una linda forma de hacer una veloicdad constante (remember vel = dist/time solo puedes cambiar 1 por vez)
		d.mov_x = cos(ang)*dist
		d.mov_y = sin(ang)*-dist
		
	def OnDialogueStarts(self, d):
		#como el org modifica la transformacion del texto (posicion, scale, rotacion)
		#le ponemos como parámetro que no transforme, es una limitacion actual
		#porque como los degradados usan tambien el origen, solo podemos cambiar 
		#o el degradado o la transformacion. (aunque en realidad solo afecta cuando realizamos escalado y/o rotacion)
		a = d.actual
		#alpha del color secundario actual a 0
		a.color2.a = 0.0
		a.modo_relleno = d.P_AN_DEG_LIN
		a.modo_borde = d.P_AN_DEG_LIN
		d.Paint()
				
	def OnSyllable(self, diag):
		#Cuando la silaba esta active
		#(cacheamos diag.actual)
		a = diag.actual
		#Copiamos el color del borde al color primario
		a.color1.CopyFrom(a.color3)
		#Lo movemos hacia la posicion que calculamos en el EnSilabaInicia
		diag.MoveTo(diag.mov_x, diag.mov_y)
		#y hacemos que se escale de 1 a 0.5
		a.scale_x = a.scale_y = common.Interpolate(diag.progress, 1, 0.5)
		#Lo desvanecemos y lo pintamos
		diag.Fade(1, 0)
		diag.Paint()
		
	def OnSyllableSleep(self, d):
		#Las sílabas inactivas...
		d.PaintWithCache()

class tradu(common.Fx):
	def OnDialogue(self, d):
		d.PaintWithCache()

	def OnDialogueIn(self, d):
		#Calculamos el desplazamiento con la funcion seno, para q parezca tener aceleacion
		#desp = sin(pi*d.progreso)*15 #aumentará hasta 20 px, en una acelearcion como una curva. q va d 0 a 1  y de nuevo a 0 (porque el angulo del seno es de 0 a 180º
		#lo movemos en las Y (verticalmente)
		#d.actual.pos_y -= desp
		d.MoveTo(0, -15, common.i_full_sin)
		d.Fade(0, 1)
		d.Paint()
		
	def OnDialogueOut(self, d):
		#desp = sin(pi*d.progreso)*15
		#d.actual.pos_y += desp
		d.MoveTo(0, 15, common.i_full_sin)
		d.Fade(1,0)
		d.Paint()

class cred(common.Fx):
	def OnDialogue(self, d):
		#Usando alpha podemos elegir un valor de alpha manualmente,
		#Entonces puedo usar la funcion seno que me dara valores de 0 a 1 en una forma mas suave
		d.Fade(0, 1, common.i_full_sin)
		#Esto tambien es posible usando Fade y especificando otro interpolador (comun.i_sin) pero eso es mas avanzado :B
		d.Paint()
		
class FxsGroup(common.FxsGroup):
	def __init__(self):
		#Opciones principales
		#Un effect si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 500 #Milisegundos para la animacion de entrada
		self.out_ms = 500 #MS para animacion d salida
		self.syl_in_ms = 250 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 250 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = ( Romanji(), tradu(), cred())
		
	def OnFrameStarts(self): #Cuando el cuadro inicie
		advanced.StartGroup() #Empezamos un grupo de pintura
		 
	def OnFrameEnds(self):#Cuando termine el cuadro
		#cerramos el grupo y guardamos lo que se pinto en un patron
		pat = advanced.EndGroup()
		#Iniciamos otro grupo
		advanced.StartGroup()
		#Ponemos el color a blanco
		video.cf.ctx.set_source_rgba(1,1,1,1)
		#Pintamos la sombra de lo que había en el patron
		advanced.Shadow(pat, 3)
		advanced.fGlow(2, 0.02)#Hacemos un glow a todo lo que se dibujóo
		advanced.EndGroup()#Y cerramos el grupo

		#De esta manera la sombra no se superpone por cada silaba
