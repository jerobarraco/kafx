/********************************************************************************
** Form generated from reading UI file 'deffect.ui'
**
** Created: Wed 4. Jan 03:37:22 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DEFFECT_H
#define UI_DEFFECT_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QSpinBox>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DEffect
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QSpinBox *spinBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QSpinBox *spinBox_2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_3;
    QSpinBox *spinBox_3;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_4;
    QSpinBox *spinBox_4;
    QCheckBox *checkBox;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_6;
    QSpinBox *spinBox_5;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_5;
    QSpinBox *spinBox_6;
    QCheckBox *checkBox_2;
    QCheckBox *checkBox_3;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DEffect)
    {
        if (DEffect->objectName().isEmpty())
            DEffect->setObjectName(QString::fromUtf8("DEffect"));
        DEffect->resize(400, 330);
        verticalLayout = new QVBoxLayout(DEffect);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DEffect);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        spinBox = new QSpinBox(DEffect);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setMaximum(999999);
        spinBox->setValue(250);

        horizontalLayout->addWidget(spinBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DEffect);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        spinBox_2 = new QSpinBox(DEffect);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));
        spinBox_2->setMaximum(999999);
        spinBox_2->setValue(150);

        horizontalLayout_2->addWidget(spinBox_2);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_3 = new QLabel(DEffect);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_3->addWidget(label_3);

        spinBox_3 = new QSpinBox(DEffect);
        spinBox_3->setObjectName(QString::fromUtf8("spinBox_3"));
        spinBox_3->setMaximum(99999);
        spinBox_3->setValue(500);

        horizontalLayout_3->addWidget(spinBox_3);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label_4 = new QLabel(DEffect);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_4->addWidget(label_4);

        spinBox_4 = new QSpinBox(DEffect);
        spinBox_4->setObjectName(QString::fromUtf8("spinBox_4"));
        spinBox_4->setMaximum(999999);
        spinBox_4->setValue(200);

        horizontalLayout_4->addWidget(spinBox_4);


        verticalLayout->addLayout(horizontalLayout_4);

        checkBox = new QCheckBox(DEffect);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));

        verticalLayout->addWidget(checkBox);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_6 = new QLabel(DEffect);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_5->addWidget(label_6);

        spinBox_5 = new QSpinBox(DEffect);
        spinBox_5->setObjectName(QString::fromUtf8("spinBox_5"));
        spinBox_5->setEnabled(false);
        spinBox_5->setMaximum(999999);
        spinBox_5->setValue(200);

        horizontalLayout_5->addWidget(spinBox_5);


        verticalLayout->addLayout(horizontalLayout_5);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        label_5 = new QLabel(DEffect);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_6->addWidget(label_5);

        spinBox_6 = new QSpinBox(DEffect);
        spinBox_6->setObjectName(QString::fromUtf8("spinBox_6"));
        spinBox_6->setEnabled(false);
        spinBox_6->setMaximum(999999);
        spinBox_6->setValue(200);

        horizontalLayout_6->addWidget(spinBox_6);


        verticalLayout->addLayout(horizontalLayout_6);

        checkBox_2 = new QCheckBox(DEffect);
        checkBox_2->setObjectName(QString::fromUtf8("checkBox_2"));

        verticalLayout->addWidget(checkBox_2);

        checkBox_3 = new QCheckBox(DEffect);
        checkBox_3->setObjectName(QString::fromUtf8("checkBox_3"));

        verticalLayout->addWidget(checkBox_3);

        buttonBox = new QDialogButtonBox(DEffect);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DEffect);
        QObject::connect(checkBox, SIGNAL(toggled(bool)), spinBox_5, SLOT(setEnabled(bool)));
        QObject::connect(checkBox, SIGNAL(toggled(bool)), spinBox_6, SLOT(setEnabled(bool)));
        QObject::connect(buttonBox, SIGNAL(accepted()), DEffect, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DEffect, SLOT(reject()));

        QMetaObject::connectSlotsByName(DEffect);
    } // setupUi

    void retranslateUi(QDialog *DEffect)
    {
        DEffect->setWindowTitle(QApplication::translate("DEffect", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DEffect", "Dialog In Millisecs", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("DEffect", "Dialog Out Millisecs", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("DEffect", "Sillabe In Millisecs", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("DEffect", "Sillabe Out Millisecs", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        checkBox->setToolTip(QApplication::translate("DEffect", "This will make loading slow, use it only if needed.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        checkBox->setText(QApplication::translate("DEffect", "Split Letters", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("DEffect", "Letter In Millisecs", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("DEffect", "Letter Out Millisecs", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        checkBox_2->setToolTip(QApplication::translate("DEffect", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This can introduce errors on some effects.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">But can speed up kafx a little, use only if needed.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        checkBox_2->setText(QApplication::translate("DEffect", "Reset Style", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        checkBox_3->setToolTip(QApplication::translate("DEffect", "This can introduce errors on some effects using particles, audio and other things similar.\n"
"Use with care, only if needed.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP
        checkBox_3->setText(QApplication::translate("DEffect", "Skip Frames", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DEffect: public Ui_DEffect {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DEFFECT_H
