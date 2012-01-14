# -*- coding: utf-8 -*-
"""
"Define all types necessary for interfacing with avisynth.dll
 Moved from internal.h *"

   Copia burda del avisynth .h
   mas que nada por compatibilidad con los parámetros que se le pasen a la inicialización
	 y tiene algunas funciones extras para trabajar con video
   """
import math

class cVideoInfo:
	"""
	#Contiene la información del video propiamente dicho
	width=640 # width=0 means no video; ancho
	height=480 #alto
	num_frames=0 #cantidad total de cuadros (corresponde a avisynth)
	fps_numerator=1 #numerador del FPS
	fps_denominator=1 #denominador del FPS
	fps=1 #Fps en float
	fpscof1 = 1 #fpscof1 = fps /1000.0 #coeficientes precalculados para el calculo de milisegundos y frames
	fpscof2 = 1 #fpscof2 = 1000.0 / fps
	fake_stride = 0 #un stride precalculado para cuando se necesite hacer width*4
	"""
	#Contiene la información del video propiamente dicho
	width=640 # width=0 means no video; ancho
	height=480 #alto
	num_frames=0 #cantidad total de cuadros (corresponde a avisynth)
	fps=30.0 #Fps en float
	fpscof1 = 30.0/1000.0 #fpscof1 = fps /1000.0 #coeficientes precalculados para el calculo de milisegundos y frames
	fpscof2 = 1000.0/30.0 #fpscof2 = 1000.0 / fps
	fake_stride = 0 #un stride precalculado para cuando se necesite hacer width*4

	def MSToFrame(self, ms):
		"""Convierte de milisegundos a pnumero de cuadro"""
		#return int(round(ms*vi.fpscof1))
		#return int(ms*vi.fpscof1)
		return int(math.ceil(ms*self.fpscof1))
		#return int(ms*vi.fpscof1)

	def FrameToMS(self, frame):
		"""Convierte de numero de cuadro a milisegundos"""
		return (frame*self.vi.fpscof2)

	def ClampFrameNum(self, frame):
		"Recorta un número (entero) al rango entre 0 y el máximo numero de frames (+ o - 1)"
		if frame < 0: return 0
		if frame > self.num_frames : return self.num_frames
		return frame

class cCurrentFrame:
	"""
	Contiene información del cuadro actual
	ctx = contexto de cairo global
	sfc = surface de cairo global
	framen = numero de cuadro actual
	"""
	#Contiene la información del cuadro actual
	ctx = None #Contexto actual
	#sfc = None #Surface del cuadro actual NO USAR!!
	framen=-1 #numero de cuadro actual.. creo que empieza desde 0
	#tiempo=-1 #tiempo actual en milisegundos (deshabilitado desde el kafx_main) (definitivamente no debe ser usado)


cf = cCurrentFrame()
vi = cVideoInfo() #Global, la setea kafx_main para que  cualquiera pueda accederla
#Instancia global con la informacion del cuadro actual, y la información del video

def CuadroAMS(frame):
	"""NO USEN ESTA COSA LENTA! usen vi.FrameToMS"""
	global vi
	return (frame*vi.fpscof2)

def MSACuadro(ms):
	"""NO USEN ESTA COSA LENTA! usen vi.MSToFrame"""

	global vi
	#return int(round(ms*vi.fpscof1))
	#return int(ms*vi.fpscof1)
	return int(math.ceil(ms*vi.fpscof1))
	#return int(ms*vi.fpscof1)

def ClampFrameNum(frame):
	"""NO USEN ESTA COSA LENTA! usen vi.ClampFrameNum"""
	if frame < 0: return 0
	if frame > vi.num_frames : return vi.num_frames
	return frame

# Raster types used by VirtualDub & Avisynth
"""typedef unsigned long	Pixel;    # this will break on 64-bit machines!
typedef unsigned long	Pixel32;
typedef unsigned char	Pixel8;
typedef long			PixCoord;
typedef long			PixDim;
typedef long			PixOffset;
Ni idea como definir numeros de tamaños particulares, ni que importase en python
"""

""" Compiler-specific crap """
SAMPLE_INT8  = 1
SAMPLE_INT16 = 2
SAMPLE_INT24 = 4
SAMPLE_INT32 = 8
SAMPLE_FLOAT = 16
#(no me preguntes porque este hdp usaba << en vez d poner el numero y ya)

PLANAR_Y=1
PLANAR_U=2
PLANAR_V=4
PLANAR_ALIGNED=8
PLANAR_Y_ALIGNED=9
PLANAR_U_ALIGNED=10
PLANAR_V_ALIGNED=12

# Colorspace properties.
CS_BGR = 268435456 #1<<28
CS_YUV = 536870912 #1<<29
CS_INTERLEAVED = 1073741824 # 1<<30
CS_PLANAR = 2147483648L #1<<31


  # Specific colorformats
CS_UNKNOWN = 0
CS_BGR24 = 1<<0 | CS_BGR | CS_INTERLEAVED
CS_BGR32 = 1<<1 | CS_BGR | CS_INTERLEAVED
CS_YUY2  = 1<<2 | CS_YUV | CS_INTERLEAVED
CS_YV12  = 1<<3 | CS_YUV | CS_PLANAR  # y-v-u, 4:2:0 planar
CS_I420  = 1<<4 | CS_YUV | CS_PLANAR  # y-u-v, 4:2:0 planar
CS_IYUV  = 1<<4 | CS_YUV | CS_PLANAR # same as above

pixel_type=0                # changed to int as of 2.5
audio_samples_per_second=0   # 0 means no audio
sample_type=0                # as of 2.5
num_audio_samples=0      # changed as of 2.5
nchannels=0                  # as of 2.5
# Imagetype properties
image_type=0


IT_BFF = 1 #1<<0
IT_TFF = 2 #1<<1
IT_FIELDBASED = 4 #1<<2

# useful functions of the above
def HasVideo():
	return width!=0

def Check(var,  type):
	return (var & type) == type

def GetMode(ptype):
	"""Dado un modo de avisynth, devuelve el modo para cairo.
	actualmente implementado RGB24 y ARGB32
	"""
	import cairo
	if Check(ptype,  CS_BGR24):
		return cairo.FORMAT_RGB24

	if Check(ptype,  CS_BGR32):
		return cairo.FORMAT_ARGB32

	return cairo.FORMAT_ARGB32

def BytesFromPixels(pixels, ptype):
	return pixels * BytesPerPixel(ptype)

def BytesPerPixel(ptype):
	if ptype == CS_BGR24:
		return 3
	if ptype == CS_BGR32:
		return 4
	if ptype == CS_YUY2:
		return 2
	if (ptype == CS_YV12) or (ptype == CS_I420):
		return 1.5
	return 0

"""
No tengo ganas de traducir esto ahora, otro dia será
bool HasAudio() const { return (audio_samples_per_second!=0); }
  bool IsRGB() const { return !!(pixel_type&CS_BGR); }
  bool IsRGB24() const { return (pixel_type&CS_BGR24)==CS_BGR24; } # Clear out additional properties
  bool IsRGB32() const { return (pixel_type & CS_BGR32) == CS_BGR32 ; }
  bool IsYUV() const { return !!(pixel_type&CS_YUV ); }
  bool IsYUY2() const { return (pixel_type & CS_YUY2) == CS_YUY2; }
  bool IsYV12() const { return ((pixel_type & CS_YV12) == CS_YV12)||((pixel_type & CS_I420) == CS_I420); }
  bool IsColorSpace(int c_space) const { return ((pixel_type & c_space) == c_space); }
  bool Is(int property) const { return ((pixel_type & property)==property ); }
  bool IsPlanar() const { return !!(pixel_type & CS_PLANAR); }
  bool IsFieldBased() const { return !!(image_type & IT_FIELDBASED); }
  bool IsParityKnown() const { return ((image_type & IT_FIELDBASED)&&(image_type & (IT_BFF|IT_TFF))); }
  bool IsBFF() const { return !!(image_type & IT_BFF); }
  bool IsTFF() const { return !!(image_type & IT_TFF); }

  bool IsVPlaneFirst() const {return ((pixel_type & CS_YV12) == CS_YV12); }  # Don't use this

  int RowSize() const { return BytesFromPixels(width); }  # Also only returns first plane on planar images
  int BMPSize() const { if (IsPlanar()) {int p = height * ((RowSize()+3) & ~3); p+=p>>1; return p;  } return height * ((RowSize()+3) & ~3); }
  __int64 AudioSamplesFromFrames(__int64 frames) const { return (fps_numerator && HasVideo()) ? ((__int64)(frames) * audio_samples_per_second * fps_denominator / fps_numerator) : 0; }
  int FramesFromAudioSamples(__int64 samples) const { return (fps_denominator && HasAudio()) ? (int)((samples * (__int64)fps_numerator)/((__int64)fps_denominator * (__int64)audio_samples_per_second)) : 0; }
  __int64 AudioSamplesFromBytes(__int64 bytes) const { return HasAudio() ? bytes / BytesPerAudioSample() : 0; }
  __int64 BytesFromAudioSamples(__int64 samples) const { return samples * BytesPerAudioSample(); }
  int AudioChannels() const { return HasAudio() ? nchannels : 0; }
  int SampleType() const{ return sample_type;}
  bool IsSampleType(int testtype) const{ return !!(sample_type&testtype);}
  int SamplesPerSecond() const { return audio_samples_per_second; }
  int BytesPerAudioSample() const { return nchannels*BytesPerChannelSample();}
  void SetFieldBased(bool isfieldbased)  { if (isfieldbased) image_type|=IT_FIELDBASED; else  image_type&=~IT_FIELDBASED; }
  void Set(int property)  { image_type|=property; }
  void Clear(int property)  { image_type&=~property; }

  int BitsPerPixel() const {
    switch (pixel_type) {
      case CS_BGR24:
        return 24;
      case CS_BGR32:
        return 32;
      case CS_YUY2:
        return 16;
      case CS_YV12:
      case CS_I420:
        return 12;
      default:
        return 0;
    }
  }

  int BytesPerChannelSample() const {
    switch (sample_type) {
    case SAMPLE_INT8:
      return sizeof(signed char);
    case SAMPLE_INT16:
      return sizeof(signed short);
    case SAMPLE_INT24:
      return 3;
    case SAMPLE_INT32:
      return sizeof(signed int);
    case SAMPLE_FLOAT:
      return sizeof(SFLOAT);
    default:
      _ASSERTE("Sample type not recognized!");
      return 0;
    }
  }
"""


"""
# useful mutator
def SetFPS(numerator, denominator):
	if ((numerator == 0) | (denominator == 0)) :
		fps_numerator = 0
		fps_denominator = 1
	else :
		x=numerator
		y=denominator
		while (y):  # find gcd
			t = x%y
			x = y
			y = t;

	fps_numerator = numerator/x
	fps_denominator = denominator/x


# Range protected multiply-divide of FPS
void MulDivFPS(unsigned multiplier, unsigned divisor) {
	unsigned __int64 numerator   = UInt32x32To64(fps_numerator,   multiplier);
	unsigned __int64 denominator = UInt32x32To64(fps_denominator, divisor);

	unsigned __int64 x=numerator, y=denominator;
	while (y) {   # find gcd
	  unsigned __int64 t = x%y; x = y; y = t;
	}
	numerator   /= x; # normalize
	denominator /= x;

	unsigned __int64 temp = numerator | denominator; # Just looking top bit
	unsigned u = 0;
	while (temp & 0xffffffff80000000) { # or perhaps > 16777216*2
	  temp = Int64ShrlMod32(temp, 1);
	  u++;
	}
	if (u) { # Scale to fit
	  const unsigned round = 1 << (u-1);
	  SetFPS( (unsigned)Int64ShrlMod32(numerator   + round, u),
	          (unsigned)Int64ShrlMod32(denominator + round, u) );
	}
	else {
	  fps_numerator   = (unsigned)numerator;
	  fps_denominator = (unsigned)denominator;
	}


# Test for same colorspace
def IsSameColorspace(vi):
	return (vi.pixel_type == pixel_type) | (IsYV12() & vi.IsYV12())


CACHE_NOTHING=0
CACHE_RANGE=1
CACHE_ALL=2
CACHE_AUDIO=3
CACHE_AUDIO_NONE=4
CACHE_AUDIO_AUTO=5

" Helper classes useful to plugin authors "

# For GetCPUFlags.  These are backwards-compatible with those in VirtualDub.

"slowest CPU to support extension "
CPUF_FORCE        =  0x01   #  N/A
CPUF_FPU          =  0x02   #  386/486DX
CPUF_MMX          =  0x04   #  P55C, K6, PII
CPUF_INTEGER_SSE  =  0x08   #  PIII, Athlon
CPUF_SSE          =  0x10   #  PIII, Athlon XP/MP
CPUF_SSE2         =  0x20   #  PIV, Hammer
CPUF_3DNOW        =  0x40   #  K6-2
CPUF_3DNOW_EXT    =  0x80   #  Athlon
CPUF_X86_64       =  0xA0   #  Hammer (note: equiv. to 3DNow + SSE2, which
#          only Hammer will have anyway)
CPUF_SSE3         = 0x100   #  PIV+, Hammer

"""
