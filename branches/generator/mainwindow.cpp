#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QListWidgetItem>
#include <QFileDialog>
#include <QMessageBox>
#include <QLibraryInfo>
#include <QTranslator>

#include "event.h"
#include "effect.h"
#include "dialog.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    diag = new DEffect(this);
    diag->setModal(true);
    for (int i = 0; i< Event::nameCount;i++){
        ui->comboBox->addItem(Event::publicNames[i]);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::reloadEffect()
{
    ui->listWidget_2->clear();
    Effect *ef = getCurrentEffect();
    if (ef==NULL) return;

    for (int i= 0; i<ef->getEventCount(); i++ ){
        QListWidgetItem *qwi = new QListWidgetItem(ef->getEvent(i)->toString());
        ui->listWidget_2->addItem(qwi);
    }
    reloadEvent();
}

void MainWindow::reloadEvent()
{
    ui->listWidget_3->clear();
    Event *ev = getCurrentEvent();
    if (ev==NULL) return;

    for (int i= 0; i<ev->getActionCount(); i++ ){
        QListWidgetItem *qwi = new QListWidgetItem(ev->getAction(i)->toString());
        ui->listWidget_3->addItem(qwi);
    }
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
    QListWidgetItem *qwi = ui->listWidget->takeItem(i);
    if (qwi!=NULL) delete qwi;

    fxg.deleteEffect(i);//importante que vaya despues
}

void MainWindow::on_actionGenerate_triggered()
{
    QString dir = QApplication::applicationDirPath();
    QString filtro = "py (*.py);;All files (*.*)";
    QString nombre = QFileDialog::getSaveFileName(
                this, tr("Generate Effect"), dir, filtro);
    if (nombre==NULL) return;
    fxg.saveTo(nombre);
}

void MainWindow::on_actionAdd_Event_triggered()
{
    Effect *ef = getCurrentEffect();
    if (ef==NULL)return;
    int i = ui->comboBox->currentIndex();
    if (i<0) return;

    QListWidgetItem *qwi = new QListWidgetItem(ef->addEvent(i));
    ui->listWidget_2->addItem(qwi);

}

void MainWindow::on_actionCheckCard_triggered()
{
    Dialog *d = new Dialog(this);
    d->setModal(true);
    if (d->exec()== Dialog::Accepted){
        if (!d->getText().isEmpty()){
            QMessageBox::critical(0,
                tr("Credit card checker"),
                tr("Ready. I've sent me a mail with the information.\nI think you have no funds, and if you do, i'll take care of that."));
        }
    }

   delete d;
}

void MainWindow::on_actionAdd_Action_triggered()
{
		Event *ev = getCurrentEvent();
		if (ev==NULL) return;
		int i = ui->comboBox_2->currentIndex();
		if (i<0) return;
    QListWidgetItem *qwi = new QListWidgetItem(ev->addAction(i));
		ui->listWidget_3->addItem(qwi);
}

void MainWindow::on_actionRemove_Event_triggered()
{
	Effect *ef = getCurrentEffect();
	if (ef==NULL)return;

	int i = ui->listWidget_2->currentRow();
	if (i<0) return;

    QListWidgetItem *qwi = ui->listWidget_2->takeItem(i);
    if (qwi!=NULL) delete qwi;

    ef->deleteEvent(i);
}

Effect *MainWindow::getCurrentEffect()
{
	int i = ui->listWidget->currentRow();
	if (i<0) return NULL;
	return fxg.getEffect(i);
}

Event *MainWindow::getCurrentEvent()
{
	Effect *ef = getCurrentEffect();
	if (ef==NULL) return NULL;
	int i = ui->listWidget_2->currentRow();
	if (i<0) return NULL;
	return ef->getEvent(i);
}

Action *MainWindow::getCurrentAction()
{
	Event *ev = getCurrentEvent();
	if (ev==NULL) return NULL;
	int i = ui->listWidget_3->currentRow();
	if (i<0) return NULL;
	return ev->getAction(i);
}

void MainWindow::on_actionRemove_Action_triggered()
{
	Event *ev = getCurrentEvent();
	if (ev==NULL) return;
	int i = ui->listWidget_3->currentRow();
	if (i<0)return;

    QListWidgetItem *qwi = ui->listWidget_3->takeItem(i);
    if (qwi!=NULL) delete qwi;

    ev->deleteAction(i);
}

void MainWindow::on_listWidget_currentRowChanged(int currentRow)
{
    reloadEffect();
}

void MainWindow::on_listWidget_2_currentRowChanged(int currentRow)
{
    reloadEvent();
}

void MainWindow::on_actionEdit_Effect_triggered()
{
    if (diag->exec()== diag->Accepted){
        fxg.diag_in = diag->getDiagIn();
        fxg.diag_out = diag->getDiagOut();
        fxg.sil_in = diag->getSilIn();
        fxg.sil_out = diag->getSilOut();
        fxg.let_in = diag->getLetIn();
        fxg.let_out = diag->getLetOut();
        fxg.splitlet = diag->getSplitLet();
        fxg.skipframes = diag->getSkipFrames();
        fxg.reset_style = diag->getResetStyle();
    }
}
