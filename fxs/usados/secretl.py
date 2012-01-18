# -*- coding: utf-8 -*-
import random
from math import pi, cos, sin, ceil

from libs.draw import avanzado, extra
from libs import comun, video

class FX1(comun.Fx):
		def __init__(self):
			#Cuando inicia el effect
			#creamos un array para poner las particulas que iremos animando,
			#esto es proque hay que hacer diferencia entre las particulas que se mueven y las que no
			#y porque el movimiento de las particulas puede durar mas que el dialog en pantalla
			self.parts = []
			#y cargamos una textura comun para intentar reducir memoria
			self.t = extra.LoadTexture('textures/star3.png') #Notar la / , no es lo mismo que \

		def EnSilabaInicia(self, s):
			#Cuando cada silaba inicie
			#configuramos el borde en degradado
			s.actual.modo_borde = s.P_DEG_VERT
			#si dura 0 o menos (?) nos salimos
			if (s._dur <= 0 ) or (s._texto.strip() == ""):
				s.parts = []
				s.partsporframe = 0
				return
			#usamos una variable con scale porque luego lo usamos en varios lados

			escala = 0.08
			#Creamos las particulas con una funcion especial.
			#scale sera la scale inicial
			#0.2 es la opacidad mínima, el resto de particulas no seran mostradas.
			s.parts = s.CreateParticles(self.t,	escala, 0.2, False, modo=0)
			#Recorremos las particulas creadas y las configuramos
			for p in s.parts:
				#Le damos un angulo de rotacion
				angulo = comun.Interpolar(random.random(), pi*0.25, pi*1.15)
				#Le damos un movimiento por el angulo ese
				#en y
				p.ya = -sin(angulo)*random.random()
				#y en x
				p.xa = cos(angulo)*random.random()
				#y un cambio de opacidad
				p.aa = comun.Interpolar(random.random(), 0.01, 0.05)
				#almacenamos la opacidad original
				p.oa = p.color.a
				#y una scale inicial
				p.s = escala
			#Y las mezclamos para que exploten desordenadamente
			random.shuffle(s.parts)
			#Y creamos una variable que dice cuantas particulas animaremos por frame
			#para asegurarnos que cuando termine la silaba estén todas animadas

			s.partsporframe = int( ceil( len(s.parts) / float( video.MSACuadro(s._dur) ) ) )
			"""
			#Para que  se entienda lo pongo en varias lineas
			#la duracion está en milisegundos, asi que los pasamos a cuadros para saber cuantos cuadros dura
			cuadros = video.MSACuadro(s._dur)

			#lo convertimos a float para que al dividir por esto de un número flotante
			cuadros = float(cuadros)

			#cuantas particulas tiene esta silaba
			particulas = len(s.parts)

			#con esto sabemos cuantas particulas tenemos que animar por cuadro para que
			#al terminar la silaba esten todas animadas
			partsporframe = particulas/cuadros

			#lo redondeamos al numero mayor entero mas cercano
			partsporframe = ceil(partsporframe)
			# y lo convertimos a entero
			partsporframe = int(partsporframe)
			"""

		def EnDialogoEntra(self, s):
			#Cuando el dialogo estan entrado
			prog = s.progreso
			#recorremos todas las silabas
			for sil in s._silabas:
				#y todas sus particulas
				#si tiene particulas
				#if hasattr(sil, 'parts'):
				for p in sil.parts:
					#y hacemos un fade in
					p.color.a = p.oa * prog #hasta el alpha original
					p.Pintar()

		def EnSilabaDorm(self, s):
			#Mientras la silaba espera, pintamos todas sus particulas
			for p in s.parts:
				p.Pintar()

		def EnSilaba(self, s):
			##abusamos de la referencia para que estén en los 2 arrays (como va a comer memoria esto)
			#las pasamos al self para q las pinte el fxsgroup

			for p in s.parts[:s.partsporframe]:#Ponemos particulas a animar
				#movemos una particula de la silaba al self (effect)
				self.parts.append(p)
				s.parts.remove(p)

			for p in s.parts:
				#Pintamos las estáticas
				p.Pintar()

class FX2(comun.Fx):
	def EnDialogoInicia(self, d):
		#cargamos una textura y le decimos que la usaremos con el relleno
		#parte = 0:borde, 1:relleno, 2:sombra
		d.LoadTexture('textures/cloud2.png', parte=d.PART_RELLENO)
		#Por cada dialogo elegimos un offset inicial para la textura (lo que hara parecer diferentes textures)
		d.start_x = random.random()*800
		d.start_y = random.random()*600

		#Un movimiento constante en alguna direccion
		#La direccion es random (un angulo)
		a = random.random()*pi*2
		#Y la cantidad d pixels es siempre constante (2px) lo q da una velocidad por frame constante
		d.dx = cos (a)*2
		d.dy = sin (a)*2
		#una opacidad inicial de 0
		d.op = 0

	def HacerCosas(self, d):
		"""Como los 3 On (EnDialogoEntra, EnDialogoSale y EnDialogo) hacen lo mismo  EXCEPTO que cambia la opacidad (que la almaceno en d.op
		metemos este codigo algo complejo en este def para no triplicar codigo """
		#"movemos" la textura, sumandole a cada offset un movimiento
		d.start_x += d.dx
		d.start_y += d.dy
		#Le asignamos una matriz a la textura (con los movimientos)
		d.MoveTexture(pos_x = d.start_x, pos_y = d.start_y, parte = d.PART_RELLENO)

		#Para poder dar una opacidad homogénea a un grupo de cosas usaremos el StartGroup
		avanzado.StartGroup()
		#Pintamos el texto
		d.Pintar()
		#Aca podriamos pintar muchas cosas, deformarlas y demás,
		#lo que simplifica mucho y haria posible dar opacidad de manera igual a cosas que quizas quedarian feas de otra forma
		#Por ejemplo, cuando se le da opacidad por separado a la sombra y al texto en ASS la sombra se ve a travez del texto,
		#o el borde encima del relleno.. usando esto, podriamos hacer que todo se transparente conjuntamente
		#y no se vea la sombra detras del texto
		#El truco esta en esto:
		#Cerramos el grupo y le decimos que lo pinte con la opacidad que le ponemos
		#de esta manera todo se ve bien, la sombra el relleno y el borde y con la opacidad que le corresponde
		#notar que de esta forma, al pintarse primero solido y luego aplicar opacidad, la sombra nunca se vera
		#a traves del borde
		avanzado.EndGroup(d.op)
		#Segun el ultimo cambio tambien podriamos haber puesto
		"""
		d.Alpha(d.op)
		d.Pintar()
		"""
		#eso es casi lo mismo, solo que cada parte si pintara por separado con esa opacidad.

	def EnDialogo(self, d):
		d.op=1.0
		self.HacerCosas(d)

	def EnDialogoEntra(self, d):
		d.op = comun.Interpolar(d.progreso, 0, 1)
		self.HacerCosas(d)

	def EnDialogoSale(self, d):
		d.op = comun.Interpolar(d.progreso, 1, 0)
		self.HacerCosas(d)


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Por las particulas ponemos esto a false, sino el kafx se saltará los cuadros
		#en que no hay ningun dialogo
		self.saltar_cuadros=False
		self.in_ms = 300 #Milisegundos para la animacion de entrada
		self.out_ms = 300 #MS para animacion d salida
		self.fxs = (FX1(), FX2())

	def EnCuadroInicia(self):
		avanzado.StartGroup()

	def EnCuadroFin(self):
		#ahora animamos las particulas que hay que animar
		for p in self.fxs[0].parts:
			#decrementamos su alpha
			p.color.a -= p.aa
			#incrementamos su scale
			p.s += 0.01
			#es mastriz inversa hay que dividir 1 por la scale
			p.scale_x = p.scale_y = 1.0/p.s

			#incrementamos las posiciones (movemos)
			p.y += p.ya
			p.x += p.xa
			#incrementamos el angulo (rotamos)
			p.angulo += p.aa
			#y FINALMENTE lo pintamos
			p.Pintar()
			#notar q las variables s, ya, xa e aa las inventé yo en el codigo de arriba

			#y si la partícula se ha vuelto demasiado transparente la eliminamos (esto ayuda mucho a la velocidad y memoria)
			if p.color.a <=0.0: self.fxs[0].parts.remove(p)
		#glow y chau
		avanzado.fGlow()
		avanzado.EndGroup()
