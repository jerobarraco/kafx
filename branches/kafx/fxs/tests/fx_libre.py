from libs import common
import kafx_main

class Fxloco(common.Fx):
	def EnDialogoInicia(self, diag):
		tempo =0
		for sil in diag._silabas:
			sil._end += 200 + tempo
			tempo += (800/len(diag._silabas))

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = [Fxloco()]
			
			