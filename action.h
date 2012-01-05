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
		virtual bool configure();
    virtual QString toString();
    virtual QStringList genStructure();
    virtual QList<int> getModules();

		static QString parts[];
		static QString partNames[];
		static const int partCount=3;
};

#endif // ACTION_H
