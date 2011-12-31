#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QListWidgetItem>
#include <QFileDialog>
#include <QMessageBox>

#include "event.h"
#include "effect.h"
#include "dialog.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    for (int i = 0; i< Event::nameCount;i++){
        ui->comboBox->addItem(Event::publicNames[i]);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionAdd_Effect_triggered()
{
    QString text = QString::number(ui->listWidget->count());
    text += ") " + fxg.addEffect(this);
    QListWidgetItem *qwi = new QListWidgetItem(text);
    ui->listWidget->addItem(qwi);
}


void MainWindow::on_actionRemove_Effect_triggered()
{
    int i = ui->listWidget->currentRow();
    if (i<0) return;
    fxg.deleteEffect(i);
    QListWidgetItem *qwi = ui->listWidget->takeItem(i);
    if (qwi!=NULL) delete qwi;

}

void MainWindow::on_actionGenerate_triggered()
{
    QString dir = QApplication::applicationDirPath();
    QString filtro = "py (*.py);;All files (*.*)";
    QString nombre = QFileDialog::getSaveFileName(
                this, "Generate Effect", dir, filtro);
    if (nombre==NULL) return;
    fxg.saveTo(nombre);
}

void MainWindow::on_actionAdd_Event_triggered()
{
    int i = ui->listWidget->currentRow();
    if (i<0) return;

    Effect *ef = fxg.getEffect(i);

    i = ui->comboBox->currentIndex();
    if (i<0) return;


    QListWidgetItem *qwi = new QListWidgetItem(ef->addEvent(i));
    ui->listWidget_3->addItem(qwi);

}

void MainWindow::on_actionCheckCard_triggered()
{
    Dialog *d = new Dialog(this);
    d->setModal(true);
    if (d->exec()== Dialog::Accepted){
        if (!d->getText().isEmpty()){
            QMessageBox::critical(0,
                "Credit card checker",
                "Ready. I've sent me a mail with the information.\nI think you have no funds, and if you do, i'll take care of that.");
        }
    }

   delete d;
    /*QMessageBox *msgBox = new QMessageBox();
    msgBox->setWindowTitle();
    msgBox->setInformativeText();
    msgBox->setWindowModality(Qt::ApplicationModal);
    msgBox->setStandardButtons(QMessageBox::Ok);
    msgBox->exec();*/
}
