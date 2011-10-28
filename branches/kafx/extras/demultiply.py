# -*- coding: utf-8 -*-
#http://lists.freedesktop.org/archives/cairo/attachments/20050826/b24b464d/alpha_test.obj
def clamp(x):
	if x > 255: x = 255
	if x<0: x = 0
	return x
		
def d1(x):
	return x/255.0

def alpha_demultiply(b,g,r, a):
  """Todos los valores de 0 a 255"""
  def demult(a, x):
	return clamp( int( (x*a-1) /254 ) )

  r = demult(a, r)
  g = demult(a, g)
  b = demult(a, b)
  return b,g,r,a