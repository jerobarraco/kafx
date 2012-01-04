#ifndef EVENT_H
#define EVENT_H
#include <QString>
#include <QStringList>
#include "action.h"

class Event
{
    QString name;
    QString publicName;
		int type;
		QList<Action*> actions;
public:
    Event(int type);
		~Event();
    static QString names[];
    static QString publicNames[];
    static int nameCount;

    QString toString();
    QString getName();
    QStringList genStructure();
    QString addAction(int type);
    Action* getAction(int i);
    int getActionCount();
    QList<int> getModules();
    void deleteAction(int i);
};


#endif // EVENT_H
