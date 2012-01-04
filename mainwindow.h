#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFile>
#include <QModelIndex>
#include "fxsgroup.h"
#include "deffect.h"

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    FxsGroup fxg;
    DEffect *diag;
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void reloadEffect();
    void reloadEvent();

private slots:
    void on_actionAdd_Effect_triggered();
    void on_actionRemove_Effect_triggered();
    void on_actionGenerate_triggered();
    void on_actionAdd_Event_triggered();
    void on_actionCheckCard_triggered();
    void on_actionAdd_Action_triggered();
    void on_actionRemove_Event_triggered();
    void on_actionRemove_Action_triggered();
    void on_listWidget_currentRowChanged(int currentRow);
    void on_listWidget_2_currentRowChanged(int currentRow);
    void on_actionEdit_Effect_triggered();

private:
    Effect * getCurrentEffect();
    Event * getCurrentEvent();
    Action * getCurrentAction();
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
