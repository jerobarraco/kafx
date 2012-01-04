#include "deffect.h"
#include "ui_deffect.h"

DEffect::DEffect(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DEffect)
{
    ui->setupUi(this);
}

DEffect::~DEffect()
{
    delete ui;
}

int DEffect::getDiagIn()
{
    return ui->spinBox->value();
}

int DEffect::getDiagOut()
{
    return ui->spinBox_2->value();
}

int DEffect::getSilIn()
{
    return ui->spinBox_3->value();
}

int DEffect::getSilOut()
{
    return ui->spinBox_4->value();
}

int DEffect::getLetIn()
{
    return ui->spinBox_5->value();
}

int DEffect::getLetOut()
{
    return ui->spinBox_6->value();
}

bool DEffect::getSplitLet()
{
    return ui->checkBox->isChecked();
}

bool DEffect::getSkipFrames()
{
    return ui->checkBox_3->isChecked();
}

bool DEffect::getResetStyle()
{
    return ui->checkBox_2->isChecked();
}
