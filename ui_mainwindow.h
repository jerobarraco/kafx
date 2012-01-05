/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Wed 4. Jan 21:22:08 2012
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
#include <QtGui/QMenu>
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
    QAction *actionCheckCard;
    QAction *actionAdd_Action;
    QAction *actionRemove_Event;
    QAction *actionRemove_Action;
    QAction *actionEdit_Effect;
    QAction *actionEdit_Action;
    QWidget *centralWidget;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QListWidget *listWidget;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_2;
    QComboBox *comboBox;
    QListWidget *listWidget_2;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_3;
    QComboBox *comboBox_2;
    QListWidget *listWidget_3;
    QMenuBar *menuBar;
    QMenu *menuEffects;
    QMenu *menuEvents;
    QMenu *menuActions;
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
        actionCheckCard = new QAction(MainWindow);
        actionCheckCard->setObjectName(QString::fromUtf8("actionCheckCard"));
        actionAdd_Action = new QAction(MainWindow);
        actionAdd_Action->setObjectName(QString::fromUtf8("actionAdd_Action"));
        actionRemove_Event = new QAction(MainWindow);
        actionRemove_Event->setObjectName(QString::fromUtf8("actionRemove_Event"));
        actionRemove_Action = new QAction(MainWindow);
        actionRemove_Action->setObjectName(QString::fromUtf8("actionRemove_Action"));
        actionEdit_Effect = new QAction(MainWindow);
        actionEdit_Effect->setObjectName(QString::fromUtf8("actionEdit_Effect"));
        actionEdit_Action = new QAction(MainWindow);
        actionEdit_Action->setObjectName(QString::fromUtf8("actionEdit_Action"));
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

        listWidget_2 = new QListWidget(centralWidget);
        listWidget_2->setObjectName(QString::fromUtf8("listWidget_2"));

        verticalLayout_2->addWidget(listWidget_2);


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

        listWidget_3 = new QListWidget(centralWidget);
        listWidget_3->setObjectName(QString::fromUtf8("listWidget_3"));

        verticalLayout_3->addWidget(listWidget_3);


        horizontalLayout->addLayout(verticalLayout_3);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 728, 22));
        menuEffects = new QMenu(menuBar);
        menuEffects->setObjectName(QString::fromUtf8("menuEffects"));
        menuEvents = new QMenu(menuBar);
        menuEvents->setObjectName(QString::fromUtf8("menuEvents"));
        menuActions = new QMenu(menuBar);
        menuActions->setObjectName(QString::fromUtf8("menuActions"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuEffects->menuAction());
        menuBar->addAction(menuEvents->menuAction());
        menuBar->addAction(menuActions->menuAction());
        menuEffects->addAction(actionAdd_Effect);
        menuEffects->addAction(actionRemove_Effect);
        menuEffects->addAction(actionEdit_Effect);
        menuEvents->addAction(actionAdd_Event);
        menuEvents->addAction(actionRemove_Event);
        menuActions->addAction(actionAdd_Action);
        menuActions->addAction(actionEdit_Action);
        menuActions->addAction(actionRemove_Action);
        mainToolBar->addAction(actionAdd_Effect);
        mainToolBar->addAction(actionRemove_Effect);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionAdd_Event);
        mainToolBar->addAction(actionRemove_Event);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionAdd_Action);
        mainToolBar->addAction(actionEdit_Action);
        mainToolBar->addAction(actionRemove_Action);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionGenerate);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionCheckCard);
        mainToolBar->addSeparator();

        retranslateUi(MainWindow);

        listWidget->setCurrentRow(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Kafx FX Generator", 0, QApplication::UnicodeUTF8));
        actionAdd_Effect->setText(QApplication::translate("MainWindow", "Add Effect", 0, QApplication::UnicodeUTF8));
        actionAdd_Event->setText(QApplication::translate("MainWindow", "Add Event", 0, QApplication::UnicodeUTF8));
        actionRemove_Effect->setText(QApplication::translate("MainWindow", "Remove Effect", 0, QApplication::UnicodeUTF8));
        actionGenerate->setText(QApplication::translate("MainWindow", "Generate", 0, QApplication::UnicodeUTF8));
        actionCheckCard->setText(QApplication::translate("MainWindow", "Check if your credit card has funds", 0, QApplication::UnicodeUTF8));
        actionAdd_Action->setText(QApplication::translate("MainWindow", "Add Action", 0, QApplication::UnicodeUTF8));
        actionRemove_Event->setText(QApplication::translate("MainWindow", "Remove Event", 0, QApplication::UnicodeUTF8));
        actionRemove_Action->setText(QApplication::translate("MainWindow", "Remove Action", 0, QApplication::UnicodeUTF8));
        actionEdit_Effect->setText(QApplication::translate("MainWindow", "Edit Effect", 0, QApplication::UnicodeUTF8));
        actionEdit_Action->setText(QApplication::translate("MainWindow", "Modify Action", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "Effects", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Events", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "Actions", 0, QApplication::UnicodeUTF8));
        comboBox_2->clear();
        comboBox_2->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "Scale", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Rotate", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Move", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Move From", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Move To", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Fade", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Paint", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Paint Reflection", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Paint using Cache", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Change Color", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Fill Mode", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Change Shadow Size", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Change Border Size", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Set Texture", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Shake", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Wiggle", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Start Group", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "End Group", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Glow", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Blur", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "RotoZoom", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Wave", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Define Variable", 0, QApplication::UnicodeUTF8)
        );
        menuEffects->setTitle(QApplication::translate("MainWindow", "Effects", 0, QApplication::UnicodeUTF8));
        menuEvents->setTitle(QApplication::translate("MainWindow", "Events", 0, QApplication::UnicodeUTF8));
        menuActions->setTitle(QApplication::translate("MainWindow", "Actions", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
