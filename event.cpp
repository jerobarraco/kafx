#include "event.h"
#include "action.h"
#include "acpaint.h"
#include "acscale.h"
#include "acchangecolor.h"
#include "acsettexture.h"

#include <QString>

Event::Event(int type)
{
    if (type <0 || type > Event::nameCount) type = 0;

    this->name = Event::names[type];
    this->publicName = Event::publicNames[type];
		this->type = type;
}

Event::~Event()
{
	Action *ac ;
	while (!actions.isEmpty()){
			ac = actions.takeFirst();
			delete ac;
	};
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
    QStringList res;
    res << "\tdef "+ name +"(self, obj):";//intuyo que el obj dara problemas :D
    //for presets
		if (actions.isEmpty()){
				res << "\t\tpass";
		}else{
				for (int i = 0; i<actions.count(); i++){
						res += actions.at(i)->genStructure();
				}
		}
		return res;
}

QString Event::addAction(int type)
{
		Action *ac;

		switch(type){
				case 0: ac = new AcScale(); break;//scale
				case 1: ac = new Action(); break;//rotate
				case 2: ac = new Action(); break; //move
				case 3: ac = new Action(); break; //fade
				case 4: ac = new AcPaint(); break;//paint
				case 5: ac = new AcChangeColor(); break; //chage color
			case 6: ac = new AcChangeColor(); break;//shadow size
			case 7: ac = new AcChangeColor(); break;//border size
			case 8: ac = new AcSetTexture(); break; // set texture
		}

		this->actions.append(ac);
		return ac->toString();
}

Action *Event::getAction(int i)
{
    return actions.at(i);
}

int Event::getActionCount()
{
    return actions.count();
}

QList<int> Event::getModules()
{
		QList<int> res;
		for (int i=0; i<actions.count(); i++){
				res.append(actions.at(i)->getModules());
		}
		return res;
}

void Event::deleteAction(int i)
{
	Action *ac= actions.takeAt(i);
	delete ac;
}
