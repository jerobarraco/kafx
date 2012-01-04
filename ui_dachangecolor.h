/********************************************************************************
** Form generated from reading UI file 'dachangecolor.ui'
**
** Created: Wed 4. Jan 03:37:22 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DACHANGECOLOR_H
#define UI_DACHANGECOLOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DAChangeColor
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label;
    QComboBox *comboBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QComboBox *comboBox_2;
    QHBoxLayout *horizontalLayout;
    QLabel *label_3;
    QComboBox *comboBox_3;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAChangeColor)
    {
        if (DAChangeColor->objectName().isEmpty())
            DAChangeColor->setObjectName(QString::fromUtf8("DAChangeColor"));
        DAChangeColor->resize(400, 158);
        verticalLayout = new QVBoxLayout(DAChangeColor);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label = new QLabel(DAChangeColor);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_3->addWidget(label);

        comboBox = new QComboBox(DAChangeColor);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_3->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DAChangeColor);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        comboBox_2 = new QComboBox(DAChangeColor);
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        horizontalLayout_2->addWidget(comboBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_3 = new QLabel(DAChangeColor);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout->addWidget(label_3);

        comboBox_3 = new QComboBox(DAChangeColor);
        comboBox_3->setObjectName(QString::fromUtf8("comboBox_3"));

        horizontalLayout->addWidget(comboBox_3);


        verticalLayout->addLayout(horizontalLayout);

        buttonBox = new QDialogButtonBox(DAChangeColor);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAChangeColor);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAChangeColor, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAChangeColor, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAChangeColor);
    } // setupUi

    void retranslateUi(QDialog *DAChangeColor)
    {
        DAChangeColor->setWindowTitle(QApplication::translate("DAChangeColor", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAChangeColor", "Change Wich Color", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DAChangeColor", "To which color", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DAChangeColor", "Interpolator", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DAChangeColor: public Ui_DAChangeColor {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DACHANGECOLOR_H
