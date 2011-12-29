#ifndef EFFECT_H
#define EFFECT_H
#include <QString>
#include <QWidget>
#include <QStringList>
#include <QList>
#include "event.h"

class Effect
{
    QString name;
    QString publicName;
    QList<Event*> events;
public:
    Effect(QWidget *parent);
    ~Effect();
    QString toString();
    QString getName();
    QStringList genStructure();
    QString addEvent(int type);
};

#endif // EFFECT_H
