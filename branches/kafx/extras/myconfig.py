# -*- coding: utf-8 -*-
assfile = "fma.ass"
fx = 'fxs.Usados.secretl'
#fx = 'fxs.t'
#video_in = 'tos open2.avi'
video_in = "fma.avi"
video_out = 'out.avi'

width = 720
height = 402
fps = 23.976
frames = 2232 #cantidad de cuadros
start_frame = 0
#Parameters for output video. "As seen in" ffmpeg
out_parameters = ['-target', 'ntsc-dvd' ,'-y', video_out ]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#	'-mbd', 'rd', '-flags', '+4mv+aic', '-trellis', '2', '-cmp', '2', '-subcmp', '2', '-g', '300',
#	'-vcodec', 'mpeg4', '-vtag', 'xvid',

out_parameters = [
'-i' , video_in, '-map','0:0', '-map', '1:1',
'-acodec', 'copy',
'-sameq',
'-vcodec', 'mpeg4', '-vtag', 'xvid', '-y', video_out ]
