#ifndef FXSGROUP_H
#define FXSGROUP_H
#include "effect.h"
#include <QList>
#include <QFile>
#include <QStringList>
#include <QString>

enum MODULES {RANDOM, RANDINT, COMUN, ASSLIB, AUDIO, FORMAS, VIDEO, AVANZADO, BASICO, EXTRA};

class FxsGroup
{
    QList<Effect*> effects;
    QFile archivo;
    QStringList genStructure();

public:
    FxsGroup();
    ~FxsGroup();
    QString addEffect(QWidget *parent);
    void deleteEffect(int index);
    bool saveTo(QString filename);
    Effect *getEffect(int index);
    QList<int> getModules();
    QStringList moduleUrls;
    //uso dos string list para no marear usando un list de map
    static const int interCant = 15;
    static QString interNames[];//el name es para el combo
    static QString interUrls[];//las urls para cargar
		static QString modules[];//las urls para cargar
    //me da paja ponerlas privadas
    int diag_in, diag_out, sil_in, sil_out, let_in, let_out;
    bool splitlet, skipframes, reset_style;
};

#endif // FXSGROUP_H
