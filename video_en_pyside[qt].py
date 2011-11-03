import sys
from PySide import QtGui, phonon

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
vw = phonon.Phonon.VideoPlayer(wid)
vw.showMaximized()




wid.show()

origen = phonon.Phonon.MediaSource("E:\\video\\recorded\\KAFX Demos - shared folder\\t21.avi")
vw.play(origen)

sys.exit(app.exec_())