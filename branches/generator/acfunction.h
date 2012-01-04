#ifndef ACFUNCTION_H
#define ACFUNCTION_H
#include "action.h"
class AcFunction : public Action
{
		QString name, fname;
		int module;
	public:
		AcFunction(QString name, QString fname,int module);
		QString toString();
		QStringList genStructure();
		QList<int> getModules();
};

#endif // ACFUNCTION_H
