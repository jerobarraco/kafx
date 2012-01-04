#ifndef DAPAINT_H
#define DAPAINT_H

#include <QDialog>

namespace Ui {
class DAPaint;
}

class DAPaint : public QDialog
{
    Q_OBJECT
    
public:
    explicit DAPaint(QWidget *parent = 0);
    ~DAPaint();
    
private:
    Ui::DAPaint *ui;
};

#endif // DAPAINT_H
