#ifndef ACONEVALUE_H
#define ACONEVALUE_H
#include "daonevalue.h"
#include "action.h"
#include <QString>
#include <QStringList>
#include <QList>

class AcOneValue : public Action
{
    DAOneValue *diag;
    QString to, name , fname;
    bool func;
public:
    AcOneValue(QString name, QString fname, bool function);
    ~AcOneValue();
    bool configure();
    QString toString();
    QStringList genStructure();
    QList<int> getModules(){return QList<int>();}
};

#endif // ACONEVALUE_H
