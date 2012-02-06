# -*- coding: utf-8 -*-

from libs import common
from random import random

class EventoExtra(common.Event):
	def EnSilaba(self, sil):
		#este seria el evento extra para cada silaba
		sil.Pintar()

	def TiempoSilaba(self, sil):
		#esto va a devolver los tiempos de inicio y fin para CADA silaba, para el evento EnSilaba de aca
		return (sil._start, sil._end+random()*500)


	def EnDialogo(self, diag):
		#este seria el evento extra para cada dialogo
		diag.Pintar()

	def TiempoDialogo(self, diag):
		#Esto define el tiempo de inicio y fin de cada dialogo para el evento EnDialogo
		return (diag._start, diag._end+(5*len(diag._silabas)))#nonsense, no le busquen la logica xD


	def EnLetra(self, letra):
		letra.Pintar()

	def TiempoLetra(self, letra):
		return (letra._start+5, letra._end+5)
#ninguna de estas seis funciones es imprescindible,
#pero si pones EnDialogo seria logico poner TiempoDialogo (lo mismo con la silaba y la letra)

class UnEfecto(common.Fx):
	def __init__(self):
		#con esto le decimos que vamos a usar un evento extra inventado por nosotros mas arriba,
		self.events = [EventoExtra()]
		#podemos usar mas events asi,
		#self.events = [EventoExtra(), OtroEventoExtra()] etc
		#obviamente tenemos que definir la clase OtroEventoExtra asi como hicimos con la otra

	#Aun despues de definir un evento extra, podemos seguir usando los events normales del kafx como siempre :D
	#obviamente no es necesario usarlos si no los querÃ©s
	def EnSilaba(self, sil):
		#evento normal de silaba
		sil.Pintar()
	def EnDialogo(self, diag):
		#el que ya conoces
		diag.Pintar()
	def EnDialogoEntra(self, diag):
		diag.Pintar()

class OtroEfecto(common.Fx):
	def __init__(self):
		self.events = [EventoExtra()] # al crear otra instancia podes compartir el mismo evento en varios efectos

class FxsGroup(common.FxsGroup):
	def __init__(self):
		#le decimos que queremos 300 milisegundos de animacion
		#de entrada y de salida respectivamente
		self.in_ms = 300
		self.out_ms = 300
		self.dividir_letras = True
		#le decimos al kafx que efectos usaremos
		self.fxs = (UnEfecto(), OtroEfecto())
