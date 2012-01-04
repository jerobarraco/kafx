#include <QtGui/QApplication>
#include "mainwindow.h"
#include <QLocale>
#include <QTranslator>
#include <QLibraryInfo>



int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QTranslator qtTranslator;
    qtTranslator.load("qt_" + QLocale::system().name(),
     QLibraryInfo::location(QLibraryInfo::TranslationsPath));
    app.installTranslator(&qtTranslator);

    myTrans.load("kafx_" + QLocale::system().name());
    app.installTranslator(&myTrans);

    //importnate para que los flotantes usen "." como separador decimal
   //esto sobreescribe las traducciones, todo: ver como hacer para que no lo haga
    QLocale::setDefault(QLocale::C);
    MainWindow w;
    w.show();

    return app.exec();
}
