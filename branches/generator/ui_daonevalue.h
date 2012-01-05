/********************************************************************************
** Form generated from reading UI file 'daonevalue.ui'
**
** Created: Wed 4. Jan 22:39:42 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DAONEVALUE_H
#define UI_DAONEVALUE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DAOneValue
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QDoubleSpinBox *doubleSpinBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAOneValue)
    {
        if (DAOneValue->objectName().isEmpty())
            DAOneValue->setObjectName(QString::fromUtf8("DAOneValue"));
        DAOneValue->resize(400, 89);
        verticalLayout = new QVBoxLayout(DAOneValue);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DAOneValue);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        doubleSpinBox = new QDoubleSpinBox(DAOneValue);
        doubleSpinBox->setObjectName(QString::fromUtf8("doubleSpinBox"));
        doubleSpinBox->setDecimals(0);
        doubleSpinBox->setMinimum(-999999);
        doubleSpinBox->setMaximum(999999);
        doubleSpinBox->setSingleStep(1);

        horizontalLayout->addWidget(doubleSpinBox);


        verticalLayout->addLayout(horizontalLayout);

        buttonBox = new QDialogButtonBox(DAOneValue);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAOneValue);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAOneValue, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAOneValue, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAOneValue);
    } // setupUi

    void retranslateUi(QDialog *DAOneValue)
    {
        DAOneValue->setWindowTitle(QApplication::translate("DAOneValue", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAOneValue", "To", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DAOneValue: public Ui_DAOneValue {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DAONEVALUE_H
