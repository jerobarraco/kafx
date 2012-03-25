# -*- coding: utf-8 -*-
"""
"Define all types necessary for interfacing with avisynth.dll
 Moved from internal.h *"

   Copia del avisynth .h
   mas que nada por compatibilidad con los parámetros que se le pasen a la inicialización
	 y tiene algunas funciones extras para trabajar con video
   """
import math

class cVideoInfo:
	"""
	#Contiene la información del video propiamente dicho
	width=640 # width=0 means no video; ancho
	height=480 #alto
	num_frames=0 #cantidad total de cuadros (corresponde a avisynth)
	fps_numerator=1 #numerador del FPS
	fps_denominator=1 #denominador del FPS
	fps=1 #Fps en float
	fpscof1 = 1 #fpscof1 = fps /1000.0 #coeficientes precalculados para el calculo de milisegundos y frames
	fpscof2 = 1 #fpscof2 = 1000.0 / fps
	fake_stride = 0 #un stride precalculado para cuando se necesite hacer width*4
	"""
	#Contiene la información del video propiamente dicho
	width=640 # width=0 means no video; ancho
	height=480 #alto
	num_frames=0 #cantidad total de cuadros (corresponde a avisynth)
	fps=30.0 #Fps en float
	fpscof1 = 30.0/1000.0 #fpscof1 = fps /1000.0 #coeficientes precalculados para el calculo de milisegundos y frames
	fpscof2 = 1000.0/30.0 #fpscof2 = 1000.0 / fps
	fake_stride = 0 #un stride precalculado para cuando se necesite hacer width*4

	def MSToFrame(self, ms):
		"""Convierte de milisegundos a pnumero de cuadro"""
		#return int(round(ms*vi.fpscof1))
		#return int(ms*vi.fpscof1)
		return int(math.ceil(ms*self.fpscof1))
		#return int(ms*vi.fpscof1)

	def FrameToMS(self, frame):
		"""Convierte de numero de cuadro a milisegundos"""
		return (frame*self.vi.fpscof2)

	def ClampFrameNum(self, frame):
		"Recorta un número (entero) al rango entre 0 y el máximo numero de frames (+ o - 1)"
		if frame < 0: return 0
		if frame > self.num_frames : return self.num_frames
		return frame

class cCurrentFrame:
	"""
	Contiene información del cuadro actual
	ctx = contexto de cairo global
	sfc = surface de cairo global
	framen = numero de cuadro actual
	"""
	#Contiene la información del cuadro actual
	ctx = None #Contexto actual
	framen = -1 #numero de cuadro actual.. creo que empieza desde 0
	#tiempo=-1 #tiempo actual en milisegundos (deshabilitado desde el kafx_main) (definitivamente no debe ser usado)


cf = cCurrentFrame()
vi = cVideoInfo() #Global, la setea kafx_main para que  cualquiera pueda accederla
#Instancia global con la informacion del cuadro actual, y la información del video

# Raster types used by VirtualDub & Avisynth
"""typedef unsigned long	Pixel;    # this will break on 64-bit machines!
typedef unsigned long	Pixel32;
typedef unsigned char	Pixel8;
typedef long			PixCoord;
typedef long			PixDim;
typedef long			PixOffset;
Ni idea como definir numeros de tamaños particulares, ni que importase en python
"""

""" Compiler-specific crap """
SAMPLE_INT8  = 1
SAMPLE_INT16 = 2
SAMPLE_INT24 = 4
SAMPLE_INT32 = 8
SAMPLE_FLOAT = 16
#(no me preguntes porque este hdp usaba << en vez d poner el numero y ya)

PLANAR_Y=1
PLANAR_U=2
PLANAR_V=4
PLANAR_ALIGNED=8
PLANAR_Y_ALIGNED=9
PLANAR_U_ALIGNED=10
PLANAR_V_ALIGNED=12

# Colorspace properties.
CS_BGR = 268435456 #1<<28
CS_YUV = 536870912 #1<<29
CS_INTERLEAVED = 1073741824 # 1<<30
CS_PLANAR = 2147483648L #1<<31


# Specific colorformats
CS_UNKNOWN = 0
CS_BGR24 = 1<<0 | CS_BGR | CS_INTERLEAVED
CS_BGR32 = 1<<1 | CS_BGR | CS_INTERLEAVED
CS_YUY2  = 1<<2 | CS_YUV | CS_INTERLEAVED
CS_YV12  = 1<<3 | CS_YUV | CS_PLANAR  # y-v-u, 4:2:0 planar
CS_I420  = 1<<4 | CS_YUV | CS_PLANAR  # y-u-v, 4:2:0 planar
CS_IYUV  = 1<<4 | CS_YUV | CS_PLANAR # same as above

pixel_type=0                # changed to int as of 2.5
audio_samples_per_second=0   # 0 means no audio
sample_type=0                # as of 2.5
num_audio_samples=0      # changed as of 2.5
nchannels=0                  # as of 2.5
# Imagetype properties
image_type=0


IT_BFF = 1 #1<<0
IT_TFF = 2 #1<<1
IT_FIELDBASED = 4 #1<<2

# useful functions of the above
def HasVideo():
	return width!=0

def Check(var,  type):
	return (var & type) == type

def GetMode(ptype):
	"""Dado un modo de avisynth, devuelve el modo para cairo.
	actualmente implementado RGB24 y ARGB32
	"""
	import cairo
	if Check(ptype,  CS_BGR24):
		return cairo.FORMAT_RGB24

	if Check(ptype,  CS_BGR32):
		return cairo.FORMAT_ARGB32

	return cairo.FORMAT_ARGB32

def BytesFromPixels(pixels, ptype):
	return pixels * BytesPerPixel(ptype)

def BytesPerPixel(ptype):
	if ptype == CS_BGR24:
		return 3
	if ptype == CS_BGR32:
		return 4
	if ptype == CS_YUY2:
		return 2
	if (ptype == CS_YV12) or (ptype == CS_I420):
		return 1.5
	return 0