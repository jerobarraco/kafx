
#ifndef DASETTEXTURE_H
#define DASETTEXTURE_H
#include <QDialog>
#include <QString>
#include "action.h"

namespace Ui {
	class DASetTexture;
}

class DASetTexture : public QDialog
{
		Q_OBJECT
		
	public:
		explicit DASetTexture(QWidget *parent = 0);
		~DASetTexture();
		QString getImage();
		int getPart();
		
	private slots:
		void on_pushButton_clicked();

	private:
		Ui::DASetTexture *ui;
};

#endif // DASETTEXTURE_H
