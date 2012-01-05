#include "acfillmode.h"

AcFillMode::AcFillMode()
{
	diag = new DAFillMode();
	part = 0;
	type = 0;
	configure();
}

AcFillMode::~AcFillMode()
{
	delete diag;
}

bool AcFillMode::configure()
{
	if (diag->exec() == diag->Accepted){
		part = diag->getPart();
		type = diag->getType();
		return true;
	}else
		return false;
}

QString AcFillMode::toString()
{
	QString res;
	res.append("Fill Mode (" + Action::partNames[part]);
	res.append(", "+ QString::number(type) + ")");
	return res;
}
QList<int> AcFillMode::getModules()
{
		//como el uso de modulos en realidad depende de la configuraion
		//del "action" entonces ponemos un getModules que calcula los modulos, no es rapido ni feliz pero es directo
		//ver moduleUrls en mainWindow
		return QList<int>();
}

QStringList AcFillMode::genStructure()
{
		QString line;
		line += tab + "obj.actual.mode_";
		switch(part){
			case 0: line += "fill";break;
			case 1: line += "border";break;
			case 2: line += "shadow";break;
			case 3: line += "particle";break;
		}
		line += " = obj.";
		switch (type){
			case 0: line += "P_SOLIDO"; break;
			case 1: line += "P_TEXTURA"; break;
			case 2: line += "P_DEG_VERT"; break;
			case 3: line += "P_DEG_HOR"; break;
			case 4: line += "P_DEG_DIAG"; break;
			case 5: line += "P_DEG_RAD"; break;
			case 6: line += "P_AN_DEG_LIN"; break;
			case 7: line += "P_AN_DEG_RAD"; break;
			case 8: line += "P_PATRON_COLOREADO"; break;
		}

		return QStringList(line);
}
