# -*- coding: utf-8 -*-
"""
How to paint an dialogue with the most basic effect.
See tutoriales for further explication.
Read the tutorials for explanation at:
svn/docs/Kafx/Avisynth_Cairo
"""
from libs import common
class Effect():
	def OnDialogue(self, diag):
		diag.Paint()
class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.fxs = (Effect(),Effect())

