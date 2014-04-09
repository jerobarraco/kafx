# -*- coding: utf-8 -*-
assfile = "empty.ass"
fx = 'fxs.simple'

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

"""tos"""
video_in ="tos open2.avi"
video_out ="out.avi"
audio_in = ''

fps = 29.970000
width = 640
height = 358
frames = 100000
start_frame = 0
#Parameters for output video. "As seen in" ffmpeg
#this is the simpliest case
#out_parameters = ['-target', 'ntsc-dvd', '-y' , video_out]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#todo put this in other module
#Parameters for output video. "As seen in" ffmpeg
#this is the simpliest case
#out_parameters = ['-target', 'ntsc-dvd', '-y' , video_out]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#this is the config nande uses , it copies the audio from source automatically
_with_audio = ['-i' , video_in, '-map','0:0', '-map', '1:1'] #this is used to copy the audio from the original video
_with_ext_audio = ['-i', audio_in, '-map','0:0', '-map', '1:0'] #this is used to copy the audio from another audio

_a_mp3 = ['-acodec', 'libmp3lame', '-ab', '192k']
_a_aac = ["-acodec", "libvo_aacenc", '-ab', '96k']
_a_copy = ["-acodec", "copy"]
_v_mp4 = ['-vcodec', 'mpeg4', "-f", 'mp4']
_v_xvid = ['-vcodec', 'mpeg4', '-vtag', 'xvid', ]
_v_ffv1 = ['-vcodec', 'ffv1']
_webpm = ['-vcodec', 'libvpx', '-vpre', 'libvpx-720p', '-b:v', '3900k', '-acodec', 'libvorbis', '-b:a', '100k']
#out_parameters = [ '-sameq' ] + _with_audio + _a_mp3 + _v_xvid +['-y', video_out]
out_parameters = _with_audio + _a_copy + [ '-sameq' ] +  _v_xvid +['-y', video_out]