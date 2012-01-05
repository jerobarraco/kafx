#ifndef DAONEVALUE_H
#define DAONEVALUE_H

#include <QDialog>

namespace Ui {
class DAOneValue;
}

class DAOneValue : public QDialog
{
    Q_OBJECT
    
public:
    explicit DAOneValue(QWidget *parent = 0);
    ~DAOneValue();
		void setFloat();
		QString getTo();
private:
    Ui::DAOneValue *ui;
};

#endif // DAONEVALUE_H
