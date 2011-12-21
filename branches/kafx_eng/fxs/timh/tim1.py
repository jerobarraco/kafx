# -*- coding: utf-8 -*-
from libs import comun
from libs.draw import avanzado

from math import sin, pi
import random

class fx1(comun.Fx):
    def EnDialogo(self,d):
        d.CargarTextura('texturas/fuego/f0000.png',1)
        d.Pintar()

    def EnSilaba(self,s):
        avanzado.GrupoInicio()
        s.Pintar()
        avanzado.fGlow(1, 0.1+(sin(pi*s.progreso)/6.0))
        avanzado.GrupoFin()

class FxsGroup(comun.FxsGroup):
	fxs = [fx1(),]