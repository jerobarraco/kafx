/********************************************************************************
** Form generated from reading UI file 'darotate.ui'
**
** Created: Wed 4. Jan 03:37:22 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DAROTATE_H
#define UI_DAROTATE_H

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

class Ui_DARotate
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

    void setupUi(QDialog *DARotate)
    {
        if (DARotate->objectName().isEmpty())
            DARotate->setObjectName(QString::fromUtf8("DARotate"));
        DARotate->resize(400, 179);
        verticalLayout = new QVBoxLayout(DARotate);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DARotate);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        doubleSpinBox = new QDoubleSpinBox(DARotate);
        doubleSpinBox->setObjectName(QString::fromUtf8("doubleSpinBox"));
        doubleSpinBox->setSingleStep(0.01);

        horizontalLayout->addWidget(doubleSpinBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DARotate);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        doubleSpinBox_2 = new QDoubleSpinBox(DARotate);
        doubleSpinBox_2->setObjectName(QString::fromUtf8("doubleSpinBox_2"));
        doubleSpinBox_2->setSingleStep(0.01);

        horizontalLayout_2->addWidget(doubleSpinBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(DARotate);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        comboBox = new QComboBox(DARotate);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_3->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_3);

        buttonBox = new QDialogButtonBox(DARotate);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DARotate);
        QObject::connect(buttonBox, SIGNAL(accepted()), DARotate, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DARotate, SLOT(reject()));

        QMetaObject::connectSlotsByName(DARotate);
    } // setupUi

    void retranslateUi(QDialog *DARotate)
    {
        DARotate->setWindowTitle(QApplication::translate("DARotate", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DARotate", "From", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DARotate", "To", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DARotate", "Interpolator", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DARotate: public Ui_DARotate {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DAROTATE_H
