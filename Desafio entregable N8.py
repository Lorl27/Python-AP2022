import os
ruta=os.path.dirname(os.path.abspath(__file__))

file=open(ruta+"\CLASE 6\Control de Misiones\Registros\mision_01.txt","r")

contenido=file.readlines()

for x in contenido:
    if "mision recreativa":
        print(x)

file.close()