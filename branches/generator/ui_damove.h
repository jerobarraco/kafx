/********************************************************************************
** Form generated from reading UI file 'damove.ui'
**
** Created: Wed 4. Jan 04:27:23 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DAMOVE_H
#define UI_DAMOVE_H

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
#include <QtGui/QSpinBox>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DAMove
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QSpinBox *spinBox;
    QSpinBox *spinBox_2;
    QHBoxLayout *horizontalLayout;
    QLabel *label_2;
    QSpinBox *spinBox_3;
    QSpinBox *spinBox_4;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QComboBox *comboBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DAMove)
    {
        if (DAMove->objectName().isEmpty())
            DAMove->setObjectName(QString::fromUtf8("DAMove"));
        DAMove->resize(400, 147);
        verticalLayout = new QVBoxLayout(DAMove);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(DAMove);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        spinBox = new QSpinBox(DAMove);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setMinimum(-999999);
        spinBox->setMaximum(999999);

        horizontalLayout_2->addWidget(spinBox);

        spinBox_2 = new QSpinBox(DAMove);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));
        spinBox_2->setMinimum(-999999);
        spinBox_2->setMaximum(999999);

        horizontalLayout_2->addWidget(spinBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_2 = new QLabel(DAMove);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout->addWidget(label_2);

        spinBox_3 = new QSpinBox(DAMove);
        spinBox_3->setObjectName(QString::fromUtf8("spinBox_3"));
        spinBox_3->setMinimum(-999999);
        spinBox_3->setMaximum(999999);

        horizontalLayout->addWidget(spinBox_3);

        spinBox_4 = new QSpinBox(DAMove);
        spinBox_4->setObjectName(QString::fromUtf8("spinBox_4"));
        spinBox_4->setMinimum(-999999);
        spinBox_4->setMaximum(999999);

        horizontalLayout->addWidget(spinBox_4);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(DAMove);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        comboBox = new QComboBox(DAMove);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_3->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_3);

        buttonBox = new QDialogButtonBox(DAMove);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DAMove);
        QObject::connect(buttonBox, SIGNAL(accepted()), DAMove, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DAMove, SLOT(reject()));

        QMetaObject::connectSlotsByName(DAMove);
    } // setupUi

    void retranslateUi(QDialog *DAMove)
    {
        DAMove->setWindowTitle(QApplication::translate("DAMove", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DAMove", "From (x, y)", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DAMove", "To (x, y)", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DAMove", "Interpolator", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DAMove: public Ui_DAMove {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DAMOVE_H
