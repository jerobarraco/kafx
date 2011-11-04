#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	import myconfig as conf
except Exception, e:
	print e
	print "No pude importar el archivo myconfig.py asegurate que exista, que este bien el nombre y que no tenga errores"
	exit()

import subprocess as s
import kafx_main as kf
from libs import video
import array

w = conf.width
h = conf.height
stride = w*4
framesize = stride*h
#ffmpeg -pix_fmt uyvy422 -s 720×576 -f rawvideo -i output_pipe -target pal-dvd -aspect 4:3 -y myDVD.mpg -f s16le -ar 48000 -ac 2 -i pcm0_pipe -acodec mp2 -ab 224k -newaudio
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

# i leave the out parameters here to let ppl know that they could choose a personalized setting for your video
#We pipe everything from the firsts subprocess, either way ffmpeg step on itself
#decode ffmpeg
in1=open('err1.txt','w')
err1 = open('err1.txt','w')
p=s.Popen(args, bufsize=framesize, stdout=s.PIPE)#, stdin=in1,  stderr=s.PIPE)

#encode ffmpeg
p2=s.Popen(args2, bufsize=framesize, stdin=s.PIPE)#, stdout=s.PIPE)
kf.OnInit(conf.fx, conf.assfile, video.CS_BGR32, 0, w, h, conf.fps, 1, conf.frames)
cuadro=conf.cuadro_inicial

try:
	while p.poll() == None:
		#out = ctypes.create_string_buffer(p.stdout.read(framesize))
		out = array.array('B')
		try:
			out.fromfile(p.stdout, framesize)
		finally:
			#en realidad si el tamaño fuese menor tendria que guardar lo que hay y copiar mas.
			kf.OnFrame(cuadro, stride, out)

			out.tofile(p2.stdin)
			cuadro+=1
finally:
	p.terminate()
	p2.terminate()
	print '\n\n\n\nFIN!'

import math

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4 import QtGui
from PyQt4.QtOpenGL import *

class SpiralWidget(QGLWidget):
    '''
    Widget for drawing two spirals.
    '''

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(500, 500)

    def paintGL(self):
        '''
        Drawing routine
        '''

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Draw the spiral in 'immediate mode'
        # WARNING: You should not be doing the spiral calculation inside the loop
        # even if you are using glBegin/glEnd, sin/cos are fairly expensive functions
        # I've left it here as is to make the code simpler.
        radius = 1.0
        x = radius*math.sin(0)
        y = radius*math.cos(0)
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_LINE_STRIP)
        for deg in xrange(1000):
            glVertex(x, y, 0.0)
            rad = math.radians(deg)
            radius -= 0.001
            x = radius*math.sin(rad)
            y = radius*math.cos(rad)
        glEnd()

        glEnableClientState(GL_VERTEX_ARRAY)

        spiral_array = []

        # Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
        radius = 0.8
        x = radius*math.sin(0)
        y = radius*math.cos(0)
        glColor(1.0, 0.0, 0.0)
        for deg in xrange(820):
            spiral_array.append([x, y])
            rad = math.radians(deg)
            radius -= 0.001
            x = radius*math.sin(rad)
            y = radius*math.cos(rad)

        glVertexPointerf(spiral_array)
        glDrawArrays(GL_LINE_STRIP, 0, len(spiral_array))
        glFlush()

    def resizeGL(self, w, h):
        '''
        Resize the GL window
        '''

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)

    def initializeGL(self):
        '''
        Initialize GL
        '''

        # set viewing projection
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)


# You don't need anything below this
class SpiralWidgetDemo(QtGui.QMainWindow):
    ''' Example class for using SpiralWidget'''

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        widget = SpiralWidget(self)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QtGui.QApplication(['Spiral Widget Demo'])
    window = SpiralWidgetDemo()
    window.show()
    app.exec_()