import compileall, os
compileall.compile_dir(os.getcwd(), force=True)
print "Listo, los pyc son tuyos :D"