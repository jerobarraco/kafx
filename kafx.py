#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO usar sys.path y current_directory
#TODO importar la configuracion con el argv
#TODO hacer ejecutable
#TODO buscar una forma de hacer como el cairodraw pero con GL (tip : leer, evaluar, redraw)
#TODO buscar como exportar a RGB32 Lossless (http://en.wikipedia.org/wiki/List_of_codecs#Lossless_compression ) (creo q ffmpeg usa FFV1)
#TODO eliminar dll >:D
#TODO Hacer multithread (buffered input, (maybe) multiproces, output)

import os
import subprocess as s
import ctypes
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import kafx_main as kf
from libs import video

class Encoder():
	running = False
	texture = None
	cuadro = 0
	def __init__(self, module, profile=False, d3=False):
		self.cwd = os.getcwd()
		if self.cwd not in os.sys.path:
			os.sys.path.insert(0,  self.cwd)
		self.module = module
		self.profile = profile
		self.d3 = d3

		kf.SetProfiling(bool(self.profile))
		try:
			self.conf = __import__(module)
			print ("importado el modulo", module, self.conf)
		except Exception, e:
			print e
			print "No pude importar el archivo "+module+"(.py) asegurate que exista, que este bien el nombre y que no tenga errores"
			exit(-1)


		self.start_frame = self.conf.start_frame
		self.getVideoInfo()
		#input args
		self.in_args = [
			#video to decode
			'ffmpeg',  '-i', self.conf.video_in,
			#pipe data
			'-pix_fmt', 'rgb32', '-f', 'rawvideo', '-y', '-' #-y IS important
		]

		if self.d3:#fast solution for flip vertical
			self.conf.out_parameters.insert(-2, "-vf")
			self.conf.out_parameters.insert(-2, "vflip")

		self.out_args =  [
			#input parameters (pipe)
			'ffmpeg', '-r', str(self.fps), '-pix_fmt', 'rgb32',
			'-s', str(self.w)+'x'+str(self.h), '-f', 'rawvideo', '-i', '-'
			#output parameters
			] + self.conf.out_parameters
		# i leave the out parameters here to let ppl know that they could choose a personalized setting for your video
		#We pipe everything from the firsts subprocess, either way ffmpeg step on itself
		#decode ffmpeg
		self.dec=s.Popen(self.in_args, bufsize=self.framesize, stdout=s.PIPE, stderr=open('in_err.txt','w'))
		#encode ffmpeg
		self.enc=s.Popen(self.out_args, bufsize=self.framesize, stdin=s.PIPE)#, stdout=s.PIPE)
		#out, err = p.communicate()#Note: The data read is buffered in memory, so do not use this method if the data size is large or unlimited. #so, we wont use this
		#import array

		#self.coords = ((-1.0, 1.0, 0.0), (-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (1.0, 1.0, 0.0))
		#self.tcoords = ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0) ,(1.0, 0.0))
		#if self.d3:
		#	self.tcoords = ( (0.0, 1.0), (0.0, 0.0) ,(1.0, 0.0), (1.0, 1.0) )
		#else:
		#	self.tcoords = ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0) ,(1.0, 0.0))
		#self.pcoords = zip(self.tcoords, self.coords)

	def Go(self):
		self.running = True
		glutInit()
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
		glutInitWindowSize(self.w, self.h)
		glutCreateWindow('KIckAss FX OpenGL! || Free As A Bird')

		glutDisplayFunc(self.Display)
		glutIdleFunc(self.Display)
		glutReshapeFunc(self.OnReshape)

		glClearColor(0.,0.,0.,1.)
		glShadeModel(GL_SMOOTH)
		#glDisable(GL_CULL_FACE)
		#glDisable(GL_DEPTH_TEST)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)


		glMatrixMode(GL_PROJECTION)
		gluPerspective(1., 1.,1.,1.)
		#gluOrtho2D(-1, 1, 1, -1)#this can flip it, it's unnecessary because glreadpixels flips it back again
		#gluOrtho2D(-1, 1, -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()

		self.texture = glGenTextures(1)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
		glBindTexture(GL_TEXTURE_2D, self.texture)#this line seems optional esta linea pareciera opcional
		glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA8, self.w, self.h, 0, GL_RGBA , GL_UNSIGNED_BYTE, [])
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

		kf.OnInit(self.conf.fx, self.conf.assfile, video.CS_BGR32, 0, self.w, self.h, self.fps, 1, self.duration)

		return glutMainLoop()

	def OnReshape(self, *args):
		glutReshapeWindow(self.w, self.h)

	def Stop(self):
		print 'Saliendo'
		self.running = False
		self.enc.terminate()
		self.dec.terminate()
		kf.OnDestroy()
		"""c= self.coords
		glPixelStorei(GL_PACK_ALIGNMENT, 1)
		return  glReadPixels(c[0], c[1], c[2], c[3],GL_RGB,GL_UNSIGNED_BYTE)
		"""

	def getVideoInfo(self):
		from libs import asslib
		infop =s.Popen(['ffmpeg', '-i', self.conf.video_in], stdout=s.PIPE, stderr=s.PIPE)
		out, err = infop.communicate()
		self.durations = "01:00:00.00"
		self.fps = 29.97
		self.w = 640
		self.h = 480
		for l in err.splitlines():
			low = l.lower()
			if "duration: " in low:
				a = l.find(": ")
				a +=2
				b = l.find(",")
				self.durations = l[a:b]
				print self.durations
			elif ("stream #" in low) and ("video: " in low):
				parts = low.split(",") #lets hope there's no codec with a "," in it...
				self.w, self.h = map(int, parts[2].strip().split(" ")[0].split("x"))
				#4th because in some the 3rd is kbps, in others it doesn't even have fps
				self.fps = float(parts[4].strip().split(" ")[0])

		self.stride = self.w*4
		self.framesize = self.stride*self.h

		video.vi.fps = self.fps
		video.vi.fpscof1 = self.fps/1000.0

		self.durationms = asslib.TimeToMS(self.durations)
		self.duration = video.vi.MSToFrame(self.durationms)
		print("frames %s, fps %s, %sx%s"%(self.duration, self.fps, self.w, self.h))

	def Display(self, *args):
		#Draw
		#pixels = array.array('B', p.stdout.read(framesize))
		if not self.running: return
		if self.dec.poll()!=None: exit(-2)
		"""p.poll()
		pixels = array.array('B')
		pixels.fromfile(p.stdout, framesize)"""

		pixels = ctypes.create_string_buffer(self.dec.stdout.read(self.framesize), self.framesize)
		"""
		the ",framesize" is VERY important, if we don't put it, python creats a character array that ends with a NULL character,
		the array has a extra byte, that way in the writing process the image becomes corrupt.
		When we give the array length (framesize), the array works correctly
		"""


		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		#pixels2 = ctypes.create_string_buffer(pixels.tostring())
		#http://www.opengl.org/wiki/Common_Mistakes#OOP_and_performance
		#we can use unpack 4 because we use 4bytes per pixel
		#glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
		glBindTexture(GL_TEXTURE_2D, self.texture)
		kf.OnFrame(self.cuadro, self.stride, pixels)
		#theoretically it's better to use textsubimage, but it looks awful! and performance seem to be the same
		#if self.d3:
		#	glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA8, self.w, self.h, 0, GL_BGRA , GL_UNSIGNED_BYTE, pixels)
		#else:
		#	glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels)
		#don't even talk about performance with mipmaps
		#gluBuild2DMipmaps( GL_TEXTURE_2D, 4, self.w, self.h,
		#                   GL_BGRA, GL_UNSIGNED_BYTE, pixels );
		glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA8, self.w, self.h, 0, GL_BGRA , GL_UNSIGNED_BYTE, pixels)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glBegin(GL_QUADS)
		"""for t, v in self.pcoords:
			glTexCoord2fv(t)
			glVertex3fv(v)"""

		glTexCoord2f(0.0, 0.0)
		glVertex3f(-1.0, 1.0, 0.0)
		glTexCoord2f(0.0, 1.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glTexCoord2f(1.0, 1.0)
		glVertex3f(1.0, -1.0, 0.0)
		glTexCoord2f(1.0, 0.0)
		glVertex3f(1.0, 1.0, 0.0)
		glEnd()

		"""
		glPushMatrix()
		glTranslatef(0, 0, -1);
		glScalef(1/200.0, 1/200.0, 1/200.0);
		for i in "hola":
			glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(i))
		glPopMatrix();
		"""

		glutSwapBuffers()
		glutPostRedisplay()#http://www.opengl.org/resources/faq/technical/glut.htm 3.050

		"""I think this won't work..
		gluOrtho2D(-1, 1, 1, -1)
		glReadPixels(0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels);
		gluOrtho2D(-1, 1, 1, -1)
		"""
		"""this works... BUT the image becomes more opaque, god knows why
		glRasterPos2f(-1,1);
		# flip the y direction
		glPixelZoom(1,-1);
		# copy in place
		glCopyPixels( 0, 0, self.w, self.h, GL_COLOR );
		glReadPixels(0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels  )"""
		if self.d3:
			glReadPixels(0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels  )

		self.enc.stdin.write(pixels)
		#pixels.tofile(p2.stdin)
		self.cuadro +=1

		return

if __name__ == '__main__':
	module = "myconfig"
	profile = False
	d3 = False
	argv = os.sys.argv
	if len(argv) > 1:
		module = argv[1]
		module = os.path.split(module)[-1]
		module = module.split('.')[0]

	if len(argv)>2:
		profile = bool(argv[2])
	if len(argv)>3:
		d3 = bool (argv[3])
	enc = Encoder(module, profile, d3)
	enc.Go()
	enc.Stop()
