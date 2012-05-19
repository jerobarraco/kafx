# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:33:53 2012
@author: Nande!
simple hack, needs improving
execute like
python slideass.py directory_of_images
it uses .png files
"""

import sys, codecs, os, urllib2
from os import path
header= """[Script Info]
; Script generated by KickASS FX!
; http://kafx.com.ar/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes
Video Aspect Ratio: 0
Video Zoom: 6
Video Position: 0
Last Style Storage: Default
Collisions: Normal

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Trad,Footlight MT Light,34,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,1,0,2,10,10,40,1
Style: Default,Eco-Files,20,&H00E3A85E,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,1,2,8,10,10,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
dialogue = """Dialogue: 0,%s,%s,Default,,0000,0000,0000,,%s\n"""
enddiag = """Dialogue: 0,%s,%s,Default,,0000,0000,0000,1,Made Automagically with
Dialogue: 0,%s,%s,Default,,0000,0000,0030,1,KickASS FX! ( kafx.com.ar )
"""
def MSToTime(ms):
	"""Converts miliseconds in integer to a string from type '0:00:00.00' for ASS """
	string = "%s:%s:%s.%s"
	div, d = divmod(ms, 1000)
	d = int(d/10)
	div, s = divmod(div, 60)
	h, m = divmod(div, 60)
	return string %(h,m,s,d)

def doFolder(directory):
	from libs import video
	out = codecs.open("out.ass", "w", "utf-8")
	out.write(header)
	begin = 1500
	last = begin
	dur = 3000
	space = 500
	for entry in os.listdir(directory):
		if os.path.splitext(entry)[-1].lower() in('.png', '.jpg'):
			ini = MSToTime(last)
			last += dur
			end = MSToTime(last)
			last += space
			fullpath = os.path.join(directory, entry)
			line = dialogue % (ini, end, fullpath)
			out.write(line)
	b=MSToTime(begin)
	e=MSToTime(last)
	line = enddiag %(b,e,b,e)
	out.write(line)
	out.close()
	print "ASS CREATED!"

def FromFolder():
	doFolder(raw_input("Enter the folder of images: "))

#def Convert(data, fname):

def DownloadFromPicasa(gdc, album, username):
	print "Downloading pictures in", album.title.text
	photos = gdc.GetFeed(
	    '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
	        username, album.gphoto_id.text))

	for photo in photos.entry:
		print 'Downloading "%s" (%sx%s)'%(photo.title.text, photo.width.text, photo.height.text)
		url = photo.GetMediaURL()
		fname = 'picasa'+url.rsplit('/',1)[-1]
		open(fname, 'wb').write(urllib2.urlopen(url).read())

def ChooseAlbum(gdc, username):
	print "\tChoose album"
	albums = gdc.GetUserFeed(user=username)
	for i, album in enumerate(albums.entry):
		print '%s\tTitle: %s (%s)' % (i, album.title.text, album.numphotos.text)
	v = int(raw_input("> "))
	return albums.entry[v]

def FromPicasa():
	import gdata.photos.service
	import gdata.media
	import gdata.geo
	gdc = gdata.photos.service.PhotosService()
	gdc.email = raw_input("EMail: ")
	gdc.password = raw_input("Password (visible): ")
	gdc.source = "kafx"
	gdc.ProgrammaticLogin()
	username= 'default'
	#user = raw_input("Enter username: ")
	album = ChooseAlbum(gdc, username)
	if not os.path.exists('picasa/'):
		os.makedirs('picasa/')
	DownloadFromPicasa(gdc, album, username)
	doFolder('picasa/')


if __name__=='__main__':
	while True:
		if len(sys.argv) >1:
			doFolder(sys.argv[1])
		print "Enter your choice :\n\t1 Local folder\n\t2 Picasa album\n\t0 Exit"
		v = int(raw_input('> '))
		if v == 0:
			break
		elif v == 1:
			FromFolder()
		elif v == 2:
			FromPicasa()