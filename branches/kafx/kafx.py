#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO usar sys.path y current_directory
#TODO importar la configuracion con el argv
#TODO hacer ejecutable
#TODO buscar una forma de hacer como el cairodraw pero con GL (tip : leer, evaluar, redraw)
#TODO buscar como exportar a RGB32 Lossless (http://en.wikipedia.org/wiki/List_of_codecs#Lossless_compression ) (creo q ffmpeg usa FFV1)
#TODO eliminar dll >:D
#TODO Hacer multithread (buffered input, (maybe) multiproces, output)

import subprocess as s
import ctypes
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import kafx_main as kf
from libs import video

def Display(*args):
	global texture, cuadro, running, w, h, ang
	#Dibujar
	#pixels = array.array('B', p.stdout.read(framesize))
	if p.poll()!=None: exit()
	"""p.poll()
	pixels = array.array('B')
	pixels.fromfile(p.stdout, framesize)"""

	pixels = ctypes.create_string_buffer(p.stdout.read(framesize), framesize)
	"""
	el ",framesize" es ultraimportante, si no se coloca, python crea un array de caracteres que termina con el caracter NULL
	lo que hace que el array tenga un byte de mas, lo que hace que al intentar escribirlo la imagen se corrompa.
	al ponerle el tamaño del array (framesize) el array funciona correctamente
	"""

	kf.OnFrame(cuadro, stride, pixels)

	#pixels2 = ctypes.create_string_buffer(pixels.tostring())
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glBindTexture(GL_TEXTURE_2D, texture)

	glTexSubImage2D(GL_TEXTURE_2D, 0, 0,0, w,h, GL_BGRA, GL_UNSIGNED_BYTE, pixels)

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(-1.0, 1.0, 0.0)

	glTexCoord2f(0.0, 1.0)
	glVertex3f(-1.0, -1.0, 0.0)

	glTexCoord2f(1.0, 1.0)
	glVertex3f(1.0, -1.0, 0.0)

	glTexCoord2f(1.0, 0.0)
	glVertex3f(1.0, 1.0, 0.0)

	glEnd()
	glFlush()

	glutSwapBuffers()
	glutPostRedisplay()#http://www.opengl.org/resources/faq/technical/glut.htm 3.050
	p2.stdin.write(pixels)
	#aca faltaria una funcion que copie el buffer de opengl a pixels antes de escribirlo
	#pixels.tofile(p2.stdin)
	cuadro +=1
	return

def OnReshape(*args):
	glutReshapeWindow(w,h)

def GLMain():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
	glutInitWindowSize(w,h)
	glutCreateWindow('KIckAss FX OpenGL! || Free As A Bird')

	glutDisplayFunc(Display)
	glutIdleFunc(Display)
	glutReshapeFunc(OnReshape)

	glClearColor(0.,0.,0.,1.)
	glShadeModel(GL_SMOOTH)
	glDisable(GL_CULL_FACE)
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)


	glMatrixMode(GL_PROJECTION)
	gluPerspective(1.,1.,1.,1.)
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()

	global texture
	texture = glGenTextures(1)
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glBindTexture(GL_TEXTURE_2D, texture)#esta linea pareciera opcional
	glTexImage2D(GL_TEXTURE_2D, 0,  GL_RGBA, w, h, 0, GL_RGBA , GL_UNSIGNED_BYTE, [])
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


	kf.OnInit(conf.fx, conf.assfile, video.CS_BGR32, 0, w, h, conf.fps, 1, conf.frames)

	glutMainLoop()
	return


if __name__ == '__main__':
	try:
		import os
		cwd = os.getcwd()

		if cwd not in os.sys.path:
			os.sys.path.insert(0,  cwd)

		module = 'myconfig'
		
		if len(os.sys.argv) > 1:
			module = os.sys.argv[1]
			module = os.path.split(module)[-1]
			module = module.split('.')[0]
		
		if len(os.sys.argv)>2:
			profiling = bool(os.sys.argv[2])
			kf.SetProfiling(profiling)

		conf = __import__(module)
		print "importado el modulo", module, conf

	except Exception, e:
		print e
		print "No pude importar el archivo "+module+"(.py) asegurate que exista, que este bien el nombre y que no tenga errores"
		exit()

	w = conf.width
	h = conf.height
	stride = w*4
	framesize = stride*h
	#input args
	args = [
		#video to decode
		'ffmpeg',  '-i', conf.video_in,
		#pipe data
		'-pix_fmt', 'rgb32', '-f', 'rawvideo', '-y', '-' #-y IS important
		]

	args2 = [
		#input parameters (pipe)
		'ffmpeg', '-r', str(conf.fps), '-pix_fmt', 'rgb32', '-s', str(w)+'x'+str(h), '-f', 'rawvideo', '-i', '-',
		#output parameters
		] + conf.out_parameters

	cuadro= conf.start_frame
	texture = None

	# i leave the out parameters here to let ppl know that they could choose a personalized setting for your video
	#We pipe everything from the firsts subprocess, either way ffmpeg step on itself
	#decode ffmpeg
	in1 = open('in_in.txt','w')
	err1 = open('in_err.txt','w')
	#decode ffmpeg
	p=s.Popen(args, bufsize=framesize, stdout=s.PIPE, stderr=err1)
	#encode ffmpeg
	p2=s.Popen(args2, bufsize=framesize, stdin=s.PIPE)#, stdout=s.PIPE)
	#out, err = p.communicate()#Note: The data read is buffered in memory, so do not use this method if the data size is large or unlimited. #so, we wont use this
	#import array
	
	#And now: do the work
	try:
		GLMain()
	finally:
		print 'saliendo'
		running = False
		p.terminate()
		p2.terminate()
		"""c= self.coords
			glPixelStorei(GL_PACK_ALIGNMENT, 1)
			return  glReadPixels(c[0], c[1], c[2], c[3],GL_RGB,GL_UNSIGNED_BYTE)
		"""
