# -*- coding: utf-8 -*-
from libs import common
from libs.draw import advanced

from math import sin, pi
import random

class fx1(common.Fx):
    def EnDialogo(self,d):
        d.LoadTexture('textures/fuego/f0000.png',1)
        d.Pintar()

    def EnSilaba(self,s):
        advanced.StartGroup()
        s.Pintar()
        advanced.fGlow(1, 0.1+(sin(pi*s.progreso)/6.0))
        advanced.EndGroup()

class FxsGroup(common.FxsGroup):
	fxs = [fx1(),]