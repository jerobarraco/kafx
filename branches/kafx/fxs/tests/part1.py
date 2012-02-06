# -*- coding: utf-8 -*-
from libs import common, physics
from libs.draw import extra, advanced
from random import randint
t = extra.LoadTexture("textures/T_NEGRO2.png")

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.syl_out_ms = 1200
		self.p = advanced.cSprite(t, 100, 100, scale=0.5)
		self.fxs = (common.Fx(),)
	def EnCuadroInicia(self):
		self.p.Paint()
