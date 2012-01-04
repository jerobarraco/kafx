#include "action.h"

Action::Action()
{
		tab = "\t\t";
		this->configure();
}

QString Action::toString()
{
		return "Not implemented yet";
}

bool Action::configure()
{
		return false;//devuelve truesi cambio algo, creo que es al pedo
}

QList<int> Action::getModules()
{
		//como el uso de modulos en realidad depende de la configuraion
		//del "action" entonces ponemos un getModules que calcula los modulos, no es rapido ni feliz pero es directo
		//ver moduleUrls en mainWindow
		return QList<int>();
}

QStringList Action::genStructure()
{
		QStringList res;
		res << tab + "pass";
		return res;
}
