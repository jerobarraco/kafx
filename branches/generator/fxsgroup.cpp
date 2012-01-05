﻿#include "fxsgroup.h"
#include <QTextStream>
#include <QStringList>
#include "mainwindow.h"

FxsGroup::FxsGroup()
{
	//esto es cohino pero bueno, no se me ocurrio otra forma mas rapida
	//debe coincidir con el enum MODULES
	//todo hacer static
	moduleUrls << "from random import random";
	moduleUrls << "from random import randint";
	moduleUrls << "from libs import common";
	moduleUrls << "from libs import asslib";
	moduleUrls << "from libs import audio";
	moduleUrls << "from libs import shapes";
	moduleUrls << "from libs import video";
	moduleUrls << "from libs.draw import advanced";
	moduleUrls << "from libs.draw import basic";
	moduleUrls << "from libs.draw import extra";
	diag_in = 200;
	diag_out = 200;
	sil_in = 200;
	sil_out = 200;
	let_in = 200;
	let_out = 200;
	splitlet = false;
	skipframes = false;
	reset_style = false;
}
FxsGroup::~FxsGroup(){
    Effect * ef;
    while (!effects.isEmpty()){
        ef = effects.takeFirst();
        delete ef;
    };
}

QString FxsGroup::addEffect(QWidget *parent)
{
    Effect *ef = new Effect(parent);
    this->effects.append(ef);
    return ef->toString();
}

void FxsGroup::deleteEffect(int index)
{
    Effect *ef = this->effects.takeAt(index);
    delete ef;
}

bool FxsGroup::saveTo(QString filename)
{
	archivo.setFileName(filename);
	if (archivo.open(QIODevice::Text | QIODevice::WriteOnly)){
		QTextStream txt(&archivo);
		QStringList structure  = genStructure();
		for (int i = 0; i< structure.count(); i++ ){
			txt << structure.at(i) << endl;
		}
		archivo.close();
		return true;
	} else{
		return false;
	}
}

QStringList FxsGroup::genStructure()
{
    QStringList ret;
    QString tab = "\t\t";
    ret << "# -*- coding: utf-8 -*-";
    ret << "#Automatically generated by the super duper tool for Kafx. (C) Jerónimo Barraco Mármol" ;

    QList<int> modules = getModules();

    for (int i =0; i<modules.count();i++)
            ret << moduleUrls.at(modules.at(i));

    ret<<"";
    //todo meter los efectos
    for (int i = 0; i< effects.count(); i++){
        ret << "";
        ret += effects[i]->genStructure();
    }

    //todo meter la config basica en la gui y aca
    ret << "";
    ret << "class FxsGroup(comun.FxsGroup):";
    ret << "\tdef __init__(self):";
    ret << tab + "#Opciones principales";

    ret << tab + "self.in_ms = " + QString::number(diag_in);
    ret << tab + "self.out_ms = " + QString::number(diag_out);
    ret << tab + "self.sil_in_ms = " + QString::number(sil_in);
    ret << tab + "self.sil_out_ms = " + QString::number(sil_out);

    if (splitlet){
        ret << tab + "self.split_letters = true";
        ret << tab + "self.let_in_ms = " + QString::number(let_in);
        ret << tab + "self.let_out_ms = " + QString::number(let_out);
    }

    if (skipframes)
        ret << tab + "self.skip_frames = true";

    if (reset_style)
        ret << tab + "self.reset_style = true";

    ret << "\t\t#Funciones (grupo de efectos) que provee";
    ret << "";

		QString fxs = tab+"self.fxs = (";
    for (int i = 0; i<effects.count(); i++){
        fxs.append(effects[i]->toString());//toString casualmetne da el name.. ojo con esto
        fxs += "(), ";
    }
    if (effects.count()==0) fxs+= ",";
    fxs += ")";
    ret << fxs;//todo meter nombres de efectos
    ret <<"";
    return ret;
}

Effect* FxsGroup::getEffect(int index)
{
		return effects[index];
}

QList<int> FxsGroup::getModules()
{
		QList<int> mods;
		mods << COMUN; //necesario para el FxsGroup
		//iteramos todos los efectos
		for (int i = 0; i<effects.count();i++){
				//tomamos el efecto y tomamos la lista de modulos del efecto
				QList<int> efmods = effects.at(i)->getModules();
				//iteramos esa lista
				for (int j=0; j<efmods.count(); j++){
						//para cada modulo de esa lista
						int efmod = efmods.at(j);
						// si no esta (evitamos repetidos)
						if (!mods.contains(efmod)){
								//lo agregamos
								mods.append(efmod);
						}
				}
		}
		return mods;
		//Uso el enum para que sea mas facil de recordar, pero se puede guarda un int.

}
/*
QString FxsGroup::interNames [] = {//que boludo estos son los actions.. igual necesitamos hacerlo
	QString("Scale"),QString("Rotate"),QString("Move"),
	QString("Fade"),QString("Paint"),QString("Change Color"),
	QString("Change Shadow Size"),QString("Change Border Size"),
	QString("Shake"),QString("Wiggle"),QString("Glow")
	,QString("Blur"),QString("Start Group"),QString("End Group")
};*/

QString FxsGroup::interNames [] = {
		Tr.tr("Lineal"),Tr.tr("Sinus"),Tr.tr("Cosinus"),
		Tr.tr("Full Sinus"),Tr.tr("Full Cosinus"),Tr.tr("Accelerate"),
		Tr.tr("Deccelerate"),Tr.tr("Random"),
		Tr.tr("Logarithmic"),Tr.tr("Ease in"),Tr.tr("Ease Out")
		,Tr.tr("Ease In Out"),Tr.tr("Cubic"),Tr.tr("BackStart"),Tr.tr("Boing")
};

QString FxsGroup::interUrls [] = {
	QString("common.i_lineal"),
	QString("common.i_sin"),QString("common.i_cos"),
	QString("common.i_full_sin"),QString("common.i_full_cos"),
	QString("common.i_accell"),QString("common.i_deccell"),
	QString("common.i_rand"),QString("common.i_log"),
	QString("common.i_b_ease_in"),QString("common.i_b_ease_out")
	,QString("common.i_b_ease_in_out"),QString("common.i_b_cubic"),
	QString("common.i_b_backstart"),QString("common.i_b_boing")
};

/*TODOS
    agregar mas actions
    al hacer doble click en un action que llame a configure
    permitir reordenar actions
    poner las acciones como static en action.h y usar translate
    arreglar translate
		hacer un dialogo que permita varios valores,
			cambiar los labels
			usar float e int
			poner interpoladores
			diferenciar function y variable
*/
