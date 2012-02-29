# -*- coding: utf-8 -*-
from libs import common, physics, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin, cos
import random
import cairo
t = extra.LoadTexture("textures/sakura3.png")


ca = extra.cCairoColor(0xFFE88CE0)#rosita
cb = extra.cCairoColor(0xFF7390AB)#gris
p = advanced.cParticleSystem(png="textures/sakura3.png", emit_parts=40, mode = 0, max_parts=80, rotation= 0.1, scale_from=0.40, scale_to= 0.7,max_life=1.6)
p.SetAngle(10, 2, 10)
p.SetGravity(0, -1)
#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.events = [Evento1(),Evento2(), Evento3()]
		self.parts = p

	def OnSyllableStarts(self, sil):
		global ca, cb, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		sil.parts = sil.CreateParticles(t, scale=0.1,alpha_min=0.4)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [advanced.cSprite(t, x +random.randint(-25, 25), y+random.randint(-25, 25), scale=random.random()*0.5 +0.5) for i in range(25)]#para que desordenen, pero no las vamos a pintar

	def OnSyllableSleep(self, sil):
		global ca, cb, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		sil.Paint()

class Evento1():
		def OnSyllable(self, sil):
			global ca, cb, t
			sil.actual.mode_fill = sil.P_DEG_VERT

			if sil.crear:
				sil.crear  = False
				for part in sil.parts:
					world.CreateSprite(part)
				for b in sil.bull:
					world.CreateSprite(b, False)
				sil.matar=True
			#alpha = common.Interpolate(sil.progress, 1, -0.2)#not needed, esto es lo que produce elbug q todas las parts tengan la misma opacidad (lo q es mentira)

			#nande: el capasactivar es como el modopintado, con llamarlo una vez basta, asi quel o pongo afuera del for
			advanced.LayerActivate(1)
			for part in sil.parts[:]:
				#advanced.StartGroup()
				part.color.a -= 0.05
				#Este numero es raro, es importante que no sea muy chico o las particulas no se van a morir!  y la animacion luego va a verse rara por todas las particuals que existen pero no se ven
				#el calculo es maso asi. tenemos 750 ms de animacion seguro (el _end+750)
				#si lo pasamos a frames son unos 25 (750/30 (fps)) (ojo no usar fps mayor)
				#si vemos cuanto podemos decrementar en 25 frames tenemos 1/25=0.05 (o algo menor, pero es mejor poner un numero mas grande
				part.Paint()
				#advanced.fBlur1(1, common.Interpolate(sil.progress, 0.2, 0))
				#advanced.EndGroup()
				#world.Resize(part, common.Interpolate(sil.progress, 0.1, 0.3))
				if part.color.a <= 0:
					sil.parts.remove(part)

			#verificamos si no hay mas parts y si se crearon, si es cierto significa que hay que matar los buls tamb
			if (not sil.parts )and sil.matar:
				for part in sil.parts:
					world.DestroySprite(part)
				sil.parts = [] #borramos las parts
				for b in sil.bull:
					world.DestroySprite(b)
				sil.bull = []

		def SyllableTime(self, sil):
			return (sil._start+((sil._end-sil._start)/2.0) , sil._end+200)
class Evento2():
		def OnSyllable(self, sil):

			global ca, cb, t, p
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.actual.color1.a = common.Interpolate(sil.progress, 0.5, 0.0)
			sil.actual.color3.a = common.Interpolate(sil.progress, 0.5, 0.0)
			advanced.LayerActivate(3)
			advanced.StartGroup()
			sil.Paint()
			advanced.fBlur1(1, ((sin(pi*sil.progress))/4.0))
			advanced.fGlow(1, ((sin(pi*sil.progress))/4.0))
			advanced.EndGroup(common.Interpolate(sil.progress, 1, 0.0))
			p.SetWindow(sil.original._width+1, 1)
			p.SetPosition(
				sil.actual.pos_x+random.randint(8,12)-(random.randint(-2,3)+(sil.original._width*(sil.progress)/4)),
            	(random.randint(1,20)+sil.actual.pos_y))

			if sil._text.strip()<>"":
				p.Emit()
		def SyllableTime(self, sil):
			return (sil._start, sil._end)
class Evento3():
		def OnSyllable(self, sil):

			global ca, cb, t

			sil.actual.mode_fill = sil.P_DEG_VERT
			advanced.LayerActivate(2)
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._start, sil._start+((sil._end-sil._start)/2.0))



class FxsGroup(common.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto())
		world = physics.World(grav_y = -0.85, grav_x = -1.35)
		self.skip_frames= False
		self.in_ms = 0
		self.out_ms = 0

	def OnFrameStarts(self):
		global world
		world.Update(True)
		advanced.StartGroup()
		advanced.LayerStarts()


	def OnFrameEnds(self):
		global p

		advanced.LayerEnd()
		micolor = extra.cCairoColor()
		factual = video.cf.framen
		if factual<=1072:
			micolor.CopyFrom(ca)
		elif 1073<=factual<=1256:
			micolor.CopyFrom(cb)


		elif 1257<=factual<=1330:
			micolor.CopyFrom(ca)
			micolor.Interpolate((1330-factual)/float(1330-1257), cb)

		elif 1331<=factual<= 2159:
			micolor.CopyFrom(ca)

		pat = advanced.EndGroup()
		ctx = video.cf.ctx
		ctx.set_source_rgba(micolor.r, micolor.g, micolor.b ,micolor.a)
		ctx.rectangle(0,0, video.vi.width, video.vi.height)
		advanced.PaintMode("screen")
		ctx.mask(pat)
		p.Paint()
		advanced.PaintMode("over")#no es realmente necesario


