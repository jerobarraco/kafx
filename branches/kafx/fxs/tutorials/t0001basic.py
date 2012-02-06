# -*- coding: utf-8 -*-
"""
Como pintar un dialogo y efectos basicos
Ver tutorials para explicacion
Read the tutorials for explanation
svn/docs/Kafx/Avisynth_Cairo
"""
from libs import common
class Effect():
	def OnDialogue(self, diag):
		diag.Paint()
class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Effect(),Effect())

