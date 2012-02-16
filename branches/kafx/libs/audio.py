# -*- coding: utf-8 -*-
"""Esta libreria trae funciones que tienen que ver con el audio.


Notas:
Al igual que con las particulas, la clase Datos requiere ciertas cosas para mantener sincronia con el video.

1) Debe llamarse al metodo "read" una y solo una vez por cada cuadro, ni mas ni menos
2) Los cuadros deben accesarse en orden
3) No deben saltarse cuadros

Por ultimo, el uso de Datos requiere tener instalado ffmpeg, y estar disponible.
(o sea, en el path o la carpeta del kafx)
"""
import subprocess, audioop

import video
class BPM():
	#Clase para el BPM (beat per minute)
	def __init__(self, fname=None):
		self.start = -1
		self.bpm = -1
		self.fpb = -1 #frames per beat
		if fname != None:
			self.OpenBPM(fname)

	def OpenBPM(self, arch):
		"""Abre un archivo especificando el BPM
		el archivo debe contener 2 numeros separados por una coma, el comienzo en milisegundos del beat y el BPM o sea beats per minute"""
		f = open(arch,"r")
		for l in f :
			args = l.split(',')
			if len(args)>1:
				self.start = video.MSACuadro(int(args[0].strip()))
				self.bpm = float(args[1].strip())
		vi = video.vi
		self.fpb = 60.0*vi.fps_numerator /vi.fps_denominator / self.bpm

	def BPM(self):
		"""devuelve un numero correspondiente a si el frame actual es un beat,
		1=beat todo lo demás no
		comienza en cero y va creciendo hasta 1, y vuelve a 0 de golpe
		"""
		if video.cf.framen < self.start: return -1
		time = video.cf.framen -self.start
		return (time % float(self.fpb)) /self.fpb

	def RevBPM(self):
		"""devuelve un numero correspondiente a si el frame actual es un beat,
		1=beat todo lo demás no
		comienza en 1 en un beat y decrece hasta 0 progresivamente
		"""
		if video.cf.framen < self.start: return -1
		time = video.cf.framen -self.start
		return (self.fpb -(time % float(self.fpb) ) ) / self.fpb


class Data():
	proc = None
	frames = ()
	maxint = float(2**31)

	def __init__(self, archive = None):
		"""@archivo nombre del archivo de donde tomar el audio. por ejemplo : 'mivideo.avi'"""
		self.frameRate = 44100 # --ar
		self.sampWidth = 4 #4 bytes --ab 32
		self.frameSize = int(self.frameRate / video.vi.fps)
		self.bufSize = self.frameSize*self.sampWidth
		self.args = [
			#video to decode
			'ffmpeg', '-loglevel', '3', '-i', archive,
			#pipe data
			'-vn',  '-acodec', 'pcm_s32le', '-ac', '1', '-ar' , str(self.frameRate), '-ab', '32', '-f', 'wav',
			'-y', '-' #-y IS important
		]
		self.proc = subprocess.Popen(
			self.args, bufsize=self.bufSize, stdout=subprocess.PIPE,
			stdin=open("audiofakein.txt", 'w'),  stderr=open('audioerr.txt', 'w')
		)

	def __del__(self):
		if self.proc:
			self.proc.terminate()

	def read(self):
		"""Lee una linea de datos, lo equivalente a un cuadro de video.
		Es necesario llamar a esta funcion por cada cuadro de video, para lograr sincronia
		(pej EnCuadroInicia)"""
		if self.proc :
			self.frames = self.proc.stdout.read(self.bufSize)
		else:
			self.frames = []
		return self.frames

	def rms(self):
		"""Devuelve el RMS para los datos actuales (Es como el poder del sonido)"""
		return audioop.rms(self.frames, self.sampWidth)/self.maxint

	def sample(self, frame):
		"""Devuelve el valor de uno de los datos,
		@cuadro : el numero de cuadro del cual se requiere el valor
		(debe ser menor a frameSize)"""

		if frame < len(self.frames):
			return audioop.getsample(self.frames, self.sampWidth, cuadro)/self.maxint
		else:
			return 0.0
