#include "acpaint.h"
#include "action.h"

AcPaint::AcPaint():Action()
{
    configure();
}

bool AcPaint::configure()
{
    return true;
}

QString AcPaint::toString()
{
    return "Paint()";
}

QStringList AcPaint::genStructure()
{
    QStringList res;
    res << "\t\tobj.Paint()";
    return res;
}
