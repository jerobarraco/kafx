# -*- coding: utf-8 -*-
"""Este módulo define las cosas necesarias para cargar un archivo ASS,
y los objetos que permiten el pintado de texto con cairo"""
import codecs, math
from draw import extra
import common

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

#De los events (Dialogos)
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
def TimeToMS(time):
	"""Convierte un string del tipo '0:00:00.00' de ASS a milisegundos en entero"""
	h, m, s = time.split(':')
	s, ms = s.split('.')
	result = int(h) *60 #Le asignamos horas y lo convertimos a minutos
	result += int(m) #Le asignamos los minutos
	result *= 60 # Lo pasamos a segundos
	result += int(s) #Le sumamos los segundos
	result *= 1000 #lo pasamos a ms
	result += int(ms)*10
	return result #y si no hay ningun caracter raro por ahi todo OK


class cProperties():
	def __init__(self, other=None, dicc=None):
		"""Hay 3 formas de crear un estilo:
		sin nada, se crea con valores default.
		cProperties(other=otroacopiar) o cProperties(otroacopiar) copia los valores de otro
		cProperties(dicc=diccionario) lo inicializa con los valores de un diccionario ass"""

		#Estos necesitan estar afuera porque si no estan inicializados, en el caso q se cree directamente una  instancia cProperties dara error!!
		self.color1 = extra.cCairoColor(number=0xFFFF2020) #Notar q el 0x hace q sea un numero de verdad, y no un string. color primario
		self.color2 = extra.cCairoColor(number=0xFF808080) #color secundario
		self.color3 = extra.cCairoColor(number=0xFF101010) #border
		self.color4 = extra.cCairoColor(number=0xFF808080) #shadow
		#colores: primario Secundario Outline Back
		self._layer = 0

		if other:
			self.CopyAllFrom(other)
		else:
			#valores por default
			#animables
			#escalado, x e y respectivamente
			self.scale_x = 1.0
			self.scale_y = 1.0
			#tamaÃ±o del border en pixels
			self.border = 3
			#tamaÃ±o de la shadow en pixels
			self.shadow = 0
			self.angle = 0
			#posición del vector (del punto de inicio del vector)
			self.pos_x = 30
			self.pos_y = 30
			#origen de las transformaciones (y de algunos pintados)
			self.org_x = 0
			self.org_y = 0
			#desplazamiento de la shadow en pixels, en x e y respectivamente
			self.shad_x = 0
			self.shad_y = 0
			#modes de pintado
			self.mode_fill = 0
			self.mode_border = 0
			self.mode_shadow = 0
			self.mode_particle = 0
			#no animables
			#nombre del estilo
			self._name ='EstiloManualmenteCreado'
			#tamaÃ±o de la fuente
			self._size = 12
			#nombre de la fuente
			self._font = "Verdana"
			#Negrita
			self._bold = False
			#Italica
			self._italic = False
			#margenes en pixels, vertical, derecho e izquierdo respectivamente
			self._marginv = 30
			self._marginr = 30
			self._marginl = 30
			#alineaciÃ³n segun ass (an creo)
			self._align = 2

			#path info #cargando de una figura esto no tiene mucho effect asi que ni siquiera se crean las variables
			self._x_bearing = 0
			self._y_bearing = 0
			self._x_advance = 0
			self._y_advance = 0
			self._ascent = 0
			self._descent = 0
			self._max_x_advance = 0
			self._max_y_advance = 0
			#no necesitados, no los pongo porque si da error es porque hay algo mal en el codiog
			#self._line_height = 0
			#self._width = 0
			if dicc:
				self.FromDict(dicc)#porque al dict le pueden faltar valores
		#estos no son necesarios, se cargan cuando se crea el vector
		#los pongo solo porque ai el ide los toma
		self._height = None
		self._width = None
		self._line_height = None

	def CopyAllFrom(self, other):
		#Esto es importante porque el estilo original de los dialgos se inicia en realidad pasandole un estilo al momento de crearlo
		self.CopyFrom(other)
		#No animables
		self._name = other._name
		self._font = other._font
		self._size  = other._size
		self._bold = other._bold
		self._italic = other._italic
		self._marginv = other._marginv
		self._marginr = other._marginr
		self._marginl = other._marginl
		self._align = other._align
		#self._layer = other._layer # no es necesario

	def CopyFrom(self,  other):
		"""Copia los datos de other objeto del mismo tipo
		@other es un objeto del tipo cProperties

		copia solo los datos animables para hacerlo mÃ¡s rapido.
		"""
		self.pos_x = other.pos_x
		self.pos_y = other.pos_y
		self.org_x = other.org_x
		self.org_y = other.org_y
		self.shad_x = other.shad_x
		self.shad_y = other.shad_y
		self.scale_x = other.scale_x
		self.scale_y = other.scale_y
		self.angle = other.angle
		self.color1.CopyFrom(other.color1)
		self.color4.CopyFrom(other.color4)
		self.color3.CopyFrom(other.color3)
		self.color2.CopyFrom(other.color2)
		self.border = other.border
		self.shadow = other.shadow
		self.mode_fill = other.mode_fill
		self.mode_border = other.mode_border
		self.mode_shadow = other.mode_shadow
		self.mode_particle = other.mode_particle

	def FromDict(self, style):
		"""Crea los valores desde un diccionario, para uso interno"""
		#animables
		self.angle = math.radians(common.SafeGetFloat(style, S_ANGLE))
		self.color1  = extra.cCairoColor(text=style.get(S_PCOLOR, 0))
		self.color3 = extra.cCairoColor(text=style.get(S_OCOLOR, 0))
		self.color4 = extra.cCairoColor(text=style.get(S_BCOLOR, 0))
		self.color2 = extra.cCairoColor(text=style.get(S_SCOLOR, 0))
		self.border = common.SafeGetFloat(style, S_OUTLINE)
		self.shadow = int(common.SafeGetFloat(style, S_SHADOW)) #el zheo me dijo q podia ser flotante pero no tiene sentido aca

		self.scale_x = common.SafeGetFloat(style, S_SCALE_X, 100)/100.0
		self.scale_y = common.SafeGetFloat(style, S_SCALE_Y, 100)/100.0

		#No animables
		self._name = style.get(S_NAME, '')
		self._font = style.get(S_FONT, '')
		self._size = common.SafeGetFloat(style, S_SIZE)
		self._bold = not (style.get(S_BOLD, '0') == '0')
		self._italic = not (style.get(S_ITALIC, '0') == '0')

		self._marginv = int(common.SafeGetFloat(style, S_MARGINV))
		self._marginr = int(common.SafeGetFloat(style, S_MARGINR))
		self._marginl = int(common.SafeGetFloat(style, S_MARGINL))
		self._align = int(common.SafeGetFloat(style, S_ALIGN))

class cSyllable(extra.cVector):
	def __init__(self,  text='', style=None, parent=None, last_pos=None):
		"""
		Una silaba, es mejor dejar que las cree el dialogo porque necesitan una inicializacion especial
		@text text de la silaba
		@style objeto del tipo cProperties
		@parent objeto padre

		para que la silaba se pueda usar luego hay que llamar a CambiarTexto(text, preposicion)
		"""
		extra.cVector.__init__(
			self, text=text, style=style, parent=parent, last_pos=last_pos)
		#self._text = text
		#defaults to [] si its iterable, this is only created if the
		#parameter FxsGroup.split_letters is True
		#or if you call self.SplitLetters
		self._letters = []

	def SplitLetters(self):
		"""Computa los caracteres de la sÃ­laba...
		Usar si cambian el _text
		es muy lento y consume mas ram
		para acceder a las Syllables luego usen _letters
		tambien activar la opcion en FxsGroup.
		"""
		#creamos el array y obtenemos valores comunes
		self._letters = []
		time = self._start
		last = (self.original.pos_x, self.original.pos_y)
		#Si hay chars
		if not self._text:#atrapa '' y None
			self._text = ''
			#para evitar codigo duplicado, de igual manera no deberias llamar a esto sin texto Ã²_Ã³
			cdur = 0.0
		else:
			#calculamos la duracion de cada caracter
			cdur = float(self._dur) / len(self._text)
		#agregamos los caracteres
		for (i, tchar) in enumerate(self._text):
			char = extra.cVector(
				text = tchar, style=self.original, parent=self, last_pos=last)
			char._indice = i
			char._start = time
			char._dur = cdur
			char._end = time = (time + cdur)
			char.effect = self.effect
			last = (char._next_x, char._next_y)
			self._letters.append(char)

	def Chain(self, function, duration=None):
		"""Permite Chain los caracteres a una animacion.
		Antes de llamar a esta funciÃ³n llamen a DivideLetters
		o activen la opcion en FxsGroup
		@function funcion a llamar con cada silaba y el progress
		@duration=None duracion de la animacion de cada caracter,
		Si no se especifica, se usarÃ¡ una duraciÃ³n tal que
		se anime solo un caracter por vez.
		(Nota: no cambien el _text si no quieren inconsistencias)
		"""
		common.Chain(self._dur, self.progress, self._letters, function, duration)

	def FullWiggle(self, amplitude=4, frequency=2, dx=None, dy=None):
		"""el wiggle que queria AbelKM, parte 2
		"""
		#(btw) abelkm expand the doc explaingin this
		if dx is None:
			dx, dy = self.Wiggle(amplitude, frequency)

		o = self.original
		if not hasattr(o, 'old_x'):
			o.old_x = o.pos_x
			o.old_y = o.pos_y
		o.pos_x = o.old_x + dx
		o.pos_y = o.old_y + dy

		for let in self._letters:
			o = let.original
			if not hasattr(o, 'old_x'):
				o.old_x = o.pos_x
				o.old_y = o.pos_y
			o.pos_x = o.old_x + dx
			o.pos_y = o.old_y + dy

class cDialogue(extra.cVector):
	"""Un Dialogo representa una linea de texto,
	Posee herramientas para tomar el texto, cada una de las Syllables del texto y sus tiempos de karaoke.
	Este objeto es el mas complejo, casi imposible que lo crees vos, mejor usar cSilaba o directamente extra.cVector
	"""
	def __init__(self, dialogue, styles, max_effect = 0):
		"""
		@dialogue es la linea de dialogo en forma ass (interno)
		@styles es el array con styles
		opcionales:
		@max_effect numero mÃ¡ximo que puede tomar como effect
		"""
		t_estilo = dialogue[E_STYLE]
		est = styles[0]
		for i in styles:
			if t_estilo == i._name:
				est = i
				break

		estilo = cProperties(est)
		#odio lo asqueroso que se pone ass
		#el or es porque el asqueroso de ass indica el margen por cada linea. PEEEEEEEEEERO si es 0 toma el del estilo ~_~
		estilo._layer = common.SafeGetFloat(dialogue, E_LAYER)	or estilo._layer
		estilo._marginv = common.SafeGetFloat(dialogue, S_MARGINV) or estilo._marginv
		estilo._marginr = common.SafeGetFloat(dialogue, S_MARGINR) or estilo._marginr
		estilo._marginl = common.SafeGetFloat(dialogue, S_MARGINL) or estilo._marginl

		#notar que no le pasamos el texto aun
		extra.cVector.__init__(self, text=None, style=estilo)
		#text=None hace que no cree el path, cuidado! si no llamamos a changeText el path no se creará y dará error!

		#Seteamos los tiempos, traducimos todo a frames
		#guardamos los tiempos como ms para tener mas precisión
		self._start = TimeToMS(dialogue[E_START])
		self._end = TimeToMS(dialogue[E_END])
		self._dur = self._end - self._start

		#Ponemos que effect debe usar
		self.effect = min(max_effect, int(common.SafeGetFloat(dialogue, E_EFFECT)))

		#Cargamos las Syllables (esta funcion setea el _text)
		self.__SetSyllables( dialogue[E_TEXT] )
		#El texto lo sabemos luego de parsear las Syllables
		#self.SetText(self._text)



	def __SetSyllables(self, text):
		"""crea los objetos Syllables de un dialogo,
		codigo tomado del proyecto hermano ZheoFX (C)

		Zheo y Alchemist, grax chicos, son grosos! :D"""
		import re
		"""
		{(?:\\.)* = toma cualkier cosa, esto se hizo por si alguien ponian algun effect y despeus el \k, pues toma el \k y bota el resto
		\\(?:[kK]?[ko]?[kf])  = toma los \k, \kf, \ko y \K
		(\d+) = cualkier digito, en este caso, el tiempo de las \k
		([\\\-a-zA-Z_0-9]*)} = para el inline_fx ({\k20\-0} karaoke)
		(\s*)([^{]*)(\s*) = espacio - cualkier caracter alfanumerico y signos-espacio"""
		#TODO probar con el nuevo regex de alch
		#TODO pensar si conviene que cree un cVector en vez de una silaba (si no trae problemas en los events)
		#si el anterior es cierto : TODO cuando encuentre la sintaxis de una forma en el dialogo que en vez de crear un dialogo lo cree usando la forma

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
		texto = re.sub(r'({[\s\w\d]+})*', '', text) #quita los comentarios o  tags que no comienzen con \
		pattern = r'(?:\\[k]?[K|ko|kf])(\d+)(?:\\[\w\d]+)*(\\-[\w\d]+)*(?:\\[\w\d]+)*}([^\{\}]+)*'
		#pattern = r"{(?:\\.)*\\(?:[kK]?[ko]?[kf])(\d+)([\\\-a-zA-Z_0-9]*)}([^{]*)"#anterior
		info = list(re.findall(pattern, texto))
		plain_text = ''.join([tx for ti, ifx, tx in info])
		if not plain_text:#no se porque hace esto, quizás si no hay {\k} el re no devuelve nada.
			plain_text = re.sub(r'{.*}', '', texto) # lineas (quitando las tags)
		self.SetText(plain_text)
		#Como la pos depende de la alineacion y por ende del tamaÃ±o del texto, solo lo podemos
		#hacer despues de parsear las Syllables
		if self.original.angle:
			#esto tendria que usarse en caso del angle pero no funciona bien (aun)
			#y calculamos el punto 0,0 del dialogo, que es el punto de inicio del texto
			pre = self.matrix.transform_point(0, 0)
		else:
			pre = self.original.pos_x, self.original.pos_y

		self._syllables = []
		tiempo = self._start
		i = 0
		for ti, ifx, tx in info:
			syl = cSyllable(tx, self.original, parent=self, last_pos=pre)
			syl._indice = i
			syl._start = tiempo

			dur = int(ti)*10.0

			syl._dur = dur
			syl._end = tiempo = syl._start + syl._dur

			if len(ifx)>2 :
				try:
					ifx = int(ifx[2:])
				except:
					ifx = None
			else:
				ifx = None
			#Ponemos ifx a none para permitir efectos = 0
			syl.effect = ifx or self.effect
			self._syllables.append(syl)
			i += 1
			pre = syl._next_x, syl._next_y

	def Chain(self, function, duration=None):
		"""Permite encadenar las syllables a una animacion
		@function funcion a llamar con cada silaba y el progress
		@duration=None duracion de la animacion de cada silaba
		Si no se especifica, se usara¡ una duracion tal que
		se anime solo una silaba por vez.
		"""
		common.Chain(self._dur, self.progress, self._syllables, function, duration)

	def FullWiggle(self, amplitude=4, frequency=2):
		"""el wiggle que queria AbelKM"""
		#TODO doc
		dx, dy = self.Wiggle(amplitude, frequency)
		for sil in self._syllables:
			sil.FullWiggle(amplitude, frequency , dx, dy)

class Ass():
	#Esta es la clase que parsea el archivo .ass con suerte no van a necesitar usarlo
	def __init__(self,  file,  max):
		"""Al crear la clase se le puede indicar de que archivo cargar
		@file archivo .ass a cargar
		@max el numero mÃ¡ximo de efectos"""

		if file:
			self.LoadFromFile(file,  max)

	def __pHeader(self,  text):
		#Funcion para parsear un header
		titulo, valor = text.split(':', 1)
		self.info[titulo.strip().lower()] = valor.strip() #el titulo en minuscula lo hace mas compatible

	def __none(self,  text):
		#parseador null
		pass#aguante el pass

	def __v4PStyle(self,  text):
		#parseador del estilo
		titulo,  valor = text.split(':', 1) #el 1 es por las dudas, uno nunca sabe
		titulo = titulo.strip().lower()
		if titulo == S_FORMAT:
			self.formato = [v.strip().lower() for v in valor.split(',')] # si que me gusta hacer codigo complicado, no?
		else: # esto no c hace, asumimos q si no es format es style, pero uno nunca sabe
			valores = [v.strip().lower() for v in valor.split(',')]
			self.styles.append( cProperties(dicc=dict(zip(self.formato,  valores))))

	def __Events(self,  text):
		#parseador de events
		titulo, valor = text.split(':', 1)
		titulo = titulo.strip().lower()
		if titulo == E_FORMAT :
			self.eformato = [v.strip().lower() for v in valor.split(',')]
		elif titulo == E_DIALOG:
			valores_raw = [v.strip() for v in valor.split(',',  len(self.eformato)-1)]
			valores = [v.lower() for v in valores_raw[:-1]]
			valores.append(valores_raw[-1]) #Esto es para q no le pase el texto del dialogo en minusculas

			nuevo_d = dict(zip(self.eformato,  valores))
			nuevo_d[E_EFFECT] = int(common.SafeGetFloat(nuevo_d, E_EFFECT))
			d = cDialogue(nuevo_d, self.styles, self.max_effect)
			d._indice = self.index
			self.dialogues.append(d)
			self.index += 1

	def LoadFromFile(self, file, max):
		#carga un archivo ass
		self.info = {}
		self.styles = []
		self.dialogues = []
		self.index = 0
		self.max_effect = max
		f = codecs.open(file, mode='r', encoding='utf-8')
		parser = self.__none
		for line in f:
			s = line.strip().lower()
			if (s=="") or (s[0] ==";"): #poniendo el s="" al principio nos evitamos error por q sea una linea vacia
				pass # me la soban los comentarios y las lineas en blanco ^_^
			elif s==F_EVENTS: #Pongo los events aca por cuestion d eficiencia, porque gralmente es lo q mas va a haber
				parser = self.__Events
			elif s == F_SINFO:
				parser = self.__pHeader
			elif (s== F_STYLE4P) or (s==F_STYLE4):
				parser = self.__v4PStyle
			else:
				parser(line)
