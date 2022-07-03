"""
Vamos a utilizar las herramientas que aprendimos hoy, para pedirle al usuario que ingrese, por consola, los comandos para nuestra misión de vuelo. Los vamos a almacenar en una lista, y luego los guardaremos en el archivo "misiónVuelo.txt".
"""

L=[]

commands=input("Ingresa los datos de la misión aquí,por favor.")

#commands="hola"

for x in commands:
    L.append(x)

archivo=open("misiónVuelo.txt","w")

archivo.write(str(L))

archivo.close()

"""
También, puede ser:

import os

ruta= os.path.dirname(os.path.abspath(__file__))

L=[]

archivo=open(ruta+/misiónVuelo.txt","r")

archivo.close

for x in range(6):
    command=input("Ingresa los datos aquí,gracias")
    L.append(command)
    
for command in L:
    archivo.write(command+"\n")
    archivo.close()
"""