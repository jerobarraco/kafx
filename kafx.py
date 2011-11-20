from PySide import QtCore, QtGui, QtUiTools, phonon
import sys

class Ventana():
	def __init__(self):
		loader = QtUiTools.QUiLoader() 
		self.ui = loader.load("gui.ui")
		#self.ui.setupUi(self)
		#QtCore.QMetaObject.connectSlotsByName(ui)
		self.ui.pushButton.clicked.connect(self.vidbutton)
		self.ui.pushButton_2.clicked.connect(self.fxbutton)
		self.ui.pushButton_3.clicked.connect(self.assbutton)
		self.ui.pushButton_4.clicked.connect(self.encbutton)
	def show(self):
		self.ui.show()
                
	@QtCore.Slot()
	def vidbutton(self):
		self.vidfile=QtGui.QFileDialog.getOpenFileName(self.ui,"Abrir archivo de video", "test/*.mkv", "Archivos de video")    
		
	@QtCore.Slot()
	def fxbutton(self):
		self.fxfile=QtGui.QFileDialog.getOpenFileName(self.ui,"Abrir archivo de efectos", "test/*.py", "Archivos de efectos")    
	@QtCore.Slot()
	def assbutton(self):
		self.assfile=QtGui.QFileDialog.getOpenFileName(self.ui,"Abrir archivo de subtitulos", "test/*.ass", "Archivos de subtitulos")    
		
	@QtCore.Slot()
	def encbutton(self):
		print "Encoding!!"  
		
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	vent = Ventana()
	vent.show()
	sys.exit(app.exec_())
