#include "dachangecolor.h"
#include "ui_dachangecolor.h"
#include "fxsgroup.h"
#include "acchangecolor.h"

DAChangeColor::DAChangeColor(QWidget *parent) :
	QDialog(parent),
	ui(new Ui::DAChangeColor)
{
	ui->setupUi(this);

	for (int i =0; i< AcChangeColor::colorCount;i++){
		ui->comboBox->addItem(AcChangeColor::colorNames[i]);
		ui->comboBox_2->addItem(AcChangeColor::colorNames[i]);
	}
	for (int i =0; i< FxsGroup::interCant ;i++){
		ui->comboBox_3->addItem(FxsGroup::interNames[i]);
	}


}

DAChangeColor::~DAChangeColor()
{
	delete ui;
}

int DAChangeColor::getFrom()
{
	return ui->comboBox->currentIndex();
}

int DAChangeColor::getTo()
{
	return ui->comboBox_2->currentIndex();
}

int DAChangeColor::getInterpolator()
{
	return ui->comboBox_3->currentIndex();
}

