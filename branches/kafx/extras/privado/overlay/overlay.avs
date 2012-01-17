LoadPlugin("unpremultiply.dll")
clip1 = AviSource("fma.avi").converttorgb32()
clip2 = unpremultiply(AviSource("video en rgb32.avi"))
Overlay(clip1, clip2, mask=ShowAlpha(clip2))