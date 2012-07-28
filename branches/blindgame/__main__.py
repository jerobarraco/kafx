# -*- coding: utf-8 -*-
#Soy malo escribiendo historias/cuentos, esto es sólo para practicar.

def MostrarDialogos(nombre_archivo):
	archivo = open(nombre_archivo, 'r')
	for linea in archivo:
		print linea
		print "╚╗\n╔╝"
		raw_input("")







print "========BLIND GAME========="

print "¿Vas a ver qué fue eso?: Y / N"
choice1 =raw_input("")
if choice1.lower().startswith('y'):
	print "Ves una silueta cerca de donde está el auto de un vecino. ¿Vas a ver quién es?: Y / N"
	choice2 =raw_input("")
	if choice2.lower().startswith('y'):

	else:

		print "¿Te das vuelta a ver de qué se trata? : Y / N"
		choice3 =raw_input("")
		if choice3.lower().startswith('y'):


		else:


else:
