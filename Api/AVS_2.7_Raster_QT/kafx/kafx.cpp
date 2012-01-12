#include "kafx.h"
#include "raster.h"
#include "include/avisynth_n.h"
#include "kafx_global.h"
Kafx::Kafx(PClip _child, IScriptEnvironment *env, const char *file, const char *datastring)
    :GenericVideoFilter(_child)
{
    Py_SetProgramName("kafx");
            Py_Initialize();
            mmodule = PyImport_AddModule("__main__");
            main_dict = PyModule_GetDict(mmodule);
            if (!main_dict)
                env->ThrowError("Dll-> No pude crear el diccionario principal de python");

            PyRun_SimpleString("import traceback");
            /*PyRun_SimpleString("traceback.sys.stdout = open('stdout.txt', 'w')");
            PyRun_SimpleString("traceback.sys.stderr = open('stderr.txt',  'w')");*/

            Py_InitModule("raster", RasterMod);

            /* Safamos cualquier error que pueda haber */
            PyRun_SimpleString("from kafx_main import *");

            main_dict = PyModule_GetDict(mmodule);
            if (!main_dict)
                env->ThrowError ("Dll-> Error al cargar kafx_main.py, mirá el archivo stderr.txt\n o stdout.txt y si tenés suerte capaz que ahi dice que pasó\n y sinó ejecutalo desde una consola, aunque eso casi no funciona en windows, pero en linux si");

            f_frame = PyObject_GetAttrString(mmodule, "OnFrame");
            if (!f_frame)
                env->ThrowError("Dll-> Inicialice python, pero no pude cargar la funcion onFrame\n Existe? Hubo error?\n Revisa los archivos stdout.txt y stderr.txt");

            debug ("Dll-> Parece que todo esta cargado, intentemos inicializar\n");
            PyObject_CallMethod (mmodule, "OnInit", "ssiiiiiii",
                file, datastring, vi.pixel_type, vi.image_type, vi.width, vi.height, vi.fps_numerator,
                vi.fps_denominator,	vi.num_frames
                );

            debug("Dll-> Ya cargamos todo\n");
}

PVideoFrame __stdcall Kafx::GetFrame(int n, IScriptEnvironment* env)
{
    //AFX_MANAGE_STATE(AfxGetStaticModuleState());// esto es del MFC
    PVideoFrame src = child->GetFrame(n, env);
    unsigned char* srcpw = src->GetWritePtr();
    const int src_pitch = src->GetPitch();
    const int height = src->GetHeight();
    PyObject *buf = PyBuffer_FromReadWriteMemory(srcpw, height*src_pitch);
    PyObject_CallFunction(f_frame, "iiO", n, src_pitch, buf);
    //Py_CLEAR(buf);

    //PyObject_CallFunction(f_frame, "iiw", n, src_pitch, srcpw);
    return src;
};

