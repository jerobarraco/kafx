from PySide import QtCore, QtGui, QtUiTools
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ff = QtCore.QFile("gui.ui")
    ff.open(QtCore.QFile.ReadOnly)
    mw = QtUiTools.QUiLoader().load(ff)
    ff.close()
    @QtCore.Slot()
    def vidbutton():
        print "Feliz Navidad!"    
    def fxbutton():
        print "Feliz Halloween!"    
    def assbutton():
        print "Feliz Carnaval!"
    def encbutton():
        print "Me quede sin ideas :("
    mw.pushButton.clicked.connect(vidbutton)
    mw.pushButton_2.clicked.connect(fxbutton)
    mw.pushButton_3.clicked.connect(assbutton)
    mw.pushButton_4.clicked.connect(encbutton)
    mw.show()
    #myapp = MyMainWindow()
    #myapp.show()
    sys.exit(app.exec_())