#include "acinterpolate.h"
#include "fxsgroup.h"

AcInterpolate::AcInterpolate(QString name, QString fname, bool function)
{
	from = "0.0";
	to = "0.0";
	this->name= name;
	this->fname = fname;
	this->func = function;
	diag = new DATwoValues();
	diag->setModal(true);
	diag->setWindowTitle(name);
	configure();
}

AcInterpolate::~AcInterpolate()
{
	if (diag!=NULL) delete diag;
}

bool AcInterpolate::configure()
{
	if (diag->exec()==diag->Accepted){
		from = diag->getFrom();
		to = diag->getTo();
		inter = diag->getInterpolator();
		return true;
	}else
		return false;
}

QString AcInterpolate::toString()
{
	QString res = name+ "("+from+", "+to;
	if (inter >0){
			res+=", "+FxsGroup::interNames[inter];
	}
	res +=")";
	return res;
}

QStringList AcInterpolate::genStructure()
{

	QString res;
	res = tab+"obj.";
	if (func){
		res += fname+ "(" +from + ", " + to ;
		if (inter>0){
			res.append(", inter=");
			res.append(FxsGroup::interUrls[inter]);
		}
		res += ")";
	}else{
		res += fname+ " = comun.Interpolate(obj.progreso, " +from + ", " + to ;
		if (inter>0){
			res.append(", ");
			res.append(FxsGroup::interUrls[inter]);
		}
		res += ")";
	}
	return QStringList(res);//podemos hacer esto porque estamos devolviendo una sola linea, cambiar si es necesario
}

QList<int> AcInterpolate::getModules()
{
	QList<int> res;
	if (inter>0)
		res.append(COMUN);
	return res;
}
