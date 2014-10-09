#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO usar sys.path y current_directory
#TODO importar la configuracion con el argv
#TODO buscar una forma de hacer como el cairodraw pero con GL (tip : leer, evaluar, redraw)
#TODO buscar como exportar a RGB32 Lossless (http://en.wikipedia.org/wiki/List_of_codecs#Lossless_compression ) (creo q ffmpeg usa FFV1)
#TODO eliminar dll >:D
#TODO Hacer multithread (buffered input, (maybe) multiproces, output)

import os
import threading
#import multiprocessing
import subprocess as s
import ctypes
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
try:
	from Queue import Queue #python2
except:
	from queue import Queue #python3

#for pyinstaller
if os.name=='nt':
	import OpenGL.platform.win32
	
import traceback
traceback.sys.stdout = open('kafx_log.txt', 'w', 0)
traceback.sys.stderr = open('error_log.txt', 'w', 0)
import kafx_main as kf
from libs import video
conf_module = None

class StopThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StopThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
	
class Decoder(StopThread):
	def __init__(self, queue, params, framesize):
		StopThread.__init__(self)
		self.inq = queue
		self.framesize = framesize
		self.dec = s.Popen(params, self.framesize, stdout=s.PIPE, stderr=open('in_err.txt','w'))
		
	def run(self):
		#set idle
		print("decoder running")
		while True:
			if self.dec.poll() != None:
				print("dec.poll failed!! im out")
				break#exit(-2)
			
			frame = ctypes.create_string_buffer(self.dec.stdout.read(self.framesize), self.framesize)
			
			#tries to put it
			try:
				self.inq.put(frame, True, 3)
			except:
				pass #only to check the friking stop flag
			if self.stopped():
				break
		#cleanup
		self.stop()#sets the flag for other ppl
		self.dec.terminate()
		self.dec.kill()

class Encoder(StopThread):
	def __init__(self, inqueue, outqueue, params, framesize):
		StopThread.__init__(self)
		self.inq = inqueue
		#outqueue is only to show encoded frames
		self.outq = outqueue
		self.framesize = framesize
		self.enc=s.Popen(params, bufsize=self.framesize, stdin=s.PIPE)

	def run(self):
		#tries to put it
		print("encoder running")
		while True:
			try:
				frame = self.inq.get(True, 3)
				self.enc.stdin.write(frame)
				self.outq.put(frame)#to be displayed
				#doesnt need a loop for out because it has no limit
			except:
				pass
			if self.stopped():
				print ("encoder stopped")
				break
		#cleanup
		self.stop()#sets the flag for other ppl
		self.enc.terminate()
		self.dec.kill()
		
class Processor(StopThread):
	def __init__(self, inqueue, outqueue, stride):
		StopThread.__init__(self)
		self.framen = 0
		self.stride = stride
		self.inq = inqueue#to be processed
		self.outq = outqueue#processed, to be encoded
		
	#So the initialization is done in the same thread as it runs (just in case)
	def preInit(self, fx, assfile, pfmt, w, h, fps, duration):
		self.fx=fx
		self.assfile = assfile
		self.pfmt=pfmt
		self.w = w
		self.h = h
		self.fps=fps
		self.duration = duration
		
		
	def run(self):
		#initialize
		print("processor running")
		kf.OnInit(self.fx, self.assfile, self.pfmt, 0, self.w, self.h, self.fps, 1, self.duration)
		while True:
			try:
				#this is repeated until it passes
				frame = self.inq.get(True, 3)
				#this happens only if it can get a frame
				self.framen +=1
				kf.OnFrame(self.framen, self.stride, frame)
				
				while True:
					try:
						self.outq.put(frame, True, 3)#to be displayed
						#needs a loop because outq has a max
						break
					except:
						pass
					if self.stopped():
						print ("processor stopped")
						break
			except:
				pass
			if self.stopped():
				print ("processor stopped")
				break
		self.stop()#sets the flag for other ppl
		#cleanup
		kf.OnDestroy()
		
class Kafx():
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
		self.inq = Queue(10)#10 frames max to hold
		self.outq = Queue(10)
		self.showq = Queue()#show has no max because its supposed to skip frames (dangerous)
		
		kf.SetProfiling(bool(self.profile))
		try:
			global conf_module
			conf_module = self.conf = __import__(module)
			print ("Module imported", module, self.conf)
		except Exception, e:
			print e
			print "I couldn't import "+module+"(.py) check that it's an existing file, the name is correct and hasn't errors"
			exit(-1)


		self.start_frame = self.conf.start_frame
		self.getVideoInfo()
		#input args
		self.in_args = [
			#video to decode
			'avconv',  '-i', self.conf.video_in,
			#pipe data
			'-pix_fmt', 'rgb32', '-f', 'rawvideo', '-y', '-' #-y IS important
		]

		if self.d3:#fast solution for flip vertical
			self.conf.out_parameters.insert(-2, "-vf")
			self.conf.out_parameters.insert(-2, "vflip")

		self.out_args =  [
			#input parameters (pipe)
			'avconv', '-r', str(self.fps), '-pix_fmt', 'rgb32',
			'-s', str(self.w)+'x'+str(self.h), '-f', 'rawvideo', '-i', '-'
			#output parameters
			] + self.conf.out_parameters
		self.dec = Decoder(self.inq, self.in_args, self.framesize)
		self.proc = Processor(self.inq, self.outq, self.stride)
		self.proc.preInit(self.conf.fx, self.conf.assfile, video.CS_BGR32, self.w, self.h, self.fps, self.duration)
		self.enc = Encoder(self.outq, self.showq, self.out_args, self.framesize)
		# i leave the out parameters here to let ppl know that they could choose a personalized setting for your video
		#We pipe everything from the firsts subprocess, either way ffmpeg step on itself
		#decode ffmpeg
		#original >>> self.dec=s.Popen(self.in_args, bufsize=self.framesize, stdout=s.PIPE, stderr=open('in_err.txt','w'))
		#encode ffmpeg
		#original >>>> self.enc=s.Popen(self.out_args, bufsize=self.framesize, stdin=s.PIPE)#, stdout=s.PIPE)
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

		#kf.OnInit(self.conf.fx, self.conf.assfile, video.CS_BGR32, 0, self.w, self.h, self.fps, 1, self.duration)
		self.dec.start()
		self.proc.start()
		self.enc.start()
		return glutMainLoop()

	def OnReshape(self, *args):
		glutReshapeWindow(self.w, self.h)

	def Stop(self):
		print ('Leaving')
		self.running = False
		self.dec.stop()
		self.proc.stop()
		self.enc.stop()
		print("waiting for other threads")
		self.dec.join()
		self.proc.join()
		self.enc.join()
		#self.enc.terminate()
		#self.dec.terminate()
		
		#kf.OnDestroy()
		"""c= self.coords
		glPixelStorei(GL_PACK_ALIGNMENT, 1)
		return  glReadPixels(c[0], c[1], c[2], c[3],GL_RGB,GL_UNSIGNED_BYTE)
		"""

	def getVideoInfo(self):
		from libs import asslib
		infop =s.Popen(['avconv', '-i', self.conf.video_in], stdout=s.PIPE, stderr=s.PIPE)
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
		if self.enc.stopped() or self.proc.stopped() or self.dec.stopped():
			self.Stop()
			return
		#original >>> if self.dec.poll()!=None: exit(-2)
		"""p.poll()
		pixels = array.array('B')
		pixels.fromfile(p.stdout, framesize)"""

		#original >>> pixels = ctypes.create_string_buffer(self.dec.stdout.read(self.framesize), self.framesize) #mover a otro thread
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
		#original >>> kf.OnFrame(self.cuadro, self.stride, pixels)
		#theoretically it's better to use textsubimage, but it looks awful! and performance seem to be the same
		#if self.d3:
		#	glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA8, self.w, self.h, 0, GL_BGRA , GL_UNSIGNED_BYTE, pixels)
		#else:
		#	glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels)
		#don't even talk about performance with mipmaps
		#gluBuild2DMipmaps( GL_TEXTURE_2D, 4, self.w, self.h,
		#                   GL_BGRA, GL_UNSIGNED_BYTE, pixels );
		try:
			pixels = self.showq.get(True, 1)
			glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA8, self.w, self.h, 0, GL_BGRA , GL_UNSIGNED_BYTE, pixels)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
			glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
			avail = self.showq.qsize()
			for i in range(avail):
				self.sowq.get(True, 0.5)
		except :
			pass #rerenders the same
		
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
		"""TODO fix
		if self.d3:
			glReadPixels(0, 0, self.w, self.h, GL_BGRA, GL_UNSIGNED_BYTE, pixels  )
		"""		
		#original >>> self.enc.stdin.write(pixels)
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
	enc = Kafx(module, profile, d3)
	enc.Go()
	print("stopping all stuff")
	enc.Stop()
