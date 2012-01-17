# -*- coding: utf8 -*-
from libs import comun
from libs.draw import avanzado
from math import pi, sin

class Fx1(comun.Fx):
	def __init__(self):
		self.parts = avanzado.cParticleSystem( png="texturas/spark3.png", max_life=3,
			emitir_parts=2, escala_de= 0.8, escala_a=0.3, modo=1,
			animador = self.mianimador
		)
		self.parts.DarVentana(6, 2)
		self.parts.DarAngulo(pi, 3, pi/4.0)
		
	def mianimador (self, part):
		part.life += part.fade
		part.activa = part.life <1

		"""#Que equivale a :
		if part.life >1:
			part.activa = False
		else:
			part.activa = True
		"""

		part.x += sin(part.angulo)*20
		part.y -= 2.0
		part.angulo += 1.0
		
		
		#part.escala = comun.Interpolar(part.life, 0.8, 0.3, comun.i_rand)
		part.escala += part.sci
		part.color.a = comun.Interpolar(part.life , 1, 0)

		"""
		#propiedades animables
		part.angulo
		part.y
		part.x
		part.escala
		part.color
		part.activa
		"""

		"""
		#Otras propiedades
		part.life
		part.fade
		#esto indica la velocidad con que muere, al tener /life ahi, el valor de esa variable, puede ser sumada a life y life pasa a funcionar como el progreso de los dialogos..
		#aumentando el valor de life aumenta la cantidad d animaciones requeridas para morir.
		#considerable como "paso" de animacion (step)


		#incremento de las posiciones (aka velocidad+direccion)
		part.xi
		part.yi

		#incremento del angulo aka animacion de la rotacon
		part.anguloi

		#incremento de la escala.
		part.sci

		#gravedad
		part.xg
		part.yg
		"""

	def EnSilaba(self, diag):
		#Cuando toca la silaba
		#si la silaba no tiene letras (un espacio o vacia) salimos
		if diag._texto.strip() =="":
			return

		#cambiamos la posicion del emisor de particulas
		self.parts.DarPosicion(
			diag.actual.pos_x + diag.progreso*diag.original._ancho,
			diag.actual.pos_y - (diag.actual.org_y)
		)
		self.parts.Emitir()
		diag.actual.color4.r=diag.actual.color4.g=diag.actual.color4.b=0.8
		diag.Desvanecer(1, 0)
		diag.Pintar()

	def EnSilabaDorm(self, diag):
		diag.PintarConCache()

		
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (Fx1(),)
		self.saltar_cuadros = False
		
	def EnCuadroFin(self):
		self.fxs[0].parts.Pintar()



"""bgm
Heian Inferno		ELEMENTAS  Sphere Caliber
7701  Betwixt & Between  the BEST of HARDCORE TANO*C
Sunset Emotion	DJ Noriken	Virtual Oblivion
Surreal			DJ Noriken		Glitters
Nocturne		DJ Noriken		omnifarious
情熱のウォブル	DJ Shimamura	SUPER SHOT 2 -美少女ゲームリミックスコレクション-
カラフル (ロックバージョン)	Duca	乙女恋心プリスター ヴォーカルコレクション
"""
