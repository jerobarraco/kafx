#ifndef DAWIGGLE_H
#define DAWIGGLE_H

#include <QDialog>

namespace Ui {
class DAWiggle;
}

class DAWiggle : public QDialog
{
    Q_OBJECT
    
public:
    explicit DAWiggle(QWidget *parent = 0);
    ~DAWiggle();
    QString getAmp();
    QString getFreq();

private:
    Ui::DAWiggle *ui;
};

#endif // DAWIGGLE_H
