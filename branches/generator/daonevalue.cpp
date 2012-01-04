#include "daonevalue.h"
#include "ui_daonevalue.h"

DAOneValue::DAOneValue(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DAOneValue)
{
    ui->setupUi(this);
}

DAOneValue::~DAOneValue()
{
    delete ui;
}

QString DAOneValue::getTo()
{
    return this->ui->spinBox->text();
}
