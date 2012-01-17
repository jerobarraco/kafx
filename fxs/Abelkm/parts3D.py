# -*- coding: utf-8 -*-
from libs import comun, physics, video
from libs.draw import extra, avanzado
from OpenGL.GLUT import *
from OpenGL.GL import *
from random import randint, random

t = extra.CargarTextura("texturas/uq7.png")

t3 = extra.CargarTextura('texturas/barra_gc.png') #entrada

#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.eventos = [Evento1()]
	def OnSyllableStarts(self, sil):
		global t
		#sil.actual.color1.CopyFrom(sil.actual.color2)
		sil.parts = sil.CrearParticulas(t, escala=0.1,alpha_min=0.4)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [avanzado.cSprite(t, x +randint(-50, 50), y+randint(-50, 50), scale=random()*0.5 +0.5) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def OnSyllableSleep(self, sil):
		sil.PaintWithCache()
	def OnDialogueIn(self, d):
		global t3
		#d.MoverDe((0+(comun.Interpolate(d.progress, -40,0, comun.i_b_backstart))) ,(0))
		mov = comun.Interpolate(d.progress,1380, 3480)#el fx parece dar toda la vuelta... o ya no?
		extra.MoveTexture(t3, mov, 50)
		avanzado.StartGroup()
		d.Paint()
		texto = avanzado.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)
	def OnSyllable(self, sil):
		xa = comun.LERP(sil.progress, sil.actual.pos_x, sil.actual.pos_x+sil.original._ancho)
		x = (xa/(video.vi.width/2.0))-1.0
		ya = comun.Interpolate(sil.progress, sil.actual.pos_y, sil.actual.pos_y+sil.original._alto,comun.i_full_sin)
		y = 1 -(ya/(video.vi.height/2.0))
		color = [1.0, 0., 0., 0.8]
		glPushMatrix()
		glTranslatef(x, y, 0);
		#glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
		#glutWireSphere(0.1,20,20)
		glutSolidTeapot(0.1)
		glPopMatrix()

class Evento1():
		def OnSyllable(self, sil):
			global world
			if sil.crear:
				sil.crear  = False
				for part in sil.parts:
					world.CreateSprite(part)
				for b in sil.bull:
					world.CreateSprite(b, False)
				sil.matar=True
			alpha = comun.Interpolate(sil.progress, 1, -0.5)
			if alpha < 0.0:
				for part in sil.parts:
						world.DestroySprite(part)
				sil.parts = [] #borramos las parts
				for b in sil.bull:
					world.DestroySprite(b)
				sil.bull = []
			else:
				for part in sil.parts[:]:
					part.color.a = alpha
					part.Paint()
					world.Resize(part, comun.Interpolate(sil.progress, 0.1, 0.2))



		def TiempoSilaba(self, sil):
                        return (sil._start, sil._end+500)



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto())
		world = physics.World(grav_y = 0)
		self.in_ms = 500


	def OnFrameStarts(self):
		global world
		world.Update(True)