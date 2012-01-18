# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado, extra
#Hecho por AbelKM con sugerencias de Nande!
#http://my.opera.com/kafx/blog/2011/09/18/tutorial

textura = extra.LoadTexture('textures/metal_pattern.png')
class FX1(comun.Fx):
	def EnDialogo(self, d):
		patron = avanzado.cSprite(texture=textura )
		patron.x = d.actual.pos_x
		#Notar que el cSprite pinta la textura sobre el video independientemente de la posicion del texto

		#Creamos un grupo para el texto
		avanzado.StartGroup()
		d.Pintar()
		#Y lo guardamos en una variable
		texto = avanzado.EndGroup(0)

		#Creamos un grupo para la mascara
		avanzado.StartGroup()
		patron.Pintar()
		#extra.DebugCairo()
		#Y la guardamos
		mascara = avanzado.EndGroup(0)

		#Asignamos el texto
		video.cf.ctx.set_source(texto)
		#Y lo pintamos usando la máscara
		video.cf.ctx.mask(mascara)


class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(), FX1())