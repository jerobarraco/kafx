/*
 * Copyright © 2008 Kristian Høgsberg
 * Copyright © 2009 Chris Wilson
 *
 * Permission to use, copy, modify, distribute, and sell this software and its
 * documentation for any purpose is hereby granted without fee, provided that
 * the above copyright notice appear in all copies and that both that copyright
 * notice and this permission notice appear in supporting documentation, and
 * that the name of the copyright holders not be used in advertising or
 * publicity pertaining to distribution of the software without specific,
 * written prior permission.  The copyright holders make no representations
 * about the suitability of this software for any purpose.  It is provided "as
 * is" without express or implied warranty.
 *
 * THE COPYRIGHT HOLDERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
 * INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
 * EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY SPECIAL, INDIRECT OR
 * CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
 * DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
 * TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
 * OF THIS SOFTWARE.
 */

#include <math.h>
//#include <stdint>
#include "include\pstdint.h"
#include "include\Python\Python.h"

//#include "include\cairo\cairo.h"
#define ARRAY_LENGTH(b) (sizeof (b) / sizeof (b)[0])
#define None Py_BuildValue("");
/* Performs a simple 2D Gaussian blur of radius @radius on surface @surface. */

//crea un modulo de python

static int *K_skern = NULL;
static int *K_skernb = NULL;
static uint32_t K_div = 1;
static uint32_t K_divb = 1;
static uint32_t K_size = 10;
static uint32_t K_half = K_size/2;

/*
static PyObject* emb_numargs(PyObject *self, PyObject *args)
{
    if(!PyArg_ParseTuple(args, ":numargs"))
        return NULL;
    return Py_BuildValue("i", 0);
}*/

static PyObject* SetKernel(PyObject *self, PyObject *args){
	PyObject* tuple = NULL;

	if(!PyArg_ParseTuple(args, "O", &tuple))
		return NULL;
	
	int s = PySequence_Length(tuple);
	if (s<=0)
		return NULL;

	K_size = s/2;
	K_half = K_size /2;

	if (K_skern != NULL)
		delete [] K_skern;
	if (K_skernb != NULL)
		delete [] K_skernb;

	K_skern = new int[K_size];
	K_skernb = new int[K_size];
	PyObject** items = PySequence_Fast_ITEMS(tuple);
	K_div =0;	
	for (int i =0; i< K_size; i++){
		//a += kernel[i] = PyInt_AsLong(PyTuple_GetItem( tuple, i ));
		K_div += K_skern[i] = PyInt_AsLong(items[i]);
		K_skernb[i] = PyInt_AsLong(items[i+K_size]);
	}

	/*
	for (int i=0; i< K_size; i++){
		for (int j=0; j<K_size; j++){
			K_div += K_skern[i]*K_skernb[j];
		}
	}*/
	if (K_div ==0) K_div =1;

	Py_XDECREF(tuple);
	return Py_BuildValue("s", "ok");
}

static int getPixelGlobalPos(uint32_t x,uint32_t y, uint32_t stride, uint32_t psize, uint32_t byten){
	return (x*psize)+(y*stride)+byten;
}
static PyObject* Filter(PyObject *self, PyObject *args)
{
	if (K_skern == NULL)
		return Py_BuildValue("s", "Debe asignar el kernel llamando a SetSepKernel");

	Py_buffer view;

	int width, height, src_stride;

	if (!PyArg_ParseTuple(args, "iiiw*:raster.blur", &width, &height, &src_stride, &view))
		  return NULL;
	
	
	uint8_t* src = (uint8_t*) view.buf;
    //int src_total = height*src_stride;	//no se usa
	int psize = 4;
	int dst_stride = width*psize;
	uint8_t* dst = new uint8_t [height*dst_stride];
	uint8_t pix;

	for (int i=0; i < height; i++) {
		for (int j=0; j<width; j++){
			for (int p=0; p<4;p++){
				pix = 0;
				for (int k = 0; k<K_half; k++){
					//tpos como relativo,
					//como pixel
					int tpos = j+k-K_half;
					if (tpos<0) tpos+=width;
					if (tpos>width) tpos -= width;
					//como byte
					tpos *= psize;
					//global
					tpos += i*src_stride;
					tpos += p;
					pix += src[tpos] * K_skern[k];
				}
				pix /= K_div; 
				if (pix >255) pix = 255;
				if (pix <0) pix = 0;
				dst[getPixelGlobalPos(j,i, dst_stride, psize, p)] = pix;
			}
		}
	}

	for (int i=0; i < height; i++) {
		for (int j=i; j<i+width; j++){
			for (int p=0; p<4;p++){
				pix = 0;
				for (int k = 0; k<K_half; k++){
					//tpos como relativo,
					//como pixel
					int tpos = i+k-K_half;
					if (tpos<0) tpos+=height;
					if (tpos>height) tpos -= height;
					//como byte
					tpos *= dst_stride;
					//global
					tpos += j*psize;
					tpos += p;
					pix += dst[tpos] * K_skernb[k];
				}
				pix /= K_div; 
				if (pix >255) pix = 255;
				if (pix <0) pix = 0;
				src[getPixelGlobalPos(j,i, src_stride, psize, p)] = pix;
			}
		}
	}

	delete [] dst;
	dst=NULL;


	PyBuffer_Release(&view);
	Py_XDECREF(&view);
	return Py_BuildValue("s", "ok");

}


static PyMethodDef RasterMod[] = {
	{"Filter", Filter, METH_VARARGS, "Apply a filter to a surface"},
	{"SetKernel", SetKernel, METH_VARARGS, "Sets the kernel for the filter"},
    {NULL, NULL, 0, NULL}
};

//Insert the above code just above the main() function. Also, insert the following two statements directly after Py_Initialize():
//
