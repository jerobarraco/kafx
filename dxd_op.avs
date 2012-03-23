loadplugin("KAFX.dll")
DirectShowSource("OP-muxed (1).avi", audio = false)
#KillAudio(ColorBars(1280,720))
#Trim(0,1700)
#Lanczos4Resize(960, 540)

converttorgb32()
FlipVertical()


KAFX("fxs.Abelkm.dxd_op", "dxd_op.ass")
FlipVertical()
