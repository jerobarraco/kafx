# -*- coding: utf-8 -*-
#fx = 'fxs.tutorials.t0037_deformar'
#fx = 'fxs.AbelKM.parts3D'
#fx = 'fxs.Abelkm.parts3'
fx = 'fxs.simple_audio'
#fx = 'fxs.used.badapple'
assfile = "empty.ass"
#assfile = "guilty/guilty.ass"
#video_in ="guilty/vid.avi"
video_in ="base_negra.mkv"
audio_in = "audio.mp3"
#video_in = "tos open2.avi"
#video_in ="guile.mp4"
video_out ="sing.avi"
start_frame = 0

#Parameters for output video. "As seen in" ffmpeg
#this is the simpliest case
#out_parameters = ['-target', 'ntsc-dvd', '-y' , video_out]#using target solves REALLY a LLLOOOOOOOOOOOOT of problems.

#this is the config nande uses , it copies the audio from source automatically
_with_audio = ['-i' , video_in, '-map','0:0', '-map', '1:1'] #this is used to copy the audio from the original video
_with_ext_audio = ['-i', audio_in, '-map','0:0', '-map', '1:0'] #this is used to copy the audio from another mp3

_a_mp3 = ['-acodec', 'libmp3lame', '-ab', '192k']
_a_aac = ["-acodec", "libvo_aacenc", '-ab', '96k']
_a_copy = ["-acodec", "copy"]
_v_mp4 = ['-vcodec', 'mpeg4', "-f", 'mp4']
_v_xvid = ['-vcodec', 'mpeg4', '-vtag', 'xvid', ]
_v_ffv1 = ['-vcodec', 'ffv1']
_webpm = ['-vcodec', 'libvpx', '-vpre', 'libvpx-720p', '-b:v', '3900k', '-acodec', 'libvorbis', '-b:a', '100k']
#out_parameters = [ '-sameq' ] + _with_audio + _a_mp3 + _v_xvid +['-y', video_out]
out_parameters = _with_ext_audio + _a_copy + [ '-sameq' ] +  _v_xvid + ['-y', video_out]
