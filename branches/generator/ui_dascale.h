/********************************************************************************
** Form generated from reading UI file 'dascale.ui'
**
** Created: Tue 3. Jan 21:57:03 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DASCALE_H
#define UI_DASCALE_H

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

class Ui_DAscale
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QDoubleSpinBox *doubleSpinBox;
    QHBoxLayout *horizontalLayout;
    QLabel *label_2;
    QDoubleSpinBox *doubleSpinBox_2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QComboBox *comboBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAscale)
    {
        if (DAscale->objectName().isEmpty())
            DAscale->setObjectName(QString::fromUtf8("DAscale"));
        DAscale->resize(400, 155);
        verticalLayout = new QVBoxLayout(DAscale);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(DAscale);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        doubleSpinBox = new QDoubleSpinBox(DAscale);
        doubleSpinBox->setObjectName(QString::fromUtf8("doubleSpinBox"));
        doubleSpinBox->setMinimum(-99);
        doubleSpinBox->setSingleStep(0.01);

        horizontalLayout_2->addWidget(doubleSpinBox);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_2 = new QLabel(DAscale);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout->addWidget(label_2);

        doubleSpinBox_2 = new QDoubleSpinBox(DAscale);
        doubleSpinBox_2->setObjectName(QString::fromUtf8("doubleSpinBox_2"));
        doubleSpinBox_2->setMinimum(-99);
        doubleSpinBox_2->setMaximum(99.99);
        doubleSpinBox_2->setSingleStep(0.01);

        horizontalLayout->addWidget(doubleSpinBox_2);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(DAscale);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        comboBox = new QComboBox(DAscale);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_3->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_3);

        buttonBox = new QDialogButtonBox(DAscale);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAscale);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAscale, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAscale, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAscale);
    } // setupUi

    void retranslateUi(QDialog *DAscale)
    {
        DAscale->setWindowTitle(QApplication::translate("DAscale", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAscale", "From", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DAscale", "To", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DAscale", "Interpolation", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DAscale: public Ui_DAscale {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DASCALE_H
