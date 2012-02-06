# -*- coding: utf-8 -*-

from libs import common, audio
from libs.draw import advanced

class FX1(common.Fx):
	def __init__(self):
	  self.mov = 0
	  self.bpm = audio.BPM('fxs/Tutoriales/wave2.bpm')

	def EnDialogo(self,  d):
	  d.PintarConCache()

	def EnSilaba(self, d):
	  d.actual.modo_relleno = d.P_DEG_VERT
	  d.PintarConCache()
	  bpm = self.bpm.RevBPM()
	  if bpm < 0.5 : bpm =0.0
	  amp = 3 * bpm
	  freq = 0.1*bpm

	  advanced.ModoPintado('add')
	  advanced.StartGroup()
	  d.PintarConCache()
	  advanced.fWave( amp, freq, amp)

	  advanced.EndGroup()
	  advanced.ModoPintado('over')

class FxsGroup(common.FxsGroup):
	def __init__(self):
		self.in_ms = 250
		self.out_ms = 250
		self.syl_in_ms = 200
		self.syl_out_ms = 200
		self.blur_type = 0
		self.fxs = (FX1(),FX1() )
