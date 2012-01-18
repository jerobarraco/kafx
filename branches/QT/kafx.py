# -*- coding: utf-8 -*-
from PySide import QtGui
import sys
import subprocess as s
import threading
from PySide.QtCore import Qt

class Encoder(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self)

    def run(self):
        print "Soy el thread"

class videoOut(QtGui.QDialog):
    def __init__(self):
        super(videoOut,self).__init__()
        self.initUI()

    def initUI(self):
        hbox=QtGui.QHBoxLayout()
        hbox1=QtGui.QHBoxLayout()
        vbox=QtGui.QVBoxLayout()
        title=QtGui.QLabel('Video Out Settings')
        widthLabel=QtGui.QLabel('Widht:',self)
        heightLabel=QtGui.QLabel('Height: ',self)
        widthEdit=QtGui.QLineEdit('',self)
        close=QtGui.QPushButton('Close',self)
        close.clicked.connect(self.close)
        vbox.addWidget(title)
        hbox1.addStretch(1)
        hbox1.addWidget(widthLabel)
        hbox1.addWidget(widthEdit)
        vbox.addLayout(hbox1)
        vbox.addWidget(widthLabel)
        vbox.addWidget(heightLabel)
        vbox.addWidget(close)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.setWindowTitle("Video Out Settings")
        self.setGeometry(100,150,100,150)
        self.show()

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        hbox=QtGui.QHBoxLayout()
        vbox=QtGui.QVBoxLayout()
        openViddeoButton=QtGui.QPushButton('Open Video',self)
        openViddeoButton.clicked.connect(self.openVideo)
        configVideoOutButton=QtGui.QPushButton('Video Out Settings',self)
        configVideoOutButton.clicked.connect(self.configVideoOut)
        encodingButton=QtGui.QPushButton('Encode',self)
        vbox.addWidget(encodingButton)
        vbox.addWidget(openViddeoButton)
        vbox.addWidget(configVideoOutButton)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        vbox.addStretch(1)
        hbox.addStretch(1)
        self.setWindowTitle("KickAssEffects 1.7")
        self.setGeometry(300,300,300,300)
        self.show()

    def openVideo(self):
        a,b=QtGui.QFileDialog().getOpenFileName(self,self.tr('Open Video'),self.tr('~/'),self.tr('AVI files (*.*)'))
        self.getVideoInfo(a)

    def configVideoOut(self):
        #a,b=QtGui.QFileDialog().getOpenFileName(self,self.tr('Open Video'),self.tr('~/'),self.tr('AVI files (*.*)'))
        #self.getVideoInfo(a)
            vop=videoOut()
            vop.exec_()

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
    t1=Encoder()
    t1.start()
    t1.join()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
