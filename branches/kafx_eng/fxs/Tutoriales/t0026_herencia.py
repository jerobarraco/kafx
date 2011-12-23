# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun

class EfectoComun(comun.Fx):#Imaginate que aca hay todo un codigo re largo que hace algo complejo pero que es exactamente igual para dos (al menos) efectos que usas
		def EnDialogo(self, diag):
				diag.Paint()


class Efecto1(EfectoComun):#pero en este efecto queremos que ADEMAS pitne la letra
        def EnLetra(self, let):
                let.actual.color1.CopyFrom(let.actual.color2)
                let.Paint()



class Efecto2 (EfectoComun):#y en este no pintamos la letra pero si la silaba
        def EnSilaba(self, diag):
                diag.actual.color1.CopyFrom(diag.actual.color3)
                diag.Paint()


#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.dividir_letras = True
		self.fxs = (Efecto1(), Efecto2())