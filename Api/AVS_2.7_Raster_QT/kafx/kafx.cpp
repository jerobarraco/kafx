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
                env->ThrowError("Dll-> Could not create main dictionary for python");

            PyRun_SimpleString("import traceback");
            /*PyRun_SimpleString("traceback.sys.stdout = open('stdout.txt', 'w')");
            PyRun_SimpleString("traceback.sys.stderr = open('stderr.txt',  'w')");*/

            Py_InitModule("raster", RasterMod);

            /* Safamos cualquier error que pueda haber */
            PyRun_SimpleString("from kafx_main import *");

            /*main_dict = PyModule_GetDict(mmodule);
            if (!main_dict)
                env->ThrowError ("Dll-> Error loading kafx_main\nLOOK INSIDE stderr.txt AND stdout.txt FILES TO SEE WHAT IS THE REAL ERROR.");
            */

            f_frame = PyObject_GetAttrString(mmodule, "OnFrame");
            if (!f_frame)
                env->ThrowError("Dll-> Python initialized, but the function \"OnFrame\" could not be found.\nPLEASE check kafx_log.txt AND error_log.txt to see the REAL error.");

            debug ("Dll-> Looks like everything is ok. Initializing....\n");
            if ( NULL == PyObject_CallMethod (mmodule, "OnInit", "ssiiiiiii",
                file, datastring, vi.pixel_type, vi.image_type, vi.width, vi.height, vi.fps_numerator,
                vi.fps_denominator,	vi.num_frames
                )){
                    debug("Dll-> Initialization failed\n");
                    env->ThrowError("Dll-> Initialization failed.\nPLEASE check kafx_log.txt AND error_log.txt to see the REAL error.");
            }else{
                debug("Dll-> Everything is loaded\n");
            };
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

