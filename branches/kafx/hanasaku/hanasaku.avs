loadplugin("KAFX.dll")

DirectShowSource("fma.avi", audio=true)

converttorgb32()
FlipVertical()


KAFX("hanasaku", "hanasaku/hanasaku.ass")
FlipVertical()
