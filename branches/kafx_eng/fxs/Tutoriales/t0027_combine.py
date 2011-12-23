class EfectoGenerico(comun.Fx):

        def EnDialogo(self, diag):

                diag.Paint()



        def EnSilaba(self, diag):

                diag.actual.color1.CopyFrom(diag.actual.color2)

                diag.Paint()





class Efecto2(comun.Fx):

        def EnLetra(self, let):

                let.Pintar()



class Compuesto (EfectoGenerico, Efecto2):

        pass



class FxsGroup(comun.FxsGroup):

        #fxs = (Compuesto(), )#si queres podes definir SOLO el compuesto

        fxs = (EfectoGenerico(), Efecto2(), Compuesto())