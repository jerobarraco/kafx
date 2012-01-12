#-------------------------------------------------
#
# Project created by QtCreator 2012-01-12T16:27:07
#
#-------------------------------------------------

QT       -= core gui

TARGET = kafx
TEMPLATE = lib
CONFIG += dll

DEFINES += KAFX_LIBRARY

SOURCES += kafx.cpp \
    raster.cpp

HEADERS += kafx.h\
    include/avisynth_n.h \
    include/python/Python.h \
    raster.h \
    kafx_global.h

symbian {
    MMP_RULES += EXPORTUNFROZEN
    TARGET.UID3 = 0xE865DAD3
    TARGET.CAPABILITY = 
    TARGET.EPOCALLOWDLLDATA = 1
    addFiles.sources = kafx.dll
    addFiles.path = !:/sys/bin
    DEPLOYMENT += addFiles
}

unix:!symbian {
    maemo5 {
        target.path = /opt/usr/lib
    } else {
        target.path = /usr/lib
    }
    INSTALLS += target
}


LIBS += libs/python27.lib
