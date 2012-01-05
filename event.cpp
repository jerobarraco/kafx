#include "event.h"
#include "action.h"
#include "acmove.h"
#include "acchangecolor.h"
#include "acsettexture.h"
#include "acinterpolate.h"
#include "aconevalue.h"
#include "acwiggle.h"
#include "acfunction.h"
#include "acfillmode.h"
#include "main.cpp"
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
		Tr.tr("Dialog is created"),
		Tr.tr("Dialog is active"),
		Tr.tr("Dialog dissapears"),
		Tr.tr("Dialog appears"),
		Tr.tr("Syllable is created"),
		Tr.tr("Syllable is active"),
		Tr.tr("Syllable dissapears"),
		Tr.tr("Syllable appears"),
		Tr.tr("Syllable is dead (after activation)"),
		Tr.tr("Syllable is sleep (before activation)"),
		Tr.tr("Letter is created"),
		Tr.tr("Letter is active"),
		Tr.tr("Letter dissapears"),
		Tr.tr("Letter appears")
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
			case 0: ac = new AcInterpolate(Tr.tr("Scale"), "Scale", true); break;//scale
			case 1: ac = new AcInterpolate(Tr.tr("Rotate"), "Rotate", true); break;//rotate
			case 2: ac = new AcMove(); break; //move
			case 3: ac = new AcInterpolate(Tr.tr("Move From"), "MoveFrom", true); break; //move from
			case 4: ac = new AcInterpolate(Tr.tr("Move To"), "MoveTo", true); break; //move to
			case 5: ac = new AcInterpolate(Tr.tr("Fade"), "Fade", true); break; //fade
			case 6: ac = new AcFunction(Tr.tr("Paint"), "obj.Paint", -1); break;//paint
			case 7: ac = new AcFunction(Tr.tr("Paint Reflection"), "obj.PaintReflection", -1); break;//paint
			case 8: ac = new AcFunction(Tr.tr("Paint Using Cache"), "obj.PaintWithCache", -1); break;//paint
			case 9: ac = new AcChangeColor(); break; //chage color
			case 10: ac = new AcFillMode(); break; //chage fill type
			case 11: ac = new AcInterpolate(Tr.tr("Shadow Size"), "actual.shadow", false); break;//shadow size
			case 12: ac = new AcInterpolate(Tr.tr("Border Size"), "actual.border", false); break;//border size
			case 13: ac = new AcSetTexture(); break; // set texture
			case 14:
				ac = new AcOneValue(Tr.tr("Shake Amplitude"), "Shake", true); break; //
			case 15: ac = new AcWiggle(); break; //
			case 16:
				ac = new AcFunction(Tr.tr("Start Group"), "advanced.StartGroup", AVANZADO); break; //
			case 17:
				ac = new AcFunction(Tr.tr("End Group"), "advanced.EndGroup", AVANZADO); break; //
			case 18:
				ac = new AcFunction(Tr.tr("Glow"), "advanced.fGlow", AVANZADO); break; //
			case 19: ac = new AcFunction(Tr.tr("Blur"), "advanced.fBlur", AVANZADO); break; //
			case 20: ac = new AcFunction(Tr.tr("RotoZoom"), "advanced.fRotoZoom", AVANZADO); break; //
			case 21: ac = new AcFunction(Tr.tr("Wave"), "advanced.fWave", AVANZADO); break; //
			default: ac = new Action();
    }
		//fdirblur fbidirblur capas(inicia, fin y activar)
		//modopintado, csprite, cparticlesystem
		//cmabiar relleno/borde/sombra
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
