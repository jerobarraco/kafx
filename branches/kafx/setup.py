#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""setup

Package installer for kafx.

"""

try:

	from distribute_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages


except ImportError, e:
	print e
	print """
	You don't have distribute installed, run:
  $ curl -O http://python-distribute.org/distribute_setup.py
	$ python distribute_setup.py"""
	exit(1)
#no puedo hacer que haga lo que yo quiero, automáticamente incluye las cosas del svn, asi que lo dejo asi
import kafx_main
setup(
	name = "kafx",
	version = '.'.join(map(str, kafx_main.version_info)),
	author = "Jerónimo Barraco Mármol",
 	author_email = "jerobarraco@yahoo.com.ar",
	url = "http://kafx.com.ar",
	download_url="http://kafx.com.ar",
	description = "A software for creating Karaoke Effects (vector graphics animation on video)",
	install_requires = ['pygtk', 'pycairo', 'pyopengl'],
	long_description = """A software for creating Karaoke Effects (vector graphics animation on video)""",
	license = "GNU LGPL",
	platforms = "Platform Independent",
	provides = ['kafx'],#importante para poder poner "import kafx"
	include_package_data=True,
	packages=find_packages(),
	#namespace_packages=['kafx'],
	#package_dir = {'':'kafx'},#NO! esto hace que construya adentro de kafx/
 	#package_data = {
	#		'':['*.ass'],
	#		'texturas':['*.png'],
	#		'bpm':'*.bpm',
	#		'':[
	#			'kafx_main.py',
	#			'kafx.py',
	#			'myconfig.py'
	#		],
	#		'':[
	#			'kafx.dll'
	#		]
	#},
	zip_safe=False,
  keywords = "kafx cairo python video audio text karaoke .ass",
  classifiers = [
	"Operating System :: OS Independent",
    "Programming Language :: Python",
	"Programming Language :: Python :: 2",
	"Natural Language :: Spanish",
 	#"License :: GNU Library or Lesser General Public License (LGPL)",
  	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
 	"Topic :: Multimedia",
 	]
#,
 #dependency_links = [
 #	'http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.0.win32-py2.6.msi'
 #]
 )