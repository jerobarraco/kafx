# -*- coding: utf-8 -*-
from PySide import QtGui
from PySide import QtCore
from PySide.QtUiTools import QUiLoader
import sys

class MainWindow():
	def __init__(self):
		self.initUI()

	def initUI(self):
		self.uiLoader = QUiLoader()
		self.window = self.uiLoader.load("gui.ui", None)
		self.window.show()
		

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	mw=MainWindow()
	sys.exit(app.exec_())
