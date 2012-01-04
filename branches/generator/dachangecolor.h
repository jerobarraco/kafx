#ifndef DACHANGECOLOR_H
#define DACHANGECOLOR_H

#include <QDialog>

namespace Ui {
	class DAChangeColor;
}

class DAChangeColor : public QDialog
{
		Q_OBJECT
		
	public:
		explicit DAChangeColor(QWidget *parent = 0);
		~DAChangeColor();
		 int getFrom();
		 int getTo();
		 int getInterpolator();

	private:
		Ui::DAChangeColor *ui;
};

#endif // DACHANGECOLOR_H
