#include "action.h"
#include <QString>
#include <QList>
#include <QStringList>
#ifndef ACFADE_H
#define ACFADE_H

class AcFade : public Action
{
	private:
		QString from, to;
		int interpolator;
	public:
		AcFade();
		/*//esto es igual a scale asi que no me voy a gastar ahora
		bool configure();
		QString toString();
		QStringList genStructure();
		QList<int> getModules();*/
};

#endif // ACFADE_H
