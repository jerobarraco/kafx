# -*- coding: utf-8 -*-
assfile = "fma.ass"
fx = 'fxs.Abelkm.znt'

"""
#this one is actually for comparing
#Fma
video_in = 'fma.avi'
video_out = 'out.avi'
fps = 29.976000000
width = 720
height = 402
frames = 100000
start_frame = 0
"""

"""
tos"""
video_in ="tos open2.avi"
video_out ="out.avi"
fps = 29.970000
width = 640
height = 358
frames = 100000
start_frame = 0
#Parameters for output video. "As seen in" ffmpeg 
#this is the simpliest case
#out_parameters = ['-target', 'ntsc-dvd', '-y' , video_out]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#this is the config nande uses , it copies the audio from source automatically
out_parameters = [
'-i' , video_in, '-map','0:0', '-map', '1:1',#this is used to copy the audio from the original video
'-sameq',
'-acodec', 'libmp3lame', '-ab', '192k',
'-vcodec', 'mpeg4', '-vtag', 'xvid',
'-y', video_out]
#