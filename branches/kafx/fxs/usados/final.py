# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado, extra
import random
from math import pi, sin

class FX1(comun.Fx):
	def __init__(self):
		#Cuando inicia el effect (cuando se crea)
		#Creamos el sistema de partículas
		self.parts = avanzado.cParticleSystem(png="texturas/star3.png",
			max_life=3, max_parts=300, emit_parts=4, scale_from=0.2, scale_to=1,
			color=extra.cCairoColor(0xFF7F7920),  modo=1)

	def EnSilabaInicia(self, d):
		#Cuando inicia la silaba la configuramos con relleno degradado
		d.original.modo_relleno = d.P_DEG_VERT
		
	def EnDialogoEntra(self, d):
		#Fade-In cuando el dialogo entra
		d.Desvanecer(0, 1)
		d.Pintar()

	def EnDialogoSale(self, d):
		#Fade-out Cuando sale
		d.Desvanecer(1, 0)
		d.Pintar()
		
	def EnDialogo(self, d):
		#Cuando el dialogo está activo
		#Pintamos con cache el dialogo
		d.PintarConCache()

	def EnDialogoInicia(self, d):
		#Cuando el dialogo inicia
		#Elegimos el modo de relleno degradado vertical
		d.original.modo_relleno = d.P_DEG_VERT
		#cacheamos la funcion interpolar porque me da paja
		i = comun.Interpolar
		#creamos la variable px asignada a None para saber cuando estamos en la primer silaba
		px = None
		#si el dialogo no contiene silabas salimos
		if not d._silabas: return

		#ahora recorremos las silabas en reversa, desde la última hasta la primera
		#y creamos cuatro puntos por cada silaba
		#puntos: p:inicial, s:segundo, l:last, f:final
		for sil in reversed(d._silabas):#las recorremos en sentido inverso (mantengan esto en mente)
			#cacheamos el estilo original
			o = sil.original
			#puntos del centro

			if px == None:#ultimo punto (el primero de la lista)
				#le inventamos puntos finales
				#el punto de inicio será el centro de la silaba
				px, py = o.pos_x+o.org_x, o.pos_y-o.org_y

				#el segundo punto (primer punto de control) un random en 40
				sx = px +i(random.random(), -40, 40)
				sy = py +i(random.random(), -40, 40)

				#el tercer punto (segundo punto de control) un random de 40
				lx = px +i(random.random(), -40, 40)
				ly = py +i(random.random(), -40, 40)

				#El ultimo punto, un random modificado para que tenga mas posibilidades de irse a la izq
				fx = px +i(random.random(), 30, 50)
				fy = py +i(random.random(), -30, 30)
			else:				
				"""
				Lo siguiente es equivalente a rotar el punto (lx, ly) en 180º con centro en (fx, fy)
				tambien conocido como multiplicar por la matriz
				|-1   0|
				|0   -1|

				Este codigo lo pense un tiempo, termino siendo muy sencillo pero no es facil de ver.
				basicamente es buscar el punto de control opuesto al punto de control anterior al punto de fin
				teniendo como eje el punto de fin.
				para eso lo que hago es tomar la distancia entre el punto de control y el punto final (con referencia en el punto final)
				(l-f) multiplicarlo por -1 para invertirlo, y sumarselo a f para calcular el proximo punto de control.

				al tener puntos de control opuestos (los 3 puntos sobre la misma linea) (control anterior, final y control siguiente)
				lo que hace es que la curva del bezier sea mas suave y parezca que sigue un bezier de muchos puntos de control
				y no solo varios bezier concatenados (sino verian que la curva hace como picos)

				Por eso cambie el nombre de CalcProgreso a Interpolar, porque el calculo es una interpolación lineal entre dos puntos.
				(interesante seria tener otras interpolaciones (sinusoidal y weas))
				"""
				lx = comun.Interpolar(-1, px, sx)
				ly = comun.Interpolar(-1, py, sy)
				#como ven, mas facil de hacer que explicar

				#para el punto final tomamos el punto origen del punto siguiente (el anterior en la lista)
				fx = px
				fy = py

				#y para el punto inicial usamos el centro de la silaba
				px = o.pos_x+o.org_x
				py = o.pos_y-o.org_y

				sx = px +i(random.random(), -40, 40)
				sy = py +i(random.random(), -40, 40)
			#Ahora agregamos el punto a la silaba (noten como uso sil. para asignar ps, eso es cada silaba)
			"""
			#esta es la forma que usa la funcion comun.Bezier
			sil.ps = [
					(px, py),
					(sx, sy),
					(lx, ly),
					(fx, fy)
				]"""
			#Esta es la forma más comoda para la funcion comun.PuntoBezier
			sil.ps = (px,py,sx,sy,lx,ly,fx,fy)

	def EnSilaba(self, d):
		#cacheamos el ps en p, por paja.
		p = d.ps
		#calculamos la pos (x,y) sobre la curva (definida por p) dependiendo del progreso
		#Una forma de llamarla
		x, y = comun.PuntoBezier(d.progreso, *p)
		#Sino podriamos haber puesto
		#x, y = comun.PuntoBezier(d.progreso, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])
		#pero mejor dejar que python haga lo que sabe

		#así lo usariamos con la otra funcion

		#x,y = comun.Bezier(d.progreso, p)

		#Ponemos la posicion del emitter
		self.parts.DarPosicion(x, y)
		#Emitimos en el punto
		self.parts.Emitir()
		#Ahora, si la duracion de la silaba es menor a 3 frames (lo cual pasa por la forma que canta utada)
		if 0<d._dur<3:
			#Cuando el progreso sea menor a 0.3 (1/3 frames)
			if d.progreso>0.3:
				#Damos la posicion de un punto con un progreso un poco menor
				self.parts.DarPosicion(*comun.PuntoBezier(d.progreso-0.3,*p))
				#Y emitimos
				self.parts.Emitir()
				#Y otra vez
				self.parts.DarPosicion(*comun.PuntoBezier(d.progreso-0.15,*p))
				self.parts.Emitir()
				#Y otra
				self.parts.DarPosicion(*comun.PuntoBezier(d.progreso-0.10,*p))
				self.parts.Emitir()
				#De esta forma intentamos evitar lo que pasa cuando el punto se mueve muy rapido y deja las particulas muy separadas

		#Pintamos el dialogo con un blur direccional que se agranda y achica y que brilla porque usamos add
		avanzado.StartGroup()

		d.Pintar()
		#Configuramos el modo de pintado a aditivo
		avanzado.ModoPintado('add')
		#blur direccional con velocidad sinusoidal y opacidad máxima 0.2
		avanzado.fBiDirBlur(pi, 5, 0.2*sin(pi*d.progreso))
		#y lo restauramos al normal
		avanzado.ModoPintado('over')

		avanzado.EndGroup()
		

class Tradu(comun.Fx):
	#Notar que los moverDe MoverA y Mover estan sincronizados para que se mueva constantemente
	#Pero con mayor velocidad cuando entra y sale
	def EnDialogoInicia(self,d):
		d.original.modo_relleno = d.P_DEG_VERT
		
	def EnDialogoEntra(self, d):
		d.Desvanecer(0, 1)
		d.MoverDe(10, 0)
		d.Pintar()

	def EnDialogo(self, d):
		d.MoverA(-10, 0)
		d.Pintar()

	def EnDialogoSale(self, d):
		#Hacemos que el dialogo salga desvaneciendoce, con un movimiento hacia la izquierda, desde -10 hasta -20
		y = d.original.pos_y
		x = d.original.pos_x
		d.Mover((x-10, y), (x-20, y))
		d.Desvanecer(1, 0)
		d.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Desactivamos el saltar_cuadros por las partículas
		self.saltar_cuadros=False
		self.in_ms = 200 #Milisegundos para la animacion de entrada
		self.out_ms = 200 #MS para animacion d salida
		self.fxs = (FX1(), Tradu())

	def EnCuadroInicia(self):
		avanzado.StartGroup()
		
	def EnCuadroFin(self):
		#Al finalizar el cuadro
		#Pintamos las particulas que pertenecen al effect 0
		self.fxs[0].parts.Pintar()
		#Le hacemos glow a todo (menos el video)
		avanzado.fGlow()
		avanzado.EndGroup()
		#Y listo
		
		
