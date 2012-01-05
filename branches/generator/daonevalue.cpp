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

void DAOneValue::setFloat()
{
	ui->doubleSpinBox->setDecimals(2);
	ui->doubleSpinBox->setSingleStep(0.01);
}

QString DAOneValue::getTo()
{
	return this->ui->doubleSpinBox->text();
}


