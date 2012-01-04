#ifndef ACINTERPOLATE_H
#define ACINTERPOLATE_H
#include "action.h"
#include "datwovalues.h"
#include <QString>
#include <QStringList>
#include <QList>

class AcInterpolate : public Action
{
		QString from, to, name, fname;
		int inter;
		bool func;
		DATwoValues *diag;
public:
		AcInterpolate(QString name, QString fname, bool function);
		virtual ~AcInterpolate();
		bool configure();
		QString toString();
		QStringList genStructure();
		QList<int> getModules();
};

#endif // ACINTERPOLATE_H
