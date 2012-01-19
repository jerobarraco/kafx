# -*- coding: utf-8 -*-
from PySide import QtGui
import sys
import subprocess as s
import threading

class Encoder(threading.Thread):
	def __init__(self,inargs,outargs):
		threading.Thread.__init__(self)
		self.inargs=inargs
		self.outargs=outargs

	def run(self):
		print "Soy el thread"

class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.initUI()

	def initUI(self):
		self.file=None
		self.w=None
		self.h=None
		self.fps=None
		hbox=QtGui.QHBoxLayout()
		vbox=QtGui.QVBoxLayout()
		openViddeoButton=QtGui.QPushButton('Open Video',self)
		openViddeoButton.clicked.connect(self.openVideo)
		encodingButton=QtGui.QPushButton('Encode',self)
		encodingButton.clicked.connect(self.encode)
		vbox.addWidget(openViddeoButton)
		vbox.addWidget(encodingButton)
		hbox.addLayout(vbox)
		self.setLayout(hbox)
		vbox.addStretch(1)
		hbox.addStretch(1)
		self.setWindowTitle("KickAssEffects 1.7")
		self.setGeometry(300,300,300,300)
		self.show()

	def openVideo(self):
		self.file,self.filter=QtGui.QFileDialog().getOpenFileName(self,self.tr('Open Video'),self.tr('~/'),self.tr('AVI files (*.*)'))
		self.getVideoInfo(self.file)
		
	def encode(self):
		if self.file:
			self.encoder=Encoder(['a','b','c'],['d','e','f'])
			print self.encoder.inargs
			print self.encoder.outargs
		elif not self.file:
			print "No file selected"

	def getVideoInfo(self,video):
		infop =s.Popen(['ffmpeg', '-i', video], stdout=s.PIPE, stderr=s.PIPE)
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
				parts = low.split(",") #esperemos que no haya ningun codec con una "," en el medio...
				self.w, self.h = map(int, parts[2].strip().split(" ")[0].split("x"))
				print self.w
				print self.h
				#4 porque en algunos el 3º es el kbps, en otros ni siquiera pone el fps
				self.fps = float(parts[4].strip().split(" ")[0])
				print self.fps


def main():
	app=QtGui.QApplication(sys.argv)
	ex=MainWindow()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
