#ifndef ACTWOVALUES_H
#define ACTWOVALUES_H
#include <QDialog>
#include <QString>
#include <QList>
#include <QStringList>
#include "datwovalues.h"
#include "action.h"

class AcTwoValues : public Action
{

    QString from, to, name, fname;
    int interpolator;
    DATwoValues *diag;
public:
    AcTwoValues(QString name, QString fname);
    virtual ~AcTwoValues();
    bool configure();
    QString toString();
    QStringList genStructure();
    QList<int> getModules();
};

#endif // ACTWOVALUES_H
