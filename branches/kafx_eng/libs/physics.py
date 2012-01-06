# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:29:45 2012

@author: Nande!
"""
import pymunk as pm
from libs import video
from math import isnan, isinf, pi

class World():
	def __init__(self, grav_x=0, grav_y=500.0, ground=True):
		self.__dt = 1.0/video.vi.fps
		self.maxx = video.vi.width
		self.maxy = video.vi.height
		self.sprites = []
		self.vectors = []

		self.hx = self.maxx/2.0
		self.hy = self.maxy/2.0#unused
		self.space = pm.Space() #2
		self.space.gravity = (grav_x, grav_y)
		if ground:
			body = pm.Body() # 1We create a "static" body. The important step is to never add it to the space. Note how static bodies are created by not passing any arguments to the Body constructor.
			body.position = (0, self.maxy)#el origin del obj como es estatico no necesito ponerlo en el centro del cuerpo
			l1 = pm.Segment(body, (0.0, 0.0), (self.maxx, 0.0), 5.0)#bottom
			#l2 = pm.Segment(body, (0.0, 0.0), (0.0, -self.maxy),5.0)#left
			#l3 = pm.Segment(body, (self.maxx, 0.0), (self.maxx, -self.maxy), 5.0)#right
			#self.space.add_static(l1,l2,l3) # 3
			self.space.add_static(l1)

	def Update(self, updateObjs=True):
		self.space.step(self.__dt)
		if updateObjs:
			for sp in self.sprites:
				UpdateSprite(sp)
			for vec in self.vectors:
				UpdateVector(vec)

	def __Destroy(self, obj):
		if obj._dynamic: self.space.remove(obj.shape.body)
		self.space.remove(obj.shape)
		del obj.shape

	def Destroy(self, obj):
		#Slower but easier to use
		if obj in self.vectors:
			self.DestroyVector(obj)
		elif obj in self.sprites:
			self.DestroySprite(obj)
		else:
			try:
				self.__Destroy(obj)
			except:
				print "quieren destruir un objeto que no existe"


	def DestroySprite(self, obj):
		self.sprites.remove(obj)
		self.__Destroy(obj)

	def DestroyVector(self, obj):
		self.vectors.remove(obj)
		self.__Destroy(obj)

	def CreateBody(self, pos_x, pos_y, width, height, angle = 0.0, dynamic = True, square=False):
		mass = 1.0
		if dynamic:
			if square:
				inertia = pm.moment_for_box(mass, width*2, height*2)
			else:
				inertia = pm.moment_for_circle(mass, 0, width) # 1
			body = pm.Body(mass, inertia) # 2
		else:
			body = pm.Body()

		body.angle = angle #the angle can only be set before adding to space

		if square:
			verts = ( (-height, -width), (-height, width), (height, width), (height, -width))
			shape = pm.Poly(body, verts )
		else:
			shape = pm.Circle(body, width) # 4

		body.position = pos_x, pos_y

		self.space.add(shape)
		if dynamic:
			self.space.add(body) # 5
		return shape

	def CreateVector(self, vector, dynamic = True, square=False):
		vector._dynamic = dynamic
		a = vector.actual

		x = a.pos_x+a.org_x
		y = a.pos_y+a.org_y
		w = vector.original._ancho /2.0
		h = vector.original._alto /2.0
		vector.shape = self.CreateBody( x, y, w, h, a.angle, dynamic, square)

		self.vectors.append(vector)

	def CreateSprite(self, sprite, dynamic = True, square=False):
		sprite._dynamic = dynamic
		x= sprite.x+sprite.org_x
		y= sprite.y+sprite.org_y
		w=sprite._ancho*(1.0/sprite.scale_x) /2.0
		h= sprite._alto*(1.0/sprite.scale_y) /2.0

		sprite.shape = self.CreateBody(x, y, w, h, sprite.angle, dynamic, square)
		self.sprites.append(sprite)

def UpdateVector(vector):
	body = vector.shape.body
	pos = body.position

	a = vector.actual
	a.angle = body.angle #+ vector.original.angle #hasta que pymunk me tome bien el ángulo
	a.pos_x = pos.x - a.org_x
	a.pos_y = pos.y - a.org_y
	#pongo el isinf 1º porque le pymunk me tira ese
	if isinf(a.angle) or isnan(a.angle) : a.angle = 0.0

def UpdateSprite(sprite):
	body = sprite.shape.body
	pos = body.position
	sprite.x = pos.x - sprite.org_x
	sprite.y = pos.y - sprite.org_y
	sprite.angle = body.angle

	if isinf(sprite.angle) or  isnan(sprite.angle) : sprite.angle =0.0

