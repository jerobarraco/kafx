# -*- coding: utf-8 -*-
"""
Kick Ass FX
copyright Barraco Mármol Jerónimo, David Pineda Melendez, Martín (Abelkm) y Colaboradores 2007
GNU/GPL
"""

"""
Nota IMPORTANTE por cuestion d tiempo NIGUNA libreria ni nada está programada completa ni mucho menos
las cosas se van a ir implementando a medida q sean necesarias y en forma que sean necesarias, siempre y cuando no sea una cosa rebuscada que no sea extensible.
asique veran que les faltan varias cosas a las librerias y muchisimas cosas por implementar
"""
import traceback, cProfile
"""
#lo dejamos por lo de kafx.py, hay que sacarlo de la dll
traceback.sys.stdout = open('stdout.txt', 'w', 0)
traceback.sys.stderr = open('stderr.txt',  'w', 0)
"""
version_info = (1, 7, 1)
print 'Python version', traceback.sys.version_info
if traceback.sys.version_info[:3] < (2, 6, 6):
	"""
	La versión de python que esta usando es menor a 2.6.6, esto puede traer problema con cairo.
	Por favor intente usar la versión 2.6.6 de python, o la última versión de python 2.6 (pero no 2.7 ni 3.2)
	"""
#TODO agregar verificacion de frame >=0 en carga de tiempos... porque me odias abel???
#TODO agregar verificacion de que se haya cargado el efecto correctamente

print "Cargando Cairo..." #si, el sistema de loggin rulea
import cairo
print 'Cairo cargado. Version:', cairo.version_info
print 'Cargando KAFX...'
from libs import video, comun, asslib
#Poner librerias recien a partir de acá :D

#hasta aca
print 'KAFX cargado. Librerias version:', version_info
print "Yay! se han cargado todas las librerias."

#Estos son los objetos globales, no muy buena práctica pero ayudan.
#cf y vi es una gran chanchada, son los mismos objetos que en video (y deben ser los mismos)
cf = None
vi = None
error_obj = asslib.cSilaba(asslib.cPropiedades())
fx = None
frames = []
no_frames = [] #cache the wantframes, wich seems to be a very slow and important for optimization.
fop = None
m = None
ass = None


def DBug(msg):
	#Esta funcion es llamada desde la dll, imprime el error actual
	traceback.sys.stdout.write(str(msg))

def PintarEnPantalla(msg):
	"pone un texto en pantalla, super slow, soporta multilinea"
	global error_obj
	lasty = 15
	for n in msg.split('\n'):
		lasty = error_obj.CambiarTexto(n, (15, lasty))[1] + error_obj.original._alto_linea
		error_obj.Pintar()

def Error(msg=""):
	"""Escribe un mensaje de error al archivo y en la pantalla,
	no siempre escribe en la pantalla, depende del error"""
	traceback.sys.stderr.write (msg+"\n")
	traceback.print_exc()
	traceback.sys.stderr.write ("\n---------------\n")
	PintarEnPantalla(traceback.format_exc())

def OnDestroy():
	"""Esta funcion es llamada desde la dll
	se llama antes de destruir todo, en python es completamente innecesario usar esto.. pero por si acaso lo dejo...
	mejor si intentan usar los metodos especiales de las clases como __del__
	"""
	print ('Me voy, me dijeron que termine')

def OnInit(filename, assfile, pixel_type, image_type, width, height, fpsn, fpsd, numframes):
	"""Esta funcion es llamada desde la dll
	inicializa todas las cosas.
	"""
	try:
		global fop, cf, vi, m, fx, ass
		DBug("ME INICIALIZAN\n")

		#Ponemos las opciones de fuentes
		fop = cairo.FontOptions()
		fop.set_antialias(cairo.ANTIALIAS_GRAY)

		#Cargamos la información del video
		cf = video.cf
		vi = video.vi
		vi.pixel_type = pixel_type #como se guarda los datos de un pixel, segun video
		vi.modo = video.GetMode(vi.pixel_type) #El modo de cairo
		vi.image_type = image_type
		vi.width = width
		vi.height = height
		vi.fps_numerator = fpsn
		vi.fps_denominator = fpsd
		vi.num_frames = numframes
		vi.fps = float(fpsn) /fpsd
		vi.fpscof1 = vi.fps / 1000.0
		vi.fpscof2 = 1000.0 / vi.fps
		vi.fake_stride = width*4 #para rgba
		#cf.tiempo = -1
		cf.ctx = cairo.Context(cairo.ImageSurface(vi.modo, vi.width, vi.height))
		#esto es porque para el ass, el tamaño d las fuentes es necesario un contexto y que tenga el tamaño correcto
		DBug("Importando el efecto\n")
		m = comun.MyImport(filename)
		DBug("Cargando los subtitulos\n")
		fx = m.FxsGroup()
		ass = asslib.Ass(assfile, len(fx.fxs) -1)
		DBug("Precalculando los eventos\n")
		__PreLoad()
		DBug("Todo se cargo aparentemente bien\n")
	except:
		print "e"
		Error()

def OnFrame(pframe, stride, cuadro):
	"""Esta funcion se llama desde la dll
	Llamada por cada cuadro
	"""
	try:
		global fx, no_frames
		if fx.saltar_cuadros: #Verificamos si se desea procesar el cuadro o si lo devolvemos tal cual
			if pframe > len(no_frames): return
			if no_frames[pframe]: return

		global cf, fop, vi
		cf.framen = pframe
		cf.sfc = cairo.ImageSurface.create_for_data(cuadro, vi.modo, vi.width, vi.height, stride)
		cf.ctx = cairo.Context(cf.sfc)

		cf.ctx.set_font_options(fop)
		cf.ctx.set_line_join(cairo.LINE_JOIN_ROUND)
		cf.ctx.set_line_cap(cairo.LINE_CAP_ROUND)
		cf.ctx.set_antialias(cairo.ANTIALIAS_GRAY)
		#definitivamente nadie lo usa. lo deshabilite porque usa mucho CPU
		#cf.tiempo = video.CuadroAMS(cf.framen)

		#Llamamos a los eventos
		#para habilitar el profiling descomentar la siguiente linea y comentar la que le sigue
		#cProfile.runctx('__CallFuncs()', globals(), locals(), filename='profile')
		__CallFuncs()
		cf.sfc.flush()
	except:
		print "e"
		Error()

def __CallFuncsProfile():
	cProfile.runctx('__CallFuncsNormal()', globals(), locals(), filename='profile')
	
def __CallFuncsNormal():
	"""Esta funcion llama a todos los eventos del efecto
	Si agregan un evento no olvidar ponerlo en __PreLoad"""
	global fx, frames, cf

	frame = frames[cf.framen]
	fx.EnCuadroInicia()

	#Nueva forma de llamar, por eventos
	for (evento, o, prog) in frame:
		o.progreso = prog
		if fx.reset_estilo:
			o.Restore()
		evento(o)

	fx.EnCuadroFin()

def __PreLoad():
	"""Esta función crea los arrays de no_frames y frames,
		y también inicializa las cosas del efecto
	"""

	global frames, vi, fx, ass, no_frames
	from libs.draw import avanzado

	num_frames = vi.num_frames #la cantidad de frames totales
	fs = fx.fxs #la lista de efectos
	avanzado.fBlur = avanzado.fBlurs[fx.tipo_blur] #elegimos el tipo de blur segun la configuración

	frames = [ [] for i in xrange(num_frames+1) ] #creamos el objeto frames q contiene todos los objetos de dialogos
	#frames = [[]]*(num_frames+1) #no hagan esto, porque [] es la misma instancia, o sea, todos los frames referencian al mismo = desastre
	#frames = [ comun.cFrame() for i in xrange(num_frames+1) ] #creamos el objeto frames q contiene todos los objetos de dialogos << no se utiliza
	#no_frames = [True for i in xrange(num_frames+1)]
	no_frames = [True, ]*(num_frames+1)#el objeto no_frames es una lista con los cuadros que no quieren ser procesados

	"""
	Nota: si bien el array frame es una referencia directa a cada frame,
	los tiempos en las silabas/dialogos están guardados en milisegundos,
	con la esperanza de darle mayor presicion.
	"""
	#cacheo las funciones porque soy raton
	ms2f = video.MSACuadro
	cfn = video.ClampFrameNum

	#los tiempos van siempre en ms para tener presición
	for diag in ass.dialogos:
		diag.progreso = 0.0
		#efecto se usa más abajo en eventos extras y las silabas lo cambian
		#notar que cada dialogo y silaba puede tener un efecto individual (sobre todo con el inline fx >.>;)
		efecto = fs[diag.efecto]

		#Llamamos a la función de cuando se inicia el dialogo
		efecto.EnDialogoInicia(diag)

		#Dialogo Sale
		ini = diag._end
		end = diag._end + fx.out_ms
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0 #division por zero
		for i, f in enumerate(xrange(inif, endf)): #El range es por frames
			p = i/diff #el +1 va en gusto, con +1 se aseguran de que llegue a 1.0, aunque puede pasarse, sin el +1 empieza siempre en 0, y quizas no llegue a 1.0
			#primero se van a dibujar todos los dialogos que salgan de todos los frames
			#frame[f] es el frame numero f, y es un array (array de dialogos con su progreso y evento)
			frames[f].append( (efecto.EnDialogoSale, diag, p) )
			#y marcamos el cuadro f como cuadro que no se puede saltear
			no_frames[f] = False

		#Dialogo Entra
		#Lo mismo p
		ini = diag._start - fx.in_ms
		end = diag._start
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(range(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnDialogoEntra, diag, p))
			no_frames[f] = False

		#Dialogo Animado o Activo
		ini = diag._start
		end = diag._end
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnDialogo, diag, p))
			no_frames[f]=False

		#Eventos personalizados
		for evento in efecto.eventos:
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios eventos extras en cada efecto
			ini, end = evento.TiempoDialogo(diag)
			dif = end - ini

			inif = cfn(ms2f(ini))
			endf = cfn(ms2f(end))
			diff = float(ms2f(dif)) or 1.0
			for i, f in enumerate(xrange(inif, endf)):
				p = i/diff
				frames[f].append( (evento.EnDialogo, diag, p ) )
				no_frames[f]=False

		#Prelodeamos las silabas :D
		#ojo con la indentación acá, notar que está dentro del for de los dialogos
		__PreLoadSilabas(diag)

	#esto tiene que ir al final de toda la iteracion porque se supone que tienen que cargar todos los diag, silabas y letras PRIMERO
	#primero ordenamos los dialogos/silabas/letras en cada frame segun sus layers
	#(aun asi quedan dialogos bajo silabas bajo letras (en el mismo layer en el mismo frame))
	def keyfunc(item):
		"""una funcion que por cada item en cada frame, devuelve el valor con que comparar
		explicado es:
		cada frame contiene muchos items, al ordenarlo, se llama a esta funcion por cada item
		cada item posee 3 elementos, el evento, el dialogo y el progreso
		tomamos el elemento 1 (el 2º) el dialogo.
		del dialogo tomamos el estilo original, y de ahi el layer
		"""
		return item[1].original._capa
		#pd: podría usar lambda, pero lo odio :D

	for i in range(len(frames)):
		f = frames[i]
		f.sort(key=keyfunc)
		#lo pasamos a tuplas con el afan de hacerlo más rapido...
		#frames[i] = tuple(f)
	#a este tambien
	#frames = tuple(frames)

	#y a este
	no_frames = tuple(no_frames)

def __PreLoadSilabas(diag):
	#notar que esto se ejecuta por cada dialogo
	global frames, vi, fx, no_frames
	#cacheos varios
	fs = fx.fxs
	ms2f = video.MSACuadro
	cfn = video.ClampFrameNum

	#Ahora las Silabas!!! (T^T)
	for sil in diag._silabas:
		sil.progreso = 0.0
		efecto = fs[sil.efecto]
		efecto.EnSilabaInicia(sil)

		#Zilaba Muerta
		ini = sil._end
		end = diag._end
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnSilabaMuerta, sil, p ) )
			no_frames[f] = False

		#Silaba Dormida
		ini = diag._start
		end = sil._start
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnSilabaDorm, sil, p ) )
			no_frames[f]=False

		#Silaba entra
		ini = sil._start - fx.sil_in_ms
		end = sil._start
		dif = end-ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnSilabaEntra, sil, p) )
			no_frames[f]=False

		#Silaba sale
		ini = sil._end
		end = sil._end + fx.sil_out_ms
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnSilabaSale, sil, p ) )
			no_frames[f]=False

		#Silaba Animada
		ini = sil._start
		end = sil._end
		dif = end-ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnSilaba, sil, p ))
			no_frames[f] = False

			#Eventos personalizados
		for evento in efecto.eventos:
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios eventos extras en cada efecto
			ini, end = evento.TiempoSilaba(sil)
			dif = end - ini

			inif = cfn(ms2f(ini))
			endf = cfn(ms2f(end))
			diff = float(ms2f(dif)) or 1.0
			for i, f in enumerate(xrange(inif, endf)):
				p = i/diff
				frames[f].append( (evento.EnSilaba, sil, p ) )
				no_frames[f]=False

		if fx.dividir_letras:
			__PreLoadLetras(sil)

def __PreLoadLetras(sil):
	#ahora las letras T_T
	#esto ya me parece una locura.
	#si quieren dividir un efecto por letras, por favor usen el aegisub
	global frames, vi, fx, no_frames
	#cacheos varios
	fs = fx.fxs
	ms2f = video.MSACuadro
	cfn = video.ClampFrameNum

	#Creamos las letras (ya que sino no se crean en memoria)
	sil.DividirLetras()
	for letra in sil._letras:
		#letra entra
		letra.progreso = 0.0
		efecto = fs[letra.efecto]
		efecto.EnLetraInicia(letra)

		ini = letra._start - fx.letra_in_ms
		end = letra._start
		dif = end-ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnLetraEntra, letra, p) )
			no_frames[f]=False

		#letra sale
		ini = letra._end
		end = letra._end + fx.letra_out_ms
		dif = end - ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnLetraSale, letra, p ) )
			no_frames[f] = False

		#letra Animada
		ini = letra._start
		end = letra._end
		dif = end-ini

		inif = cfn(ms2f(ini))
		endf = cfn(ms2f(end))
		diff = float(ms2f(dif)) or 1.0
		for i, f in enumerate(xrange(inif, endf)):
			p = i/diff
			frames[f].append( (efecto.EnLetra, letra, p ))
			no_frames[f] = False

		#Eventos personalizados
		for evento in efecto.eventos:
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios eventos extras en cada efecto
			ini, end = evento.TiempoLetra(letra)
			dif = end - ini

			inif = cfn(ms2f(ini))
			endf = cfn(ms2f(end))
			diff = float(ms2f(dif)) or 1.0
			for i, f in enumerate(xrange(inif, endf)):
				p = i/diff
				frames[f].append( (evento.EnLetra, letra, p ) )
				no_frames[f]=False

#Esto es para profiling, como es algo lento, intentamos hacerlo mas rapido con este hack
#En cualquier caso iniciamos la funcion __CallFuncs que se llama en OnFrame con el CallFuncsNormal
__CallFuncs = __CallFuncsNormal
def SetProfiling(do=False):
	global __CallFuncs, __CallFuncsNormal, __CallFuncsProfile
	#Si do es True (Y lo pongo en otra variable para que el dia de mañana pueda venir como parametro)
	if do:
		#CallFuncs ahora apunta al CallFuncs del Profile
		print "Profiling active"
		__CallFuncs = __CallFuncsProfile
	else:
		print "Profiling inactive"
		__CallFuncs = __CallFuncsNormal
		
#Esto podria venir por parametro luego
SetProfiling(False)