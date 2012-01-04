#include "aconevalue.h"

AcOneValue::AcOneValue(QString name, QString fname)
{
    diag = new DAOneValue();
    diag->setModal(true);
    this->name = name;
    this->fname = fname;
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
    res << tab+ "obj." + fname + " = " + to;
    return res;
}
