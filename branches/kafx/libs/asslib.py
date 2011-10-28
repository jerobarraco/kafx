# -*- coding: utf-8 -*-
import codecs
from draw import extra
import comun
"""Este módulo define las cosas necesarias para cargar un archivo ASS, y los objetos que permiten el pintado de texto con cairo"""

#Constantes, no cambien nada si no quieren que el programa se rompa
#Del Estilo
S_NAME = 'name'
S_FONT = 'fontname'
S_SIZE = 'fontsize'
S_FORMAT ='format'
S_PCOLOR = 'primarycolour'
S_SCOLOR = 'secondarycolour'
S_OCOLOR = 'outlinecolour'
S_BCOLOR = 'backcolour'
S_MARGINV = 'marginv'
S_MARGINR = 'marginr'
S_MARGINL = 'marginl'
S_OUTLINE = 'outline'
S_ALIGN = 'alignment'
S_SHADOW = 'shadow'
S_BOLD ='bold'
S_ITALIC = 'italic'
S_ANGLE = 'angle'
S_SCALE_X = 'scalex'
S_SCALE_Y = 'scaley'

#De los eventos (Dialogos)
E_FORMAT ='format'
E_DIALOG = 'dialogue'
E_START = 'start'
E_END = 'end'
E_LAYER = 'layer'
E_STYLE = 'style'
E_TEXT = 'text'
E_EFFECT = 'effect'

#Del script ([F]ile)
F_EVENTS = '[events]'
F_SINFO = '[script info]'
F_STYLE4P = '[v4+ styles]' #La p es de PLUS (o sea +)
F_STYLE4 = '[v4 styles]'

#Estas funciones estan definidas afuera para que sean usables por cualquiera que llama al modulo
def TimeToMS(tiempo):
	"""Convierte un string del tipo '0:00:00.00' de ASS a milisegundos en entero"""
	h, m, s = tiempo.split(':')
	s, ms = s.split('.')
	result = int(h) *60 #Le asignamos horas y lo convertimos a minutos
	result += int(m) #Le asignamos los minutos
	result *= 60 # Lo pasamos a segundos
	result += int(s) #Le sumamos los segundos
	result *= 1000 #lo pasamos a ms
	result += int(ms)*10
	return result #y si no hay ningun caracter raro por ahi todo OK


class cPropiedades():
	def __init__(self, otro=None, dicc=None):
		"""Hay 3 formas de crear un estilo:
			sin nada, se crea con valores default.
			cPropiedades(otro=otroacopiar) o cPropiedades(otroacopiar) copia los valores de otro
			cPropiedades(dicc=diccionario) lo inicializa con los valores de un diccionario ass"""

		#Estos necesitan estar afuera porque si no estan inicializados, en el caso q se cree directamente una  instancia cPropiedades dara error!!
		self.color1 = extra.cCairoColor(numero=0xFFFF2020) #Notar q el 0x hace q sea un numero de verdad, y no un string. color primario
		self.color2 = extra.cCairoColor(numero=0xFF808080) #color secundario
		self.color3 = extra.cCairoColor(numero=0xFF101010) #borde
		self.color4 = extra.cCairoColor(numero=0xFF808080) #sombra
		#colores: primario Secundario Outline Back
		self._capa = 0
		
		if otro:
			self.CopiarTodoDe(otro)
		else:
			#valores por default
			#animables
			#escalado, x e y respectivamente
			self.scale_x = 1.0
			self.scale_y = 1.0
			#tamaño del borde en pixels
			self.borde = 3
			#tamaño de la sombra en pixels
			self.sombra = 0
			self.angulo = 0
			#posición del vector (del punto de inicio del vector)
			self.pos_x = 30
			self.pos_y = 30
			#origen de las transformaciones (y de algunos pintados)
			self.org_x = 0
			self.org_y = 0
			#desplazamiento de la sombra en pixels, en x e y respectivamente
			self.shad_x = 0
			self.shad_y = 0
			#modos de pintado
			self.modo_relleno = 0
			self.modo_borde = 0
			self.modo_sombra = 0
			self.modo_particula = 0
			#no animables
			#nombre del estilo
			self._name ='EstiloManualmenteCreado'
			#tamaño de la fuente
			self._size = 12
			#nombre de la fuente
			self._fuente = "Verdana"
			#Negrita
			self._negrita = False
			#Italica
			self._italica = False
			#margenes en pixels, vertical, derecho e izquierdo respectivamente
			self._marginv = 30
			self._marginr = 30
			self._marginl = 30
			#alineación segun ass (an creo)
			self._alin = 2
			#capa, completamente sin usar
			self._capa = 0

			#path info #cargando de una figura esto no tiene mucho efecto asi que ni siquiera se crean las variables
			self._x_bearing = 0
			self._y_bearing = 0
			self._x_advance = 0
			self._y_advance = 0
			self._ascent = 0
			self._descent = 0
			self._max_x_advance = 0
			self._max_y_advance = 0
			if dicc:
				self.FromDict(dicc)#porque al dict le pueden faltar valores

	def CopiarTodoDe(self, otro):
		#Esto es importante porque el estilo original de los dialgos se inicia en realidad pasandole un estilo al momento de crearlo
		self.CopiarDe(otro)
		#No animables
		self._name = otro._name
		self._fuente = otro._fuente
		self._size  = otro._size
		self._negrita = otro._negrita
		self._italica = otro._italica
		self._marginv = otro._marginv
		self._marginr = otro._marginr
		self._marginl = otro._marginl
		self._alin = otro._alin
		#self._capa = otro._capa # no es necesario

		"""
		calculados
		self._ancho = otro._ancho
		self._alto = otro._alto
		self._alto_linea = otro._alto_linea

		self._x_bearing = otro._x_bearing
		self._y_bearing = otro._y_bearing
		self._x_advance = otro._x_advance
		self._y_advance = otro._y_advance
		self._ascent = otro._ascent
		self._descent = otro._descent
		self._max_x_advance = otro._max_x_advance
		self._max_y_advance = otro._max_y_advance"""

	def CopiarDe(self,  otro):
		"""Copia los datos de otro objeto del mismo tipo
		@otro es un objeto del tipo cPropiedades

		copia solo los datos animables para hacerlo más rapido.
		"""
		self.pos_x = otro.pos_x
		self.pos_y = otro.pos_y
		self.org_x = otro.org_x
		self.org_y = otro.org_y
		self.shad_x = otro.shad_x
		self.shad_y = otro.shad_y
		self.scale_x = otro.scale_x
		self.scale_y = otro.scale_y
		self.angulo = otro.angulo
		self.color1.CopiarDe(otro.color1)
		self.color4.CopiarDe(otro.color4)
		self.color3.CopiarDe(otro.color3)
		self.color2.CopiarDe(otro.color2)
		self.borde = otro.borde
		self.sombra = otro.sombra
		self.modo_relleno = otro.modo_relleno
		self.modo_borde = otro.modo_borde
		self.modo_sombra = otro.modo_sombra
		self.modo_particula = otro.modo_particula

	def FromDict(self, estilo):
		"""Crea los valores desde un diccionario, para uso interno"""
		#animables
		import math
		self.angulo = math.radians(comun.SafeGetFloat(estilo, S_ANGLE))
		self.color1  = extra.cCairoColor(texto=estilo.get(S_PCOLOR, 0))
		self.color3 = extra.cCairoColor(texto=estilo.get(S_OCOLOR, 0))
		self.color4 = extra.cCairoColor(texto=estilo.get(S_BCOLOR, 0))
		self.color2 = extra.cCairoColor(texto=estilo.get(S_SCOLOR, 0))
		self.borde = comun.SafeGetFloat(estilo, S_OUTLINE)
		self.sombra = int(comun.SafeGetFloat(estilo, S_SHADOW)) #el zheo me dijo q podia ser flotante pero no tiene sentido aca

		self.scale_x = comun.SafeGetFloat(estilo, S_SCALE_X, 100)/100.0
		self.scale_y = comun.SafeGetFloat(estilo, S_SCALE_Y, 100)/100.0

		#No animables
		self._name = estilo.get(S_NAME, '')
		self._fuente = estilo.get(S_FONT, '')
		self._size = comun.SafeGetFloat(estilo, S_SIZE)
		self._negrita = not (estilo.get(S_BOLD, '0') == '0')
		self._italica = not (estilo.get(S_ITALIC, '0') == '0')

		self._marginv = int(comun.SafeGetFloat(estilo, S_MARGINV))
		self._marginr = int(comun.SafeGetFloat(estilo, S_MARGINR))
		self._marginl = int(comun.SafeGetFloat(estilo, S_MARGINL))
		self._alin = int(comun.SafeGetFloat(estilo, S_ALIGN))

class cSilaba(extra.cVector):
	def __init__(self,  texto='', estilo=None, parent=None):
		"""
		Una silaba, es mejor dejar que las cree el dialogo porque necesitan una inicializacion especial
		@texto texto de la silaba
		@estilo objeto del tipo cPropiedades
		@parent objeto padre

		para que la silaba se pueda usar luego hay que llamar a CambiarTexto(texto, preposicion)
		"""
		extra.cVector.__init__(self, estilo, parent=parent)
		self._texto = texto
		self._letras = None

	def DividirLetras(self):
		"""Computa los caracteres de la sílaba...
		Usar si cambian el _texto
		es muy lento y consume mas ram
		para acceder a las silabas luego usen _letras
		tambien activar la opcion en FxsGroup.
		"""
		#creamos el array y obtenemos valores comunes
		self._letras = []
		time = self._start
		last = (self.original.pos_x, self.original.pos_y)
		#Si hay chars
		if not self._texto:#atrapa '' y None
			self._texto = ' '
			#para evitar codigo duplicado, de igual manera no deberias llamar a esto sin texto ò_ó

		#calculamos la duracion de cada caracter
		cdur = float(self._dur) / len(self._texto)
		#agregamos los caracteres
		for (i, tchar) in enumerate(self._texto):
			char = extra.cVector(estilo=self.original, parent=self)
			char._indice = i
			char._start = time
			char._dur = cdur
			char._end = time = (time + cdur)
			char.efecto = self.efecto #no sirve de nada pero bueno
			last = char.CambiarTexto(tchar, last)
			self._letras.append(char)

	def Encadenar(self, funcion, duracion=None):
		"""Permite encadenar los caracteres a una animacion.
		Antes de llamar a esta función llamen a DividirLetras
		o activen la opcion en FxsGroup
		@funcion funcion a llamar con cada silaba y el progreso
		@duracion=None duracion de la animacion de cada caracter,
			Si no se especifica, se usará una duración tal que
			se anime solo un caracter por vez.
		(Nota: no cambien el _texto si no quieren inconsistencias)
		"""
		comun.Encadenar(self._dur, self.progreso, self._letras, funcion, duracion)

class cDialogo(extra.cVector):
	"""Un Dialogo representa una linea de texto,
	Posee herramientas para tomar el texto, cada una de las silabas del texto y sus tiempos de karaoke.
	Este objeto es el mas complejo, casi imposible que lo crees vos, mejor usar cSilaba o directamente extra.cVector
	"""

	def __init__(self, dialogo, estilos, max_effect = 0):
		"""
		@dialogo es la linea de dialogo en forma ass (interno)
		@estilos es el array con estilos
		opcionales
		@max_effect numero máximo que puede tomar como efecto
		"""
		t_estilo = dialogo[E_STYLE]
		est = estilos[0]
		for i in estilos:
			if t_estilo == i._name:
				est = i
				break

		estilo = cPropiedades(est)
		#odio lo asqueroso que se pone ass
		#el or es porque el asqueroso de ass indica el margen por cada linea. PEEEEEEEEEERO si es 0 toma el del estilo ~_~
		estilo._capa = comun.SafeGetFloat(dialogo, E_LAYER)	or estilo._capa
		estilo._marginv = comun.SafeGetFloat(dialogo, S_MARGINV) or estilo._marginv
		estilo._marginr = comun.SafeGetFloat(dialogo, S_MARGINR) or estilo._marginr
		estilo._marginl = comun.SafeGetFloat(dialogo, S_MARGINL) or estilo._marginl

		extra.cVector.__init__(self, estilo)

		#Seteamos los tiempos, traducimos todo a frames
		#guardamos los tiempos como ms para tener mas precisión
		self._start = TimeToMS(dialogo[E_START])
		self._end = TimeToMS(dialogo[E_END])
		self._dur = self._end - self._start

		#Ponemos que efecto debe usar
		self.efecto = min(max_effect, int(comun.SafeGetFloat(dialogo, E_EFFECT)))

		#Cargamos las silabas (esta función setea el _texto)
		self.__SetSilabas( dialogo[E_TEXT] )
		#El texto lo sabemos luego de parsear las silabas
		self.CambiarTexto(self._texto)

		#Como la pos depende de la alineacion y por ende del tamaño del texto, solo lo podemos
		#hacer despues de parsear las silabas
		o = self.original
		px= o.pos_x
		py= o.pos_y

		if o.angulo :
			"""#esto funciona bastante bien pero obliga a cambiarle el origen a 0,0
			#se compportaria como si el dialogo tuviese \an1
			o.org_x = 0
			o.org_y = 0
			pre = px, py
			"""

			"""
			#basico y obsoleto (tendria problemas con scale y translates)
			r = sqrt((px**2)+(py**2))
			pre = cos(o.angulo)*r , sin(o.angulo)*r
			"""

			#esto tendria que usarse en caso del angulo pero no funciona bien (aun)
			#creamos la matriz de transformacion del dialogo
			self._UpdateMatrix()
			#y calculamos el punto 0,0 del dialogo, que es el punto de inicio del texto
			pre = self.matrix.transform_point(0, 0)
		else:
			pre = px, py

		for sil in self._silabas:
			pre = sil.CambiarTexto(sil._texto, pre)

	def __SetSilabas(self, texto):
		"""crea los objetos silabas de un dialogo,
		codigo tomado del proyecto hermano ZheoFX (C)

		Zheo y Alchemist, grax chicos, son grosos! :D"""
		import re
		self._texto = ''
		self._silabas = []
		tiempo = self._start
		i = 0
		"""
		{(?:\\.)* = toma cualkier cosa, esto se hizo por si alguien ponian algun efecto y despeus el \k, pues toma el \k y bota el resto
		\\(?:[kK]?[ko]?[kf])  = toma los \k, \kf, \ko y \K
		(\d+) = cualkier digito, en este caso, el tiempo de las \k
		([\\\-a-zA-Z_0-9]*)} = para el inline_fx ({\k20\-0} karaoke)
		(\s*)([^{]*)(\s*) = espacio - cualkier caracter alfanumerico y signos-espacio"""
		#probar con el nuevo regex de alch
		"""KARA = re.compile(
    r'''
    (?:\\[\w\d]+)*              # ignore tags before k
    \\[k|ko|kf](\d+)            # k duration in centiseconds(k, K, kf, ko)
    (?:\\[\w\d]+)*              # ignore tags before inlinefx
    (\\-[\w\d]+)*               # inlinefx
    (?:\\[\w\d]+)*              # ignore tags after inlinefx
    }                           # start of text
    (?:{\\[\w\d]+})*            # ignore tags before k
    (\s+)*                      # prespace
    ([^\s\{\}]+)*               # stripped text
    (\s+)*                      # postspace
    ''',
    re.IGNORECASE | re.UNICODE | re.VERBOSE)"""

		texto = re.sub(r'({[\s\w\d]+})*', '', texto) #quita los comentarios o  tags que no comienzen con \
		pattern = r'(?:\\[k]?[K|ko|kf])(\d+)(?:\\[\w\d]+)*(\\-[\w\d]+)*(?:\\[\w\d]+)*}([^\{\}]+)*'
		#pattern = r"{(?:\\.)*\\(?:[kK]?[ko]?[kf])(\d+)([\\\-a-zA-Z_0-9]*)}([^{]*)"#anterior
		for ti, ifx, tx in re.findall(pattern, texto):
			syl = cSilaba(tx, self.original, parent=self)
			syl._indice = i
			syl._start = tiempo

			dur = int(ti)*10.0
			
			syl._dur = dur
			syl._end = tiempo =  syl._start + syl._dur

			if len(ifx)>2 :
				try:
					ifx = int(ifx[2:])
				except:
					ifx = None
			else:
				ifx = None
			#Ponemos ifx a none para permitir efectos = 0
			syl.efecto = ifx or self.efecto
			self._silabas.append(syl)
			self._texto += tx
			i += 1

		if not self._texto: #no se porque hace esto, quizás si no hay {\k} el re no devuelve nada.
			self._texto = re.sub(r'{.*}', '', texto) # lineas (quitando las tags)

	def Encadenar(self, funcion, duracion=None):
		"""Permite encadenar las silabas a una animacion
		@funcion funcion a llamar con cada silaba y el progreso
		@duracion=None duracion de la animacion de cada silaba
			Si no se especifica, se usará una duración tal que
			se anime solo una silaba por vez.
		"""
		comun.Encadenar(self._dur, self.progreso, self._silabas, funcion, duracion)

	def FullWiggle(self, amplitud=4, frecuencia=2):
		#el wiggle que queria AbelKM
		dx, dy = self.Wiggle(amplitud, frecuencia)
		for sil in self._silabas:
			o = sil.original
			if not hasattr(o, 'old_x'):
				o.old_x = o.pos_x
				o.old_y = o.pos_y
			o.pos_x = o.old_x + dx
			o.pos_y = o.old_y + dy

class Ass():
	#Esta es la clase que parsea el archivo .ass con suerte no van a necesitar usarlo
	def __init__(self,  file,  max):
		"""Al crear la clase se le puede indicar de que archivo cargar
		@file archivo .ass a cargar
		@max el numero máximo de efectos"""

		if file:
			self.LoadFromFile(file,  max)

	def __pHeader(self,  text):
		#Funcion para parsear un header
		titulo, valor = text.split(':', 1)
		self.info[titulo.strip().lower()] = valor.strip() #el titulo en minuscula lo hace mas compatible

	def __none(self,  text):
		#parseador null
		pass#aguante el pass

	def __v4PStyle(self,  texto):
		#parseador del estilo
		titulo,  valor = texto.split(':', 1) #el 1 es por las dudas, uno nunca sabe
		titulo = titulo.strip().lower()
		if titulo == S_FORMAT:
			self.formato = [v.strip().lower() for v in valor.split(',')] # si que me gusta hacer codigo complicado, no?
		else: # esto no c hace, asumimos q si no es format es style, pero uno nunca sabe
			valores = [v.strip().lower() for v in valor.split(',')]
			self.estilos.append( cPropiedades(dicc=dict(zip(self.formato,  valores))))

	def __Events(self,  texto):
		#parseador de eventos
		titulo, valor = texto.split(':', 1)
		titulo = titulo.strip().lower()
		if titulo == E_FORMAT :
			self.eformato = [v.strip().lower() for v in valor.split(',')]
		elif titulo == E_DIALOG:
			valores_raw = [v.strip() for v in valor.split(',',  len(self.eformato)-1)]
			valores = [v.lower() for v in valores_raw[:-1]]
			valores.append(valores_raw[-1]) #Esto es para q no le pase el texto del dialogo en minusculas

			nuevo_d = dict(zip(self.eformato,  valores))
			nuevo_d[E_EFFECT] = int(comun.SafeGetFloat(nuevo_d, E_EFFECT))
			d = cDialogo(nuevo_d, self.estilos, self.max_effect)
			d.indice = self.indice
			self.dialogos.append(d)
			self.indice += 1

	def LoadFromFile(self, file, max):
		#carga un archivo ass
		self.info = {}
		self.estilos = []
		self.dialogos = []
		self.indice = 0
		self.max_effect = max
		f = codecs.open(file, mode='r', encoding='utf-8')
		parser = self.__none
		for line in f:
			s = line.strip().lower()
			if (s=="") or (s[0] ==";"): #poniendo el s="" al principio nos evitamos error por q sea una linea vacia
				pass # me la soban los comentarios y las lineas en blanco ^_^
			elif s==F_EVENTS: #Pongo los eventos aca por cuestion d eficiencia, porque gralmente es lo q mas va a haber
				parser = self.__Events
			elif s == F_SINFO:
				parser = self.__pHeader
			elif (s== F_STYLE4P) or (s==F_STYLE4):
				parser = self.__v4PStyle
			else:
				parser(line)
