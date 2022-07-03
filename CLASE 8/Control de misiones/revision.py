import os
ruta=os.path.dirname(os.path.abspath(__file__))

file=open(ruta+"\Registros\misionesDeVuelo.txt","r")

contenido=file.readlines()

for x in contenido:
    print(x)

file.close()