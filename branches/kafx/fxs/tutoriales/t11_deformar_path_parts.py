# -*- coding: utf-8 -*-
"""Este efecto muestra lo mas simple, lo basico"""
from libs import comun
from libs.draw import avanzado
from math import pi

class EfectoGenerico(comun.Fx):
	def __init__(self):
		#Cuando se cree el effect
		#Creamos las particulas
		self.parts = avanzado.cParticleSystem(png="textures/spark5.png",
		max_life=3, max_parts=10000, emit_parts=10, scale_from= 0.05, scale_to=0.5, mode=1, rotation=0)
		#Configuramos la ventana y el angulo
		self.parts.SetWindow(0, 0)
		#self.parts.DarGravedad(pi/2.0, 0.01)
		self.parts.SetAngle(pi/2,0.5,  pi)

	def OnDialogueStarts(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT
		diag.original.modo_borde = diag.P_DEG_VERT

	def OnSyllableStarts(self, d):
		d.original.modo_relleno = d.P_DEG_VERT

	def deform(self, sil, vector):
		pos_x = sil.actual.pos_x
		pos_y = sil.actual.pos_y + 20
		last = (0, 0)
		for t, p in vector:
			l = len(p)
			if (l == 2) or (l == 6):
				if l ==2:
					px = comun.LERP(sil.progress, last[0], p[0])
					py = comun.LERP(sil.progress, last[1], p[1])
					last = p
				else:
					px, py = comun.PointBezier(
						sil.progreso, last[0], last[1], p[0], p[1], p[2], p[3], p[4], p[5])
					last = p[4:]
				self.parts.SetPosition(pos_x+px, pos_y+py)
				self.parts.Emit()
		return vector

	def OnSyllable(self, d):
		d.actual.color1.Interpolate(d.progress, d.actual.color2)
		d.Paint()
		d.CompleteDeform(self.deform)

	def OnDialogue(self, d):
		#Cuando el dialogo sea mostrado
		d.PaintReflection()
		d.Paint()


	def chainin(self, s, p):
		s.progreso = p
		s.Fade(0,1)
		s.PaintReflection()
		s.Paint()


	def OnDialogueIn(self, d):
		d.Chain(self.chainin)

	def chainout(self, s, p):
		s.progreso = p
		s.Fade(1, 0)
		s.PaintReflection()
		s.Paint()


	def OnDialogueOut(self, d):
		d.Chain(self.chainout)

#Esta es la clase principal de donde kafx tomara toda la info, tiene que tener este nombre
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.in_ms = 150 #Milisegundos para la animacion de entrada
		self.out_ms = 250 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		self.skip_frames = False
		#Un effect si o si tiene que definir lo siguiente, si o si con este nombre
		#Funciones (grupo de efectos) que provee
		self.fxs = (EfectoGenerico(), EfectoGenerico())

	def OnFrameEnds(self):
		#Pintamos las partículas con un modo aditivo
		avanzado.PaintMode('add')
		self.fxs[0].parts.Paint()
		avanzado.PaintMode('over')