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
		int module;
public:
		AcOneValue(QString name, QString fname, bool function, bool integer, int module=-1);
    ~AcOneValue();
    bool configure();
    QString toString();
    QStringList genStructure();
		QList<int> getModules();
};

#endif // ACONEVALUE_H
