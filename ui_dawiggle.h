/********************************************************************************
** Form generated from reading UI file 'dawiggle.ui'
**
** Created: Wed 4. Jan 16:18:04 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DAWIGGLE_H
#define UI_DAWIGGLE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpinBox>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DAWiggle
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QSpinBox *spinBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QSpinBox *spinBox_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAWiggle)
    {
        if (DAWiggle->objectName().isEmpty())
            DAWiggle->setObjectName(QString::fromUtf8("DAWiggle"));
        DAWiggle->resize(400, 127);
        verticalLayout = new QVBoxLayout(DAWiggle);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DAWiggle);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        spinBox = new QSpinBox(DAWiggle);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));

        horizontalLayout->addWidget(spinBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DAWiggle);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        spinBox_2 = new QSpinBox(DAWiggle);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));

        horizontalLayout_2->addWidget(spinBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        buttonBox = new QDialogButtonBox(DAWiggle);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAWiggle);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAWiggle, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAWiggle, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAWiggle);
    } // setupUi

    void retranslateUi(QDialog *DAWiggle)
    {
        DAWiggle->setWindowTitle(QApplication::translate("DAWiggle", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAWiggle", "Amplitude", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DAWiggle", "Frequency", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DAWiggle: public Ui_DAWiggle {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DAWIGGLE_H
