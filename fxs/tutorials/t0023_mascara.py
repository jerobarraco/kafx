# -*- coding: utf-8 -*-
from libs import common, video
from libs.draw import advanced, extra
#Hecho por AbelKM con sugerencias de Nande!
#http://my.opera.com/kafx/blog/2011/09/18/tutorial

textura = extra.LoadTexture('textures/metal_pattern.png')
class FX1(common.Fx):
	def EnDialogo(self, d):
		patron = advanced.cSprite(texture=textura )
		patron.x = d.actual.pos_x
		#Notar que el cSprite pinta la textura sobre el video independientemente de la posicion del texto

		#Creamos un grupo para el texto
		advanced.StartGroup()
		d.Pintar()
		#Y lo guardamos en una variable
		texto = advanced.EndGroup(0)

		#Creamos un grupo para la mascara
		advanced.StartGroup()
		patron.Pintar()
		#extra.DebugCairo()
		#Y la guardamos
		mascara = advanced.EndGroup(0)

		#Asignamos el texto
		video.cf.ctx.set_source(texto)
		#Y lo pintamos usando la máscara
		video.cf.ctx.mask(mascara)


class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (FX1(), FX1())