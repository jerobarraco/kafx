#include "acfunction.h"

AcFunction::AcFunction(QString name, QString fname, int module)
{
	this->name = name;
	this->fname = fname;
	this->module = module;
}

QString AcFunction::toString()
{
	return name+"()";
}

QStringList AcFunction::genStructure()
{
	return QStringList(tab+fname+"()");
}

QList<int> AcFunction::getModules()
{
	QList<int> res;
	if (module>=0){
		res.append(module);
	}
	return res;
}
