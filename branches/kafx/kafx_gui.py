#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
import gtk, gtk.glade
import gobject, weakref, gc

class Window():
	window = None
	def __init__(self):
		xml = gtk.glade.XML('gui.glade')
		self.window = xml.get_widget('Window')

	def Show(self):
		if self.window:
			self.window.show()
		else:
			print "No pude cargar la ventana, D:!"
			
	def Process_Click(self):
		print "asldk"
if __name__ == "__main__":
	ventana = Window()
	ventana.Show()
	gtk.main()

