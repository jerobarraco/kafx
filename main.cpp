#include <QtGui/QApplication>
#include "mainwindow.h"
#include <QLocale>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QLocale::setDefault(QLocale::C);
    MainWindow w;
    w.show();

    return a.exec();
}
