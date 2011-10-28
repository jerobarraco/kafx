#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
import gtk, gtk.glade
import gobject, weakref, gc

class Ventana():
	window = None
	def __init__(self):
		xml = gtk.glade.XML('gui.glade')
		self.window = xml.get_widget('Window')

	def Mostrar(self):
		if self.window:
			self.window.show()
		else:
			print "No pude cargar la ventana, D:!"
			
	def Procesar_Click(self):
		print "asldk"
if __name__ == "__main__":
	ventana = Ventana()
	ventana.Mostrar()
	gtk.main()

