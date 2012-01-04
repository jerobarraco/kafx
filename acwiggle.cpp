#include "acwiggle.h"

AcWiggle::AcWiggle()
{
		diag = new DAWiggle();
		diag->setModal(true);
		amp = "4";
		freq = "2";
		configure();
}

QString AcWiggle::toString()
{
		return "Wiggle ( amp=" + amp + ", freq="+freq +")";
}

QStringList AcWiggle::genStructure()
{
		return QStringList(tab+"obj.Wiggle("+amp+", "+freq+")");
}

bool AcWiggle::configure()
{
		if (diag->exec()==diag->Accepted){
				amp = diag->getAmp();
				freq = diag->getFreq();
				return true;
		}else
				return false;
}

QList<int> AcWiggle::getModules()
{
		return QList<int>();
}
