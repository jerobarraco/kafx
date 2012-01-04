#include "dascale.h"
#include "ui_dascale.h"
#include "fxsgroup.h"

DAscale::DAscale(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DAscale)
{
    ui->setupUi(this);
		for (int i =0; i< FxsGroup::interCant ;i++){
			ui->comboBox->addItem(FxsGroup::interNames[i]);
		}
}

DAscale::~DAscale()
{
		delete ui;
}

QString DAscale::getFrom()
{
		QLocale c;
		c.setDefault(QLocale::C);
		return c.toString(this->ui->doubleSpinBox->value(), 'f');
}

QString DAscale::getTo()
{
		QLocale c;
		c.setDefault(QLocale::C);
		return c.toString(this->ui->doubleSpinBox_2->value(), 'f');
}

int DAscale::getInterpolator()
{
		return ui->comboBox->currentIndex();
}
