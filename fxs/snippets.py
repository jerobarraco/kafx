# -*- coding: utf-8 -*-
"""Pequeños pedazos de código mostrando como hacer ciertas cosas, pueden ser totalmente beta y no funcionar
y NO se usan simplemente importando acá, no ejecuten este archivo; copien, peguen y modifiquen."""

#Ejemplos de tipos de pintados
class TiposDePintados(comun.Fx):
	def EnDialogoInicia(self, d):
		d.modo_borde = d.P_SOLIDO
		d.modo_relleno = d.P_TEXTURA
		d.modo_sombra = d.P_DEG_VERT
		d.CargarTextura('texturas/star1.png', parte=d.PART_RELLENO)
		#para pintar con textura hay que hacer:
		#diag.actual.texturas[1] = y cualquier cosa que sea un source, podes definir tus propios degradados
		#un color en especial (random? (aunque para eso mejor cambia el actual.color1) )
		#o una textura con ImageSource

	def EnDialogo(self, diag):
		#Cuando el dialogo sea mostrado
		diag.Pintar()#Lo pintamos en la pantalla

#Ejemplo de particulas con un animador personalizado
class ParticulasConAnimadorPersonalizado(comun.Fx):
		def __init__(self):
			self.p = avanzado.cParticleSystem(png='texturas/snowflake2.png',
				max_parts=100, emitir_parts=10, max_life=3, modo=0, escala_a=0.5,
				animador=self.panimador)
			#png="texturas/blast.png", particulas=100, maxparticulas=10, color=None, maxlife=2, modo = 0, escala_de=1.0, escala_a=2.0, animador=None
			#Parametros son:x, y , w, h, angulo, vel, apertura, grav_angulo=None, grav_vel=None
			self.p.DarPosicion(0, 0)
			self.p.DarVentana(30, 5)
			self.p.DarAngulo(pi*1.5, 3, 2)
			self.p.DarGravedad(0, 0)

		def panimador(self, p):
			#Esta funcion se llamara por cada cuadro por cada partícula
			#El parámetro p es la partícula a animar
			p.x += cos(p.xi)*3 #el x sera un movimiento sinusoidal
			p.xi+=0.3 #para q vaya cambiando la rotacion
			p.y += p.yi #la y ira aumentando
			p.color.a -= p.fade #para que vaya desapareciendo
			p.escala += p.sci #y se vaya achicando

		def EnDialogo(self, d):
			d.PintarConCache() #Pintar mas rapido

		def EnSilaba(self, d):
			d.Pintar()
			a = d.actual
			self.p.DarPosicion(comun.Interpolar(d.progreso, a.pos_x, a.pos_x+a.ancho), a.org_y) #Movemos el emitter
			self.p.Emitir() #Damos la orden de emitir (luego en el EnCuadroInicia o EnCuadroFin hay que llamar al p.Pintar(), algo como self.fxs[0].p.Pintar()



####RotoZoom
def EnSilaba(self, d):
	o=d.original
	dx = o.pos_x+(o._ancho*d.progreso*2)
	dy = o.pos_y-o.org_y
	op = 0.3*sin(d.progreso*2*pi)
	
	avanzado.GrupoInicio()
	d.Pintar()		
	avanzado.fRotoZoom(org_x=dx, org_y=dy, opacidad=op, escala=0.15)
	avanzado.GrupoFin()


###Cargar Forma ass
from libs import formas
#.........
class FX1(comun.Fx):
		def __init__(self):
			self.coso = extra.cVector(figura=formas.CALAVERA1)
		#...
			self.coso.Pintar()

###Bezier
class FX1(comun.Fx):
	def __init__(self):
		#Creamos el sistema de partículas
		self.parts = avanzado.cParticleSystem(png="texturas/snowflake1.png",
			max_life=3, emitir_parts= 30, escala_de=0.2, escala_a=2,
			color=extra.cCairoColor(0x88FFFFFF), max_parts=30, modo=1)
			
	def EnDialogoInicia(self, d):
		"""Cuando cada dialogo inicie, creamos la lista de puntos en los que
		#se movera el emitter de las partículas"""
		d.ps = [ (random()*640, random()*480) for i in range(4)]

	def EnDialogo(self, d):
		#Separamos los puntos de control en diferentes variables
		x1,y1 = d.ps[0]
		x2,y2 = d.ps[1]
		x3,y3 = d.ps[2]
		x4,y4 = d.ps[3]
		#Obtenemos el punto sobre la curva bezier para el progreso y los puntos
		#de control dados
		x,y = comun.PuntoBezier(d.progreso, x1,y1,x2,y2,x3,y3,x4,y4)
		self.parts.DarPosicion(x, y)
		self.parts.Emitir()
		d.PintarConCache()
#wave con librerias
class FX1(comun.Fx):
	def EnDialogoInicia(self, d):
		d.movimiento = 0#creamos una variable para que vaya animandose el movimiento

	def EnDialogo(self, d):
		avanzado.GrupoInicio()
		d.Pintar()
		avanzado.fWave( d.movimiento, 0.01, 10,  True)
		pat = avanzado.GrupoFin()
		d.movimiento += 1
		
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 250
		self.out_ms = 250
		self.sil_in_ms = 200
		self.sil_out_ms = 200
		self.fxs = (FX1(),FX1() )		
#un wave por zeth
class FX1(comun.Fx):
	def EnDialogoInicia(self, d):
		d.movimiento = 0#creamos una variable para que vaya animandose el movimiento
	def EnDialogo(self, d):
		avanzado.GrupoInicio()
		d.Pintar()
		patron = avanzado.GrupoFin(opacidad=0)
		x1, y1, ancho, alto = d.Box()
		ctx = video.cf.ctx
		x1 += d.actual.pos_x
		y1 += d.actual.pos_y 
		alto *=2
		for i in xrange(int(x1), int(x1+ancho)):
			dif = (i+d.movimiento)/10.0
			patron.set_matrix(extra.CrearMatriz(0, cos(pi*dif) ) )
			ctx.set_source(patron)
			ctx.rectangle(i, y1, 1, alto)
			ctx.fill()
		d.movimiento +=1
