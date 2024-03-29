# -*- coding: utf8 -*-
from libs import common
from libs.draw import advanced
from math import pi, sin

class Fx1(common.Fx):
	def __init__(self):
		self.parts = advanced.cParticleSystem( png="textures/spark3.png", max_life=3,
			emit_parts=2, scale_from= 0.8, scale_to=0.3, modo=1,
			animator= self.mianimador
		)
		self.parts.DarVentana(6, 2)
		self.parts.DarAngulo(pi, 3, pi/4.0)
		
	def mianimador (self, part):
		part.life += part.fade
		part.activa = part.life <1

		"""#Que equivale a :
		if part.life >1:
			part.active = False
		else:
			part.active = True
		"""

		part.x += sin(part.angulo)*20
		part.y -= 2.0
		part.angulo += 1.0
		
		
		#part.scale = comun.Interpolar(part.life, 0.8, 0.3, comun.i_rand)
		part.escala += part.sci
		part.color.a = common.Interpolar(part.life , 1, 0)

		"""
		#propiedades animables
		part.angulo
		part.y
		part.x
		part.scale
		part.color
		part.active
		"""

		"""
		#Otras propiedades
		part.life
		part.fade
		#esto indica la velocidad con que muere, al tener /life ahi, el valor de esa variable, puede ser sumada a life y life pasa a funcionar como el progreso de los dialogues..
		#aumentando el valor de life aumenta la cantidad d animaciones requeridas para morir.
		#considerable como "paso" de animacion (step)


		#incremento de las posiciones (aka velocidad+direccion)
		part.xi
		part.yi

		#incremento del angulo aka animacion de la rotacon
		part.anguloi

		#incremento de la scale.
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

		#cambiamos la posicion del emitter de particulas
		self.parts.DarPosicion(
			diag.actual.pos_x + diag.progreso*diag.original._ancho,
			diag.actual.pos_y - (diag.actual.org_y)
		)
		self.parts.Emitir()
		diag.actual.color4.r=diag.actual.color4.g=diag.actual.color4.b=0.8
		diag.Fade(1, 0)
		diag.Pintar()

	def EnSilabaDorm(self, diag):
		diag.PintarConCache()

		
class FxsGroup(common.FxsGroup):
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
