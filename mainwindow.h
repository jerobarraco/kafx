#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFile>
#include "fxsgroup.h"
namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    FxsGroup fxg;
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_actionAdd_Effect_triggered();
    void on_actionRemove_Effect_triggered();
    void on_actionGenerate_triggered();
    void on_actionAdd_Event_triggered();
    void on_actionCheckCard_triggered();

private:

    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
