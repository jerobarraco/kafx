# -*- coding: utf-8 -*-
from libs import comun, video
from libs.draw import avanzado
import math
global pat
pat = None #en esta variable global pondremos la textura
#no es lindo codigo, pero asi puedo usar la misma textura en dialogues y silabas de diferentes efectos.


class Roman(comun.Fx):
	def EnDialogoInicia(self, s):
		#Como el dialogo siempre va con texura.. ya lo ponemos una vez y nos dejamos de joder
		s.original.modo_relleno = s.P_TEXTURA
		#Con esto indicamos que el relleno del dialogo usará el source (textura/patron/degradado) almacenado en s.actual.textura

	def EnSilaba(self, s):
		#"accesos directos"
		a = s.actual
		c = a.color1
		global pat
		#Ponemos relleno solido (temporalmente, asigandolo a actual)
		a.modo_relleno = s.P_SOLIDO
		#este es el peor caso para la velocidad tener que cambiar el modo de relleno una vez por cuadro, pero es raro q pase.

		#usamos blending aditivo (rlz)
		avanzado.ModoPintado('add')
		#Calculamos el la opacidad de la animacion en funcion de seno
		p = math.sin(math.pi*s.progreso)/4.0 #el rango sería d 0 a 0.25 (0.25 =1/4)
		#calculamos el angulo, fijense que le sumo s.index para q no sean todas las rotaciones iguales
		r = math.pi*((s.progreso+s._indice)/2.0)
		#s.index es una nueva variable, es el index de la silaba/dialogo, hace que la rotacion no se vea repetitiva.

		#le sacamos la sombra y el borde
		a.sombra = 0
		a.borde = 0

		#le ponemos color "rojo" (mezclado con verde y azul para mejorar como se ve y como "blendea")
		c.b = 0.2
		c.g = 0.2
		c.r = 1

		#Y lo pintamos haciendole un blur bi-direccional de 6 pasos con opacidad "P"
		avanzado.GrupoInicio()
		s.Pintar()
		#recuerden lo pusimos para q ponga solo el relleno de un color solido, asi el blur queda como yo quiero
		#lo pintamos con un glow q crece
		avanzado.fBiDirBlur(r, 6, p)
		avanzado.GrupoFin()

		#hacemos lo mismo pero con color "verde",
		#y con una rotacion aumentada en 2.09 (radianes)
		c.b = 0.2
		c.g = 1
		c.r = 0.2
		avanzado.GrupoInicio()
		s.Pintar()
		avanzado.fBiDirBlur(r+2.09, 6, p)
		avanzado.GrupoFin()

		#lo mismo con "azul"
		# pero con rotacion aumentada en 4.18, de esa forma los tres colores quedan separados
		#siempre en angulos equidistantes, (2.09 d cada uno) (4.18+2.09 ~= 6.27 ~= 2*pi (360º)
		c.b = 1
		c.g = 0.2
		c.r = 0.2
		avanzado.GrupoInicio()
		s.Pintar()
		avanzado.fBiDirBlur(r+4.18, 6, p)
		avanzado.GrupoFin()

		#Restauramos el modo a over (importante)
		avanzado.ModoPintado('over')
		#Le decimos que use relleno del tipo textura
		a.modo_relleno =  s.P_TEXTURA
		#y llamamos al EnDialogo que carga la textura y pinta
		#Cargamos la textura global en la textura local
		#s.texturas[s.PART_BORDE] = pat
		s.texturas[s.PART_RELLENO] = pat
		#s.texturas[s.PART_SOMBRA] = pat
		#ver aclaracion en EnDialogo
		#s.MoverTextura(-s.actual.pos_x, -s.actual.pos_y, parte = s.PART_BORDE)
		s.MoverTextura(-s.actual.pos_x, -s.actual.pos_y+s.original._y_bearing, parte = s.PART_RELLENO)
		#s.MoverTextura(-s.actual.pos_x, -s.actual.pos_y, parte = s.PART_SOMBRA)
		#Y pintamos todo
		s.Pintar()

	def EnDialogo(self, diag):
		global pat
		#Cargamos la textura global en la textura local
		diag.texturas[diag.PART_RELLENO] = pat
		#No hay que olvidarse que la textura depende del punto de origen del texto
		#o sea el baseline (pos_x, pos_y) (la textura se mueve con el texto)
		diag.MoverTextura(-diag.actual.pos_x, -diag.actual.pos_y+diag.original._y_bearing, parte = diag.PART_RELLENO)
		#Y pintamos todo
		diag.Pintar()
		#con la nueva forma de pintado usar una textura aleatoria para pintar una parte del texto
		#es trivial. es mas podriamos  haber usado la textura para el borde y/o la sombra!

	def EnDialogoEntra(self, s):
		global pat
		s.Desvanecer(0, 1)
		s.MoverDe(10, 0)
		#Cargamos la textura global en la textura local
		s.texturas[s.PART_RELLENO] = pat
		#ver aclaracion en EnDialogo
		s.MoverTextura(-s.actual.pos_x, -s.actual.pos_y, parte = s.PART_RELLENO)
		#Y pintamos todo
		s.Pintar()

	def EnDialogoSale(self, s):
		global pat
		s.Desvanecer(1, 0)
		s.MoverA(-10, 0)
		#Cargamos la textura global en la textura local
		s.texturas[s.PART_RELLENO] = pat
		#ver aclaracion en EnDialogo
		s.MoverTextura(-s.actual.pos_x, -s.actual.pos_y, parte = s.PART_RELLENO)
		#Y pintamos todo
		s.Pintar()

class tradu(comun.Fx):
	def EnDialogoInicia(self, s):
		#Seteamos el modo de relleno como degradadolineal
		o = s.original
		o.modo_relleno = s.P_DEG_VERT
		o.org_x = o.pos_x
		o.org_y = o.pos_y -(o._alto/2.0)
		#cambiamos el org para el degradado, lo ponemos en original para que persista en todos los frames

	#a partir de acá es tipico
	#el glow lo hago por pintada, lo qu lo hace mas lento de lo normal, pero pasa q si uso un glow a nivel general
	#haria glow sobre el romanji y el effect se cagaria.
	def EnDialogoEntra(self, s):
		s.Desvanecer(0,1)
		s.MoverDe(10,0)
		avanzado.GrupoInicio()
		s.Pintar()
		avanzado.fGlow()
		avanzado.GrupoFin()

	def EnDialogoSale(self, s):
		s.Desvanecer(1,0)
		s.MoverA(-10,0)
		avanzado.GrupoInicio()
		s.Pintar()
		avanzado.fGlow()
		avanzado.GrupoFin()

	def EnDialogo(self, s):
		avanzado.GrupoInicio()
		s.Pintar()
		avanzado.fGlow()
		avanzado.GrupoFin()

class FxsGroup(comun.FxsGroup):
	def __init__(self):
		self.in_ms = 150
		self.out_ms = 150
		self.fxs = (Roman(), tradu())

	def EnCuadroInicia(self):
		#Como vamos a usar el patron para la silaba y el dialogo lo mejor es capturar el fondo una vez y procesarlo una vez.
		avanzado.GrupoInicio(True)
		#El "True" es para que empiece el grupo y "deje" pintado lo que ya estaba (llamese cuadro de video)
		#el valor default es False
		#y a eso (o sea lo q veiamos (en este caso seria solo el video) le hacemos un glow de 2
		avanzado.fGlow(3, 0.05)
		#y al hacer pop_group no se pinta el grupo y nos devuelve un pattern :D
		#(tambien podriamos hacer un avanzado.EndGroup(opacidad=0)
		global pat
		pat = video.cf.ctx.pop_group()
