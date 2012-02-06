# -*- coding: utf-8 -*-
from libs import common
from libs.draw import extra

#Lo primero y mas importante es conseguirse una animacion
#Puede ser un gif animado, un avi, whatever, pero hay que convertirlo
#y pasarlo a una secuencia de pngs (o sea, varios archivos .png cada uno para cada cuadro de la animacion)
#La forma de cargarlo es muy sencilla, pero la funcion del kafx necesita que los .png tengan un nombre que
#termine en numeros ordenados.

#la numeracion comienza desde 0

#pongo las textures acá afuera con el solo fin de mostrarles que pueden usarlas
#en cualquier parte del script, pero si lo van a usar en un solo effect,
#entonces mejor declarenlo en el __init__ del effect, como en neko.py

framecount = 42
texturas = extra.LoadSequence('textures/fuego/f', framecount, 4)
#los parametros son
#la parte del archivo antes de los digitos
#la cantidad de imagenes
#la cantidad de digitos
#el extend
#el extend default es EXTEND_REPEAT eso hace que la textura se repita, si lo quieren cambiar fijense las otras variables del tipo EXTEND en la libreria cairo

#si esta imagen tuviese transparecia, se vería mejor.

class UnEfecto(common.Fx):
	def __init__(self):
		self.frame = 0 #aca vamos a contar el frame actual

	def EnSilabaInicia(self, sil):
		#cuando inicie la silaba le decimos que vamos a pintar el relleno con una textura
		sil.original.modo_relleno = sil.P_TEXTURA
		#ojo que si despues no ponemos una textura, vamos a tener problemas

	def EnSilaba(self, sil):
		#evento normal de silaba
		#ponemos esto para poder acceder a las variables de afuera de esta funcion
		global texturas, framecount

		#elegimos la textura
		sil.texturas[sil.PART_RELLENO] = texturas[self.frame]
		sil.Pintar()
		#icrementamos el cuadro
		self.frame = (self.frame +1) % framecount
		#el %fcount es el resto de la division, lo que hace es que el numero vaya de 0 a 42 y de nuevo a 0

	def EnDialogo(self, diag):
		#el que ya conoces
		diag.Pintar()
	def EnDialogoEntra(self, diag):
		diag.Pintar()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		#le decimos que queremos 300 milisegundos de animacion
		#de entrada y de salida respectivamente
		self.in_ms = 300
		self.out_ms = 300
		#le decimos al kafx que efectos usaremos
		self.fxs = (UnEfecto(), UnEfecto())