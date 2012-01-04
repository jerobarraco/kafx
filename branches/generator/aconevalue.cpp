#include "aconevalue.h"

AcOneValue::AcOneValue(QString name, QString fname, bool function)
{
    diag = new DAOneValue();
    diag->setModal(true);
    diag->setWindowTitle(name);
    this->name = name;
    this->fname = fname;
    this->func = function;
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
    return name+ "("+to + ")";
}

QStringList AcOneValue::genStructure()
{
    QStringList res ;
    QString line ;
    line = tab+ "obj." + fname;
    if (func){
        line += "("+to +")";
    }else{
        line += " = " + to;
    }
    res << line;
    return res;
}
