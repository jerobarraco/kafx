# -*- coding: utf-8 -*-
"""
.. module:: libs.draw.extra
	:platform: Unix, Windows
	:synopsis:
		This module contains useful functions on which other drawing functions depend.
.. moduleauthor:: Kafx team http://kafx.com.ar
"""

from math import ceil
from random import random
import itertools

import cairo
from libs import video, common
import basic, advanced


global debugi
debugi=-1

def DebugCairo(folder="caps/"):
	#Todo docstring (explain)
	global debugi
	debugi+=1
	video.cf.ctx.get_group_target().write_to_png(folder+str(debugi).zfill(5)+'.png')

def LoadSequence(folder, count, digits=3, extend=cairo.EXTEND_NONE):
	"""Loads a set of textures
	@folder : folder containing the images
	if there's a common prefix you can include it,
	use '/'

	@count : image count [0 -> count-1]

	@digits: number of digits used

	@extend: texture's extend (default EXTEND_NONE)
			if used with cSprite extend must be set to cairo.EXTEND_NONE
	"""
	#this is the short way
	#it's called list comprehension
	return [
		LoadTexture(folder + str(i).zfill(digits) + '.png', extend)
		for i in range(count)
		]

	#Explanation
	"""
	#textures array
	textures = []
	for i in range (count):
		#we'll create the filename using the number
		#to string and then filled with 0s to match digits
		num = str(i).zfill(digits)
		imgname = folder + num + '.png'
		text = LoadTexture(imgname, extend)
		textures.append(text)
	return textures"""

def LoadTexture(filename, extend=cairo.EXTEND_REPEAT):
	"""Returns a cairo texture (`cairo.SurfacePattern`) using a png filename
	Used in set_source or whatever
	@filename: png filename

	@extend: texture's extend (default `cairo.EXTEND_REPEAT`)
			if used with cSprite extend MUST be set to `cairo.EXTEND_NONE`
	"""
	t = cairo.SurfacePattern(cairo.ImageSurface.create_from_png(filename))
	t.set_extend(extend)
	return t

def MoveTexture(pattern, x, y, org_x=0.0, org_y=0.0, angle=0.0, scale_x=1.0, scale_y=1.0):
	"""Moves, rotates and scales a texture loaded with LoadTexture, or any other cairo pattern"""
	pattern.set_matrix(CreateMatrix(x, y, org_x, org_y, angle, scale_x, scale_y, True))

def SetStyle(style):
	"""Prepares cairo with the styles
	Before drawing any text you can call this function to set up the basic stuff
	the style type has to be :class:`libs.asslib.cProperties`
	"""
	ctx = video.cf.ctx
	ctx.select_font_face(style._font, int(style._italic),  int(style._bold))
	ctx.set_font_size(style._size)

def CreateMatrix(pos_x=0, pos_y=0, org_x=0, org_y=0, angle=0, scale_x=1, scale_y=1, inverse=False):
	"""Creates a matrix with standard transforms
	pos_x, pos_y: x/y final position
	org_x, org_y: origin for the transform
	angle: (radians)
	scale_x scale_y: obvious, ain't it?
	inverse = False inverse matrices or not
	scales must be inverted if matrix is inverse: scale=1.0/scale"""
	m = cairo.Matrix()

	#dividing by 0 isn't a nice thing to do
	if not scale_x: scale_x = 0.00001
	if not scale_y: scale_y = 0.00001

	if inverse:
		#UNTESTED
		#position origin is not the same as the origin here and it's always in the baseline,
		#that's why we gotta move it to the origin point
		m.translate(org_x, org_y)
		m.rotate(angle)
		m.scale(scale_x, scale_y)
		m.translate(-pos_x, -pos_y)
	else:
		#fixing this was a week's worth of work and even some mails to cairo list
		#when typing "it seems the rotation is applied _after_ the translation"
		#I thought about inverse matrices and maybe that was inverted too
		#remember: read the docs and always think things through
		m.translate(pos_x, pos_y)
		m.scale(scale_x, scale_y)
		m.rotate(-angle)
		m.translate(-org_x, -org_y)
	return m

#Clases
class cCairoColor():
	"""Class for solid colors"""
	def __init__(self, number=None, text='', ccolor=None, components=None):
		"""
		4 independent ways to initialize
		If no argument is given the resultant is White
		@number through FromNumber, receives an integer (0xAARRGGBB)
		@texto through FromText, receives a string ('AARRGGBB')
		@ccolor through CopyFrom, receives a cCairoColor object
		"""
		if number is not None: #0 doesn't return false
			self.FromNumber(number)
		elif text:
			self.FromText(text)
		elif ccolor:
			self.CopyFrom(ccolor)
		elif components:
			self.a , self.r, self.g, self.b = components
		else:
			self.r= self.g= self.b= self.a=1.0

	def Pattern(self):
		"""Returns a cairo patter for usage in functions  receiving one
		you can also use video.cf.ctx.set_source_rgba(a.r, a.g, a.b, a.a) directly
        but this syntax is way better, right?"""
		return cairo.SolidPattern(self.r, self.g, self.b, self.a)

	def FromText(self, color):
		"""Creates a color from another
		color may be either '&HAARRGGBB' or 'AARRGGBB'
		"""
		if color[0]=='&':
			color = color[1:]
		if color[0].lower()=='h':
			color = color[1:]

		color.zfill(8)#0-fill
		self.a = (255-ord(color[:2].decode('hex')))/255.0 #alpha,
		self.b = ord(color[2:4].decode('hex'))/255.0 #blue
		self.g = ord(color[4:6].decode('hex'))/255.0 #green and shift
		self.r = ord(color[6:8].decode('hex'))/255.0 #red and shift

	def FromNumber(self,  color):
		"""Creates a color from another
		color is an integer: 31238231 or 0xAARRGGBB"""
		self.b = (color & 0xFF) /255.0 #and-mask to take 8-bit chunk
		color >>= 8 #8-bit shift
		self.g = (color & 0xFF) /255.0 #same here
		color >>= 8
		self.r = (color & 0xFF) /255.0
		color >>= 8
		self.a = color /255.0
		"""
		self.b = (color % 256)/255.0
		color = color / 256
		self.g = (color % 256)/255.0
		color = color /256
		self.r = (color % 256.0)/255.0
		color = color / 256
		self.a = color / 255.0"""

	def CopyFrom(self, other):
		"""Copies a color
		@other is a cCairoColor object"""
		self.r=other.r
		self.g=other.g
		self.b=other.b
		self.a=other.a

	def Interpolate(self, progress, other, inter=common.i_lineal):
		"""Linear interpolation of two colors

		@progress : [0,1] interpolation factor/ratio
		    - 0 means the first color, 1 the second color
		@other : second color
		"""
		i = common.Interpolate
		self.r = i(progress, self.r, other.r, inter)
		self.g = i(progress, self.g, other.g, inter)
		self.b = i(progress, self.b, other.b, inter)
		self.a = i(progress, self.a, other.a, inter)

class cVector():
	"""Base cairo object class includes drawing utils for cairo
	it may be instanced @text or @figure or using the setters afterwards
	"""
	#This is the same as in basic.sources, also defined here.
	P_SOLID = 0
	P_TEXTURE = 1
	P_DEG_VERT = 2
	P_DEG_HOR = 3
	P_DEG_DIAG = 4
	P_DEG_RAD = 5
	P_AN_DEG_LIN = 6
	P_AN_DEG_RAD = 7
	P_COLORED_PATTERN = 8
	PART_BORDER = 0
	PART_FILL = 1
	PART_SHADOW = 2
	PART_PARTICLE = 3

	def __init__(self, text='', style=None, figure=None, parent=None, last_pos = None):
		"""Parameters
		@style cProperties object to inherit from
		@text creates an object from text
		@figure from ass shape
		@parent parent object
		"""
		from libs import asslib #must import it here
		#initialize vector components
		self.progress = 0.0
		self._end = 0
		self._start = 0
		self._dur = 0
		self._indice = 0
		self._parent = parent
		self._next_x = 0
		self._next_y = 0
		self.effect = 0
		self.textures = [None, None, None, None] #border, fill, shadow, particles
		#vector transform matrix

		self.original = asslib.cProperties(style)
		self.actual = asslib.cProperties(style)
		self.matrix = None
		self._UpdateMatrix()

		self._text = ""
		self.pointsw = None
		self._old_path = self.path = None
		#pattern used in PaintWithCache, you can assign None if you wanna delete this, never use "del _pat"
		self._pat_cache = None
		if figure :
			self.CreateFromFigure(figure)
		elif text is not None:
			self.SetText(text, last_pos=last_pos)
	#end def

	def _SetTextVertPos(self):
		"""Updates vertical align from the ass align
		it is recommended to use _SetTextProps instead
		"""
		props = self.original
		vert = ceil(props._align/3.0) # 1=bottom, 2=mid, 3=top
		if vert == 1 : #bottom
			props.pos_y = video.vi.height - props._marginv #- props._descent
		elif vert == 2: #middle
			props.pos_y = (video.vi.height - props._line_height )/2 #- props._descent
		else: #top
			props.pos_y = props._marginv -props._y_bearing #+ props._line_height #- props._y_bearing
		return

	def _SetTextHorizPos(self):
		"""Updates horizontal align from the ass align
		it is recommended to use _SetTextProps instead
		 1=bottom, 2=mid, 3=top
		"""
		props = self.original
		horiz = props._align % 3 #1 = left, 2 mid, 0 right

		if horiz == 1:
			props.pos_x = props._marginl
		elif horiz == 2:
			props.pos_x = ((video.vi.width - props._width) / 2.0)
		else:
			props.pos_x = video.vi.width - props._width - props._marginr
		return
		"""if props.angle and not self._parent:
				props.pos_x, props.pos_y = self.matrix.transform_distance(props.pos_x, props.pos_y)"""

	def _SetTextProps(self, lasts=None):
		"""Sets properties according to text
		used when the text is created
		(usually position and size)
		@lasts -> coordinates for the text to start
		@return -> coordinates for the next text [[TO-DO] - Check this stuff, it doesn't make much sense]

		"""
		ctx = video.cf.ctx
		props = self.original
		SetStyle(props)

		props._x_bearing, props._y_bearing, props._width, props._height, props._x_advance, props._y_advance = ctx.text_extents(self._text)
		props._ascent, props._descent, props._line_height, props._max_x_advance, props._max_y_advance = ctx.font_extents()

		if lasts:
			props.pos_x = lasts[0]
			props.pos_y = lasts[1]
		else:
			self._SetTextHorizPos()
			self._SetTextVertPos()

		if self._parent and props.angle:
			#workaround, we don't alter the dialogue using this
			#fixes some trouble with the origin
			props.org_x = 0
			props.org_y = 0
			#self._UpdateMatrix()
			#this calculates x_advance and y_advance from the syllable matrix
			#this may cause problems if there are different transforms for syllable and dialogue
			#we could use self._parent.matrix too
			props._x_advance, props._y_advance = self._parent.matrix.transform_distance(props._x_advance, props._y_advance)
		else:
			props.org_x = (props._width/2.0)
			props.org_y = -(props._line_height/2.0) + props._descent

		self.actual.CopyAllFrom(props)
		self._next_x = props.pos_x + props._x_advance
		self._next_y = props.pos_y + props._y_advance

	def _SetPathProps(self):
		"""Sets props for the path
		it must be the active path
		"""
		o = self.original
		e = video.cf.ctx.path_extents()#x1,y2,x2,y2
		o._width = e[2]-e[0]
		o._height  = o._line_height = (e[3]-e[1])
		#descent is pretty much like e[1]
		o._x_bearing = e[0]
		o._y_bearing = e[1]

		o.org_x = o._x_bearing + (o._width/2.0)
		o.org_y = -(o._height/2.0)
		self.actual.CopyAllFrom(o)

	def GetShape(self):
		"""
		Creates a string like 'm 13 13 13 31 b 31 31 13 31' used in ass subs
		this is for zheo, ass sucks, don't use it, seriously, do NEVER use it,
		just for you to know a little bit more about ass and useless stuff
		"""
		#toma los puntos del path
		#See UpdateTextPath too, it uses ctx.copy_path
		figura = ''
		lp = '' # last point, vsfilter's fault
		mapa = ['m ', 'l ', 'b ', 'c ']
		"""esta es la correspondencia (aproximada) entre el tipo de punto de cairo y el tipo en ass
			teniendo en cuenta que
			move_to = 0 = 'm'
			line_to = 1 = 'l'
			curve_to = 2 = 'b' #o 's'
			close_path = 3 = 'c'
		"""

		if self._old_path:#if path not created
			for t, p in self._old_path:
				figura += lp #ignoring the last point
				if t < 3:
					lp = mapa[t] #adding the point type
					for coord in p:
						lp += str(int(round(coord))) + ' '
					mapa[0] = 'n '
				else:
					lp = ''
					mapa[0] = 'm '
			figura += " c"
		return figura


	def CreateFromFigure(self, ass):
		"""SLOW - vector from ass shape"""
		arr = ass.lower().split(' ')
		ctx = video.cf.ctx
		ctx_funcs = ( #mapping types to functions
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to,
			ctx.close_path
		)

		def get(a, i):
			#this function returns an array with the ammount of items in i, all parsed as float, if there aren't enough items in a, then it fills with 0
			return [ float(a.pop(0) if a else 0.0) for x in xrange(i)]

		ctx.new_path()
		t='m'
		while arr:
			if arr[0] in 'mnlbsc':
				t = arr.pop(0)
			if (t =='m') or (t=='n'):
				ctx_funcs[3]()
				ctx_funcs[0](*get(arr , 2))
			elif t == 'l':
				ctx_funcs[1](*get(arr , 2))
			elif (t=='b') or (t=='s'):
				ctx_funcs[2](*get(arr , 6))
			"""best management using
			elif t == 'c':
				ctx_funcs[3]()"""
		ctx_funcs[3]()

		self._old_path = self.path = ctx.copy_path() #setProperties resets this
		self._SetPathProps()

	def _UpdateMatrix(self):
		#updates the transformation matrix for the vector with the current style
		a = self.actual
		self.matrix = CreateMatrix(a.pos_x+a.org_x, a.pos_y-a.org_y, a.org_x, a.org_y, a.angle, a.scale_x, a.scale_y, False)

	def _UpdateTextPath(self):
		#Creates the path from a text, the style must be already set, position is ignored
		SetStyle(self.original)
		ctx = video.cf.ctx
		ctx.new_path()
		ctx.text_path(self._text)
		self._old_path = self.path = ctx.copy_path()

	def SetText(self, text, last_pos=None):
		"""SLOW:
		Changes the text asociated to a vector
		@text used text
		It'll use the original properties but re-calculating position and stuff
		optional:
		@last_pos=None (x,y) coordinates of the last syllable"""
		self._text = text
		self._SetTextProps(last_pos)
		self._UpdateTextPath()

	def Deform(self, func):
		"""Deforms vector object
		@func is a function called once for each point group in the vector, receives the following params:
		self : Dialog you want to Deform
		tipo : Integer indicating the point type (0=move, 1=line, 2=curve, 3=close (from some cairo stuff))
		points : coordinates array
		returns a modified points array
		"""
		ctx = video.cf.ctx
		ctx_funcs = ( #This maps the item types to their functions, everything else is manual.
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to
		)
		ctx.new_path()
		for t, p in self._old_path:
			if t<3:
				p = func(self, t, p)
				ctx_funcs[t](*p)
			else:
				ctx.close_path()
		self.path = ctx.copy_path()

	def CompleteDeform(self, func):
		"""Like Deform but it only receives an object, it's expected to return just a coordinates array
		This leads to better control of the points
		"""
		ctx = video.cf.ctx
		ctx_funcs = (
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to
		)
		ctx.new_path()

		for t, p in func(self, self._old_path):
			if t<3:
				ctx_funcs[t](*p)
			else:
				ctx.close_path()
		self.path = ctx.copy_path()

	def __GroupPath(self, path): #check ok
		#Check blank-path stuff
		gpath = []
		thispath = []
		if not path: return [ [(1, (0.0, 0.0))] ]
		for i in path:
			if i[0]==3:
				if thispath:
					gpath.append(thispath)
					thispath = []
			else:
				thispath.append(i)
		if thispath:
			gpath.append(thispath)

		return gpath

	def __NormalizePath(self, fg, tg):
		lastfp = fg[0]
		lasttp = tg[0]
		fromg = []
		tog = []
		for fp , tp in itertools.izip_longest(fg, tg, fillvalue=None):
			#i could use the fact that lists are mutable, but that would make my code obscure
			if not fp :
				fp = lastfp[:]
			if not tp :
				tp = lasttp[:]

			#the type
			tfp, ttp = fp[0], tp[0]
			if (tfp ==2) or (ttp==2):
				#each type is managed diferently
				if tfp<2:
					fpp = fp[1]
					#we recreate thepoint, the first coord (two values) is the last coord of the last point (can be bezier or line_to)
					fp = (2, (lastfp[1][-2], lastfp[1][-1],fpp[0], fpp[1], fpp[0], fpp[1]))
				elif ttp<2:
					tpp = tp[1]
					#we recreate thepoint, the first coord (two values) is the last coord of the last point (can be bezier or line_to)
					tp = (2, (lasttp[1][-2], lasttp[1][-1], tpp[0], tpp[1], tpp[0], tpp[1]))
				#else both are 2
			fromg.append(fp)
			tog.append(tp)

			lastfp = fp
			lasttp = tp
		return fromg, tog

	def __NormalizePathGroups(self, a, b): #check ok
		lastf = a[0][:] #first group
		lastt = b[0][:] #first group
		frompg= []
		topg = []
		for fg, tg in itertools.izip_longest(a, b, fillvalue=None):
			#if there's no points we take the last one
			if not fg :
				fg = lastf[:]
				a.append(lastf)
			if not tg :
				tg = lastt[:]
				b.append(lastf)

			lastf, lastt = self.__NormalizePath(fg, tg)
			frompg.append(lastf)
			topg.append(lastt)
		return frompg, topg

	def __FlattenPathGroup(self, path): #check ok
		for g in path:
			g.append((3, ()))#a close in each group
			#beware of tuples as parameters
		return tuple(itertools.chain.from_iterable(path))

	def __CreateDiffPath(self, other): #Check ok
		#as cairo's vectors are way more complicated I need to format both
		#if we keep the less complicated of the two we may lose information, so... we use the other one
		fgp = self.__GroupPath(self._old_path)
		tgp = self.__GroupPath(other.path)
		#first we gotta normalize the groups, we need the same number of them
		fgp, tgp = self.__NormalizePathGroups(fgp, tgp)

		self.__from_path = self.__FlattenPathGroup( fgp)

		self.__to_path = self.__FlattenPathGroup( tgp)

	def Morph(self, other):
		if not self._text : return
		if not hasattr(self, "__from_path"):
			self.__CreateDiffPath(other)

		ctx = video.cf.ctx
		ctx_funcs = (
			ctx.move_to,
			ctx.line_to,
			ctx.curve_to
		)
		ctx.new_path()
		for fcom, tcom, x in zip(self.__from_path, self.__to_path, itertools.count(1)):
			t = fcom[0]
			fpoints = fcom[1]
			tpoints = tcom[1]
			if t<3:
				p = [common.LERP(self.progress, i, j) for i, j in zip(fpoints, tpoints)]
				ctx_funcs[t](*p)
			else:
				ctx.close_path()
		self.path = ctx.copy_path()

	def Restore(self):
		"""Restores a vector's style"""
		self.actual.CopyFrom(self.original)
		self.path = self._old_path

	def PaintWithCache(self, background=False, matrix=None):
		"""Uses cache to draw a vector.
		It's only created the first time you call it, it uses the cache afterwards
		optional
		@background=False Boolean, decides if the text receives the background
		@matrix=None transform matrix for EndGroup
		"""
		if self._pat_cache :
			ctx = video.cf.ctx
			ctx.set_source(self._pat_cache)
			ctx.paint()
		else:
			self._pat_cache = self.Paint(background, matrix)
		return self._pat_cache

	def DeleteCache(self):
		#Deletes the cache, simple and useful
		self._pat_cache = None

	def Paint(self, background=False, matrix=None, matrix2=None):
		"""Draws a vector using current style.
		optional:
		@background=False Boolean, decides if the text receives the background
		@matrix=None -vector's- transform matrix
		@matrix2=None transform matrix for EndGroup
		"""
		a = self.actual
		ctx = video.cf.ctx
		#new group for the shadow
		advanced.StartGroup(background)

		if matrix:
			#this enables transform matrix use
			#not nice though
			self.matrix = matrix
		else:
			#otherwise, we use one created from animatable properties
			self._UpdateMatrix()

		ctx.set_matrix(self.matrix)
		#ctx.transform existes, but I think that multiplies the matrices, so... the error propagates
		ctx.new_path()
		ctx.append_path(self.path)
		#border
		if a.border:
			#if there IS a border we do everything (this actually speeds things up if you want NO outlines
			ctx.set_line_width(a.border)
			#this applies the texture/source selected
			basic.sources[a.mode_border](self, a.color3, 0)
			ctx.stroke_preserve()

		#fill
		basic.sources[a.mode_fill](self, a.color1, 1)
		ctx.fill()

		#end group and apply 2nd matrix
		#it is applied after the pattern
		#is rasterized, so there might be some trouble
		pat = advanced.EndGroup(0.0, matrix2)

		#shadow, before loading the initial matrix
		basic.sources[a.mode_shadow](self, a.color4, 2)

		#returns the pattern with the shadow
		pat =  advanced.Shadow(pat, a.shadow, a.shad_x, a.shad_y)
		ctx.identity_matrix()
		return pat

	def PaintReference(self, matrix=None):
		"""Draws the vector reference points, note that some transforms may not be possible"""
		ctx = video.cf.ctx
		if matrix:
			self.matrix = matrix
		else:
			self._UpdateMatrix()
		ctx.set_matrix(self.matrix)
		ctx.rectangle(*self.Box())
		#position
		"""x1, y1, x2, y2 = self.Box()
		#obtenemos los valores de ancho y alto
		x2 -= x1
		y2 -= y1
		ctx.rectangle(x1, y1, x2, y2)"""
		ctx.set_source_rgba(1,0,1,1)
		ctx.stroke()

		ctx.arc(0,0, 4, 0, 6.283)#posx, posy and text baseline
		ctx.set_source_rgba(0,1,0,1)
		ctx.fill()

		#origin
		ctx.set_source_rgba(0,1,1, 1)
		a = self.actual
		ctx.arc(a.org_x, a.org_y, 3, 0, 6.283)
		#ctx.arc(self.actual.pos_x, self.actual.pos_y, 4, 0, 6.283)
		ctx.fill()
		ctx.identity_matrix ()

	def Box(self):
		"""Returns the bounding box with 4 components (x,y, width, height), values
		relative to vector's 0,0 point (baseline). Not valid for deformed paths,
		in that case you should use ctx.path_extents
		"""
		o= self.original
		bord= self.actual.border
		#compatible with cairo's rectangle
		return (-o._x_bearing-bord, -o._height-bord, o._x_bearing+o._width+(bord*2), o._height+o._descent+(bord*2))
		#do -NOT- forget it's x, y, width, height

	def Center(self):
		"""Returns a vector's center"""
		"""o = self.original
		x = o._width/2.0
		props.org_y = -(props._line_height/2.0) + props._descent"""
		x = self.actual.pos_x +(self.original._width/2.0)
		y = self.actual.pos_y -(self.original._height/2.0)
		return (x, y) #I may change this to the way it is for Box

	def Move(self, from_, to, inter=common.i_lineal):
		"""Animates a movement from the from_ position till to position
		@from_ (x,y)
		@to (x,y)
		"""
		self.actual.pos_x = common.Interpolate(self.progress, from_[0], to[0], inter)
		self.actual.pos_y = common.Interpolate(self.progress, from_[1], to[1], inter)

	def MoveTo(self, dx, dy, inter=common.i_lineal):
		"""Animates movement back to the original position -CHECK THIS-
		@dx, dy position relative to origin
		"""
		org = self.original
		px = org.pos_x
		py = org.pos_y
		self.Move( (px, py), (dx+px, dy+py), inter)

	def MoveFrom(self, dx, dy, inter=common.i_lineal):
		"""Animates the movement of a vector to the given point from its original position
		@dx, dy final position
		"""
		org = self.original
		px = org.pos_x
		py = org.pos_y
		self.Move((px+dx, py+dy), (px, py), inter)

	def Fade(self, from_, to, inter=common.i_lineal):
		"""Animated fade of a vector
		@from_ float for initial value
		@to float for final value
		both of them [0-1]
		"""
		self.Alpha(common.Interpolate(self.progress, from_, to, inter))

	def Alpha(self, alpha):
		"""Specifies alpha, for all colors
		@alpha float value for alpha channel, [0-1]
		"""
		self.actual.color1.a = self.actual.color2.a = self.actual.color3.a = self.actual.color4.a = alpha

	def Rotate(self, from_, to, inter=common.i_lineal):
		"""Animates vector rotation
		@from_ initial angle, radians
		@to final angle, radians
		"""
		self.actual.angle = common.Interpolate(self.progress, from_, to, inter)

	def Scale(self, from_, to_, inter=common.i_lineal):
		"""Animates vector scaling
		@from_ initial scale
		@to_ final scale
		both of them are float, 1 is default, natural scale; >1 is bigger; <1 is smaller
		"""
		self.actual.scale_x = self.actual.scale_y = common.Interpolate(self.progress, from_, to_, inter)

	def Shake(self, amplitude=4):
		"""
		Creates a shake from the position
		@amplitude of the movement in pixels
		"""
		self.actual.pos_x = self.original.pos_x + common.Interpolate(self.progress, -amplitude, amplitude, common.i_rand)
		self.actual.pos_y = self.original.pos_y +common.Interpolate(self.progress, -amplitude, amplitude, common.i_rand)

	def Wiggle(self, amplitude=4, frequency=2):
		"""
		Movement between random points
		@amplitude of the movement in pixels
		@frequency number of points
		"""
		if self.pointsw is None:
			self.pointsw = []
			self.pointsw.append( (0, 0) )
			for i in range(frequency):
				randomx = common.LERP(random(), -amplitude, amplitude)
				randomy = common.LERP(random(), -amplitude, amplitude)
				self.pointsw.append( (randomx, randomy) )
				self.pointsw.append( (0, 0) )
		x, y = common.RanmaBezier(self.progress, self.pointsw)
		self.actual.pos_x = self.original.pos_x +x
		self.actual.pos_y = self.original.pos_y +y
		return x, y

	def LoadTexture(self, filename, part=PART_BORDER, extend=cairo.EXTEND_REPEAT):
		"""This loads texture for every drawing function
		@filename .png filename
		@part what is it for? (0=outline, 1=fill, 2=shadow, 3=particles)
		(or .PART_BORDER .PART_FILL .PART_SHADOW, .PART_PARTICULAS) <- TODO-CHECK THIS
		@extend type of extend for cairo
		"""
		t = LoadTexture(filename, extend)
		self.textures[part] = t
		self.MoveTexture(pos_x = 0, pos_y=-self.original._ascent, part=part)
		a = self.actual
		o = self.original
		if part == self.PART_BORDER:
			o.mode_border = a.mode_border = self.P_TEXTURE
		elif part == self.PART_FILL:
			o.mode_fill = a.mode_fill = self.P_TEXTURE
		elif part == self.PART_SHADOW:
			o.mode_shadow = a.mode_shadow = self.P_TEXTURE
		elif part == self.PART_PARTICLE:
			o.mode_particle = a.mode_particle = self.P_TEXTURE

	def MoveTexture(self, pos_x, pos_y, org_x=0, org_y=0, angle=0, scale_x=1, scale_y=1, part=0):
		self.textures[part].set_matrix(CreateMatrix(pos_x, pos_y, org_x, org_y, angle, scale_x, scale_y, inverse=True))

	def CreateParticles(self, texture=None, scale=1.0, alpha_min=0.2, vertical=True, mode=0):
		"""Extremely SLOW
		parameters
		@texture -> pattern with the texture
		optional
		@scale=1.0 -> scale wanted
		@alpha_min=0.2 -> minimum alpha threshold [0-255] <- TODO- CHECK THIS
		@vertical=True -> boolean, sets order for particle creation, True = Vertical, False = Horizontal
		@mode=0 -> particle mode
		"""
		if not texture:
			texture = self.textures[3]

		x1, y1, x2, y2 = map(int, self.Box())
		a = self.actual
		#absolute coordinates [got relative]
		x1 += int(a.pos_x-a.border)
		x2 += int(a.pos_x+a.border)
		y1 += int(a.pos_y-a.border)
		y2 += int(a.pos_y+a.border)

		box = (x1, y1, x2, y2)

		#New group
		advanced.StartGroup()
		#Drawing function
		self.Paint()
		parts = advanced.CreateParticles(box, texture, scale, alpha_min, vertical, mode)
		advanced.EndGroup(opacity=0.0)
		return parts

	def PaintReflection(self, height = None):
		"""@height : pixel height for gradient, etc"""

		#cache
		posy = self.actual.pos_y
		alto_linea = self.original._line_height
		descent = self.original._descent
		height = height or self.original._height

		advanced.StartGroup()
		self.Paint()
		advanced.fBlur()
		mt = CreateMatrix(org_y=posy-self.actual.org_y, pos_y=posy+alto_linea+descent, scale_y = -1)
		pat = advanced.EndGroup(0.0, matrix= mt)

		video.cf.ctx.set_source(pat)
		lineal = cairo.LinearGradient(0, posy+height, 0, posy+(height*2.0))
		lineal.add_color_stop_rgba(1, 0, 0, 0, 0)
		lineal.add_color_stop_rgba(0, 1, 1, 1, 1)
		video.cf.ctx.mask(lineal)

#Colors in cairo use premultiplied alpha, in case you need to unpremultiply them (rgba overlay, i.e.)
#http://lists.freedesktop.org/archives/cairo/attachments/20050826/b24b464d/alpha_test.obj
def DemultipyAlpha(b,g,r,a):
	"""
	@b, g, r, a
	Todos los valores de 0 a 255"""
	#z = Demult(r, a)
	#g = Demult(g, a)
	#b = Demult(b, a)
	return Demult(b, a), Demult(g, a), Demult(r, a), a

def D1(x):
	return x/255.0

def D2(x):
	return (x+0.5)/256.0

def Demult(x, a):
	return common.ClampB( int( ((x*a)-1) /254 ) )

def DuplicateSurface(surface):
	vi = video.vi
	sfc2 = surface.create_similar(cairo.CONTENT_COLOR_ALPHA,  vi.width,  vi.height)
	ctx2 = cairo.Context(sfc2)
	ctx2.set_source_surface(surface)
	ctx2.set_operator(cairo.OPERATOR_SOURCE)
	ctx2.paint()
	return sfc2

def CopyTarget():
	return DuplicateSurface(video.cf.ctx.get_group_target())
