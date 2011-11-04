from PySide import QtCore, QtGui, QtUiTools
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ff = QtCore.QFile("gui.ui")
    ff.open(QtCore.QFile.ReadOnly)
    mw = QtUiTools.QUiLoader().load(ff)
    ff.close()
    mw.show()
    #myapp = MyMainWindow()
    #myapp.show()
    sys.exit(app.exec_())
