#include "action.h"
#include <QString>
#include <QStringList>
#include "dascale.h"

#ifndef ACSCALE_H
#define ACSCALE_H

class AcScale : public Action
{
        DAscale *diag;
		QString from, to;
		int interpolator;
public:
		AcScale();
        ~AcScale();
		bool configure();
		QString toString();
		QStringList genStructure();
		QList<int> getModules();
};

#endif // ACSCALE_H
