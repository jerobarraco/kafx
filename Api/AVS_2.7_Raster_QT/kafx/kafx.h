#ifndef KAFX_H
#define KAFX_H

#include "kafx_global.h"
#include "include/avisynth_n.h"
#include "include/python/Python.h"

class KAFXSHARED_EXPORT Kafx: public GenericVideoFilter {
private:
    PyObject* mmodule; //main module
    PyObject* main_dict;
    PyObject* f_frame;
    unsigned frame_size; // Lo cacheamos acá para no hacer la misma op por cada cuadro
    unsigned char *frame;
public:
    PVideoFrame __stdcall GetFrame(int n, IScriptEnvironment* env);
    void debug(char * msg){
        PyObject_CallMethod (mmodule, "DBug", "s" ,msg);
        return;
    }
    Kafx(PClip _child, IScriptEnvironment *env, const char *file, const char *datastring);
    ~Kafx(){
        if (Py_IsInitialized()){
            PyObject_CallMethod (mmodule, "OnDestroy", "" , NULL);

            Py_Finalize();
        };
    }
};

AVSValue __cdecl Create_Instance(AVSValue args, void* user_data, IScriptEnvironment* env)
{
    return new Kafx(args[0].AsClip(), env, args[1].AsString(), args[2].AsString(0));
}

#define DLLEXPORT __declspec(dllexport)

// extern "C" DLLEXPORT const char* __stdcall AvisynthPluginInit2(IScriptEnvironment* env) {
extern "C" KAFXSHARED_EXPORT const char* __stdcall AvisynthPluginInit2(IScriptEnvironment* env) {
    env->AddFunction("KAFX", "cs[data]s", Create_Instance, 0);
    return "Kick ASS Effects";
}
#endif // KAFX_H
