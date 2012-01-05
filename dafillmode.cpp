#include "dafillmode.h"
#include "ui_dafillmode.h"
#include "action.h"

DAFillMode::DAFillMode(QWidget *parent) :
	QDialog(parent),
	ui(new Ui::DAFillMode)
{
	ui->setupUi(this);
	for (int i = 0; i< Action::partCount; i++){
		ui->comboBox->addItem(Action::partNames[i]);
	}
}

DAFillMode::~DAFillMode()
{
	delete ui;
}

int DAFillMode::getPart()
{
	return ui->comboBox->currentIndex();
}

int DAFillMode::getType()
{
	return ui->comboBox_2->currentIndex();
}
