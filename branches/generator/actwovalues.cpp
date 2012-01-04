#include "actwovalues.h"
#include "fxsgroup.h"

AcTwoValues::AcTwoValues(QString name, QString fname)
{
    from = "0.0";
    to = "0.0";
    this->name = name;
    this->fname = fname;
    diag = new DATwoValues();
    diag->setModal(true);
    diag->setWindowTitle(name);
    configure();
}

AcTwoValues::~AcTwoValues()
{
    if (diag!=NULL)
        delete diag;
}


bool AcTwoValues::configure()
{
    if (diag->exec()==diag->Accepted){
        from = diag->getFrom();
        to = diag->getTo();
        interpolator = diag->getInterpolator();
        return true;
    }else{return false;}
}

QString AcTwoValues::toString()
{
    QString res = name+ "("+from+", "+to;
    if (interpolator >0){
        res+=", "+FxsGroup::interNames[interpolator];
    }
    res +=")";
    return res;
}

QStringList AcTwoValues::genStructure()
{
    QStringList res ;
    QString str ;
    str = tab+ "obj." + fname + "(" +from+ ", " +to;
    if (interpolator >0){
        str.append(", inter=");
        str.append(FxsGroup::interUrls[interpolator]);
    }
    str.append(")");
    res << str;

    return res;
}

QList<int> AcTwoValues::getModules()
{
    QList<int> res;
    //>0 obvia el -1 (vacio) y el 0 que es el default, podria obviar esto, pero asi muestro para que realmente es util el getmodules.

    if (interpolator>0){
            res.append(COMUN);
    }
    return res;
}
