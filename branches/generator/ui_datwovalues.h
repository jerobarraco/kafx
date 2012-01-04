/********************************************************************************
** Form generated from reading UI file 'datwovalues.ui'
**
** Created: Wed 4. Jan 19:21:49 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DATWOVALUES_H
#define UI_DATWOVALUES_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DATwoValues
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QDoubleSpinBox *doubleSpinBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QDoubleSpinBox *doubleSpinBox_2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QComboBox *comboBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DATwoValues)
    {
        if (DATwoValues->objectName().isEmpty())
            DATwoValues->setObjectName(QString::fromUtf8("DATwoValues"));
        DATwoValues->resize(400, 173);
        verticalLayout = new QVBoxLayout(DATwoValues);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DATwoValues);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        doubleSpinBox = new QDoubleSpinBox(DATwoValues);
        doubleSpinBox->setObjectName(QString::fromUtf8("doubleSpinBox"));
        doubleSpinBox->setMinimum(-999999);
        doubleSpinBox->setMaximum(1e+06);
        doubleSpinBox->setSingleStep(10000);

        horizontalLayout->addWidget(doubleSpinBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DATwoValues);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        doubleSpinBox_2 = new QDoubleSpinBox(DATwoValues);
        doubleSpinBox_2->setObjectName(QString::fromUtf8("doubleSpinBox_2"));
        doubleSpinBox_2->setMinimum(-99999);
        doubleSpinBox_2->setMaximum(100000);
        doubleSpinBox_2->setSingleStep(0.01);

        horizontalLayout_2->addWidget(doubleSpinBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(DATwoValues);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        comboBox = new QComboBox(DATwoValues);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_3->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_3);

        buttonBox = new QDialogButtonBox(DATwoValues);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DATwoValues);
        QObject::connect(buttonBox, SIGNAL(accepted()), DATwoValues, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DATwoValues, SLOT(reject()));

        QMetaObject::connectSlotsByName(DATwoValues);
    } // setupUi

    void retranslateUi(QDialog *DATwoValues)
    {
        DATwoValues->setWindowTitle(QApplication::translate("DATwoValues", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DATwoValues", "From", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DATwoValues", "To", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DATwoValues", "Interpolator", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DATwoValues: public Ui_DATwoValues {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DATWOVALUES_H
