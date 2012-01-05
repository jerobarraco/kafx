#include "action.h"
#include "dasettexture.h"
#include <QString>

#ifndef ACSETTEXTURE_H
#define ACSETTEXTURE_H

class AcSetTexture : public Action
{
		DASetTexture *diag;
		int part;
		QString image;
	public:
		AcSetTexture();
		~AcSetTexture();
		bool configure();
		QString toString();
		QStringList genStructure();
		QList<int> getModules();
};

#endif // ACSETTEXTURE_H
