#ifndef DATWOVALUES_H
#define DATWOVALUES_H

#include <QDialog>

namespace Ui {
class DATwoValues;
}

class DATwoValues : public QDialog
{
    Q_OBJECT
    
public:
    explicit DATwoValues(QWidget *parent = 0);
    ~DATwoValues();
    QString getFrom();
    QString getTo();
    int getInterpolator();
private:
    Ui::DATwoValues *ui;

};

#endif // DATWOVALUES_H
