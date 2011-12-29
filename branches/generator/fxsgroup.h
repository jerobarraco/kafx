#ifndef FXSGROUP_H
#define FXSGROUP_H
#include "effect.h"
#include <QList>
#include <QFile>
#include <QStringList>
#include <QString>

class FxsGroup
{
    QList<Effect*> effects;
    QFile archivo;
    QStringList genStructure();
public:
    FxsGroup();
    ~FxsGroup();
    QString addEffect(QWidget *parent);
    void deleteEffect(int index);
    bool saveTo(QString filename);
    Effect *getEffect(int index);
};

#endif // FXSGROUP_H
