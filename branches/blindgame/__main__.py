# -*- coding: utf-8 -*-
#Soy malo escribiendo historias/cuentos, esto es sólo para practicar.

def MostrarDialogos(nombre_archivo):
	archivo = open(nombre_archivo, 'r')
	for linea in archivo:
		raw_input(linea + "\234")
		
print "========BLIND GAME========="
MostrarDialogos("start.txt")
print "¿Vas a ver qué fue eso?: Y / N"
choice1 =raw_input("")
if choice1.lower().startswith('y'):
	MostrarDialogos("c1y.txt")
	print "Ves una silueta cerca de donde está el auto de un vecino. ¿Vas a ver quién es?: Y / N"
	choice2 =raw_input("")
	if choice2.lower().startswith('y'):
		MostrarDialogos("c2y.txt")
	else:
		MostrarDialogos("c2n.txt")
		print "¿Te das vuelta a ver de qué se trata? : Y / N"
		choice3 =raw_input("")
		if choice3.lower().startswith('y'):
			MostrarDialogos("c3y.txt")


		else:
			MostrarDialogos("c3n.txt")



else:
	MostrarDialogos("c1n.txt")
