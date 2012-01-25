# -*- coding: utf-8 -*-
from libs import comun, physics, video
from libs.draw import extra, avanzado

from random import randint, random
from math import pi, sin
t = extra.LoadTexture("texturas/uq7.png")

t3 = extra.LoadTexture('texturas/barra_gc.png') #entrada
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


#If you use physics in only one effect you can assign to "self" in that effect, that would make it slightly faster
world = None
class Efecto():
	def __init__(self):
		self.events = [Evento1()]
	def OnSyllableStarts(self, sil):
		global colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		factual = video.cf.framen
		micolor = extra.cCairoColor()
		if factual<=571:
			micolor.CopyFrom(colora)
		elif 572<=factual<=694:
			micolor.CopyFrom(colorb)
		elif 695<=factual<=700:
			micolor.CopyFrom(colorc)
			micolor.Interpolate((700-factual)/float(700-695), colorb)

		elif 701<=factual<=825:
			micolor.CopyFrom(colorc)
		elif 826<=factual<=833:
			micolor.CopyFrom(colord)
			micolor.Interpolate((833-factual)/float(833-826), colorc)
		elif 834<=factual<=904:
			micolor.CopyFrom(colord)
		elif 905<=factual<=970:
			micolor.CopyFrom(colore)
		elif 971<=factual<=1127:
			micolor.CopyFrom(colorf)

		elif 1128<=factual<=1255:
			micolor.CopyFrom(colorg)
		elif 1256<=factual<=1400:
			micolor.CopyFrom(colorh)
		elif 1401<=factual<=1520:
			micolor.CopyFrom(colori)
		elif 1521<=factual<=1667:
			micolor.CopyFrom(colorj)
		elif 1668<=factual<=1751:
			micolor.CopyFrom(colorm)
		elif 1752<=factual<=1824:
			micolor.CopyFrom(colorn)
		elif 1825<=factual<=1940:
			micolor.CopyFrom(colorg)
		elif 1941<=factual<=1958:
			micolor.CopyFrom(colorm)
		elif 1959<=factual<=1960:
			micolor.CopyFrom(colorn)
		elif 1961<=factual<=1971:
			micolor.CopyFrom(colorf)
		elif 1971<=factual<=2000:
			micolor.CopyFrom(colorn)
		sil.actual.color1.CopyFrom(micolor)
		sil.actual.color3.CopyFrom(micolor)
		sil.parts = sil.CreateParticles(t, scale=0.1,alpha_min=0.4)
		sil.crear = True
		x = sil.actual.pos_x+ sil.actual.org_x
		y = sil.actual.pos_y + sil.actual.org_y
		sil.bull = [avanzado.cSprite(t, x +randint(-50, 50), y+randint(-50, 50), scale=random()*0.5 +0.5) for i in range(50)]#para que desordenen, pero no las vamos a pintar

	def OnSyllableSleep(self, sil):
		global colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t
		sil.actual.mode_fill = sil.P_DEG_VERT
		factual = video.cf.framen
		micolor = extra.cCairoColor()
		if factual<=571:
			micolor.CopyFrom(colora)
		elif 572<=factual<=694:
			micolor.CopyFrom(colorb)
		elif 695<=factual<=700:
			micolor.CopyFrom(colorc)
			micolor.Interpolate((700-factual)/float(700-695), colorb)

		elif 701<=factual<=825:
			micolor.CopyFrom(colorc)
		elif 826<=factual<=833:
			micolor.CopyFrom(colord)
			micolor.Interpolate((833-factual)/float(833-826), colorc)
		elif 834<=factual<=904:
			micolor.CopyFrom(colord)
		elif 905<=factual<=970:
			micolor.CopyFrom(colore)
		elif 971<=factual<=1127:
			micolor.CopyFrom(colorf)

		elif 1128<=factual<=1255:
			micolor.CopyFrom(colorg)
		elif 1256<=factual<=1400:
			micolor.CopyFrom(colorh)
		elif 1401<=factual<=1520:
			micolor.CopyFrom(colori)
		elif 1521<=factual<=1667:
			micolor.CopyFrom(colorj)
		elif 1668<=factual<=1751:
			micolor.CopyFrom(colorm)
		elif 1752<=factual<=1824:
			micolor.CopyFrom(colorn)
		elif 1825<=factual<=1940:
			micolor.CopyFrom(colorg)
		elif 1941<=factual<=1958:
			micolor.CopyFrom(colorm)
		elif 1959<=factual<=1960:
			micolor.CopyFrom(colorn)
		elif 1961<=factual<=1971:
			micolor.CopyFrom(colorf)
		elif 1971<=factual<=2000:
			micolor.CopyFrom(colorn)
		sil.actual.color1.CopyFrom(micolor)
		sil.actual.color3.CopyFrom(micolor)
		sil.Paint()
	def OnDialogueIn(self, d):
		global colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl, t3
		d.actual.mode_fill = d.P_DEG_VERT
		factual = video.cf.framen
		micolor = extra.cCairoColor()
		if factual<=571:
			micolor.CopyFrom(colora)
		elif 572<=factual<=694:
			micolor.CopyFrom(colorb)
		elif 695<=factual<=700:
			micolor.CopyFrom(colorc)
			micolor.Interpolate((700-factual)/float(700-695), colorb)

		elif 701<=factual<=825:
			micolor.CopyFrom(colorc)

		elif 826<=factual<=833:
			micolor.CopyFrom(colord)
			micolor.Interpolate((833-factual)/float(833-826), colorc)
		elif 834<=factual<=904:
			micolor.CopyFrom(colord)
		elif 905<=factual<=970:
			micolor.CopyFrom(colore)
		elif 971<=factual<=1127:
			micolor.CopyFrom(colorf)
		elif 1128<=factual<=1255:
			micolor.CopyFrom(colorg)
		elif 1256<=factual<=1400:
			micolor.CopyFrom(colorh)
		elif 1401<=factual<=1520:
			micolor.CopyFrom(colori)
		elif 1521<=factual<=1667:
			micolor.CopyFrom(colorj)
		elif 1668<=factual<=1751:
			micolor.CopyFrom(colorm)
		elif 1752<=factual<=1824:
			micolor.CopyFrom(colorn)
		elif 1825<=factual<=1940:
			micolor.CopyFrom(colorg)
		elif 1941<=factual<=1958:
			micolor.CopyFrom(colorm)
		elif 1959<=factual<=1960:
			micolor.CopyFrom(colorn)
		elif 1961<=factual<=1971:
			micolor.CopyFrom(colorf)
		elif 1971<=factual<=2000:
			micolor.CopyFrom(colorn)
		d.actual.color1.CopyFrom(micolor)
		d.actual.color3.CopyFrom(micolor)
		#d.MoveFrom((0+(comun.Interpolate(d.progress, -40,0, comun.i_b_backstart))) ,(0))
		mov = comun.Interpolate(d.progress,1380, 3480)#el fx parece dar toda la vuelta... o ya no?
		extra.MoveTexture(t3, mov, 50)
		avanzado.StartGroup()
		d.Paint()
		texto = avanzado.EndGroup(0)
		video.cf.ctx.set_source(texto)
		video.cf.ctx.mask(t3)

class Evento1():
		def OnSyllable(self, sil):
			global world, colora, colorb, colorc, colord, colore, colorf, colorg, colorh, colori, colorm, colorn, colork, coloro, colorl
			if sil.crear:
				sil.crear  = False
				for part in sil.parts:
					world.CreateSprite(part)
				for b in sil.bull:
					world.CreateSprite(b, False)
				sil.matar=True
			alpha = comun.Interpolate(sil.progress, 1, -0.2)
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
					sil.actual.mode_fill = sil.P_DEG_VERT
					factual = video.cf.framen
					micolor = extra.cCairoColor()
					if factual<=571:
						micolor.CopyFrom(colora)
					elif 572<=factual<=694:
						micolor.CopyFrom(colorb)
					elif 695<=factual<=700:
						micolor.CopyFrom(colorc)
						micolor.Interpolate((700-factual)/float(700-695), colorb)

					elif 701<=factual<=825:
						micolor.CopyFrom(colorc)

					elif 826<=factual<=833:
						micolor.CopyFrom(colord)
						micolor.Interpolate((833-factual)/float(833-826), colorc)
					elif 834<=factual<=904:
						micolor.CopyFrom(colord)
					elif 905<=factual<=970:
						micolor.CopyFrom(colore)
					elif 971<=factual<=1127:
						micolor.CopyFrom(colorf)

					elif 1128<=factual<=1255:
						micolor.CopyFrom(colorg)
					elif 1256<=factual<=1400:
						micolor.CopyFrom(colorh)
					elif 1401<=factual<=1520:
						micolor.CopyFrom(colori)
					elif 1521<=factual<=1667:
						micolor.CopyFrom(colorj)
					elif 1668<=factual<=1751:
						micolor.CopyFrom(colorm)
					elif 1752<=factual<=1824:
						micolor.CopyFrom(colorn)
					elif 1825<=factual<=1940:
						micolor.CopyFrom(colorg)
					elif 1941<=factual<=1958:
						micolor.CopyFrom(colorm)
					elif 1959<=factual<=1960:
						micolor.CopyFrom(colorn)
					elif 1961<=factual<=1971:
						micolor.CopyFrom(colorf)
					elif 1971<=factual<=2000:
						micolor.CopyFrom(colorn)

					sil.actual.color1.CopyFrom(micolor)
					sil.actual.color3.CopyFrom(micolor)



					#avanzado.StartGroup()
					part.Paint()
					#avanzado.fGlow(1, 0.1+(sin(pi*sil.progress)/6.0))
					#avanzado.EndGroup()

					world.Resize(part, comun.Interpolate(sil.progress, 0.1, 0.2))

		def SyllableTime(self, sil):
			return (sil._start, sil._end+750)



class FxsGroup(comun.FxsGroup):
	def __init__(self):
		global world
		self.fxs = (Efecto(),Efecto())
		world = physics.World(grav_y = 0)
		self.in_ms = 500

	def OnFrameStarts(self):
		global world
		world.Update(True)