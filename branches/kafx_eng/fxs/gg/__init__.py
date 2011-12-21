from libs import comun
import math

class FX1(comun.Fx):
    def Chain2(self, l, p):
        l.progreso = p
        l.MoverDe(0, -30)
        l.Desvanecer(0, 1)
        l.actual.scale_x = -math.cos(math.pi*p)
        l.Pintar()

    def Chain1(self, sil, p):
        sil.progreso = p
        #sil.Encadenar(self.Chain2)
        sil.progreso = p
        sil.MoverDe(0, -30)
        sil.Desvanecer(0, 1)
        sil.actual.scale_x = -math.cos(math.pi*p)
        sil.Pintar()

    def EnDialogoEntra(self, d):
        d.Encadenar(self.Chain1)

    def EnSilabaDorm(self, d):
        d.PintarConCache()

    def EnSilaba(self, d):
        d.actual.borde += 4 *d.progreso
        d.actual.color.Interpolar(d.progreso, d.actual.scolor)
        d.Pintar()

    def Chain3(self, d, p):
        d.progreso = p
        d.Desvanecer(1,0)
        d.actual.color.CopyFrom(d.actual.scolor)
        d.Pintar()

    def EnSilabaSale(self, d):
        d.Encadenar(self.Chain3)


class FxsGroup(comun.FxsGroup):
    def __init__(self):
        self.fxs = [ FX1() ]
        self.sil_in_ms = 300
        self.sil_out_ms = 300
        self.out_ms = 300
        self.in_ms = 500