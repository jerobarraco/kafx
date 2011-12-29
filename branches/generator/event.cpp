#include "event.h"
#include <QString>

Event::Event(int type)
{
    if (type <0 || type > Event::nameCount) type = 0;

    this->name = Event::names[type];
    this->publicName = Event::publicNames[type];
    this->type = type;
}

QString Event::getName()
{
    return name;
}
QString Event::toString()
{
    return publicName;
}

QString Event::names[] = {
    QString("EnDialogoInicia"),
    QString("EnDialogo"),
    QString("EnDialogoSale"),
    QString("EnDialogoEntra")
};
QString Event::publicNames[] = {
    QString("When the dialog is created"),
    QString("When the dialog is active"),
    QString("When the dialog dissapears"),
    QString("When the dialog appears")
};
int Event::nameCount= 4;

QStringList Event::genStructure()
{
    QString tab = "\t\t";
    QStringList res;
    res << "\tdef "+ name +"(self, obj):";//intuyo que el obj dara problemas :D
    //for presets
    res << tab + "pass";
    return res;
}
