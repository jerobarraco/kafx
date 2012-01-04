#include "acscale.h"
#include "fxsgroup.h"//para el enum de modules
AcScale::AcScale()
{
    from = "0.0";
    to="0.0";
    interpolator  = 0;//el default
    diag = new DAscale();
    diag->setModal(true);
    configure();

}

AcScale::~AcScale()
{
    delete diag;
}

bool AcScale::configure()
{
    if (diag->exec()==diag->Accepted){
        from = diag->getFrom();
        to = diag->getTo();
        interpolator = diag->getInterpolator();
        return true;
    }else{return false;}
}

QString AcScale::toString()
{
		QString res ="Scale("+from+", "+to;
		if (interpolator >1){
			res+=", "+FxsGroup::interNames[interpolator];
		}
		res +=")";
		return res;
}

QStringList AcScale::genStructure()
{
		QStringList res ;
		QString str ;
		str = tab+ "obj.Scale(" +from+ ", " +to;
		if (interpolator >0){
				str.append(", inter=");
				str.append(FxsGroup::interUrls[interpolator]);
		}
		str.append(")");
		res << str;

		return res;
}

QList<int> AcScale::getModules()
{
		QList<int> res;
		//>0 obvia el -1 (vacio) y el 0 que es el default, podria obviar esto, pero asi muestro para que realmente es util el getmodules.

		if (interpolator>0){
				res.append(COMUN);
		}
		return res;
}

