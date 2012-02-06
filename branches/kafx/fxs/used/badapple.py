# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced

#Para los cŕeditos
class ECredits(common.Fx):
	def OnDialogueIn(s,d):
		#Cuando entra, un fade-in hasta 50% de opacidad
		d.Fade(0, 0.5)
		#Lo movemos desde 10 pixels verticalmente
		d.MoveFrom(0, 10)
		d.Paint()

	def OnDialogue(s,d):
		#Cuando el dialogo debe mostrarse
		d.MoveTo(0, -10)
		d.Paint()

	def OnDialogueOut(s,d):
		#Cuando sale
		#Lo movemos desde -10 pixels verticales a -20 pixels verticales
		d.Move((0, -10), (0, -20))
		d.Fade(0.5, 0)
		d.Paint()

#Para el kanji
class EKanji(common.Fx):
	def OnDialogueIn(self, d):
		d.Fade(0, 0.5)
		d.MoveFrom(-50, 0)
		advanced.StartGroup()
		d.Paint()
		#Un blur direccional decreciente a medida que va avanzando
		advanced.fDirBlur(0, 10-int(10*d.progress), 0.3)
		advanced.EndGroup()

	def OnDialogueOut(self,d):
		d.Fade(1, 0)
		d.MoveTo(50, 0)
		d.Paint()

	def OnSyllableSleep(self,diag):
		#Mientras la silaba esta dormida
		#La pintamos usando caché
		diag.PaintWithCache()

	def OnSyllable(self,diag):
		#Fade-in desde 50% a 100%
		diag.Fade(0.5, 1)
		#Elegimos el modo de relleno Degradado Vertical
		diag.actual.mode_fill = diag.P_DEG_VERT
		diag.Paint()

	def OnSyllableDead(self, s):
		#Usamos el color secundario
		s.actual.color1.CopyFrom(s.actual.color2)
		s.Paint()

class ERoman(common.Fx):
	def OnDialogueStarts(self, d):
		d.original.modo_relleno =  d.P_DEG_VERT

	def OnDialogueIn(self, d):
		d.Fade(0, 1)
		d.MoveFrom(-50, 0)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(0, 10- int(10*d.progress), 0.3)
		advanced.EndGroup()

	def OnDialogue(s,d):
		d.PaintWithCache()

	def OnDialogueOut(self,d):
		d.Fade(1, 0)
		d.MoveTo(50, 0)
		d.Paint()

class ERo(common.Fx):
	def OnDialogueIn(self, d):
		d.Fade(0, 1)
		d.MoveFrom(-50, 0)
		advanced.StartGroup()
		d.Paint()
		advanced.fDirBlur(0, 10-int(10*d.progress), 0.3)
		advanced.EndGroup()

	def OnSyllableSleep(self,s):
		s.PaintWithCache()

	def OnSyllable(self,s):
		s.MoveTo(-60,0)
		s.Fade(1,-1)
		s.actual.mode_fill = s.P_DEG_VERT
		s.Paint()

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 250 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 200 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.fxs = (EKanji(), ERo(), ERoman(), ECredits())

	def OnFrameStarts(self):
		advanced.StartGroup()

	def OnFrameEnds(self):
		advanced.fGlow(3, 0.04)
		#advanced.PaintMode("exclusion")
		advanced.EndGroup()
