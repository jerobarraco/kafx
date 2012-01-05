#include "action.h"
#include <QString>
#include <QStringList>
#include <QList>
#include "dachangecolor.h"

#ifndef ACCHANGECOLOR_H
#define ACCHANGECOLOR_H

class AcChangeColor : public Action
{
	private:
		DAChangeColor *diag;
		int from, to, interpolator;
		bool interpolate;
	public:
		AcChangeColor();
		~AcChangeColor();
		bool configure();
		QString toString();
		QStringList genStructure();
		QList<int> getModules();
		static QString colorNames[];
		static const int colorCount=4;
};

#endif // ACCHANGECOLOR_H
