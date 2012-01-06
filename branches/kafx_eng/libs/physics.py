# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:29:45 2012

@author: Nande!
"""
import Box2D as bd
from libs import video
__env = None
__world = None
__ground = None
__timeStep = 1.0 / 30.0 # So don't tie the time step to your frame rate (unless you really, really have to) #dice la documentacion de b2d
velocityIterations = 10; #bigger=acuracy = slow
positionIterations = 8;

def DestroySprite(sprite):
	global __world
	__world.DestroyBody(sprite.body)
	del sprite.body
	
def CreateSprite(sprite, dynamic = True):
	sprite.body = __CreateBody(
		sprite.x+sprite.org_x, sprite.y+sprite.org_y,
		sprite._ancho*(1.0/sprite.scale_x) /2.0,
		sprite._alto*(1.0/sprite.scale_y) /2.0, dynamic)
		#todo check pos or org
	
def StartMoving(obj):
	body = obj.body
	if body.isSleeping:
		body.WakeUp()

def StopMoving(obj):
	obj.body.PutToSleep()#que nombre de mierda si me permiten
	
def UpdateSprite(sprite):
	pos = sprite.body.position
	sprite.x = pos.x - sprite.org_x
	sprite.y = pos.y - sprite.org_y
	sprite.angle = sprite.body.GetAngle()
	
def __CreateBody(pos_x, pos_y, width, height, dynamic = True):
	global __world
	
	bodyDef = bd.b2BodyDef()
	bodyDef.position = (pos_x, pos_y)
	body = __world.CreateBody(bodyDef)

	shape = bd.b2PolygonDef()
	shape.SetAsBox(width, height)
	if dynamic :
		shape.density = 1.0
	shape.friction = 0.3
	
	# Add the ground shape to the ground body.
	body.CreateShape(shape)
	if dynamic:
		body.SetMassFromShapes()
	#body.PutToSleep()
	return body
		
def Create(grav_x=0, grav_y=1000.0, ground=True):
	global __env, __world, __ground, __localStep
	
	maxx = video.vi.width
	maxy = video.vi.height
	
	hx = maxx/2.0
	hy = maxy/2.0
	__env = bd.b2AABB()
	__env.lowerBound.Set(0, 0);
	__env.upperBound.Set(maxx, maxy);
	# Define the gravity vector.
	gravity = bd.b2Vec2(grav_x, grav_y);
	# Construct a world object, which will hold and simulate the rigid bodies.
	__world = bd.b2World(__env, gravity, True)#true para doSleep
	if ground:
		groundBodyDef = bd.b2BodyDef()
		groundBodyDef.position = [hx, maxy]
		groundBody = __world.CreateBody(groundBodyDef)
		# Define the ground box shape.
		groundShapeDef = bd.b2PolygonDef()
		# The extents are the half-widths of the box.
		groundShapeDef.SetAsBox(hx, 2)
		# Add the ground shape to the ground body.
		groundBody.CreateShape(groundShapeDef)
	
def Update():
	global __timeStep, __world, velocityIterations, positionIterations
	__world.Step(__timeStep, velocityIterations, positionIterations)
	
