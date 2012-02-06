# -*- coding: utf-8 -*-

from libs import common
from libs.draw import advanced, extra
import math

class FX1(common.Fx):
    def EnDialogo(self, s):
        s.MoveTexture( 120*s.progreso, 120*s.progreso, parte = s.PART_BORDE)
        s.Pintar()

    def EnDialogoSale(self, s):
        s.Fade(1, 0)
        s.Pintar()

    def EnDialogoInicia(self, s):
        #Cargamos las textures al INICIAR el dialogo, y le especificamos en que parte se usaran
        s.LoadTexture('textures/scan.png', s.PART_BORDE)
        s.LoadTexture('textures/cloud2.png', s.PART_RELLENO)

    def EnSilaba(self, s):
        s.actual.modo_relleno = s.P_DEG_VERT
        s.Fade(1, 0.5)
        s.Rotate(0, -math.pi)
        s.Scale(1, 2)
        s.Pintar()

        s.Restore()
        s.actual.modo_relleno = s.P_AN_DEG_RAD
        s.Alpha(0.50000000000)
        s.Move((30, 30), (123, 60))
        s.Pintar()


class FxsGroup(common.FxsGroup):
    def __init__(self):
        self.fxs = [ FX1() ]
        self.syl_in_ms = 300
        self.syl_out_ms = 250
        self.out_ms = 300

        self.reset_style = True

    def EnCuadroInicia(self):
        advanced.StartGroup()

    def EnCuadroFin(self):
        advanced.fGlow()
        advanced.EndGroup()