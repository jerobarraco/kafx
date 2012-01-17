from math import pi, cos
import cairo

from libs import comun
from libs.draw import avanzado, extra


class Kara(comun.Fx):
	def __init__(self):
		#voy a crear una funcion en extra para eso
		self.cuadros = 42
		self.gatos = [
			avanzado.cSprite(text)
			for text in extra.CargarSecuencia('texturas/fuego/f', self.cuadros, 4, cairo.EXTEND_NONE)
		]

		"""Esta era la forma anterior, para que entiendan que hacia
		#Indicamos la carpeta
		path = 'Y:\\Working Projects\\Jrev\\neko ni fuusen\\gato\\'
		#Cremos un array donde pondremos los sprites
		self.gatos=[]
		for i in range (12):
			#creamos un sprite a partir del nombre que generamos
			tcat = avanzado.cSprite(path+str(i)+'.png')
			#modificamos el origen
			tcat.org_x, tcat.org_y = 65, 30
			tcat.angulo = 0
			#y lo agregamos al array
			self.gatos.append(tcat)"""
		#Con esto contamos en que cuadro de animacion vamos
		self.frame = 0.0
		
		#y con esto cuanto tiempo nos quedamos en cada animacion
		self.frame_inc = 0.34

	def EnDialogoInicia(self, diag):
		diag.original.modo_relleno = diag.P_DEG_VERT

	def EnDialogoEntra(self, diag):
		diag.Desvanecer(0, 1)
		diag.Pintar()

	def EnSilabaDorm(self, diag):
		diag.Pintar()

	def EnSilabaMuerta(self, diag):
		diag.Pintar()

	def EnSilaba(self, diag):
		if diag._texto.strip() == "":
			return
		#Si el dialogo no tiene texto nos la tomamos.
		#Cambiamos la scale vertical
		diag.actual.scale_y = abs(comun.Interpolar(diag.progreso, 0, 1, comun.i_cos))
		diag.Pintar()

	def EnDialogo(self, diag):
		org = diag.original
		#Elegimos un gato del array dependiendo del cuadro
		cat = self.gatos[int(self.frame)]
		#Damos una opacidad
		cat.color.a = 0.5
		#Cambiamos la posicion del kitty
		cat.x = org.pos_x + (org._ancho*diag.progreso)
		cat.y = org.pos_y-30
		#y lo plasmamos
		cat.Pintar()
		#incrementamos el frame
		self.frame += self.frame_inc
		#si el frame pasa la cantidad de gatos, reiniciamos
		#self.frame = self.frame % 12.0
		self.frame %= self.cuadros

	def EnDialogoSale(self, diag):
		org = diag.original
		cat = self.gatos[int(self.frame)]
		cat.color.a = 0.5 - diag.progreso
		cat.x = org.pos_x + (org._ancho)
		cat.y = org.pos_y - 30
		cat.Pintar()

	def EnDialogoEntra(self, diag):
		org = diag.original
		cat = self.gatos[int(self.frame)]
		cat.color.a = diag.progreso - 0.5
		cat.x = org.pos_x
		cat.y = org.pos_y - 30
		cat.Pintar()

class Kanji(comun.Fx):
		def EnDialogo(self, diag):
			diag.PintarConCache()

		def EnDialogoSale(self, diag):
			diag.Desvanecer(1, 0)
			diag.MoverA(-10, 0)
			diag.Pintar()

		def EnDialogoEntra(self, diag):
			diag.Desvanecer(0, 1)
			diag.MoverDe(10, 0)
			diag.Pintar()

class Cred(comun.Fx):
		def EnDialogo(self, diag):
			diag.PintarConCache()

		def EnDialogoSale(self, diag):
			diag.Desvanecer(1, 0)
			diag.MoverA(0, 30)
			diag.Pintar()

		def EnDialogoEntra(self, diag):
			diag.Desvanecer(0, 1)
			diag.MoverDe(0, 30)
			diag.Pintar()

class Trad(comun.Fx):
		def EnDialogo(self, diag):
			diag.PintarConCache()

		def EnSilabaDormIn(self, diag):
			diag.MoverDe(20,10)
			diag.Pintar()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		#Opciones principales
		self.saltar_cuadros = False
		self.in_ms = 300 #Milisegundos para la animacion de entrada
		self.out_ms = 300 #MS para animacion d salida
		self.syl_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)
		self.syl_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)
		#~~~~~
		self.fxs = [ Kara(),Trad(), Kanji(), Cred()]

	def EnCuadroInicia(self):
		avanzado.StartGroup()

	def EnCuadroFin(self):
		avanzado.fGlow(3, 0.04)
		avanzado.EndGroup()
