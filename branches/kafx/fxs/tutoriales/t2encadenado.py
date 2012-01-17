# -*- coding: utf-8 -*-
from libs import comun
from math import sin, pi
"""Este es un archivo que muestra como usar la funcion comun.Encadenar que está wrappeada y "eficientizada" en las clases
cDialogo y cSilaba en el asslib,
normalmente uno trabajará con esas funciones dentro de las clases anteriormente mencionadas, pero para efectos raros se
permite usar el metodo comun.Encadenar directamente (por ahora hasta q le encuentre una merjor utilidad).
Nota, este metodo es bastante ineficiente, y la idea es que luego se incluya un metodo en la base de KAFX q defina una
funcion onda OnBarridoSilabaIn/Out pero aun no c q nombre ponerle."""

class Kara(comun.Fx):
	def EnDialogoEntra(self, diag):
		"""Para hacer un efecto de barrido, lo que hacemos es llamar a la funcion Encadenar del dialogo
		al definir el "Encadenado" en la funcion EnDialogoEntra estamos diciendo que queremos que el barrido
		se realize cuando la funcion está entrando."""
		def PorCadaSilabaHagoEsto(sil, prog):
			"""ESTA ES LA FORMA INCOOOOOREEEEECTAAAA DE DEFINIR UNA FUNCIOOOON!!!!
			THIS IS BAD! DO NOT DO THIS!!!!
			pero es para que vean, que es una funcion independiente de todo
			requiere si o si q tenga los parametros sil y prog (pueden tener cualquier nombre, pero
			deben ser al menos dos (despues le podes agregar *args y **kwargs si queres)"""
			sil.Restore() #Esto lo ponemos por la naturaleza de kafx
			#Basicamente es para evitar producir efectos raros, metemos esto
			sil.progreso = prog#Esto es para que las funciones internas de la silaba tomen el progreso
			sil.actual.scale_x = sil.actual.scale_y = 4 - (prog*3)  #que se vaya achicando
			sil.Desvanecer(0.0, 1.0)#podemos acceder a las funciones normales (dado a la linea sil.progreso=..)
			sil.Pintar()#very important...

		diag.Encadenar(PorCadaSilabaHagoEsto)
		"""Le decimos a q funcion tiene q llamar por cada silaba
		noten que le pasamos solo EL NOMBRE nada de (),
		sino estariamos llamando a la susodicha funcion.
		Necesita solo un parametro (el otro es opcional) y es a q funcion va a llamar por cada silaba.
		"""

	def SilabasQueSalen(self, s, p):
		"""Esta esc la forma correcta!!! THIS IS CORRECT!
		notar que le pusimos el "self" al principio,
		porque esta funcion pertenece a la clase Tradu (por ende
		recibe la instancia en self"""
		s.Restore()
		s.progreso = p
		s.Desvanecer(1, 0)
		s.actual.scale_x = 1-p #para q vaya disminuyendo
		s.Pintar()
		#El problema d meterlo asi es que confunde con los otros metodos,
		#pero python lo ejecuta mejor, en una de esas lo pueden poner en otro modulo,
		#porque no importa la instancia (igual, recomiendo que para efectos complejos,
		#un modulo aparte para cada clase

	def EnDialogoSale(self, diag):
		diag.Encadenar(self.SilabasQueSalen, duracion=50)
		"""Este segundo parametro, q es opcional, dice cuanto tiempo queres
		que se anime cada silaba si no se pone, se anima cada silaba con el tiempo maximo, sin que
		se animen 2 a la vez.
		al ponerle un tiempo que sea mayor, entonces el efecto va a ser mas suave, pero van a animarse
		mas de una por vez (lo que no es malo) y algunas incluso van a empezar a media animacion.
		pd: no es necesario (por ahora) poner 'duracion=' pero eso es sintaxis python, para esta
		altura ya lo deberian saber."""


	def Montanitas(self, s, p):
		s.Restore()
		s.actual.scale_y = 1 + sin(pi*p)
		s.Pintar()

	def EnDialogo(self, diag):
		diag.Encadenar(self.Montanitas)
		#noten que se pueden usar varios efectos al mismo tiempo, traten de ser organizados
		#PAra evitar pisarnos, uso el s.Restore()

class Tradu(comun.Fx):#AVANZADO! si no entendes no importa
	"""La tradu no tiene karaoke eso es {\\k}
	las k's son las que dividen el dialogo en silabas
	de otra forma, el dialogo solo contiene una sola 'silaba'
	q es todo el texto,
	En esos caso la animacion por Encadenar no es posible basicamente porque cada letra es
	un objeto del tipo string que no continee metodos especiales de cairo que yo implemente que facilitan
	pintarlo"""

	def EnDialogo(self, diag):
		diag.Pintar()

	def EnDialogoEntra(self,diag):
		diag.Desvanecer(0,1)
		diag.Pintar()

	def EnDialogoSale(self, diag):
		diag.Desvanecer(1,0)
		diag.Pintar()

class FxsGroup(comun.FxsGroup):
	"""Explicacion:
                normalmente al hacer una animacion cuando entra un dialogo se usa EnDialogoEntra.
                Pero tiene una limitacion (no es limitacion, sino que esta diseñado para esto y no para lo otro) y es
                no permite trabajar sobre las silabas (directamente). Para hacer una animacion _secuencial_ pero individual
                sobre las silabas, usamos la nueva funcion Encadenar """      
                        
	def __init__(self):
		#Opciones principales
		self.in_ms = 500 #Milisegundos para la animacion de entrada
		self.out_ms = 500 #MS para animacion d salida
		self.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 500 #ms para la animacion de cada silaba muerta (en el dialogo actual)

		self.fxs = (Kara(), Tradu())

