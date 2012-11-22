loadplugin("KAFX.dll")
DirectShowSource("[Shin]C3_-_OP[TV-720p][BA8D388F].mkv", audio = true)
#KillAudio(ColorBars(1280,720))
#Trim(0,1700)
#Lanczos4Resize(960, 540)

converttorgb32()
FlipVertical()


KAFX("fxs.Abelkm.c^3_op1v2", "[Shin]C3_-_OP[TV-720p][BA8D388F]_Track3.ass")
FlipVertical()
