# -*- coding: utf-8 -*-
#Soy malo escribiendo historias/cuentos, esto es sólo para practicar.

def MostrarDialogos(nombre_archivo):
	archivo = open(nombre_archivo, 'r')
	for linea in archivo:
		print linea
		print "╚╗\n╔╝"
		raw_input("")







print "========BLIND GAME========="
print" ... "
raw_input("")
print " ...... "
raw_input("")
print " ... Te despiertas en medio de la madrugada,"
raw_input("")
print " no sabes por qué, pero hay algo que te molesta."
raw_input("")
print " Te levantas para acercarte a la ventana de tu habitación."
raw_input("")
raw_input(" Abres la ventana.")
raw_input("")
raw_input(" En ese momento sientes una fría brisa que te recuerda que todavía es invierno.")
raw_input("")
raw_input(" Miras hacia arriba, pero lo único que se ve es la luna, brillando solitaria.")
raw_input("")
raw_input(" \"...\" ")
raw_input("")
raw_input(" Bajas la vista, ves la calle y las casas vecinas; nada fuera de lugar.")
raw_input("")
raw_input(" O eso creías, hasta que ves \"algo\" cerca de la case de los vecinos de enfrente.")
raw_input("")
raw_input(" Fue fugaz, pero estás casi seguro que has visto algo.")
raw_input("")
print "¿Vas a ver qué fue eso?: Y / N"
choice1 =raw_input("")
if choice1.lower().startswith('y'):
	print "..."
	raw_input("\"No. Algo no está bien.\"")
	raw_input("\"Voy a investigar.\"")
	raw_input("...")
	print "Sales de tu casa y te miras hacia la calle. Está más tranquila que de costumbre, pero nada más alla de eso."
	raw_input("...")
	raw_input("")
	print "Ves una silueta cerca de donde está el auto de un vecino. ¿Vas a ver quién es?: Y / N"
	choice2 =raw_input("")
	if choice2.lower().startswith('y'):
		print "..."
		raw_input("Te acercas tranquilamente, mientras que la silueta se hace más y más clara.")
		raw_input("")
		print "!!!"
		raw_input("")
		raw_input("¡Tus ojos no pueden creer lo que ven! Desde lejos no se notaba, pero te has topado con algo que definitivamente no es de este mundo!")
		raw_input("")

	else:
		print "......"
		raw_input("")
		print "Te das vuelta para entrar a tu casa, en ese momento escuchas un ruido."
		raw_input("")
		print "¿Te das vuelta a ver de qué se trata? : Y / N"
		choice3 =raw_input("")
		if choice3.lower().startswith('y'):
			print "..."
			raw_input("...")
			raw_input("")
			print "Sin tiempo de reaccionar, una bestia fantástica corre hacia ti y te ataca--"
			raw_input("SLASH!")
			raw_input("")
			print "Con garras tan largas y filosas como cuchillos, este ser corta tu carne sin mucha resistencia."
			raw_input("")
			print "Mueres a los pocos segundos por los cortes severos que recives en tus partes vitales."
			raw_input("")
			print "BAD END 3"
			raw_input("")

		else:
			raw_input(" ... \"¿Supongo que después de todo no pasó nada?\" -- Piensas en voz alta mientras ladeas tu cabeza y levantas los hombros.")
			raw_input("")
			raw_input(" \"No sé qué estaba esperando que sucediese...\"")
			raw_input("")
			raw_input(" \"...\" ")
			raw_input("")
			raw_input("Decides cerrar la puerta y volver a la cama para intentar dormir de nuevo.")
			raw_input("")
			print "BAD END 2"
			raw_input("")
			raw_input("")
			raw_input("")

else:
	print "......"
	raw_input(" ... \"Haa...\" -- Se te escapa un suspiro.")
	raw_input("")
	raw_input(" \"No sé qué estaba esperando que sucediese...\" -- Te preguntas en voz alta.")
	raw_input("")
	raw_input(" \"...\" ")
	raw_input("")
	raw_input("Decides cerrar la ventana y volver a la cama para intentar dormir de nuevo.")
	raw_input("")
	print "BAD END"
	raw_input("")
	raw_input("")
	raw_input("")