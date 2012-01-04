#include "event.h"
#include "action.h"
#include "acpaint.h"
#include "acmove.h"
#include "acchangecolor.h"
#include "acsettexture.h"
#include "actwovalues.h"
#include "aconevalue.h"
#include "main.cpp"
#include <QString>
//todo usar translate
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
    QString("OnDialogoCreate"),
    QString("OnDialog"),
    QString("OnDialogOut"),
    QString("OnDialogIn"),
    QString("OnSyllableCreate"),
    QString("OnSyllable"),
    QString("OnSyllableOut"),
    QString("OnSyllableIn"),
    QString("OnSyllableDead"),
    QString("OnSyllableSleep"),
    QString("OnLetterCreate"),
    QString("OnLetter"),
    QString("OnLetterOut"),
    QString("OnLetterIn")
};

QString Event::publicNames[] = {
    myTrans.tr("Dialog is created"),
    myTrans.tr("Dialog is active"),
    myTrans.tr("Dialog dissapears"),
    myTrans.tr("Dialog appears"),
    myTrans.tr("Syllable is created"),
    myTrans.tr("Syllable is active"),
    myTrans.tr("Syllable dissapears"),
    myTrans.tr("Syllable appears"),
    myTrans.tr("Syllable is dead (after activation)"),
    myTrans.tr("Syllable is sleep (before activation)"),
    myTrans.tr("Letter is created"),
    myTrans.tr("Letter is active"),
    myTrans.tr("Letter dissapears"),
    myTrans.tr("Letter appears")
};

int Event::nameCount = 14;

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
        case 0: ac = new AcTwoValues("Scale", "Scale"); break;//scale
        case 1: ac = new AcTwoValues("Rotate", "Rotate"); break;//rotate
        case 2: ac = new AcMove(); break; //move
        case 3: ac = new AcTwoValues("Move From", "MoveFrom"); break; //move from
        case 4: ac = new AcTwoValues("Move To", "MoveTo"); break; //move to
        case 5: ac = new AcTwoValues("Fade", "Fade"); break; //fade
        case 6: ac = new AcPaint(); break;//paint
        case 7: ac = new AcChangeColor(); break; //chage color
        case 8: ac = new AcOneValue("Shadow Size", "actual.shadow"); break;//shadow size
        case 9: ac = new AcOneValue("Border Size", "actual.border"); break;//border size
        case 10: ac = new AcSetTexture(); break; // set texture
        default : ac = new Action();
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
