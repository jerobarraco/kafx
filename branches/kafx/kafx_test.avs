loadplugin("KAFX.dll")
#DirectShowSource("OP-muxed (1).avi", audio = true)
Blankclip(5000, 1280,720,color = $FFFFFF) #para blanco
#Blankclip(5000, 1280,720) #para negro
Trim(0,914)
#Lanczos4Resize(960, 540)

converttorgb32()
FlipVertical()


KAFX("fxs.Abelkm.colors_lincycle", "kafx_test.ass")
FlipVertical()
