loadplugin("KAFX.dll")

KillAudio(ColorBars(1280,720))
Trim(0,1700)
#Lanczos4Resize(960, 540)

converttorgb32()
FlipVertical()


KAFX("fxs.Abelkm.testa", "test.ass")
FlipVertical()
