#include "aconevalue.h"

AcOneValue::AcOneValue(QString name, QString fname, bool function, bool integer, int module)
{
    diag = new DAOneValue();
    diag->setModal(true);
    diag->setWindowTitle(name);
		if (!integer)
			diag->setFloat();
    this->name = name;
    this->fname = fname;
    this->func = function;
		this->module = module;
		to ="0";
    configure();
}

AcOneValue::~AcOneValue()
{
    delete diag;
}

bool AcOneValue::configure()
{
	if (diag->exec()==diag->Accepted){
		to = diag->getTo();
		return true;
	}else
		return false;
}

QString AcOneValue::toString()
{
		return name+ "("+ to + ")";
}

QStringList AcOneValue::genStructure()
{
    QStringList res ;
    QString line ;
		line = tab+ fname;
    if (func){
				line += "("+ to +")";
    }else{
        line += " = " + to;
    }
    res << line;
		return res;
}

QList<int> AcOneValue::getModules()
{
	QList<int> res;
	if (module>=0)
		res.append(module);
	return res;
}
