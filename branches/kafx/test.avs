#This is a test avs script, open it with the media player or any program
# like virtualdub or avsp to make it work or encode it.

#----------||||||||||||||||----------#
#          Start avs script
#----------||||||||||||||||----------#

loadplugin("KAFX.dll") #With this you load the dll of kafx
KillAudio(ColorBars()) #And with this you use a fake video, at the bottom are other options.
 
converttorgb32() #Don't remove, KAFX needs to work with alpha channel!

FlipVertical() #This makes the process a little bit faster, don't remove. 

KAFX("fxs.simple", "test.ass") #Here you can chose your fx script and your 

FlipVertical() #This makes the process a little bit faster, don't remove. 

#-----------|||||||||||||------------#
#           End of script
#-----------|||||||||||||------------#

#Other options for video source (there are more!):

#FFVideoSource("C:\folder_name\my_video.mkv",fpsnum=24000, fpsden=1001)#Highly Recommended.
#ffms2.dll is necessary to use this function, http://code.google.com/p/ffmpegsource/downloads/list

#AvcSource("C:\folder_name\my_video.mkv")#Needs to be indexed previously through dgavcindex,
# also recommended.

#DirectShowSource("C:\folder_name\my_video.mkv")#Good and easy to use, but can cause nullframes.
#AviSource("C:\folder_name\my_video.mkv")#Pretty old and not recommended at all!

#Way of use: replace the "KillAudio(ColorBars())" with the source you want.

#--------------|||||-----------------#
#              Notes
#--------------|||||-----------------#

#Don't remove either converttorgb32 nor FlipVertical!

#Remember to load the KAFX.dll; the video, using directshowsource, ffvideosource, or even with the 
#colorbars (and don't load two or more videos at the same time!); your python script 
#(without the *.py extention) and the subtitle file (with the extention *.ass).

#Make a copy of this file and have fun.

#As a side note, the "#" comments everything that is after it, so keep that in mind.