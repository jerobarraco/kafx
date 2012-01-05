#ifndef DAFILLMODE_H
#define DAFILLMODE_H

#include <QDialog>

namespace Ui {
	class DAFillMode;
}

class DAFillMode : public QDialog
{
		Q_OBJECT
		
	public:
		explicit DAFillMode(QWidget *parent = 0);
		~DAFillMode();
		int getPart();
		int getType();
	private:
		Ui::DAFillMode *ui;
};

#endif // DAFILLMODE_H
