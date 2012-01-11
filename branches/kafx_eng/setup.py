#!/usr/bin/env python

from distutils.core import setup

from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(name = 'kafx',
        version = '1.6.2',
        description = 'laskd',
        author = 'nande',
        author_email = 'lol@nande.com.ar',
        url = 'kafx.com.ar',
        classifiers = [
              'Development Status :: 4 - Beta',
              'Development Status :: 5 - Production/Stable',
              'Development Status :: 6 - Mature',
              'Environment :: MacOS X :: Aqua',
              'Environment :: MacOS X :: Carbon',
              'Environment :: MacOS X :: Cocoa',
              'Environment :: Win32 (MS Windows)',
              'Environment :: X11 Applications :: GTK',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Information Technology',
              'Intended Audience :: Other Audience',
              'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
              'Natural Language :: English',
              'Natural Language :: Spanish',
              'Programming Language :: Python :: 2',
           ],
        packages = ['.', '.\\extras', '.\\fxs', '.\\fxs\\AbelKM', '.\\fxs\\Tutoriales', '.\\fxs\\Usados', '.\\fxs\\gg', '.\\fxs\\pruebas', '.\\fxs\\timh', '.\\libs', '.\\libs\\draw'],
        package_dir = {'.\\fxs\\pruebas': 'fxs\\pruebas', '.\\libs\\draw': 'libs\\draw', '.\\fxs\\Usados': 'fxs\\Usados', '.\\fxs\\timh': 'fxs\\timh', '.\\fxs': 'fxs', '.': '', '.\\fxs\\Tutoriales': 'fxs\\Tutoriales', '.\\libs': 'libs', '.\\fxs\\AbelKM': 'fxs\\AbelKM', '.\\extras': 'extras', '.\\fxs\\gg': 'fxs\\gg'},
        #scripts = ['path/to/script']
        )
