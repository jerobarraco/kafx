#ifndef DASCALE_H
#define DASCALE_H

#include <QDialog>

namespace Ui {
	class DAscale;
}

class DAscale : public QDialog
{
    Q_OBJECT
    
public:
    explicit DAscale(QWidget *parent = 0);
    ~DAscale();
		QString getFrom();
		QString getTo();
		int getInterpolator();//Todo hacer una clase que maneje los interpoladores, con su indice nombre y nombre completo
private:
    Ui::DAscale *ui;
};

#endif // DASCALE_H
