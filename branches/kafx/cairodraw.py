#!/usr/bin/env python

import pygtk; pygtk.require("2.0")
import gtk
import cairo
import pango
import sys
import os
import math

DEFAULT_BUFFER = """\
# This is a Python script to quickly test Cairo stuff!
#Modified for use with KAFX
from libs import comun, video, asslib, formas
from libs.draw import basico, extra, avanzado

video.vi.width = w
video.vi.height = h
video.cf.ctx = c

#para cargar de un ass
ass = asslib.Ass("test.ass", 3)
d = ass.dialogues[5]
d.Paint()
s = d._silabas[2]
s.actual.color1.CopyFrom(s.actual.color2)
s.Paint()

##Para crear un texto a mano
##creamos un estilo #no es indispensable
#estilo = asslib.cPropiedades()
#estilo._size = 80
#estilo._font = "Verdana"
#estilo._italic = True
#estilo._align = 5
##creamos un vector
#d = extra.cVector(texto="Hihi!", estilo=estilo)
#d.Pintar()
"""

CAIRODRAW_LIBRARY_ROUTINES        = {}
CAIRODRAW_LIBRARY_ROUTINE_DATA    = {}
CAIRODRAW_LIBRARY_GLOBALS         = {}
CAIRODRAW_LIBRARY_GLOBAL_CALLBACK = lambda *a, **k: None

def CairoDrawLibrarySetGlobal(g, val):
	global CAIRODRAW_LIBRARY_GLOBALS

	CAIRODRAW_LIBRARY_GLOBALS[g] = val

	CAIRODRAW_LIBRARY_GLOBAL_CALLBACK()

def CairoDrawLibraryRoutine(function):
	global CAIRODRAW_LIBRARY_ROUTINES
	global CAIRODRAW_LIBRARY_ROUTINE_DATA

	CAIRODRAW_LIBRARY_ROUTINES[function.func_name] = function

	CAIRODRAW_LIBRARY_ROUTINE_DATA[function.func_name] = (
		" ".join(function.func_code.co_varnames[:function.func_code.co_argcount]),
		function.func_doc.lstrip().rstrip().replace("\t", "")
	)

	def CairoDrawLibraryRoutineDecorator(*args, **kargs):
		try:
			return function(*args, **kargs)

		except Exception, e:
			print "Exception in CairoDrawLibraryRoutine", function.func_name,
			print " - error was:", e

	return CairoDrawLibraryRoutineDecorator

# -------------------------------------------------------------------------------------------------

@CairoDrawLibraryRoutine
def drawLinePath(cr, x, y, xx, yy, seg):
	"""Draws a segmented line path using the given segment distance, starting
	at the coords x, y and ending at the coords xx, yy."""

	pass

@CairoDrawLibraryRoutine
def drawRoundedRectangle(cr, x, y, width, height, radius):
	"""Takes the X, Y, width, and height values and 'rounds' them usiing the
	given radius."""

	cr.move_to(x + radius, y)
	cr.line_to(x + width - radius, y)

	cr.arc(
		x + width - radius,
		y + radius,
		radius,
		-90.0 * math.pi / 180.0,
		0.0 * math.pi / 180.0
	)

	cr.line_to(x + width, y + height - radius)

	cr.arc(
		x + width - radius,
		y + height - radius,
		radius,
		0.0 * math.pi / 180.0,
		90.0 * math.pi / 180.0
	)

	cr.line_to(x + radius, y + height)

	cr.arc(
		x + radius,
		y + height - radius,
		radius,
		90.0 * math.pi / 180.0,
		180.0 * math.pi / 180.0
	)

	cr.line_to(x, y + radius)

	cr.arc(
		x + radius,
		y + radius,
		radius,
		180.0 * math.pi / 180.0,
		270.0 * math.pi / 180.0
	)


@CairoDrawLibraryRoutine
def createPattern(cr, w, h, r):
	"""Creates a pattern; sets the variable 'pattern'"""

	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(w), int(h))
	context = cairo.Context(surface)
	matrix  = cairo.Matrix()

	matrix.rotate(r)

	context.scale(w, h)
	context.rectangle(0.0, 0.0, 1.0, 1.0)
	context.set_source_rgba(0.0, 0.0, 0.0, 0.0)
	context.fill()
	context.set_line_width(0.01)
	context.set_source_rgba(0.5, 0.5, 0.5, 1.0)

	drawLinePath(context, 5)

	pattern = cairo.SurfacePattern(surface)

	pattern.set_matrix(matrix)

	context.stroke()

	CairoDrawLibrarySetGlobal("pattern", pattern)

	return pattern

@CairoDrawLibraryRoutine
def createShadow(x, y, r1, r2):
	"""Creates a RadianGradient"""

	radial = cairo.RadialGradient(x, y, r1, x, y, r2)

	radial.add_color_stop_rgba(0.0, 0.0, 0.0, 0.0, 1.0)
	radial.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)

	return radial

@CairoDrawLibraryRoutine
def drawRadialGradientCircle(cr, x, y, r1, r2, colStart, colEnd):
	"""Creates a RadianGradient"""

	radial = cairo.RadialGradient(x, y, r1, x, y, r2)

	radial.add_color_stop_rgba(*((1.0,) + colStart))
	radial.add_color_stop_rgba(*((0.0,) + colEnd))

	cr.set_source(radial)
	cr.arc(x, y, r2, 0, 2 * math.pi)

def createLinearGradient(h, downUp=False):
	linear = cairo.LinearGradient(0.0, 0.0, 0.0, h)

	if downUp:
		linear.add_color_stop_rgba(0.0, 0.3, 0.3, 0.3, 1.0)
		linear.add_color_stop_rgba(1.0, 0.7, 0.7, 0.7, 1.0)

	else:
		linear.add_color_stop_rgba(0.0, 0.7, 0.7, 0.7, 1.0)
		linear.add_color_stop_rgba(1.0, 0.3, 0.3, 0.3, 1.0)

	return linear

def createLinearGradientFill(h, downUp=False):
	linear = cairo.LinearGradient(0.0, 0.0, 0.0, h)

	linear.add_color_stop_rgba(0.0, 0.3, 0.3, 0.3, 0.2)
	linear.add_color_stop_rgba(1.0, 0.7, 0.7, 0.7, 0.2)

	return linear

def draw(cr, w, h, r):
	pattern = createPattern(14.0, 14.0, r)

	pattern.set_extend(cairo.EXTEND_REPEAT)

	cr.set_source(pattern)

	cr.scale(w, h)
	cr.rectangle(0.0, 0.0, 1.0, 1.0)
	cr.fill_preserve()

# -------------------------------------------------------------------------------------------------

class CairoDrawingArea(gtk.DrawingArea):
	def __init__(self, width=0, height=0, win=None, buf=DEFAULT_BUFFER):
		gtk.DrawingArea.__init__(self)

		self.__buffer = buf
		self.__win    = win

		self.set_size_request(width, height)

		self.connect("expose-event", self.__render)

	def __render(self, widget, event):
		cr   = self.window.cairo_create()
		w, h = self.allocation.width, self.allocation.height

		if self.__win:
			self.__win.SetStatus(w, h)

		self.__eval(self.__buffer, cr, w, h)

		return True

	def __eval(self, buf, cr, w, h):
		CairoDrawLibrarySetGlobal("c", cr)
		CairoDrawLibrarySetGlobal("w", w)
		CairoDrawLibrarySetGlobal("h", h)

		glbls = {}

		glbls.update(CAIRODRAW_LIBRARY_ROUTINES)
		glbls.update(CAIRODRAW_LIBRARY_GLOBALS)

		eval(compile(buf, "<cairoscript>", "exec"), glbls)

	def Parse(self, buf):
		self.__buffer = buf

		self.queue_draw()

	def WriteToPNG(self, path):
		w, h = self.allocation.width, self.allocation.height

		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
		context = cairo.Context(surface)

		self.__eval(self.__buffer, context, w, h)

		surface.write_to_png(path)

	def WriteToSVG(self, path):
		w, h = self.allocation.width, self.allocation.height

		surface = cairo.SVGSurface(path, w, h)
		context = cairo.Context(surface)

		self.__eval(self.__buffer, context, w, h)

		surface.flush()
		surface.finish()

class TextView(gtk.TextView):
	def __init__(self, text=""):
		gtk.TextView.__init__(self)

		buf = gtk.TextBuffer()

		buf.set_text(text)

		self.set_buffer(buf)
		self.set_size_request(-1, 300)
		self.connect("realize", self.__realize)

	def __realize(self, *args):
		self.SetFontSize(12)

	def SetText(self, text):
		self.get_buffer().set_text(text)

	def SetFontSize(self, size):
		font = pango.FontDescription("monospace")

		font.set_size(pango.SCALE * size)

		self.modify_font(font)

	def GetText(self):
		buf = self.get_buffer()

		return buf.get_text(buf.get_start_iter(), buf.get_end_iter())

class NotebookTab(gtk.HBox):
	def __init__(self, text, stock):
		gtk.HBox.__init__(self)

		image = gtk.Image()
		label = gtk.Label(text)

		image.set_from_stock(stock, gtk.ICON_SIZE_MENU)

		label.set_alignment(0.5, 0.5)
		label.set_padding(2, 2)

		self.pack_start(image, False, False)
		self.pack_start(label, False, False)
		self.show_all()

class ColorBox(gtk.VBox):
	def __init__(self, color="#b8c2dd"):
		gtk.VBox.__init__(self)

		self.__bg    = None
		self.__color = color

	def __callbackMouseOver(self, widget, event, mouseover):
		if mouseover:
			if not self.__bg:
				self.__bg = widget.get_style().bg[gtk.STATE_NORMAL]

			colormap = gtk.gdk.Colormap(gtk.gdk.visual_get_system(), True)
			color    = colormap.alloc_color(self.__color)

			widget.modify_bg(gtk.STATE_NORMAL, color)

		else:
			widget.modify_bg(gtk.STATE_NORMAL, self.__bg)

		widget.queue_draw()

	def __callbackChildOver(self, widget, event, child, callback):
		callback(child, event)

	def __callbackChildClick(self, widget, event, child, callback):
		callback(child, event)

	def Pack(
		self,
		child,
		expand=True,
		fill=True,
		padding=0,
		onover=lambda *a: None,
		onout=lambda *a: None,
		onclick=lambda *a: None
	):
		evbox = gtk.EventBox()

		evbox.add(child)
		evbox.modify_bg(gtk.STATE_NORMAL, self.__bg)

		self.pack_start(evbox, expand, fill, padding)

		evbox.connect("enter-notify-event", self.__callbackMouseOver, True)
		evbox.connect_after("enter-notify-event", self.__callbackChildOver, child, onover)

		evbox.connect("leave-notify-event", self.__callbackMouseOver, False)
		evbox.connect_after("leave-notify-event", self.__callbackChildOver, child, onout)

		evbox.connect("button-press-event", self.__callbackChildClick, child, onclick)

class LibraryRoutine(gtk.Alignment):
	def __init__(self, name, args="", help=""):
		gtk.Alignment.__init__(self, 0.0, 0.0, 1.0, 1.0)

		self.__help = gtk.Label()

		self.set_padding(10, 10, 10, 10)

		vbox = gtk.VBox()
		hbox = gtk.HBox()

		nameLabel = gtk.Label()
		argsLabel = gtk.Label()

		nameLabel.set_markup("<b>%s</b>" % name)
		nameLabel.set_alignment(0.0, 0.5)

		if args:
			argsLabel.set_markup("(<i>%s</i>)" % ", ".join(args.split()))
			argsLabel.set_alignment(0.0, 0.5)
			argsLabel.set_padding(5, 0)

		self.SetHelp(help)
		self.__help.set_alignment(0.0, 0.0)

		hbox.pack_start(nameLabel, False, False)
		hbox.pack_start(argsLabel)

		vbox.pack_start(hbox)
		vbox.pack_start(self.__help, padding=5)

		self.add(vbox)

	def SetHelp(self, help):
		self.__help.set_markup("<span size='smaller'>%s</span>" % help)

class CairoWindow(gtk.Window):
	def __init__(self, w, h, script=None):
		gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)

		b = script and file(script).read() or DEFAULT_BUFFER

		self.__draw   = CairoDrawingArea(w, h, self, b)
		self.__text   = TextView(b)
		self.__help   = ColorBox()
		self.__glbls  = LibraryRoutine("GLOBALS")
		self.__err    = TextView()
		self.__status = gtk.Statusbar()

		tool    = gtk.HBox()
		vbox    = gtk.VBox()
		scroll1 = gtk.ScrolledWindow()
		scroll2 = gtk.ScrolledWindow()
		paned   = gtk.VPaned()
		noteb   = gtk.Notebook()
		viewp   = gtk.Viewport()

		scroll1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		scroll1.add(self.__text)

		viewp.set_shadow_type(gtk.SHADOW_NONE)
		viewp.add(self.__help)

		scroll2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		scroll2.add(viewp)

		global CAIRODRAW_LIBRARY_GLOBAL_CALLBACK

		CAIRODRAW_LIBRARY_GLOBAL_CALLBACK = self.__updateGlobals

		self.__help.Pack(self.__glbls)
		self.__help.pack_start(gtk.HSeparator(), False, True)

		self.__updateGlobals()

		for lrn, lrd in CAIRODRAW_LIBRARY_ROUTINE_DATA.iteritems():
			self.__help.Pack(LibraryRoutine(lrn, *lrd))

			# This is a clever trick that lets us remove the last
			# one added, since there's still a reference around.
			hsep = gtk.HSeparator()

			self.__help.pack_start(hsep, False, True)

		self.__help.remove(hsep)

		noteb.append_page(scroll1, NotebookTab("Source", gtk.STOCK_EDIT))
		noteb.append_page(scroll2, NotebookTab("Library Routines & Globals", gtk.STOCK_HELP))
		noteb.append_page(self.__err, NotebookTab("Error Log", gtk.STOCK_DIALOG_WARNING))

		paned.add1(self.__draw)
		paned.add2(noteb)

		vbox.pack_start(paned)
		vbox.pack_start(tool, False, False, 2)
		vbox.pack_start(self.__status, False, False)

		for st, tt, cb in zip((
			gtk.STOCK_OPEN,
			gtk.STOCK_SAVE,
			gtk.STOCK_YES,
			gtk.STOCK_REFRESH,
			gtk.STOCK_QUIT
		), (
			"Open an existing CairoScript",
			"Save this CairoScript",
			"Write CairoScript to PNG/SVG images",
			"Refresh the DrawingArea",
			"Quit the application"
		), (
			self.__openScript,
			self.__saveScript,
			self.__savePNG,
			self.__parseCode,
			lambda *a, **k: gtk.main_quit()
		)):
			button = gtk.Button()
			image  = gtk.Image()

			image.set_from_stock(st, gtk.ICON_SIZE_MENU)

			button.set_relief(gtk.RELIEF_NONE)
			button.set_focus_on_click(False)
			button.set_image(image)
			button.set_tooltip_text(tt)
			button.connect("clicked", cb)

			tool.pack_start(button, False, False)

		fontSizeLabel = gtk.Label("Font Size:")
		fontSize      = gtk.combo_box_new_text()

		fontSizeLabel.set_alignment(1.0, 0.5)

		[fontSize.append_text("%i" % i) for i in range(5, 13)]

		fontSize.connect("changed", self.__setFont)
		fontSize.set_active(0)

		tool.pack_start(fontSizeLabel, True, True, 5)
		tool.pack_start(fontSize, False, False)

		self.set_title("cairodraw - kafx edition")
		self.add(vbox)
		self.set_focus(self.__text)

	def __updateGlobals(self, *args):
		self.__glbls.SetHelp(", ".join(
			g for g in CAIRODRAW_LIBRARY_GLOBALS if not g == "__builtins__"
		))

	def __openScript(self, *args):
		fc = gtk.FileChooserDialog(
			"Select a CairoScript file...",
			self,
			buttons=(gtk.STOCK_CANCEL, 0, gtk.STOCK_OPEN, 1)
		)

		fl1 = gtk.FileFilter()

		fl1.set_name("CairoScripts")
		fl1.add_pattern("*.cairo")

		fl2 = gtk.FileFilter()

		fl2.set_name("All Files")
		fl2.add_pattern("*")

		fc.add_filter(fl1)
		fc.add_filter(fl2)

		if fc.run():
			self.__text.SetText(file(fc.get_filename()).read())

			self.__parseCode()

		fc.destroy()

	def __saveScript(self, *args):
		fc = gtk.FileChooserDialog(
			"Save File As...",
			self,
			gtk.FILE_CHOOSER_ACTION_SAVE,
			(gtk.STOCK_CANCEL, 0, gtk.STOCK_SAVE, 1)
		)

		if fc.run():
			f = fc.get_filename()

			if not ".cairo" in f:
				f += ".cairo"

			print >> file(f, "w"), self.__text.GetText()

		fc.destroy()

	def __savePNG(self, *args):
		fc = gtk.FileChooserDialog(
			"Save PNG/SVG Images As...",
			self,
			gtk.FILE_CHOOSER_ACTION_SAVE,
			(gtk.STOCK_CANCEL, 0, gtk.STOCK_SAVE, 1)
		)

		if fc.run():
			self.__draw.WriteToPNG(fc.get_filename() + ".png")
			self.__draw.WriteToSVG(fc.get_filename() + ".svg")

		fc.destroy()

	def __parseCode(self, *args):
		self.__draw.Parse(self.__text.GetText())

	def __setFont(self, cb):
		self.__text.SetFontSize(int(cb.get_active_text()))

	def SetStatus(self, w, h):
		self.__status.push(0, "Dimensions: %i x %i" % (w, h))

if __name__ == "__main__":
	f = None

	if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
		f = sys.argv[1]

	cw = CairoWindow(640, 480, f)

	cw.connect("destroy", gtk.main_quit)
	cw.show_all()

	gtk.main()
