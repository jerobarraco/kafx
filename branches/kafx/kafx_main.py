# -*- coding: utf-8 -*-
"""
Kick Ass FX
copyright Barraco Mármol Jerónimo, David Pineda Melendez, Martín Dunn y Colaboradores 2007
GNU/GPL
"""

"""
Nota IMPORTANTE
por cuestion de tiempo las cosas se van a ir implementando a medida q sean necesarias y en forma que sean necesarias,
siempre y cuando no sea una cosa rebuscada que no sea extensible.
"""
import traceback, cProfile

#traceback.sys.stdout = open('kafx_log.txt', 'w', 0)
#traceback.sys.stderr = open('error_log.txt', 'w', 0)


version_info = (1, 8, 0, 'newfinalrc4')
print 'Python version', traceback.sys.version_info
if traceback.sys.version_info[:3] < (2, 7, 0):
	print """
	The python version used isn't 2.7, this can bring problems with cairo.
	Please try to use version  2.7 of python (do not use 3.2).
	"""
#TO-DO agregar verificacion de frame >=0 en carga de tiempos... porque me odias abel??? --Abelkm: esto no esta hecho ya?
#TO-DO agregar verificacion de que se haya cargado el effect correctamente -- Abelkm: idem
#TO-DO cambiar el preload para que organice las cosas como debe

print "Loading Cairo..." #si, el sistema de loggin rulea
import cairo
#import cProfile
print 'Cairo loaded. Version:', cairo.version_info
print 'Loading KAFX...'
from libs import video, common, asslib

#Insert libraries from here :D

#to here
print 'KAFX loaded. Libreries version:', version_info
print "Yay! The libraries were successfully loaded."

#This are the global objects, not a good thing to do but they help
#cf y vi are gross, same objects as in video (and they must be the same)
cf = None
vi = None
fx = None
frames = []
no_frames = [] #cache the wantframes, wich seems to be a very slow and important for optimization.
fop = None
m = None
ass = None

def DBug(msg):
	#This function is called from the dll, prints the actual error
	traceback.sys.stdout.write(str(msg))

def PainOnScreen(msg):
	"Prints text on screen, super slow, multiline supported"
	lasty = 10
	for line in msg.split('\n'):
		error_obj = asslib.cSyllable(line, last_pos=(20, lasty))
		error_obj.Paint()
		lasty += error_obj.original._line_height

def Error(msg=""):
	"""Prints the error message in archive and on screen,
	not always on screen, depends on the error"""
	traceback.sys.stderr.write (msg+"\n")
	traceback.print_exc()
	traceback.sys.stderr.write ("\n---------------\n")
	PainOnScreen(traceback.format_exc())

def OnDestroy():
	"""This function is called from the dll
	it's called before destroying everything, it's completely unnecessary to use this in python... but just in case...
	It's better to use special methods from __del__ class
	"""
	print "I'm leaving, I've been told to finish."

def OnInit(filename, assfile, pixel_type, image_type, width, height, fpsn, fpsd, numframes):
	"""This function is called from dll
	initialize everything
	"""
	try:
		global fop, cf, vi, m, fx, ass
		DBug("I'm being initialized...\n")

		#We put the Font Options
		fop = cairo.FontOptions()
		fop.set_antialias(cairo.ANTIALIAS_SUBPIXEL)#hay que ver si esto no lo hace mas lento

		#We load the information of the video Cargamos la información del video
		cf = video.cf
		vi = video.vi
		vi.pixel_type = pixel_type #the way the data of a pixel is saved, according to video
		vi.modo = video.GetMode(vi.pixel_type) #cairos mode
		vi.image_type = image_type
		vi.width = width
		vi.height = height
		vi.fps_numerator = fpsn
		vi.fps_denominator = fpsd
		vi.num_frames = numframes
		vi.fps = float(fpsn) /fpsd
		vi.fpscof1 = vi.fps / 1000.0
		vi.fpscof2 = 1000.0 / vi.fps
		vi.fake_stride = width*4 #for rgba
		#cf.tiempo = -1
		cf.ctx = cairo.Context(cairo.ImageSurface(vi.modo, vi.width, vi.height))
		#this is because the ass needs a contexts for the font size with the correct size
		DBug("Importing Effect.\n")
		m = common.MyImport(filename)
		DBug("Loading Subtitles.\n")
		fx = m.FxsGroup()
		ass = asslib.Ass(assfile, len(fx.fxs) -1)
		DBug("Making calculations for events.\n")
		__PreLoad()
		DBug("All was apparently successfully loaded.\n")
	except:
		print "Something bad happened and we don't know what it is. It is really bad. Seriously, it is really bad. Really."
		Error()

def OnFrame(pframe, stride, cuadro):
	"""This function is called from dll
	It's called for each frame
	"""
	try:
		global fx, no_frames
		if fx.skip_frames: #We verify if the frame wants to be processed or just return it
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

		#Calling the events
		__CallFuncs()
		cf.sfc.flush()
	except:
		print "e"
		Error()

def __CallFuncsProfile():
	cProfile.runctx('__CallFuncsNormal()', globals(), locals(), filename='profile')

def __CallFuncsNormal():
	"""This function calls all the events of the effect
	If an event is added, don't forget to add it in __PreLoad"""
	global fx, frames, cf

	frame = frames[cf.framen]
	fx.OnFrameStarts()

	#New way for calling per events
	for (evento, o, prog) in frame:
		o.progress = prog
		if fx.reset_style:
			o.Restore()
		evento(o)

	fx.OnFrameEnds()

#This is for profiling, as it is kind of slow, we try to make it faster with this hack
#Either way, we initialize __CalFuncs function that it's called in OnFrame with CallFuncsNormal
__CallFuncs = __CallFuncsNormal
def SetProfiling(do=False):
	global __CallFuncs, __CallFuncsNormal, __CallFuncsProfile
	#Si do es True (Y lo pongo en otra variable para que el dia de mañana pueda venir como parametro)
	if do:
		#CallFuncs now points to CallFuncs from Profile
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
	"""This function creates arrays of no_frames and frames,
	and initializes things of the effect, too
	"""

	global frames, fx, ass, no_frames
	from libs.draw import advanced

	num_frames = vi.num_frames #total number of frames
	fs = fx.fxs #list of effects
	advanced.fBlur = advanced.fBlurs[fx.blur_type] #we select the type of blur according to the configuration

	#no_frames = [True for i in xrange(num_frames+1)] #this way is slower
	no_frames = [True, ]*(num_frames+1)#the object no_frames is a list with the frames that don't want to be processed
	#frames = [[]]*(num_frames+1) #no hagan esto, porque [] es la misma instancia, o sea, todos los frames referencian al mismo = desastre
	frames = [ [] for i in range(num_frames+1) ] #we create the object 'frames' that has all the objects of dialogues

	"""
	Nota: Even though array frame is a direct reference to each frame,
	the times of syllables/dialogues are saved in miliseconds,
	with the hope of having more precision
	"""

	#functions cached #this actually speed things up
	dialogos = ass.dialogues

	#We need to iterate several times each object, one per event, this way
	#things will be draw in a predetermined order. Otherwise, they step over each other

	#Times are always in ms for better precision
	for diag in dialogos:
		diag.progress = 0.0
		#effect will be used later in events extras and the syllables will change it
		#please note that each dialogue and syllable can have an individual effect (especially with inline fx >.>;)
		efecto = fs[diag.effect]

		#We call the function when the dialogue is inicialized
		#There's no need for a special iteration for this, since there shouldn't be anything to draw here
		inicio = getattr(efecto, "OnDialogueStarts", None)
		if inicio: inicio(diag)

		#Dialogue leaves
		#we check if the OnDialogueOut is defined
		evento = getattr(efecto, "OnDialogueOut", None)
		#If it wasn't, it isn't wanted and we don't load it. We go to the next dialogye with 'continue'
		if not evento: continue

		ini = diag._end
		end = diag._end + fx.out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Dialogue enters
	for diag in dialogos:
		evento = getattr(fs[diag.effect], "OnDialogueIn", None)
		if not evento: continue

		ini = diag._start - fx.in_ms
		end = diag._start
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Animated or Active Dialogue
	for diag in dialogos:
		evento = getattr(fs[diag.effect], "OnDialogue", None)
		if not evento: continue

		ini = diag._start
		end = diag._end
		dif = end - ini
		__AddEvent(ini, end, dif, evento, diag)

	#Custom Events
	for diag in dialogos:
		eventos = getattr(fs[diag.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			#We calculate the duration of each extra event
			#Note that there can be several extra events in each effect
			enDialogo = getattr(evento, "OnDialogue", None)
			if not enDialogo: continue

			ini, end = evento.DialogueTime(diag)
			dif = end - ini
			__AddEvent(ini, end, dif, enDialogo, diag)

	#Preload of syllables :D
	for diag in dialogos:
		__PreLoadSyllables(diag)

	#This is necessary so that the syllables don't step over the letters
	#again, there's no other way
	if fx.split_letters:
		for diag in dialogos:
			syllables = diag._syllables
			for sil in syllables:
				__PreLoadLetters(sil)

	#First we order the dialogues/syllables/letters in each frame according to their layers
	#(still there are dialogues under syllables under letters (in the same layer in the same frame))
	def keyfunc(item):
		"""A function that for each item in each frame, returns the value which to compare with
		explanation:
		each frame contains several items, in the ordering process, this function is called for each item
		each item has 3 elements (event, dialogue and progress)
		we take the element 1 (the 2nd) the dialogue.
		from the dialogue we take the original style, and from there the layer
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
		Loads syllables
	"""
	#note that this is executed for each dialogue
	global fx
	#several caching
	fs = fx.fxs

	#Now the syllables!!! (T^T)
	syllables = diag._syllables

	#Beginning
	for sil in syllables:
		sil.progress = 0.0
		#1st inicialization
		inicio = getattr(fs[sil.effect], "OnSyllableStarts", None)
		if inicio: inicio(sil)

	#Dead Syllable
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableDead", None)
		if not evento: continue

		ini = sil._end
		end = diag._end
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)

	#Sleep Syllable
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableSleep", None)
		if not evento: continue

		ini = diag._start
		end = sil._start
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)


	#Syllable leaves
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableOut", None)
		if not evento: continue

		ini = sil._end
		end = sil._end + fx.syl_out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, sil)

	#Syllable enters
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllableIn", None)
		if not evento: continue

		ini = sil._start - fx.syl_in_ms
		end = sil._start
		dif = end-ini
		__AddEvent(ini, end, dif, evento, sil)

	#Animated Syllable
	for sil in syllables:
		evento = getattr(fs[sil.effect], "OnSyllable", None)
		if not evento: continue

		ini = sil._start
		end = sil._end
		dif = end-ini
		__AddEvent(ini, end, dif, evento, sil)

	#Custom Events
	for sil in syllables:
		eventos = getattr(fs[sil.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			enSilaba = getattr(evento, "OnSyllable", None)
			if not enSilaba: continue
			#Calculating the duration of each extra event
			#Note that there can be several extra events in each effect
			ini, end = evento.SyllableTime(sil)
			dif = end - ini
			__AddEvent(ini, end, dif, enSilaba, sil)


def __PreLoadLetters(sil):
	#now the letters T_T
	#this is insane.
	#If you want to split an effect per letter, use aegisub
	global  fx
	#several caches
	fs = fx.fxs

	#We create the letters (otherwise they will not be created in memory)
	sil.SplitLetters()
	letras = sil._letters

	#Beginning and letter enters
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

	#letter leaves
	for letra in letras:
		evento = getattr(fs[letra.effect], "OnLetterOut", None)
		if not evento: continue

		ini = letra._end
		end = letra._end + fx.letter_out_ms
		dif = end - ini
		__AddEvent(ini, end, dif, evento, letra)

	#Animated letter
	for letra in letras:
		evento = getattr(fs[letra.effect], "OnLetter", None)
		if not evento: continue

		ini = letra._start
		end = letra._end
		dif = end-ini
		__AddEvent(ini, end, dif, evento, letra)

	#Custom Events
	for letra in letras:
		eventos = getattr(fs[letra.effect], "events", None)
		if not eventos: continue

		for evento in eventos:
			enLetra = getattr(evento, "OnLetter", None)
			if not enLetra: continue
			#Calculating the duration of each extra event
			#Note that there can be several extra events in each effect
			ini, end = evento.LetterTime(letra)
			dif = end - ini
			__AddEvent(ini, end, dif, enLetra, letra)
#creo que falta traducir, al menos eso creo al ver "letra" y "enletra" escrito por ahi..., ademas, "evento/s".
