# -*- coding: utf-8 -*-
from libs import comun, physics
from libs.draw import extra
				
t1 = extra.CargarTextura("texturas/T_Negro2.png")				
world = None #globales on son buena idea, alentan todo y es mas dificil saber que estas haciendo
objs = []
objs2 = []
class Efecto():		
	def EnSilabaInicia(self, sil):
		parts = sil.CrearParticulas(t1, escala=0.4 ) 
		sil.parts = [parts[pos] for pos in xrange(0, len(parts), 5) ] #tomamos 1 cada 100 parts
		sil.moving = False

	def EnSilabaDorm(self, sil):
		sil.PaintWithCache()
		
	def EnSilaba(self, sil):
		global world, objs
		if not sil.moving:
			sil.moving = True
			for p in sil.parts:
				world.CreateSprite(p)
				objs.append(p)
				
class Efecto2():
	def EnSilabaInicia(self, s):
		s.nueva= True
	def EnDialogo(self, d):
		d.PaintWithCache()
		
	def EnSilaba(self, s):
		global world,objs2
		if s.nueva:			
			s.nueva= False
			world.CreateVector(s)
			objs2.append(s)
			s.original.color1.CopyFrom(s.original.color2)
	
		
			
class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(), Efecto2(), Efecto2())
		#no puedo crear dos efecto() porque intentaria crear dos mundos
		self.saltar_cuadros = False
		world = physics.World()
				
	def EnCuadroFin(self):
		global world, objs,objs2
		world.Update(True)
		for o in objs[:]:#[:]es para poder hacer remove
			o.Paint()
			o.color.a -= 0.01
			if o.color.a <0.0:
				world.Destroy(o)
				objs.remove(o)
				
		for o in objs2[:]:#[:]es para poder hacer remove
			o.Paint()
			o.original.color1.a -= 0.01
			if o.original.color1.a <0.0:
				world.Destroy(o)
				objs2.remove(o)