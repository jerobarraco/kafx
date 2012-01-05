#-------------------------------------------------
#
# Project created by QtCreator 2011-12-28T18:27:58
#
#-------------------------------------------------

QT       += core gui

TARGET = kafx_d_generator
TEMPLATE = app
TRANSLATIONS = kafx_es.tr

SOURCES += main.cpp\
        mainwindow.cpp \
    fxsgroup.cpp \
    effect.cpp \
    event.cpp \
    dialog.cpp \
    action.cpp \
    dachangecolor.cpp \
    acchangecolor.cpp \
    acsettexture.cpp \
    dasettexture.cpp \
    deffect.cpp \
    datwovalues.cpp \
    acmove.cpp \
    damove.cpp \
    daonevalue.cpp \
    aconevalue.cpp \
    dawiggle.cpp \
    acwiggle.cpp \
    acfunction.cpp \
    acinterpolate.cpp \
    dafillmode.cpp \
    acfillmode.cpp

HEADERS  += mainwindow.h \
    fxsgroup.h \
    effect.h \
    event.h \
    dialog.h \
    action.h \
    dachangecolor.h \
    acchangecolor.h \
    acsettexture.h \
    dasettexture.h \
    deffect.h \
    datwovalues.h \
    acmove.h \
    damove.h \
    daonevalue.h \
    aconevalue.h \
    dawiggle.h \
    acwiggle.h \
    acfunction.h \
    acinterpolate.h \
    dafillmode.h \
    acfillmode.h

FORMS    += mainwindow.ui \
    dialog.ui \
    dachangecolor.ui \
    dasettexture.ui \
    deffect.ui \
    datwovalues.ui \
    damove.ui \
    daonevalue.ui \
    dawiggle.ui \
    dafillmode.ui

RESOURCES += \
		resources.qrc

win32:RC_FILE = icono.rc
