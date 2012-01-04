#include <QString>
#include <QStringList>

#ifndef ACTION_H
#define ACTION_H

class Action
{
protected:
		QString tab;
public:
    Action();
    virtual QString toString();
    virtual QStringList genStructure();
    virtual bool configure();
    virtual QList<int> getModules();
};

#endif // ACTION_H
