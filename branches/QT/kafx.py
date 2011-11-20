# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui, QtUiTools, phonon
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ff = QtCore.QFile("gui.ui")
    ff.open(QtCore.QFile.ReadOnly)
    mw = QtUiTools.QUiLoader().load(ff)
    ff.close()
    @QtCore.Slot()
    def vidbutton():
        vidfile=QtGui.QFileDialog.getOpenFileName(mw,"Abrir archivo de vídeo", "test/*.mkv", "Archivos de vídeo")    
    def fxbutton():
        fxfile=QtGui.QFileDialog.getOpenFileName(mw,"Abrir archivo de efectos", "test/*.py", "Archivos de efectos")    
    def assbutton():
        assfile=QtGui.QFileDialog.getOpenFileName(mw,"Abrir archivo de subtítulos", "test/*.ass", "Archivos de subtítulos")    
    def encbutton():
        print "Encoding!!"  
    mw.pushButton.clicked.connect(vidbutton)
    mw.pushButton_2.clicked.connect(fxbutton)
    mw.pushButton_3.clicked.connect(assbutton)
    mw.pushButton_4.clicked.connect(encbutton)
    mw.show()
    #myapp = MyMainWindow()
    #myapp.show()
    sys.exit(app.exec_())