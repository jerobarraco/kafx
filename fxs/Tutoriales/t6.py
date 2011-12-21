# -*- coding: utf-8 -*-

from libs import comun
from libs.draw import avanzado, extra
import math

class FX1(comun.Fx):
    def EnDialogo(self, s):
        s.MoverTextura( 120*s.progreso, 120*s.progreso, parte = s.PART_BORDE)
        s.Pintar()

    def EnDialogoSale(self, s):
        s.Desvanecer(1, 0)
        s.Pintar()

    def EnDialogoInicia(self, s):
        #Cargamos las texturas al INICIAR el dialogo, y le especificamos en que parte se usaran
        s.CargarTextura('texturas/scan.png', s.PART_BORDE)
        s.CargarTextura('texturas/cloud2.png', s.PART_RELLENO)

    def EnSilaba(self, s):
        s.actual.modo_relleno = s.P_DEG_VERT
        s.Desvanecer(1, 0.5)
        s.Girar(0, -math.pi)
        s.Escalar(1, 2)
        s.Pintar()

        s.Restore()
        s.actual.modo_relleno = s.P_AN_DEG_RAD
        s.Alpha(0.50000000000)
        s.Mover((30, 30), (123, 60))
        s.Pintar()


class FxsGroup(comun.FxsGroup):
    def __init__(self):
        self.fxs = [ FX1() ]
        self.sil_in_ms = 300
        self.sil_out_ms = 250
        self.out_ms = 300

        self.reset_estilo = True

    def EnCuadroInicia(self):
        avanzado.GrupoInicio()

    def EnCuadroFin(self):
        avanzado.fGlow()
        avanzado.GrupoFin()