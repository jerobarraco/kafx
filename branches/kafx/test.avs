#Este es un archivo de prueba, abrelo con el media player para verlo funcionando

#para crear el tuyo copia este archivo
loadplugin("KAFX.dll")
#En vez de la siguiente linea, pon algo como 
#AviSource("C:\mivideito.avi")
#o
#DirectShowSource("c:\mivideo.mkv")
KillAudio(ColorBars())
converttorgb32()
FlipVertical()
#coloca donde dice fxs.simple el nombre del archivo .py en la carpeta fxs (sin el py)
#y donde dice test.ass el nombre de archivo con el karaoke
#(y colocalo en esta misma carpeta)
KAFX("fxs.simple", "test.ass")
FlipVertical()

#y abre tu archivo con el virtualdub, y guardalo con el formato que desees