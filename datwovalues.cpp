#include "datwovalues.h"
#include "ui_datwovalues.h"
#include "fxsgroup.h"

DATwoValues::DATwoValues(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DATwoValues)
{
    ui->setupUi(this);
    for (int i =0; i< FxsGroup::interCant ;i++){
        ui->comboBox->addItem(FxsGroup::interNames[i]);
    }
}

DATwoValues::~DATwoValues()
{
    delete ui;
}

QString DATwoValues::getFrom()
{
    return QString::number(this->ui->doubleSpinBox->value(), 'f');
}

QString DATwoValues::getTo()
{
    return QString::number(this->ui->doubleSpinBox_2->value(), 'f');
}

int DATwoValues::getInterpolator()
{
    return ui->comboBox->currentIndex();
}
