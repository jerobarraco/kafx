#include "dafade.h"
#include "ui_dafade.h"

DAFade::DAFade(QWidget *parent) :
	QDialog(parent),
	ui(new Ui::DAFade)
{
	ui->setupUi(this);
}

DAFade::~DAFade()
{
	delete ui;
}
