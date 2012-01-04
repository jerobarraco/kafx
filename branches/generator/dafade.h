#ifndef DAFADE_H
#define DAFADE_H

#include <QDialog>

namespace Ui {
	class DAFade;
}

class DAFade : public QDialog
{
		Q_OBJECT
		
	public:
		explicit DAFade(QWidget *parent = 0);
		~DAFade();
		
	private:
		Ui::DAFade *ui;
};

#endif // DAFADE_H
