#ifndef KAFX_GLOBAL_H
#define KAFX_GLOBAL_H
#include <QtCore/qglobal.h>

#if defined(KAFX_LIBRARY)
#  define KAFXSHARED_EXPORT Q_DECL_EXPORT
#else
#  define KAFXSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // KAFX_GLOBAL_H
