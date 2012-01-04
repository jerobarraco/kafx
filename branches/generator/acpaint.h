#include "action.h"
#include "dapaint.h"
#ifndef ACPAINT_H
#define ACPAINT_H

class AcPaint : public Action
{
public:
    AcPaint();
    bool configure();
    QString toString();
    QStringList genStructure();
};

#endif // ACPAINT_H
