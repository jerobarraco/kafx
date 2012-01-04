#include "dasettexture.h"
#include "ui_dasettexture.h"
#include <QFileDialog>

DASetTexture::DASetTexture(QWidget *parent) :
	QDialog(parent),
	ui(new Ui::DASetTexture)
{
	ui->setupUi(this);
}

DASetTexture::~DASetTexture()
{
	delete ui;
}

QString DASetTexture::getImage()
{
	return ui->lineEdit->text();
}

int DASetTexture::getPart()
{
	return ui->comboBox->currentIndex();
}

void DASetTexture::on_pushButton_clicked()
{
	QString dir = QApplication::applicationDirPath();
	QString filtro = "Png images (*.png);;All files (*.*)";
	QString nombre = QFileDialog::getOpenFileName(
							this, "Choose Texture", dir, filtro);
	if (nombre==NULL) return;

	ui->lineEdit->setText(nombre);
}
