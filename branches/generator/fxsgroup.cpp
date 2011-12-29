#include "fxsgroup.h"
#include <QTextStream>
#include <QStringList>
FxsGroup::FxsGroup()
{
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
    ret << "# -*- coding: utf-8 -*-";
    ret << "#Automatically generated by the super duper tool for Kafx. (C) Jer�nimo Barraco M�rmol" ;
    //todo un metodo de llevar cuenta de las libs que se importan
    ret << "from libs import comun";


    //todo meter los efectos
    for (int i = 0; i< effects.count(); i++){
        ret << "";
        ret += effects[i]->genStructure();
    }
    //todo meter la config basica en la gui y aca
    ret << "";
    ret << "class FxsGroup(comun.FxsGroup):";
    ret << "\tdef __init__(self):";
    ret << "\t\t#Opciones principales";
    ret << "\t\tself.in_ms = 150 #Milisegundos para la animacion de entrada";
    ret << "\t\tself.out_ms = 250 #MS para animacion d salida";
    ret << "\t\tself.sil_in_ms = 500 #ms para la animacion de entrada de cada silaba sin animar (en el dialogo actual)";
    ret << "\t\tself.sil_out_ms = 200 #ms para la animacion de cada silaba muerta (en el dialogo actual)";

    ret << "\t\t#Un efecto si o si tiene que definir lo siguiente, si o si con este nombre";
    ret << "\t\t#Funciones (grupo de efectos) que provee";
    ret << "";

    QString fxs = "\t\tself.fxs = (";
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
    //if (i<0 or i>=effects.count()) return null;
    return effects[index];
}

