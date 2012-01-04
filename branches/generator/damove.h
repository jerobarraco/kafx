#ifndef DAMOVE_H
#define DAMOVE_H

#include <QDialog>

namespace Ui {
class DAMove;
}

class DAMove : public QDialog
{
    Q_OBJECT
    
public:
    explicit DAMove(QWidget *parent = 0);
    ~DAMove();
    QString getFromX();
    QString getFromY();
    QString getToX();
    QString getToY();
    int getInterpolator();
private:
    Ui::DAMove *ui;
};

#endif // DAMOVE_H
