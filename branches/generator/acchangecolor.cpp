#include "acchangecolor.h"
#include "fxsgroup.h"

AcChangeColor::AcChangeColor()
{
	from = 0;
	to=0;
	interpolator  = 0;//el default
	diag = new DAChangeColor();
	diag->setModal(true);
	configure();
}

AcChangeColor::~AcChangeColor()
{
	delete diag;
}

bool AcChangeColor::configure()
{
	if (diag->exec()==diag->Accepted){
        from = diag->getFrom();
        to = diag->getTo();
        interpolator = diag->getInterpolator();
				interpolate = diag->getInterpolate();
        return true;
	}else{return false;}
}

QString AcChangeColor::toString()
{
	QString res ="ChangeColor("+QString::number(from)
			+", "+QString::number(to);//todo, usar los nombres en los combos con diag->getFromText y getToText
	if (interpolate && (interpolator>0)){
		res+=", "+FxsGroup::interNames[interpolator];
	}
	res +=")";
	return res;
}

QStringList AcChangeColor::genStructure()
{
	QString str, colorA, colorB;
	colorA = "obj.actual.color";
	switch(from){
		case 0: colorA.append("1");break;
		case 1: colorA.append("2");break;
		case 2: colorA.append("3");break;
		case 3: colorA.append("4");break;
	}

	colorB = "obj.original.color";
	switch(to){
		case 0: colorB.append("1");break;
		case 1: colorB.append("2");break;
		case 2: colorB.append("3");break;
		case 3: colorB.append("4");break;
	}

	str = tab+ colorA;
	if (interpolate){
		str.append(".Interpolate(obj.progress, ");
		str.append(colorB);
		if (interpolator >0){
				str.append(", inter=");
				str.append(FxsGroup::interUrls[interpolator]);
		}
		str.append(")");
	}else{
		str.append(".CopyFrom(");
		str.append(colorB);
		str.append(")");
	}

	return QStringList(str);
}

QList<int> AcChangeColor::getModules()
{
	QList<int> res;
	//>0 obvia el -1 (vacio) y el 0 que es el default, podria obviar esto, pero asi muestro para que realmente es util el getmodules.

	if (interpolator>0){
			res.append(COMUN);
	}
	return res;
}

QString AcChangeColor::colorNames[] = {
		QString("Primary"),	QString("Secundary"),QString("Border"),	QString("Shadow")
	};
