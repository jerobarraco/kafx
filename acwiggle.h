#ifndef ACWIGGLE_H
#define ACWIGGLE_H
#include "action.h"
#include "dawiggle.h"
#include <QString>
#include <QStringList>
#include <QList>


class AcWiggle: public Action
{
		QString amp, freq;
		DAWiggle *diag;
public:
    AcWiggle();
		~AcWiggle();
		QString toString();
		QStringList genStructure();
		bool configure();
		QList<int> getModules();
};

#endif // ACWIGGLE_H
