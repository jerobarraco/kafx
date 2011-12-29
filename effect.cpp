#include "effect.h"
#include <QInputDialog>

Effect::Effect(QWidget *parent)
{
    name = QInputDialog::getText(
                parent , "Insert name for effect",
                "Enter a name for the effect, please use only one word, starting with a letter (a to z)");
}
Effect::~Effect(){
    Event* ev;
    while (!events.isEmpty()){
        ev = events.takeFirst();
        delete ev;
    };
}

QString Effect::toString()
{
    return name;
}

QStringList Effect::genStructure()
{
    QStringList res;
    res << "class " + name + "(comun.Fx):";
    //todo estructura de los eventos
     for (int i = 0; i< events.count(); i++){
            res += events[i]->genStructure();//todo alguna forma de cambiar la tabulacion
        }

    return res;
}

QString Effect::addEvent(int type)
{
    Event *ev = new Event(type);//todo check que no hayan 2 eventos iguales
    this->events.append(ev);
    return ev->toString();
}

QString Effect::getName()
{
    return name;
}
