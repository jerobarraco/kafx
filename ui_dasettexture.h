/********************************************************************************
** Form generated from reading UI file 'dasettexture.ui'
**
** Created: Tue 3. Jan 21:57:03 2012
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DASETTEXTURE_H
#define UI_DASETTEXTURE_H

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
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DASetTexture
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *comboBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QPushButton *pushButton;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DASetTexture)
    {
        if (DASetTexture->objectName().isEmpty())
            DASetTexture->setObjectName(QString::fromUtf8("DASetTexture"));
        DASetTexture->resize(400, 132);
        verticalLayout = new QVBoxLayout(DASetTexture);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(DASetTexture);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        comboBox = new QComboBox(DASetTexture);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(DASetTexture);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        lineEdit = new QLineEdit(DASetTexture);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setReadOnly(true);

        horizontalLayout_2->addWidget(lineEdit);

        pushButton = new QPushButton(DASetTexture);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_2->addWidget(pushButton);


        verticalLayout->addLayout(horizontalLayout_2);

        buttonBox = new QDialogButtonBox(DASetTexture);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DASetTexture);
        QObject::connect(buttonBox, SIGNAL(accepted()), DASetTexture, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DASetTexture, SLOT(reject()));

        QMetaObject::connectSlotsByName(DASetTexture);
    } // setupUi

    void retranslateUi(QDialog *DASetTexture)
    {
        DASetTexture->setWindowTitle(QApplication::translate("DASetTexture", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("DASetTexture", "Part", 0, QApplication::UnicodeUTF8));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("DASetTexture", "Fill", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DASetTexture", "Border", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("DASetTexture", "Shadow", 0, QApplication::UnicodeUTF8)
        );
        label_2->setText(QApplication::translate("DASetTexture", "Texture", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("DASetTexture", "...", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class DASetTexture: public Ui_DASetTexture {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DASETTEXTURE_H
