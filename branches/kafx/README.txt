How to install:
Avisynth only works for windows, so this is for windows users. 
Though i'm creating a script for running kafx using ffmpeg for encoding, in that case you won't need avisynth, and you can run on linux. 
Installing the other stuff in that case will be trivial.

When using windows, at ALL CASES you'll need 32bit binaries.
This is because Avisynth is in 32b, so the kafx api dll is 32 bits. so python is 32 bits. Also, cairo in 64 bits is experimental.
And on top of that i don't use 64b, so there's no real reason to have 2 dlls when we can use the old 32b.

For using on linux, there's an experimental way to achieve this, read "kafx without avisynth" on the "extra" folder


Simply install: (The order is very important)
1) Avisynth
2) Cairo (gtk+)
	Try using the installer : 
		Select the option that installs the "Compatibility DLL's"
		I recommend to install on the recommended location (<programfiles>/bin)		
3) Python 2.6.6 (for the dll)
4) PyCairo
	MAKE SURE PYTHON AND GTK+ ARE INSTALLED CORRECTLY BEFORE INSTALLING PYCAIRO
	Check that both, python AND gtk+ are in the path.
	Common locations are:
	c:\Python26
	c:\Python26\Scripts
	c:\Program Files\GTK2-runtime\bin
	

Copy this files to another folder, and play some .avs file (test.avs is the simplest one you can do to test the instalation)

Download Links:
Avisynth:
	From www.avisynth.org
	Example link: http://sourceforge.net/projects/avisynth2/

Python:
	From www.python.org
	You'll need python 2.6 (newest version of 2.6 (actually is 2.6.6) (not 2.7))
	example link: http://python.org/download/releases/2.6.6/

Cairo:
	From cairographics.org
	You need the binaries, you can get them installing gtk+.
	There are several ways of achieving this the best one is using the installer. 
	Using the installer:
		Example link: http://sourceforge.net/projects/gtk-win/ or http://gtk-win.sourceforge.net/home/index.php/en/Downloads

	If you can't get the installer, you can try luck with the binaries downloading the "gtk bundle" (i DO recommend the installer)
	Examples : from http://www.gtk.org/download-windows.html 
		2.16 (recommended) http://ftp.gnome.org/pub/gnome/binaries/win32/gtk+/2.16/gtk+-bundle_2.16.6-20100207_win32.zip
		2.22 (newer, less stable ) http://ftp.gnome.org/pub/gnome/binaries/win32/gtk+/2.22/gtk+-bundle_2.22.1-20101227_win32.zip
	In those cases you'll need to copy the content of the folder bin to some place in the "Path" that will be, kafx folder or c:\windows\system32

You can install PyGTK PyGObject and PyCairo by using the PyGtk-All-In-One (if you use this, you can skip the other 3 links down)
PyGtk-All-In-One
	http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.22/pygtk-all-in-one-2.22.6.win32-py2.6.msi 
	http://www.pygtk.org/ 
	
PyCairo
	From http://cairographics.org/pycairo/ or http://www.salsabeatmachine.org/python/pycairo-win32-packages.html
	The installer is "hidden" in some other place, i've found it here: http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/1.8/pycairo-1.8.10.win32-py2.6.exe

PyGTK (if you want to run cairodraw)
	http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.22/pygtk-2.22.0-1.win32-py2.6.exe
	
PyGObject

Optionals:

	PIL
		From http://www.pythonware.com/products/pil/
		Example link: http://effbot.org/downloads/PIL-1.1.7.win32-py2.6.exe
		IMPORTANT: this will actually requiere a system restart in order to work properly (even it doesnt tells you)

	PyOpenGl
		From http://pyopengl.sourceforge.net/ (or http://pypi.python.org/pypi/PyOpenGL and http://pypi.python.org/pypi/PyOpenGL-accelerate )
		Example link: 
			PyOpenGl http://pypi.python.org/packages/any/P/PyOpenGL/PyOpenGL-3.0.1.win32.exe#md5=513cc194af65af4c5a640cf9a1bd8462
			PyOpenGl-accelerate http://pypi.python.org/packages/2.6/P/PyOpenGL-accelerate/PyOpenGL-accelerate-3.0.1.win32-py2.6.exe#md5=11c46ad43040324d55ffaf4b04f25b87
