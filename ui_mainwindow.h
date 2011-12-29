/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Thu 29. Dec 04:40:23 2011
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QListWidget>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionAdd_Effect;
    QAction *actionAdd_Event;
    QAction *actionRemove_Effect;
    QAction *actionGenerate;
    QWidget *centralWidget;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QListWidget *listWidget;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_2;
    QComboBox *comboBox;
    QListWidget *listWidget_3;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_3;
    QComboBox *comboBox_2;
    QListWidget *listWidget_2;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(728, 365);
        actionAdd_Effect = new QAction(MainWindow);
        actionAdd_Effect->setObjectName(QString::fromUtf8("actionAdd_Effect"));
        actionAdd_Event = new QAction(MainWindow);
        actionAdd_Event->setObjectName(QString::fromUtf8("actionAdd_Event"));
        actionRemove_Effect = new QAction(MainWindow);
        actionRemove_Effect->setObjectName(QString::fromUtf8("actionRemove_Effect"));
        actionGenerate = new QAction(MainWindow);
        actionGenerate->setObjectName(QString::fromUtf8("actionGenerate"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        horizontalLayout = new QHBoxLayout(centralWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout->addWidget(label);

        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);


        horizontalLayout->addLayout(verticalLayout);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        verticalLayout_2->addWidget(label_2);

        comboBox = new QComboBox(centralWidget);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        verticalLayout_2->addWidget(comboBox);

        listWidget_3 = new QListWidget(centralWidget);
        listWidget_3->setObjectName(QString::fromUtf8("listWidget_3"));

        verticalLayout_2->addWidget(listWidget_3);


        horizontalLayout->addLayout(verticalLayout_2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout_3->addWidget(label_3);

        comboBox_2 = new QComboBox(centralWidget);
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        verticalLayout_3->addWidget(comboBox_2);

        listWidget_2 = new QListWidget(centralWidget);
        listWidget_2->setObjectName(QString::fromUtf8("listWidget_2"));

        verticalLayout_3->addWidget(listWidget_2);


        horizontalLayout->addLayout(verticalLayout_3);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 728, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        mainToolBar->addAction(actionAdd_Effect);
        mainToolBar->addAction(actionRemove_Effect);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionAdd_Event);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionGenerate);

        retranslateUi(MainWindow);

        listWidget->setCurrentRow(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        actionAdd_Effect->setText(QApplication::translate("MainWindow", "Add Effect", 0, QApplication::UnicodeUTF8));
        actionAdd_Event->setText(QApplication::translate("MainWindow", "Add Event", 0, QApplication::UnicodeUTF8));
        actionRemove_Effect->setText(QApplication::translate("MainWindow", "Remove Effect", 0, QApplication::UnicodeUTF8));
        actionGenerate->setText(QApplication::translate("MainWindow", "Generate", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "Effects", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Events", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "Preset", 0, QApplication::UnicodeUTF8));
        comboBox_2->clear();
        comboBox_2->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "Move", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Glow", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Paint", 0, QApplication::UnicodeUTF8)
        );
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
