#include "acmove.h"
#include "fxsgroup.h"

AcMove::AcMove()
{
    fromx = "0";
    fromy = "0";
    toy = "0";
    tox = "0";
    inter = 0;
    diag = new DAMove();
    diag->setModal(true);
    configure();
}

AcMove::~AcMove()
{
    delete diag;
}

QString AcMove::toString()
{
    QString res = "Move ( (" + fromx + ", " +fromy +"), (";
    res.append(tox +", "+toy);
    if (inter >0){
        res +=", "+FxsGroup::interNames[inter];
    }
    res +=")";
    return res;
}

QStringList AcMove::genStructure()
{
    QStringList res ;
    QString str = tab+ "obj.Move((" + fromx + ", " +fromy;
    str.append("), (" +tox + ", "+toy+")");
    if (inter >0){
        str.append(", inter=");
        str.append(FxsGroup::interUrls[inter]);
    }
    str.append(")");
    res << str;
    return res;
}

bool AcMove::configure()
{
    if (diag->exec()==diag->Accepted){
        fromx = diag->getFromX();
        fromy = diag->getFromY();
        tox = diag->getToX();
        toy = diag->getToY();
        inter = diag->getInterpolator();
        return true;
    }else{return false;}
}

QList<int> AcMove::getModules()
{
    QList<int> res;
    //>0 obvia el -1 (vacio) y el 0 que es el default, podria obviar esto, pero asi muestro para que realmente es util el getmodules.

    if (inter>0){
        res.append(COMUN);
    }
    return res;
}
