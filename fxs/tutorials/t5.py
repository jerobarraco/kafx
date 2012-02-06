from libs import common
import random

class FX1(common.Fx):
    def EnDialogoInicia(self, d):
        d.x_inicial = random.random() * 20

    def EnDialogo(self, d):
        d.MoveFrom( d.x_inicial , 0)
        d.Pintar()

    def EnSilaba(self, s):
        s.actual.color1.CopiarDe(s.actual.color2)
        s.Pintar()

class FxsGroup(common.FxsGroup):
    def __init__(self):
        self.fxs = [ FX1()]
        self.syl_in_ms =300
        self.syl_out_ms = 250

