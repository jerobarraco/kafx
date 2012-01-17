# -*- coding: utf8 -*-
from libs import basico, extra, comun, avanzado
#no usar, esta demasiado desactualizado

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.parts = avanzado.cParticleSystem(png="p01.png", max_parts=20, parts_por_cuadro=20,
			color=extra.cCairoColor(0xFFD9C7A2), max_life=1, modo=0)
		self.parts.DarAngulo(4, 40, 2)
		self.parts.DarGravedad(90, 1)
		
		self.saltar_cuadros=False
		self.OnFrame= self.General
		#--ACÁ SON LOS FX DEL KARAOKE--
		ef1= comun.Fx() #Comienza la funcion (?)
		ef1.EnDialogo = self.DibujarSilsback #Silabas que van atras
		ef1.EnSilabaMuertaOut=self.DibujarSilsFront #Silabas muertas
		ef1.EnSilaba = self.DibujarSilAFront #Silabas del FX
		ef1.EnDialogoSale = self.SilSale #Silabas de salida
		
		#--ACÁ SON LOS FX DE LA TRADU--
		ef2 = comun.Fx() #Comienza Funcion
		ef2.EnDialogo = self.DibujarLinea #Traduccion completa
		ef2.EnDialogoSale = self.DiagSale #Traduccion de entrada
		ef2.EnDialogoEntra = self.DiagEntra #Traduccion de salida
		
		#Un efecto si o si tiene q definir lo siguiente, si o si con esos nombres
		self.in_ms = 100 #Milisegundos para la animacion de entrada
		self.out_ms = 200 #MS para animacion d salida
		self.sil_in_ms = 100 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		
		#Funciones (grupo de efectos) que se provee
		self.funcs =[ef1,  ef2]
		
		#Esto indica si se resetea el estilo (se vuelve al original) tras cada cuadro para cada silaba.
		#En caso que los CUADROS sean accedidos en forma secuencial, puede ayudar a hacer ciertos efectos.
		#En caso que se accedan como quieren, entonces puede provocar errores.
		#Se ha comprobado que VirtualDub al comprimir, accede de cualquier forma, y genera cosas raras.		
		self.reset_estilo = True

		##Como se definen los efectos?
		"""Basicamente contamos con una variable llamada funcs, esta tiene q llamarse asi porque la usara directamente el kafx_main
			funcs es un array, cada item representa un EFECTO (grupo de efectos en realidad) del archivo Ass, que se define en cada linea de dialogo...
			(generalmente ass lo usa para poner cosas como "karaoke" "scroll" acá usaremos un numero, 0 para el primer grupo de efectos, 1 para el siguiente y ansii)"""

##############################	COMIENZAN LOS EVENTOS PARA LOS EFECTOS	##############################
			
	def General(self, cf):
		self.parts.Dibujar(cf.ctx)
		#self.parts.ModEmisor(-300,-300,0,0 ,90,1,grav_angulo=270, grav_vel=6)
		self.parts.Pausa()

##EFECTOS DEL KARAOKE

	def DibujarSilsback(self,  cf,  diag): #Silabas que van atras
		basico.aFade(diag, 0.0, 1.0)
		extra.SetEstilo(cf.ctx,  diag.actual)
		basico.pSombra(cf.ctx,  diag)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)

	def DibujarSilsFront(self,  cf,  diag): #Silabas muertas
		basico.aFade(diag, 1.0, 0.0)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)

	def DibujarSilAFront(self,  cf, diag): #Silabas del FX
		#diag.actual.borde= diag.original.borde+(6*diag.progreso)
		basico.aFade(diag, 0.0, 1)
		avanzado.GrupoInicio()
		basico.pTexto(diag)
		avanzado.pGlow(cf.ctx,  3,  diag.progreso*0.25)
		avanzado.GrupoFin(cf.ctx)

		self.parts.DarVentana(diag.original._ancho, 4)
		
		#El alto lo divide en 2 cuando lo cargas, por el h
		#Parametros x, y, h, w, angulo,vel, grav_angulo=90, grav_vel=3)			
		self.parts.Emitir()

	def SilSale(self, cf, diag): #Silabas de salida
		basico.aFade(diag, 1.0, 0.0)
		extra.SetEstilo(cf.ctx,  diag.actual)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)
		

##EFECTOS DE TRADUCCION
		
	def DibujarLinea(self,  cf,  diag):
		#basico.aFade(diag, 0.0, 1.0)
		avanzado.GrupoInicio(cf.ctx)
		avanzado.pGlow(cf.ctx,  1,  diag.progreso*0.25)
		avanzado.pBlur(cf.ctx, 1)
		avanzado.GrupoFin(cf.ctx)
		extra.SetEstilo(cf.ctx,  diag.actual)
		basico.pSombra(cf.ctx,  diag)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)

	def DiagEntra(self, cf, diag):
		basico.aFade(diag, 0.0, 1.0)
		avanzado.GrupoInicio(cf.ctx)
		avanzado.pGlow(cf.ctx,  1,  diag.progreso*0.25)
		avanzado.pBlur(cf.ctx, 1)
		avanzado.GrupoFin(cf.ctx)
		extra.SetEstilo(cf.ctx,  diag.actual)
		basico.pSombra(cf.ctx,  diag)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)
		
	def DiagSale(self, cf, diag):
		basico.aFade(diag, 1.0, 0.0)
		avanzado.GrupoInicio(cf.ctx)
		avanzado.pGlow(cf.ctx,  1,  diag.progreso*0.25)
		avanzado.pBlur(cf.ctx, 1)
		avanzado.GrupoFin(cf.ctx)
		extra.SetEstilo(cf.ctx,  diag.actual)
		basico.pSombra(cf.ctx,  diag)
		basico.pTextoDegradado(cf.ctx,  diag,  extra.cCairoColor(0xFFFFFFFF),  diag.actual.color)




