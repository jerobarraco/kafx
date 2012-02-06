# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced, extra
import math, random, cairo
from math import pi, sin, cos
from random import randint

class FX1(common.Fx):
	def EnDialogo(self,d):
		print(d.progress)
		d.Paint()

class FxsGroup(common.FxsGroup):

	def __init__(self):
		self.in_ms = 200
		self.out_ms = 250
		self.fxs = (FX1(), common.Fx())