#ifndef DEFFECT_H
#define DEFFECT_H

#include <QDialog>

namespace Ui {
class DEffect;
}

class DEffect : public QDialog
{
    Q_OBJECT
    
public:
    explicit DEffect(QWidget *parent = 0);
    ~DEffect();
    int getDiagIn();
    int getDiagOut();
    int getSilIn();
    int getSilOut();
    int getLetIn();
    int getLetOut();
    bool getSplitLet();
    bool getSkipFrames();
    bool getResetStyle();
    
private slots:

private:
    Ui::DEffect *ui;
};

#endif // DEFFECT_H
