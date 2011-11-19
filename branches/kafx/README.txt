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
2) All in one (gtk+)
	Try using the installer : 
		Select the option that installs the "Compatibility DLL's"
		I recommend to install on the recommended location (<programfiles>/bin)		
3) Python 2.6.6 (for the dll)

	

Copy this files to another folder, and play some .avs file (test.avs is the simplest one you can do to test the instalation)

Download Links:
Avisynth:
	From www.avisynth.org
	Example link: http://sourceforge.net/projects/avisynth2/

Python:
	From www.python.org
	You'll need python 2.6 (newest version of 2.6 (actually is 2.6.6) (not 2.7))
	example link: http://python.org/download/releases/2.6.6/

All in one:
	http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.0.win32-py2.6.msi
	
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
