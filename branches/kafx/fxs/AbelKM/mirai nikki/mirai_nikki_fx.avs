loadplugin("KAFX.dll")
DirectShowSource("[Shin]Mirai_Nikki_-_OP[TV-720p][A07551F2].mkv", audio = true)
#KillAudio(ColorBars(1280,720))
#Trim(0,1700)
#Lanczos4Resize(960, 540)

converttorgb32()
FlipVertical()


KAFX("fxs.AbelKM.mirai_nikki_op", "[Shin]Mirai_Nikki_-_OP[TV-720p][A07551F2] (1)_Track3.ass")
FlipVertical()
