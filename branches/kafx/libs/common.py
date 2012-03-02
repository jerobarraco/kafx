# -*- coding: utf-8 -*-
"""
Module with different kind of functions
theoretically it doesn't depend on things like cairo or ass
"""
import math
import random
import itertools
from libs import video

def chunker(seq, size):
	return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return itertools.izip_longest(fillvalue=fillvalue, *args)

def ClampB(x):
	"Cuts a number (integer) to range 0 to 255"
	if x > 255: x = 255
	if x < 0: x = 0
	return x

def Clamp(num):
	"Cuts a float number to range 0.0 to 1.0"
	if num < 0.0 : return 0.0
	if num > 1.0 : return 1.0
	return num

def ChooseByFrame(start_frame, end_frame, active, inactive=None ):
	"""start_frame has the starting frame
	end_frame the ending frame
	active is what is returned if the actual frame is in range
	inactive is what is returned if the actual frame is not between start_frame and end_frame
	example:
	d.actual.pos_x = ChooseByFrame(100, 200, 0, 20)
	this makes the position_x from dialogue to ONLY be 20 between frames 100 and 200, then it goes back to 0
	other objects can be used like:
	d.actual.color1.CopyFrom(ChooseByFrame(100, 400, d.actual.color2, d.actual.color3)
	"""

	if start_frame <= video.cf.framen  <= end_frame:
		return active
	else:
		return inactive #the else is not necessary, it's to understand
	#this can also be used, just for the lulz
	#return ( (start_frame <= video.cf.framen) and active) or inactive

def Choose(progress, vector):
	#According to progress (form 0.0 to 1.0), returns an item from a vector (array or list) of elements
	progress = Clamp(progress)#clamp is important, if not it gives access error
	l = len(vector)
	i = int(l*progress)
	if i == l: i = l-1
	return vector[i]

#functions for interpolate
#given a value between 0-1, reutnrs another value between 0-1
def i_lineal(p): return float(p)
def i_sin(p): return math.sin(math.pi*p)
def i_cos(p): return math.cos(math.pi*p)
#in case if somthing "circular" wants to be done
def i_full_sin(p): return math.sin(2*math.pi*p)
def i_full_cos(p): return math.cos(2*math.pi*p)

def i_accel(p): return math.sin(math.pi*p*0.5)**2 #pi/2 = 90º
def i_deccel(p): return 1-i_accel(p)
def i_rand(p): return random.random()
def i_log(p):
	#be careful when using, numbers less than 1 gives error
	return math.log((p*2)+1)

#http://www.the-art-of-web.com/css/timing-function/ <<
#this is what I wanted to do with beizers a looooong time ago, but I couldn't
#same results, the idea is to do it with splines, it's not worth it though
def i_b_default(p):
	return PointBezier(p, 0, 0, 0.25, 0.1, 0.25, 1, 1, 1)[1]

def i_b_ease_in(p):
	return PointBezier(p, 0, 0, 0.42, 0.0, 1, 1, 1, 1)[1]

def i_b_ease_out(p):
	return PointBezier(p, 0, 0, 0, 0, 0.58, 1, 1, 1)[1]

def i_b_ease_in_out(p):
	return PointBezier(p, 0, 0, 0.42, 0.0, 0.58, 1, 1, 1)[1]

def i_b_cubic(p):
	return PointBezier(p, 0, 0, 0, 1.0, 1.0, 0, 1, 1)[1]

def i_b_backstart(p):
	return PointBezier(p, 0, 0,
		0.2, -0.3, 0.6, 0.26,
		1, 1)[1]

def i_b_boing(p):
	return PointBezier(p,
	0, 0,
	0.42, 0.0,
	0.58, 1.5,
	1, 1
	)[1]

def Interpolate(progress, fom_val, to_val, function=i_lineal):
	"""
	returns a floating number between 2 values, the returned number corresponds to the amount given in the first value
	@progress indicates how close to the start or end should the returned value be, must be a number between 0 and 1 (other values are valid, though)
	@from_val starting value or beginning of range
	@to_val ending value, or end of range
	@function personal function that returns a value between 0 and 1 (always float) of a given value of progress between 0 and 1
	(puede usar las funciones que comienzan por i_)
	"""
	#http://es.wikipedia.org/wiki/Interpolación - http://en.wikipedia.org/wiki/Interpolation
	return (function(progress) * (to_val-fom_val))+fom_val

def LERP(progress, from_val, to_val):
	"""
	returns a float number between 2 values, this number corresponds to the amount given in the first value
	@progress indicates how close to the start or end of the range should be the returned value, must be a number between 0 and 1 (other values work, too)
	@from_val starting value, or beginning of range
	@to_val ending value, or end of range
	This function is the same as linear interpolate, but it's faster,
	only for functions that only require linear interpolation
	"""
	return from_val+(float(progress)*(to_val-from_val))

def RanmaBezier(progress, points):
	"""
	Returns a point (x, y) over a bezier curve, given the progress over it
	Allows biezer curves of any order
	@progress as in interpolate, normally a number between 0 and 1 giving the progress over the curve
	@points : array of points -> [ [0, 0], [1, 1], [2, 2] ]
	It's like PointBezier, but allows vurces of any amount of control points (from 1 to (theoretically) infinit)
	written by Ranma42 @ irc.freenode.net/#cairo
	"""

	while len(points)>1:
		points2 = []
		for i in range(len(points) - 1):
			px0,py0 = points[i]
			px1,py1 = points[i+1]
			p = (LERP(progress, px0, px1), LERP(progress, py0, py1))
			points2.append(p)
		points = points2
	return points[0]

def PointBezier(progress, x_start, y_start,  x1, y1, x2, y2, x_end, y_end):
	"""
	Returns a point (x, y) over a bezier curve given the progress over it
	@x_start, y_start : starting point of the curve
	@x1, y1 : 1st control point of the curve
	@x2, y2 : 2nd control point of the curve
	@x_end, y_end : ending point of the curve
	@progress : progress over the curve (0 to 1)
	This function is like Bezier, but a little faster, also,
	It's limited to:
	1 Starting point
	2 control points
	1 Ending Point
	and all the points are given sequentially by parameter.
	#with help of ranma42!
	"""

	curvx1 = LERP(progress, x_start, x1)
	curvx2 = LERP(progress, x1, x2)
	curvx3 = LERP(progress, x2, x_end)

	curvx4 = LERP(progress, curvx1, curvx2)
	curvx5 = LERP(progress, curvx2, curvx3)

	curvx6 = LERP(progress, curvx4, curvx5)

	curvy1 = LERP(progress, y_start, y1)
	curvy2 = LERP(progress, y1, y2)
	curvy3 = LERP(progress, y2, y_end)

	curvy4 = LERP(progress, curvy1, curvy2)
	curvy5 = LERP(progress, curvy2, curvy3)

	curvy6 = LERP(progress, curvy4, curvy5)
	return curvx6, curvy6

def Chain(duration, progress, objects, function, time=None):
	"""Makes a chain animation.
	Given a master duration, a master progress applied to
	an array of objects and an animation time per object,
	progress gets calculated for each object and calls the function given by parameter for each one.

	The idea is to be able to animate syllables according to the dialogue, or letters according to the syllable,
	however I put it here so it can be used in other ways.

	@duration Duration fo master time
	@progress float in range from 0 to 1, indicates the master progress
	@objects array of objects to be animated in chain.
		they will be given to the function func. (it only needs implement len and be iterable (string and array work))

	@function must be a function
	it will be called forth for eac object in appearance order with the following parameters:
		object, progress

	@time defines how long the animation is for each object
		if time is greater than duration/len(objects)
		then the animations will overlap.
		if time is None (or not specified) the animations go
		one after another, so time = duration/len(objects)
		if it's less, I don't know.
	"""
	duration = float(duration)
	slen = len(objects)
	if slen == 0 : return
	tsil = duration/slen#Time per syllable in constant progress

	if not time:
		time = tsil
	#Progress will be calculated back and forth. In few words, they end when they must.
	#But they will begin when it's better to adjust animation time

	#How much of dialogues progress belongs to
	#each syllable
	#Therefore, calculation of syllables must be sequential and in order
	finacum = tsil#Accumulates the times of fin (in what each syllable ends (accoding to the dialogue))
	tactualdiag=(progress*duration)
	for obj in objects:
		tini = finacum - time
		tactualsilaba = (tactualdiag - tini)
		if tactualsilaba <= 0:# Still not animated (if it's less than 0, then tini es greater than tactual)
			prog = 0.0
		elif tactualsilaba >= time:#If syllables time is greater than the time that it must be
			prog = 1.0
		else:
			prog = tactualsilaba/time

		function(obj, prog)#This is magic!
		finacum += tsil

def SafeGetFloat(dicc, prop, default=0.0):
	"""
	Returns a property, a dictionary converted to float, or a default value
	@dict dictionary
	@prop property of the dictionary to return
	@default, optional, default value 0.0, it's the returned value if there's an error in the convertion of the dictionarys property
	"""
	try:
		return float(dicc[prop]) #porque en algunos lados se puede pasar algo que devuelve un string no valido como float, lo tenemos que poner dentro del try, así evitamos cosas
	except:
		return default

class FxsGroup():
	"""Clase de la que desciende un grupo de efectos"""

	"""
	Decidí pasar los elementos acá para para evitar tener que explicar el __init__ en las instancias
	me baso en esto:

	"All variables at the class method (irrespective of mutability -- lists and dicts are mutable) are shared.
	With immutable objects, the sharing isn't interesting. With mutable objects (lists and dicts) the sharing is significant.
	– S.Lott Oct 8 '09 at 11:58 @stackoverflow.com"

	the only problem would be with the fxs array, but while appends or that kind of things aren't used, it will be alright
	also they won't create two instances descendant of FxsGroup at the same time
	"""
	in_ms = 0
	#Miliseconds for the entering animation
	out_ms = 0
	#ms for output animation
	syl_in_ms = 0
	#ms for the entering animation of each not animated syllable (in actual dialogue)
	syl_out_ms = 0
	#ms for animation of each dead syllable (in actual dialogue)
	letter_in_ms = 0
	#ms for animation of each sleeping letter (in actual syllable)
	letter_out_ms = 0
	#ms for animation of each dead letter (in actual syllable)
	skip_frames = True
	#Indicates if all the frames of the video will be used, including the ones without dialogues or syllables.
	reset_style = True
	#Indicates if style will be reseted (goes back to original) after each frame for each syllable.
	split_letters = False
	#Indicates if letters will be divided from syllables when loading

	fxs = []
	#Unlike the previous ones this is the only property that must be defined.
	#This property has the different effects that will be done. For example for a video with a line of kanjis,
	#other of translation, and other with the lyrics; there can be an effect for each type.

	blur_type = 0
	#This is for choosing the blur type, it's experimental and advanced (and not much useful)

	def OnFrameStarts(self):
		#This runs at the beginning of the frame. Before any dialogue.
		pass

	def OnFrameEnds(self):
		#This runs at the end of the frame. After all the dialogues.
		pass

class Fx():
	"""Class that an effect inherits from"""
	events = []
	#Array with customized events, must contain instances from Event class

	def OnDialogue(self, diag):
		pass
	def OnSyllable(self, sil):
		pass
	def OnLetter(self, let):
		pass


	def OnSyllableDead(self, sil):
		pass
	def OnSyllableSleep(self, sil):
		#Common sleeping syllable (progress is the same for all the sleeping syllables from the same dialogue)
		pass
	def OnLetterDead(self, let):
		pass
	def OnLetterSleep(self, let):
		pass

	#Till here are all normal animations
	def OnDialogueIn(self, diag):
		pass
	def OnSyllableIn(self, sil):
		pass
	def OnLetterIn(self, let):
		pass

	def OnDialogueOut(self, diag):
		pass
	def OnSyllableOut(self, sil):
		pass
	def OnLetterOut(self, let):
		pass

	def OnDialogueStarts(self, diag):
		pass
	def OnSyllableStarts(self, sil):
		pass
	def OnLetterStarts(self, let):
		pass

class Event():
	def OnSyllable(self, sil):
		pass
	def OnDialogue(self, diag):
		pass
	def OnLetter(self, let):
		pass

	def SyllableTime(self, sil):
		return (0, 0)
	def DialogueTime(self, diag):
		return (0, 0)
	def LetterTime(self, let):
		return (0, 0)


####Inner things

def MyImport(name):
	#Inner function to load a module from a string divided by points, I don't recommend its use
	mod = __import__(name)
	components = name.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod
