#ifndef EVENT_H
#define EVENT_H
#include <QString>
#include <QStringList>
class Event
{
    QString name;
    QString publicName;
    int type;
    //QList<Preset> presets;
public:
    Event(int type);
    static QString names[];
    static QString publicNames[];
    static int nameCount;

    QString toString();
    QString getName();
    QStringList genStructure();
};


#endif // EVENT_H
