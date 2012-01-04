#ifndef ACMOVE_H
#define ACMOVE_H
#include "action.h"
#include <QString>
#include "damove.h"

class AcMove : public Action
{
    DAMove *diag;
    QString fromx, fromy, tox, toy;
    int inter;
public:
    AcMove();
    ~AcMove();
    QString toString();
    QStringList genStructure();
    bool configure();
    QList<int> getModules();
};

#endif // ACMOVE_H
