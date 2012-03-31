# -*- coding: utf-8 -*-
"""This module defines the necessary things to load an ASS file,
and the objects that allow to draw text with cairo"""
import codecs, math
from draw import extra
import common

#Constants, don't change anything if you don't want the program to crash
#From Style
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

#From events (Dialogues)
E_FORMAT ='format'
E_DIALOG = 'dialogue'
E_START = 'start'
E_END = 'end'
E_LAYER = 'layer'
E_STYLE = 'style'
E_TEXT = 'text'
E_EFFECT = 'effect'

#From script ([F]ile)
F_EVENTS = '[events]'
F_SINFO = '[script info]'
F_STYLE4P = '[v4+ styles]' #p for PLUS (like "+")
F_STYLE4 = '[v4 styles]'

#This functions are defined out so they can be used for everyone who uses the module
def TimeToMS(time):
	"""Converts a string from type '0:00:00.00' from ASS to miliseconds in integer"""
	h, m, s = time.split(':')
	s, ms = s.split('.')
	result = int(h) *60 #We assign hours and convert it to minutes
	result += int(m) #Add the minutes
	result *= 60 #Convert it to seconds
	result += int(s) #Add the seconds
	result *= 1000 #Converting to ms
	result += int(ms)*10
	return result #and if there's no strange character around it's all OK


class cProperties():
	def __init__(self, other=None, dicc=None):
		"""There are 3 ways to create a style:
		with nothing, it's done with default values.
		cProperties(other=othercopy) or cProperties(othercopy) copies the values of other
		cProperties(dicc=dictionary) initialize with the values of a ass dictionary"""

		#This ones need to be outside, because if they aren't initialized, in case an instance cProperties is created directly, it will raise an error!!
		self.color1 = extra.cCairoColor(number=0xFFFF2020) #Note that the 0x makes them a real number and not a string. primary color
		self.color2 = extra.cCairoColor(number=0xFF808080) #secondary color
		self.color3 = extra.cCairoColor(number=0xFF101010) #border
		self.color4 = extra.cCairoColor(number=0xFF808080) #shadow
		#colors: primary Secondary Outline Back
		self._layer = 0

		if other:
			self.CopyAllFrom(other)
		else:
			#default values
			#animatable
			#scaling, x and y respectively
			self.scale_x = 1.0
			self.scale_y = 1.0
			#size of border in pixels
			self.border = 3
			#size of shadow in pixels
			self.shadow = 0
			self.angle = 0
			#position of vector (beginning point of vector)
			self.pos_x = 30
			self.pos_y = 30
			#transformation's origin (and some draws)
			self.org_x = 0
			self.org_y = 0
			#displacement of shadow in pixels, in x and y repsectively
			self.shad_x = 0
			self.shad_y = 0
			#drawing modes
			self.mode_fill = 0
			self.mode_border = 0
			self.mode_shadow = 0
			self.mode_particle = 0
			#not animatable
			#style's name
			self._name ='EstiloManualmenteCreado'
			#font size
			self._size = 12
			#font name
			self._font = "Verdana"
			#Bold
			self._bold = False
			#Italic
			self._italic = False
			#margins in pixels, vertical, right and left respectively
			self._marginv = 30
			self._marginr = 30
			self._marginl = 30
			#alignment according to ass (an creo)
			self._align = 2

			#path info #loading a figure, this doesn't have much effect so variables aren't needed
			self._x_bearing = 0
			self._y_bearing = 0
			self._x_advance = 0
			self._y_advance = 0
			self._ascent = 0
			self._descent = 0
			self._max_x_advance = 0
			self._max_y_advance = 0
			#unneeded, I don't put them because if there's an error something should be wrong in coding
			#self._line_height = 0
			#self._width = 0
			if dicc:
				self.FromDict(dicc)#bacause the dict could lack values
		#this aren't needed, loaded when the vector is created
		#there are just there because the ide catch them
		self._height = None
		self._width = None
		self._line_height = None

	def CopyAllFrom(self, other):
		#This is important because the original style from the dialogues intializes giving a style the moment it's created
		self.CopyFrom(other)
		#Not animatable
		self._name = other._name
		self._font = other._font
		self._size  = other._size
		self._bold = other._bold
		self._italic = other._italic
		self._marginv = other._marginv
		self._marginr = other._marginr
		self._marginl = other._marginl
		self._align = other._align
		#self._layer = other._layer # not necessary

	def CopyFrom(self,  other):
		"""Copies the data of another object from the same type
		@other it's an object of cProperties type

		only the animatable data is copied, it makes them faster that way.
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
		"""Creates the values from a dictionary for internal use"""
		#animatable
		self.angle = math.radians(common.SafeGetFloat(style, S_ANGLE))
		self.color1  = extra.cCairoColor(text=style.get(S_PCOLOR, 0))
		self.color3 = extra.cCairoColor(text=style.get(S_OCOLOR, 0))
		self.color4 = extra.cCairoColor(text=style.get(S_BCOLOR, 0))
		self.color2 = extra.cCairoColor(text=style.get(S_SCOLOR, 0))
		self.border = common.SafeGetFloat(style, S_OUTLINE)
		self.shadow = int(common.SafeGetFloat(style, S_SHADOW)) #zheo told me that it could be float but it doesn't make sense here

		self.scale_x = common.SafeGetFloat(style, S_SCALE_X, 100)/100.0
		self.scale_y = common.SafeGetFloat(style, S_SCALE_Y, 100)/100.0

		#Not animatable
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
		A syllable. It's better that the dialogue creates them because they need a special initialization.
		To use the syllable later we must call changeText(text, preposition)

		:param text: syllable's text
		:param style: Style of the syllable
		:param parent: Parent object
		:type text: string
		:type style: :class:`cProperties`
		:type parent: :class:`cDialogue`
		"""
		extra.cVector.__init__(
			self, text=text, style=style, parent=parent, last_pos=last_pos)
		#self._text = text
		#defaults to [] if its iterable, this is only created if the
		#parameter FxsGroup.split_letters is True
		#or if you call self.SplitLetters
		self._letters = []

	def SplitLetters(self):
		"""Computes the characters of the syllable...
		Use if you change __text
		it's slow and eats more ram
		to access the Syllables use _letters later
		and activate the option in FxsGroup, too.
		"""
		#we create the array and get common values
		self._letters = []
		time = self._start
		last = (self.original.pos_x, self.original.pos_y)
		#If there are chars
		if not self._text:#catchs '' and None
			self._text = ''
			#to avoide duplicated code, even though you shouldn't call this function without text Ã²_Ã³
			cdur = 0.0
		else:
			#calculation of each character's duration
			cdur = float(self._dur) / len(self._text)
		#adding the characters
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
		"""Allows to Chain the characters to a animation.
		Before calling this function call DivideLetters
		or enable the option in FxsGroup
		@function function that will be called for each syllable and the progress
		@duration=None duration of the animatio of each character
		If not specified, a duration that animates one character per time will be used.
		(Note: do not change _text if you don't want inconsistencies)
		"""
		common.Chain(self._dur, self.progress, self._letters, function, duration)

	def FullWiggle(self, amplitude=4, frequency=2, dx=None, dy=None):
		"""the wiggle that AbelKM wanted, part 2
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
	"""A Dialogue represents a text line,
	This takes the text, each Syllable of the text and it's karaoke times.
	This object is the most complex one, almost imposible for you to create, better use cSyllable or directly extra.cVector
	"""
	def __init__(self, dialogue, styles, max_effect = 0):
		"""
		@dialogue the dialogue line in ASS form (inner)
		@styles array with styles
		optionals:
		@max_effect maximum number that can take as effect
		"""
		t_estilo = dialogue[E_STYLE]
		est = styles[0]
		for i in styles:
			if t_estilo == i._name:
				est = i
				break

		estilo = cProperties(est)
		#I hate how aweful can become ass 
		#the "or" is because the scumbag ass indicates the margin for each line. BUUUUUT if it's 0 it takes the style ~_~
		estilo._layer = common.SafeGetFloat(dialogue, E_LAYER)	or estilo._layer
		estilo._marginv = common.SafeGetFloat(dialogue, S_MARGINV) or estilo._marginv
		estilo._marginr = common.SafeGetFloat(dialogue, S_MARGINR) or estilo._marginr
		estilo._marginl = common.SafeGetFloat(dialogue, S_MARGINL) or estilo._marginl

		#note that we haven't given the text yet
		extra.cVector.__init__(self, text=None, style=estilo)
		#text=None this way the path won't be created, attention! if we don't call changeText the path won't be created and it will raise an error!

		#Setting times, translating all to frames
		#we sabe the times as ms for better accuracy
		self._start = TimeToMS(dialogue[E_START])
		self._end = TimeToMS(dialogue[E_END])
		self._dur = self._end - self._start

		#Setting the effect to use
		self.effect = min(max_effect, int(common.SafeGetFloat(dialogue, E_EFFECT)))

		#Loading Syllables (this function sets the _text)
		self.__SetSyllables( dialogue[E_TEXT] )
		#We know the text after parsing the Syllables
		#self.SetText(self._text)



	def __SetSyllables(self, text):
		"""Creats the objects Syllables from a dialogue,
		code was taken from ZheoFX (C) brother project

		Zheo y Alchemist, thanks guys, you're awesome! :D"""
		import re
		"""
		{(?:\\.)* = takes anything, this was made so if someone put some effect and \k after it, it takes the \k and drops the rest
		\\(?:[kK]?[ko]?[kf])  = takes \k, \kf, \ko and \K
		(\d+) = any digit, in this case, \k timming
		([\\\-a-zA-Z_0-9]*)} = for inline_fx ({\k20\-0} karaoke)
		(\s*)([^{]*)(\s*) = space - any alphanumeric character and signs-space"""
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
		texto = re.sub(r'({[\s\w\d]+})*', '', text) #removes comments and tags that don't begin with \
		pattern = r'(?:\\[k]?[K|ko|kf])(\d+)(?:\\[\w\d]+)*(\\-[\w\d]+)*(?:\\[\w\d]+)*}([^\{\}]+)*'
		#pattern = r"{(?:\\.)*\\(?:[kK]?[ko]?[kf])(\d+)([\\\-a-zA-Z_0-9]*)}([^{]*)"#previous
		info = list(re.findall(pattern, texto))
		plain_text = ''.join([tx for ti, ifx, tx in info])
		if not plain_text:#I don't know why it does this, maybe if there isn't {\k}, re doesn't return anything.
			plain_text = re.sub(r'{.*}', '', texto) # lines (removing tags)
		self.SetText(plain_text)
		#Since pos depends of the alignment and hence of the text's size, we can only
		#do it after parsing the Syllables
		if self.original.angle:
			#this should be used in case of the angle, but it doesn't work good (yet)
			#calculating point 0,0 of dialogue, the text's beginning point
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
			#ifx=None to allow effects = 0
			syl.effect = ifx or self.effect
			self._syllables.append(syl)
			i += 1
			pre = syl._next_x, syl._next_y

	def Chain(self, function, duration=None):
		"""
		Allows to chain the Syllables to a animationn

		:param function: function to call for each syllable and the progress
		:param duraton:
			duration of the animation of each syllable
			If not specified, a duration that animates
			one syllable per time will be used.
		:type function: `method`
		:type duration: int milliseconds

		"""
		common.Chain(self._dur, self.progress, self._syllables, function, duration)

	def FullWiggle(self, amplitude=4, frequency=2):
		"""el wiggle que queria AbelKM"""
		#TODO doc
		dx, dy = self.Wiggle(amplitude, frequency)
		for sil in self._syllables:
			sil.FullWiggle(amplitude, frequency , dx, dy)

class Ass():
	"""This class parses the .ass file, luckily you won't need to use it"""
	def __init__(self,  file,  max):
		"""When initialized, the file to load can be specified
		@file .ass file to load
		@max maximum number of effects"""

		if file:
			self.LoadFromFile(file,  max)

	def __pHeader(self,  text):
		"""Function to parse a header"""
		titulo, valor = text.split(':', 1)
		self.info[titulo.strip().lower()] = valor.strip() #the title in lower case makes it more compatible

	def __none(self,  text):
		"""null parseator"""
		pass#pass rules

	def __v4PStyle(self,  text):
		"""style parseator"""
		titulo,  valor = text.split(':', 1) #the 1 is just in case, one never knows
		titulo = titulo.strip().lower()
		if titulo == S_FORMAT:
			self.formato = [v.strip().lower() for v in valor.split(',')] # si que me gusta hacer codigo complicado, no?
		else: # this shouldn't be done, we asume that it's not format and it's style, but one never knows
			valores = [v.strip().lower() for v in valor.split(',')]
			self.styles.append( cProperties(dicc=dict(zip(self.formato,  valores))))

	def __Events(self,  text):
		"""event parseator"""
		titulo, valor = text.split(':', 1)
		titulo = titulo.strip().lower()
		if titulo == E_FORMAT :
			self.eformato = [v.strip().lower() for v in valor.split(',')]
		elif titulo == E_DIALOG:
			valores_raw = [v.strip() for v in valor.split(',',  len(self.eformato)-1)]
			valores = [v.lower() for v in valores_raw[:-1]]
			valores.append(valores_raw[-1]) #The text won't be given in lower case this way

			nuevo_d = dict(zip(self.eformato,  valores))
			nuevo_d[E_EFFECT] = int(common.SafeGetFloat(nuevo_d, E_EFFECT))
			d = cDialogue(nuevo_d, self.styles, self.max_effect)
			d._indice = self.index
			self.dialogues.append(d)
			self.index += 1

	def LoadFromFile(self, file, max):
		"""Loading a ass file"""
		self.info = {}
		self.styles = []
		self.dialogues = []
		self.index = 0
		self.max_effect = max
		f = codecs.open(file, mode='r', encoding='utf-8')
		parser = self.__none
		for line in f:
			s = line.strip().lower()
			if (s=="") or (s[0] ==";"): #with s="" we avoid errors if it's an empty line
				pass # me la soban los comentarios y las lineas en blanco ^_^
			elif s==F_EVENTS: #The events go here because it's more efficient, generally there will be lot of them
				parser = self.__Events
			elif s == F_SINFO:
				parser = self.__pHeader
			elif (s== F_STYLE4P) or (s==F_STYLE4):
				parser = self.__v4PStyle
			else:
				parser(line)
