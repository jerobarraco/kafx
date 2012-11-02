loadplugin("KAFX.dll")
#Blankclip(500, 1280,720, color = $FFFFFF)
#Trim(0,500)
DirectShowSource("OP01 (1).mkv", audio = true)
converttorgb32()
FlipVertical()


KAFX("fxs.Abelkm.kuroko", "kuroko_op.ass")
#KAFX("fxs.tutorials.t0038_timeblur", "kuroko_op.ass")

FlipVertical()
