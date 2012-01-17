# -*- coding: utf-8 -*-
"""
Kick Ass FX
copyright Barraco Mármol Jerónimo, David Pineda Melendez, Martín (Abelkm) y Colaboradores 2007
GNU/GPL
"""

"""
Nota IMPORTANTE
por cuestion de tiempo las cosas se van a ir implementando a medida q sean necesarias y en forma que sean necesarias,
siempre y cuando no sea una cosa rebuscada que no sea extensible.
"""
import traceback, cProfile

traceback.sys.stdout = open('stdout.txt', 'w', 0)
traceback.sys.stderr = open('stderr.txt', 'w', 0)


version_info = (1, 8, 0, 'newfinalrc4')
print 'Python version', traceback.sys.version_info
if traceback.sys.version_info[:3] < (2, 6, 6):
	print """
	La versión de python que esta usando es menor a 2.6.6, esto puede traer problema con cairo.
	Por favor intente usar la versión 2.6.6 de python, o la última versión de python 2.6 (pero no 2.7 ni 3.2)
	"""
#TODO agregar verificacion de frame >=0 en carga de tiempos... porque me odias abel???
#TODO agregar verificacion de que se haya cargado el effect correctamente
#TODO cambiar el preload para que organice las cosas como debe

print "Cargando Cairo..." #si, el sistema de loggin rulea
import cairo
#import cProfile
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
error_obj = asslib.cSilaba(asslib.cProperties())
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
		lasty = error_obj.ChangeText(n, (15, lasty))[1] + error_obj.original._alto_linea
		error_obj.Paint()

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
		fop.set_antialias(cairo.ANTIALIAS_SUBPIXEL)#hay que ver si esto no lo hace mas lento

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
		DBug("Precalculando los events\n")
		__PreLoad()
		DBug("Todo se cargo aparentemente bien\n")
	except:
		print "Something bad happened and we don't know what it is. It is really bad. Seriously, it is really bad. Really."
		Error()

def OnFrame(pframe, stride, cuadro):
	"""Esta funcion se llama desde la dll
	Llamada por cada cuadro
	"""
	try:
		global fx, no_frames
		if fx.skip_frames: #Verificamos si se desea procesar el cuadro o si lo devolvemos tal cual
			if pframe > len(no_frames): return
			if no_frames[pframe]: return

		global cf, fop, vi
		cf.framen = pframe
		cf.sfc = cairo.ImageSurface.create_for_data(cuadro, vi.modo, vi.width, vi.height, stride)
		cf.ctx = cairo.Context(cf.sfc)

		cf.ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
		#cairo.ANTIALIAS_SUBPIXEL
		#cairo.ANTIALIAS_NONE
		#cairo.ANTIALIAS_GRAY
		cf.ctx.set_font_options(fop)
		cf.ctx.set_line_join(cairo.LINE_JOIN_ROUND)
		cf.ctx.set_line_cap(cairo.LINE_CAP_ROUND)

		#definitivamente nadie lo usa. lo deshabilite porque usa mucho CPU
		#cf.tiempo = video.CuadroAMS(cf.framen)

		#Llamamos a los events
		__CallFuncs()
		cf.sfc.flush()
	except:
		print "e"
		Error()

def __CallFuncsProfile():
	cProfile.runctx('__CallFuncsNormal()', globals(), locals(), filename='profile')

def __CallFuncsNormal():
	"""Esta funcion llama a todos los events del efecto
	Si agregan un evento no olvidar ponerlo en __PreLoad"""
	global fx, frames, cf

	frame = frames[cf.framen]
	fx.OnFrameStarts()

	#Nueva forma de llamar, por events
	for (evento, o, prog) in frame:
		o.progress = prog
		if fx.reset_style:
			o.Restore()
		evento(o)

	fx.OnFrameEnds()

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

def __AddEvent(ini, end, dif, evento, element):
	global frames, noframes
	ms2f = video.vi.MSToFrame
	cfn = video.vi.ClampFrameNum
	inif = cfn(ms2f(ini))
	endf = cfn(ms2f(end))
	diff = float(ms2f(dif)-1) or 1.0
	for i, f in enumerate(xrange(inif, endf)):
		p = i/diff
		frames[f].append((evento, element, p ) )
		no_frames[f] = False

def __PreLoad():
	"""Esta función crea los arrays de no_frames y frames,
		y también inicializa las cosas del efecto
	"""

	global frames, fx, ass, no_frames
	from libs.draw import avanzado

	num_frames = vi.num_frames #la cantidad de frames totales
	fs = fx.fxs #la lista de efectos
	avanzado.fBlur = avanzado.fBlurs[fx.blur_type] #elegimos el tipo de blur segun la configuración

	#no_frames = [True for i in xrange(num_frames+1)] #this way is slower
	no_frames = [True, ]*(num_frames+1)#el objeto no_frames es una lista con los cuadros que no quieren ser procesados
	#frames = [[]]*(num_frames+1) #no hagan esto, porque [] es la misma instancia, o sea, todos los frames referencian al mismo = desastre
	frames = [ [] for i in range(num_frames+1) ] #creamos el objeto frames q contiene todos los objetos de dialogues

	"""
	Nota: si bien el array frame es una referencia directa a cada frame,
	los tiempos en las syllables/dialogues están guardados en milisegundos,
	con la esperanza de darle mayor presición.
	"""

	#cacheo las funciones porque soy raton #this actually speed things up
	dialogos = ass.dialogues

	#Para poder hacer que las cosas se pinten en un orden predeterminado es necesario
	#iterar varias veces cada objeto, una por cada evento. caso contrario, se pisan.

	#los tiempos van siempre en ms para tener presición
	for diag in dialogos:
		diag.progress = 0.0
		#effect se usa más abajo en events extras y las syllables lo cambian
		#notar que cada dialogo y silaba puede tener un effect individual (sobre todo con el inline fx >.>;)
		efecto = fs[diag.effect]

		#Llamamos a la función de cuando se inicia el dialogo
		#No es necsaria una iteracion especial para esto, ya que no deberia pintarse nada aca
		inicio = getattr(efecto, "OnDialogueStarts", None)
		if inicio: inicio(diag)

		#Dialogo Sale
		#nos fijamos si definio la funcion EnDialogoSale
		evento = getattr(efecto, "OnDialogueOut", None)
		#Si no la definio entonces no la quiere, y no la cargamos y con continue vamos al siguiente dialogo
		if not evento: continue

		ini = diag._end
		end = diag._end + fx.out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Dialogo Entra
	for diag in dialogos:
		evento = getattr(fs[diag.effect], "OnDialogueIn", None)
		if not evento: continue

		ini = diag._start - fx.in_ms
		end = diag._start
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Dialogo Animado o Activo
	for diag in dialogos:
		evento = getattr(fs[diag.effect], "OnDialogue", None)
		if not evento: continue

		ini = diag._start
		end = diag._end
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Eventos personalizados
	for diag in dialogos:
		eventos = getattr(fs[diag.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios events extras en cada effect
			enDialogo = getattr(evento, "OnDialogue", None)
			if not enDialogo: continue

			ini, end = evento.TiempoDialogo(diag)
			dif = end - ini
			__AddEvent(ini, end, dif, enDialogo, diag)

	#Prelodeamos las syllables :D
	for diag in dialogos:
		__PreLoadSyllables(diag)

	#Necesario poner esto aca para que las maldetas syllables no pisen las letras
	#sep, una vez mas, no queda otra
	if fx.split_letters:
		for diag in dialogos:
			syllables = diag._syllables
			for sil in syllables:
				__PreLoadLetters(sil)

	#primero ordenamos los dialogues/syllables/letras en cada frame segun sus layers
	#(aun asi quedan dialogues bajo syllables bajo letras (en el mismo layer en el mismo frame))
	def keyfunc(item):
		"""una funcion que por cada item en cada frame, devuelve el valor con que comparar
		explicado es:
		cada frame contiene muchos items, al ordenarlo, se llama a esta funcion por cada item
		cada item posee 3 elementos, el evento, el dialogo y el progress
		tomamos el elemento 1 (el 2º) el dialogo.
		del dialogo tomamos el estilo original, y de ahi el layer
		"""
		return item[1].original._layer
		#pd: podría usar lambda, pero lo odio :D

	for i in range(len(frames)):
		f = frames[i]
		f.sort(key=keyfunc)
		#lo pasamos a tuplas con el afan de hacerlo más rapido...
		frames[i] = tuple(f)
	#a este tambien
	frames = tuple(frames)
	#y a este
	no_frames = tuple(no_frames)

def __PreLoadSyllables(diag):
	"""
		Carga las syllables
	"""
	#notar que esto se ejecuta por cada dialogo
	global fx
	#cacheos varios
	fs = fx.fxs

	#Ahora las syllables!!! (T^T)
	syllables = diag._syllables

	#Inicio
	for sil in syllables:
		sil.progress = 0.0
		#1º la inicializamos
		inicio = getattr(fs[sil.effect], "OnSyllableStarts", None)
		if inicio: inicio(sil)

	#Zilaba Muerta
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableDead", None)
		if not evento: continue

		ini = sil._end
		end = diag._end
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)

	#Silaba Dormida
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableSleep", None)
		if not evento: continue

		ini = diag._start
		end = sil._start
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)


	#Silaba sale
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableOut", None)
		if not evento: continue

		ini = sil._end
		end = sil._end + fx.sil_out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)

	#Silaba entra
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableIn", None)
		if not evento: continue

		ini = sil._start - fx.sil_in_ms
		end = sil._start
		dif = end-ini
		__AddEvent(ini, end, dif, evento, sil)

	#Silaba Animada
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllable", None)
		if not evento: continue

		ini = sil._start
		end = sil._end
		dif = end-ini
		__AddEvent(ini, end, dif, evento, sil)

	#Eventos personalizados
	for sil in syllables:
		eventos = getattr(fs[sil.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			enSilaba = getattr(evento, "OnSyllable", None)
			if not enSilaba: continue
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios events extras en cada effect
			ini, end = evento.TiempoSilaba(sil)
			dif = end - ini
			__AddEvent(ini, end, dif, enSilaba, sil)


def __PreLoadLetters(sil):
	#ahora las letras T_T
	#esto ya me parece una locura.
	#si quieren dividir un effect por letras, por favor usen el aegisub
	global  fx
	#cacheos varios
	fs = fx.fxs

	#Creamos las letras (ya que sino no se crean en memoria)
	sil.SplitLetters()
	letras = sil._letters

	#inicio y letra entra
	for letra in letras:
		letra.progress = 0.0

		efecto = fs[letra.effect]

		inicio = getattr(efecto, "OnLetterStarts", None)
		if inicio: inicio(letra)

		evento = getattr(fs[sil.effect], "OnLetterDead", None)
		if not evento: continue

		ini = letra._end
		end = sil._end
		dif = end - ini
		__AddEvent(ini, end, dif, evento, letra)


	for letra in letras:
		evento = getattr(fs[sil.effect], "OnLetterSleep", None)
		if not evento: continue

		ini = sil._start
		end = letra._start
		dif = end - ini
		__AddEvent(ini, end, dif, evento, letra)

	for letra in letras:
		letra.progress = 0.0
		efecto = fs[letra.effect]
		evento = getattr(efecto, "OnLetterIn", None)
		if not evento: continue

		ini = letra._start - fx.letter_in_ms
		end = letra._start
		dif = end-ini
		__AddEvent(ini, end, dif, evento, letra)

	#letra sale
	for letra in letras:
		evento = getattr(fs[letra.effect], "OnLetterOut", None)
		if not evento: continue

		ini = letra._end
		end = letra._end + fx.letter_out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, letra)

	#letra Animada
	for letra in letras:
		evento = getattr(fs[letra.effect], "OnLetter", None)
		if not evento: continue

		ini = letra._start
		end = letra._end
		dif = end-ini
		__AddEvent(ini, end, dif, evento, letra)

	#Eventos personalizados
	for letra in letras:
		eventos = getattr(fs[letra.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			enLetra = getattr(evento, "OnLetter", None)
			if not enLetra: continue
			#Calculamos la duracion de cada evento extra
			#Notar que puede haber varios events extras en cada effect
			ini, end = evento.TiempoLetra(letra)
			dif = end - ini
			__AddEvent(ini, end, dif, enLetra, letra)

