# -*- coding: utf-8 -*-
from libs import common, physics, video
from libs.draw import extra, advanced

from random import randint, random
from math import pi, sin, cos
t = extra.LoadTexture("textures/uq7.png")

t3 = extra.LoadTexture('textures/barra_gc2.png') #entrada
t4 = extra.LoadTexture('textures/barra_gc3.png') #salida

colora = extra.cCairoColor(0xFF8B5BBD)#violeta
colorb = extra.cCairoColor(0xFF7BBCC3)#verde
colorc = extra.cCairoColor(0xFF804E3F)#marrón
colord = extra.cCairoColor(0xFFAA6CC5)#violeta claro
colore = extra.cCairoColor(0xFF5ED38C)#verde fluor (esto se va a ver horrible)
colorf = extra.cCairoColor(0xFF413582)#azul
colorg = extra.cCairoColor(0xFF629EAA)#azul tirando a gris
colorh = extra.cCairoColor(0xFFC5B179)#naranja tirando a amarillo oscuro
colori = extra.cCairoColor(0xFF62ACAC)#verde feo
colorj = colorg #extra.cCairoColor(0xFF4AC6D6)#celeste
colork = colori #extra.cCairoColor(0xFF5188A6)#otro celeste
colorl = extra.cCairoColor(0xFFE09149)#naranja

colorm = extra.cCairoColor(0xFF4AC7B6)#otro verde
colorn = extra.cCairoColor(0xFF68D6D7)#otro celeste
coloro = extra.cCairoColor(0xFF5188A6)#otro celeste
colorp = extra.cCairoColor(0xFF9D2B2C)#rojo  6F3845
colorq = extra.cCairoColor(0xFF49779C)#azul
colorr = extra.cCairoColor(0xFFD38634)#naranja
colors = extra.cCairoColor(0xFFBD51A8)#violeta (puede no pegar)
colort = extra.cCairoColor(0xFF9032CE)#violeta, otro
#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.events = [Evento1(),Evento2(), Evento3()]

	def OnSyllableStarts(self, sil):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		sil.parts = sil.CreateParticles(t, scale=0.1,alpha_min=0.4)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [advanced.cSprite(t, x +randint(-50, 50), y+randint(-50, 50), scale=random()*0.5 +0.5) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def OnSyllableSleep(self, sil):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		sil.Paint()
	def OnDialogueIn(self, d):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t3
		d.actual.mode_fill = d.P_DEG_VERT
		mov = common.Interpolate(d.progress,1380, 3480)
		extra.MoveTexture(t3, mov, 50)
		advanced.StartGroup()
		d.Paint()
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

class Evento1():
		def OnSyllable(self, sil):
			global world, colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
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
				world.Resize(part, common.Interpolate(sil.progress, 0.1, 0.2))
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
			return (sil._start+((sil._end-sil._start)/2.0) , sil._end+750)
class Evento2():
		def OnSyllable(self, sil):

			global world, colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
			sil.actual.mode_fill = sil.P_DEG_VERT
			sil.actual.color1.a = common.Interpolate(sil.progress, 0.5, 0.0)
			sil.actual.color3.a = common.Interpolate(sil.progress, 0.5, 0.0)
			advanced.LayerActivate(3)
			advanced.StartGroup()
			sil.Paint()
			advanced.fBlur1(1, ((sin(pi*sil.progress))/6.0))
			advanced.fGlow(2, ((sin(pi*sil.progress))/6.0))
			advanced.EndGroup(common.Interpolate(sil.progress, 1, 0.0))

		def SyllableTime(self, sil):
			return (sil._start, sil._end)
class Evento3():
		def OnSyllable(self, sil):

			global world, colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t

			sil.actual.mode_fill = sil.P_DEG_VERT
			advanced.LayerActivate(2)
			sil.Paint()

		def SyllableTime(self, sil):
			return (sil._start, sil._start+((sil._end-sil._start)/2.0))

class Efecto1():

	def OnDialogue(self, d):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
		d.actual.mode_fill = d.P_DEG_VERT
		d.Paint()
	def OnDialogueIn(self, d):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t3
		d.actual.mode_fill = d.P_DEG_VERT
		mov = common.Interpolate(d.progress,1380, 3480)
		extra.MoveTexture(t3, mov, 50)
		advanced.StartGroup()
		d.Paint()
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

	def OnDialogueOut(self, d):
		global colort, colors, colorr, colorq, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t3,t4
		d.actual.mode_fill = d.P_DEG_VERT
		mov = common.Interpolate(d.progress, 1380, 3480)
		extra.MoveTexture(t4, mov, 50)
		advanced.StartGroup()
		d.Paint()
		texto = advanced.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t4)


class FxsGroup(common.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto1())
		world = physics.World(grav_y = 0)
		self.in_ms = 500
		self.out_ms = 500

	def OnFrameStarts(self):
		global world
		world.Update(True)
		advanced.StartGroup()
		advanced.LayerStarts()


	def OnFrameEnds(self):
		advanced.LayerEnd()
		micolor = extra.cCairoColor()
		factual = video.cf.framen
		if factual<=375:
			micolor.CopyFrom(colora)
		elif 376<=factual<=694:
			micolor.CopyFrom(colorb)
		elif 695<=factual<=700:
			micolor.CopyFrom(colorc)
			micolor.Interpolate((700-factual)/float(700-695), colorb)

		elif 701<=factual<=825:
			micolor.CopyFrom(colorc)
		elif 826<=factual<=833:
			micolor.CopyFrom(colord)
			micolor.Interpolate((833-factual)/float(833-826), colorc)

		elif 834<=factual<=894:
			micolor.CopyFrom(colord)

		elif 895<=factual<=904:
			micolor.CopyFrom(colore)#agregar coso con siguiente
			micolor.Interpolate((904-factual)/float(904-895), colord)

		elif 905<=factual<=959:
			micolor.CopyFrom(colore)
		elif 960<=factual<=970:
			micolor.CopyFrom(colorf)#agregar coso con siguiente
			micolor.Interpolate((970-factual)/float(970-960), colore)


		elif 971<=factual<=1091:
			micolor.CopyFrom(colorf)#--- hasta acá todo bien.

		elif 1092<=factual<=1245:
			micolor.CopyFrom(colorg)#agregar coso con siguiente

		elif 1246<=factual<=1255:
			micolor.CopyFrom(colorh)#agregar coso con siguiente
			micolor.Interpolate((1255-factual)/float(1255-1246), colorg)
		elif 1256<=factual<=1365:
			micolor.CopyFrom(colorh)#agregar coso con siguiente

		elif 1366<=factual<=1375:
			micolor.CopyFrom(colorh)#agregar coso con siguiente
			micolor.Interpolate((1375-factual)/float(1375-1366), colorh)
		elif 1376<=factual<=1396:
			micolor.CopyFrom(colori)#agregar coso con siguiente
			micolor.Interpolate((1396-factual)/float(1396-1376), colorh)

		elif 1397<=factual<=1520:
			micolor.CopyFrom(colori)
		elif 1521<=factual<=1660:
			micolor.CopyFrom(colorj)#agregar coso con siguiente
		elif 1661<=factual<=1667:
			micolor.CopyFrom(colorm)#agregar coso con siguiente
			micolor.Interpolate((1667-factual)/float(1667-1661), colorj)

		elif 1668<=factual<=1751:
			micolor.CopyFrom(colorm)
		elif 1752<=factual<=1815:
			micolor.CopyFrom(colorn)#agregar coso con siguiente
		elif 1816<=factual<=1824:
			micolor.CopyFrom(colorq)#agregar coso con siguiente
			micolor.Interpolate((1824-factual)/float(1824-1816), colorn)#no me gusta el color

		elif 1825<=factual<=1930:
			micolor.CopyFrom(colorq)

		elif 1931<=factual<=1940:
			micolor.CopyFrom(colorm)
			micolor.Interpolate((1940-factual)/float(1940-1931), colorq)
		elif 1941<=factual<=1950:
			micolor.CopyFrom(colorm)

		elif 1951<=factual<=1960:
			micolor.CopyFrom(colorf)#agregar coso con siguiente
			micolor.Interpolate((1960-factual)/float(1960-1951), colorn)
		elif 1961<=factual<=1970:
			micolor.CopyFrom(colorf)

		elif 1971<=factual<=1993:
			micolor.CopyFrom(colort)
			micolor.Interpolate((1993-factual)/float(1993-1971), colorf)
		elif 1994<=factual<=1996:
			micolor.CopyFrom(colorp)
			micolor.Interpolate((1996-factual)/float(1996-1994), colort)
		elif 1997<=factual<=2015:
			micolor.CopyFrom(colorp)
		elif 2016<=factual<=2041:
			micolor.CopyFrom(colors)
			micolor.Interpolate((2041-factual)/float(2041-2016), colorp)

		elif 2042<=factual<=2080:
			micolor.CopyFrom(colorr)
			micolor.Interpolate((2080-factual)/float(2080-2042), colors)

		elif 2081<=factual<= 2177:
			micolor.CopyFrom(colorr)

		pat = advanced.EndGroup()
		ctx = video.cf.ctx
		ctx.set_source_rgba(micolor.r, micolor.g, micolor.b ,micolor.a)
		ctx.rectangle(0,0, video.vi.width, video.vi.height)
		advanced.PaintMode("screen")
		ctx.mask(pat)
		advanced.PaintMode("over")#no es realmente necesario
