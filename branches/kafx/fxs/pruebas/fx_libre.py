from libs import comun
import kafx_main

class Fxloco(comun.Fx):
	def EnDialogoInicia(self, diag):
		tempo =0
		for sil in diag._silabas:
			sil._end += 200 + tempo
			tempo += (800/len(diag._silabas))

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.fxs = [Fxloco()]
			
			