loadplugin("KAFX.dll")
DirectShowSource("[RAW] Dantalian OP01.avi", audio = false)
#KillAudio(ColorBars(1280,720))
#Trim(0,3000)
#Lanczos4Resize(1280,720)

converttorgb32()
FlipVertical()


KAFX("fxs.AbelKM.dan", "[RAW] Dantalian OP01.ass")
FlipVertical()
