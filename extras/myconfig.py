# -*- coding: utf-8 -*-
assfile = "fma.ass"
fx = 'fxs.Usados.secretl'
video_in = "fma.avi"
video_out = 'out.avi'

width = 720
height = 402
fps = 23.976
frames = 2232 #cantidad de cuadros
start_frame = 0
#Parameters for output video. "As seen in" ffmpeg
#this is the simpliest case, uncomment this, and comment the next one to use it
#out_parameters = ['-target', 'ntsc-dvd' ,'-y', video_out ]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#this is the config nande uses , it copies the audio from source automatically
out_parameters = [
'-i' , video_in, '-map','0:0', '-map', '1:1',
'-acodec', 'copy',
'-sameq',
'-vcodec', 'mpeg4', '-vtag', 'xvid', '-y', video_out ]
