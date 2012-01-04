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

Event *Effect::getEvent(int i)
{
    return events.at(i);
}

int Effect::getEventCount()
{
    return events.size();
}

void Effect::deleteEvent(int i)
{
	Event* ev = events.takeAt(i);
	delete ev;
}

QList<int> Effect::getModules()
{
		QList<int> res;
		for (int i = 0; i< events.count(); i++){
				QList<int> evmods = events.at(i)->getModules();
				res.append(evmods);//teoricamente si pasamos una lista a res, agrega cada uno de los elementos
		}
		return res;
}

QString Effect::getName()
{
    return name;
}
