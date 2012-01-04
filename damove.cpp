#include "damove.h"
#include "ui_damove.h"
#include "fxsgroup.h"

DAMove::DAMove(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DAMove)
{
    ui->setupUi(this);
    for (int i =0; i< FxsGroup::interCant ;i++){
        ui->comboBox->addItem(FxsGroup::interNames[i]);
    }
}

DAMove::~DAMove()
{
    delete ui;
}

QString DAMove::getFromX()
{
    return ui->spinBox->text();
}

QString DAMove::getFromY()
{
    return ui->spinBox_2->text();
}

QString DAMove::getToX()
{
    return ui->spinBox_3->text();
}

QString DAMove::getToY()
{
    return ui->spinBox_4->text();
}

int DAMove::getInterpolator()
{
    return ui->comboBox->currentIndex();
}
