/********************************************************************************
** Form generated from reading UI file 'dafillmode.ui'
**
** Created: Wed 4. Jan 21:09:53 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DAFILLMODE_H
#define UI_DAFILLMODE_H

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

class Ui_DAFillMode
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *comboBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QComboBox *comboBox_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAFillMode)
    {
        if (DAFillMode->objectName().isEmpty())
            DAFillMode->setObjectName(QString::fromUtf8("DAFillMode"));
        DAFillMode->setWindowModality(Qt::WindowModal);
        DAFillMode->resize(400, 120);
        verticalLayout = new QVBoxLayout(DAFillMode);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DAFillMode);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        comboBox = new QComboBox(DAFillMode);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DAFillMode);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        comboBox_2 = new QComboBox(DAFillMode);
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        horizontalLayout_2->addWidget(comboBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        buttonBox = new QDialogButtonBox(DAFillMode);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAFillMode);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAFillMode, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAFillMode, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAFillMode);
    } // setupUi

    void retranslateUi(QDialog *DAFillMode)
    {
        DAFillMode->setWindowTitle(QApplication::translate("DAFillMode", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAFillMode", "Part", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DAFillMode", "Type", 0, QApplication::UnicodeUTF8));
        comboBox_2->clear();
        comboBox_2->insertItems(0, QStringList()
         << QApplication::translate("DAFillMode", "Solid", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Texture", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Vertical Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Horizontal Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Diagonal Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Radial Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Animated Lineal Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Animated Radial Gradient", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DAFillMode", "Colored Pattern", 0, QApplication::UnicodeUTF8)
        );
    } // retranslateUi

};

namespace Ui {
    class DAFillMode: public Ui_DAFillMode {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DAFILLMODE_H
