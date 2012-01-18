# -*- coding: utf-8 -*-
from PySide import QtGui
import sys
import subprocess as s
import threading

class Encoder(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self)

    def run(self):
        print "Soy el thread"


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.lb1=QtGui.QLabel()
        self.lb2=QtGui.QLabel()
        openVideoAction=QtGui.QAction(QtGui.QIcon('addVideo.png'),'Open Video',self,triggered=self.openVideo)
        self.toolbar=self.addToolBar('Open Video')
        self.toolbar.addAction(openVideoAction)
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("KickAssEffects 1.7")
        self.show()

    def openVideo(self):
        a,b=QtGui.QFileDialog().getOpenFileName(self,self.tr('Open Video'),self.tr('~/'),self.tr('AVI files (*.*)'))
        self.getVideoInfo(a)

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