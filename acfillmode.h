#ifndef ACFILLMODE_H
#define ACFILLMODE_H
#include "action.h"
#include "dafillmode.h"

class AcFillMode : public Action
{
	DAFillMode *diag;
	int part, type;
	public:
		AcFillMode();
		~AcFillMode();
		bool configure();
		QString toString();
		QList<int> getModules();
		QStringList genStructure();
};

#endif // ACFILLMODE_H
