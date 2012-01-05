#include "acsettexture.h"

AcSetTexture::AcSetTexture()
{
	part = 0;
	image = "";
	diag = new DASetTexture();
	diag->setModal(true);
	configure();
}

AcSetTexture::~AcSetTexture()
{
    delete diag;
}
bool AcSetTexture::configure()
{
	if (diag->exec()==diag->Accepted){
		part = diag->getPart();
		image = diag->getImage();
		return true;
	}else
		return false;
}

QString AcSetTexture::toString()
{
	return "Set Texture("+QString::number(part)//todo, usar los nombres en los combos con diag->getFromText y getToText
			+", "+image.split("/").last() + ")";
}

QStringList AcSetTexture::genStructure()
{
	QStringList res ;
	QString str ;
	str = tab+ "obj.LoadTexture(r\"";
	str.append(image);
	str.append("\", part=");
	switch(part){
		case 1: str.append("obj.PART_BORDER"); break;
		case 2: str.append("obj.PART_SHADOW"); break;
		default: str.append("obj.PART_FILL"); break;
	}
	str.append(")");
	res << str;
	return res;
}

QList<int> AcSetTexture::getModules()
{
	return QList<int>();
}
