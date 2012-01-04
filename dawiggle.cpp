#include "dawiggle.h"
#include "ui_dawiggle.h"

DAWiggle::DAWiggle(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DAWiggle)
{
    ui->setupUi(this);
}

DAWiggle::~DAWiggle()
{
		delete ui;
}

QString DAWiggle::getAmp()
{
		return ui->spinBox->text();
}

QString DAWiggle::getFreq()
{
		return ui->spinBox_2->text();
}
