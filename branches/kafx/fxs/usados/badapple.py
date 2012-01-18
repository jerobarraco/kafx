# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado

#Para los cŕeditos
class ECredits(comun.Fx):
	def EnDialogoEntra(s,d):
		#Cuando entra, un fade-in hasta 50% de opacidad
		d.Fade(0, 0.5)
		#Lo movemos desde 10 pixels verticalmente
		d.MoveFrom(0, 10)
		d.Pintar()

	def EnDialogo(s,d):
		#Cuando el dialogo debe mostrarse
		d.MoveTo(0, -10)
		d.Pintar()

	def EnDialogoSale(s,d):
		#Cuando sale
		#Lo movemos desde -10 pixels verticales a -20 pixels verticales
		d.Move((0, -10), (0, -20))
		d.Fade(0.5,0)
		d.Pintar()

#Para el kanji
class EKanji(comun.Fx):
	def EnDialogoEntra(self, d):
		d.Fade(0, 0.5)
		d.MoveFrom(-50, 0)
		avanzado.StartGroup()
		d.Pintar()
		#Un blur direccional decreciente a medida que va avanzando
		avanzado.fDirBlur(0, 10-int(10*d.progreso), 0.3)
		avanzado.EndGroup()

	def EnDialogoSale(self,d):
		d.Fade(1, 0)
		d.MoveTo(50, 0)
		d.Pintar()

	def EnSilabaDorm(self,diag):
		#Mientras la silaba esta dormida
		#La pintamos usando caché
		diag.PintarConCache()

	def EnSilaba(self,diag):
		#Fade-in desde 50% a 100%
		diag.Fade(0.5, 1)
		#Elegimos el modo de relleno Degradado Vertical
		diag.actual.modo_relleno = diag.P_DEG_VERT
		diag.Pintar()

	def EnSilabaMuerta(self, s):
		#Usamos el color secundario
		s.actual.color1.CopiarDe(s.actual.color2)
		s.Pintar()

class ERoman(comun.Fx):
	def EnDialogoInicia(self, d):
		d.original.modo_relleno =  d.P_DEG_VERT

	def EnDialogoEntra(self, d):
		d.Fade(0, 1)
		d.MoveFrom(-50, 0)
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fDirBlur(0, 10- int(10*d.progreso), 0.3)
		avanzado.EndGroup()

	def EnDialogo(s,d):
		d.PintarConCache()

	def EnDialogoSale(self,d):
		d.Fade(1, 0)
		d.MoveTo(50, 0)
		d.Pintar()

class ERo(comun.Fx):
	def EnDialogoEntra(self, d):
		d.Fade(0, 1)
		d.MoveFrom(-50, 0)
		avanzado.StartGroup()
		d.Pintar()
		avanzado.fDirBlur(0, 10-int(10*d.progreso), 0.3)
		avanzado.EndGroup()

	def EnSilabaDorm(self,s):
		s.PintarConCache()

	def EnSilaba(self,s):
		s.MoveTo(-60,0)
		s.Fade(1,-1)
		s.actual.modo_relleno = s.P_DEG_VERT
		s.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 250 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 200 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (EKanji(), ERo(), ERoman(), ECredits())

	def EnCuadroInicia(self):
		avanzado.StartGroup()

	def EnCuadroFin(self):
		avanzado.fGlow(3, 0.04)
		avanzado.EndGroup()
