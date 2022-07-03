# coding: utf8
import recursos.moduloTello as moduloTello
import recursos.moduloInterfaz as moduloInterfaz
import threading
import datetime


import tkinter as coso
from tkinter.constants import END
import os

rutita = os.path.dirname(os.path.abspath(__file__)) 

# --- SECCIÓN INICIALIZACION ---
miDron = moduloTello.Tello() #Para inicializar el Dron
# miDron = moduloTello.TelloSinEstados(). Si existen problemas al decodificar según versión SDK
miInterfaz = moduloInterfaz.Interfaz() #Se crea  la interfaz
miInterfaz.setear_dron_controlado(miDron) #Se une el dron con la interfaz

# HACIENDO EL DESAFÍO:
"""
Pantalla 1:
-Tener una etiqueta de información, que le indique al operador que ingrese su nombre en un widget de tipo Entry.
-Tener un botón que capture y guarde el texto.
-Tener un botón "Siguiente" que oculte esta primera parte de la interfaz, y muestre la siguiente.

Pantalla 2:
-Tener una etiqueta de información, que le indique al operador que ingrese los comandos de vuelo del dron en un widget de tipo Text.
-Tener un botón que capture y guarde el texto en el archivo "misionVuelo.txt".
-Tener un botón "Siguiente" que oculte esta segunda parte de la interfaz, y muestre la siguiente.

Pantalla 3:
-Tener un botón "Ejecutar misión autónoma" que, al ser clickeado, ejecute una función llamada leerComandosArchivo
"""
ventanita=coso.Tk()
ventanita.geometry("600x400")
ventanita.title="Bienvenido al Dron"

# crear ventanas: 

#VENTANA 1:
ventana1=coso.Frame(ventanita)
ventana1.grid(row=0,column=1)

text1=coso.Label(ventana1,text="Ingresá tu nombre, apretá el botón y, luego 'continuar' ")
text1.grid()

input1=coso.Entry(ventana1)
input1.grid()

def nombreAqui():
    name=text1.get()
    nameVisi=coso.Label(ventana2,text="Operador:" + name) #Se mostrará en la ventana2
    nameVisi.grid()

boton1=coso.Button(ventana1,text="Save",command=nombreAqui)
boton1.grid()

#Cambiar de pantalla 1 a 2:
def SwitchPantallas():
    ventana1.grid_remove()
    ventana2.grid()

cambio=coso.Button(ventana1,text="continuar",command=SwitchPantallas) #Botón "Continuar"
cambio.grid()

# VENTANA 2:
ventana2=coso.Frame(ventanita) #No le ponemos grid asi no la inicializamos al comienzo (mostramos)

text2=coso.Label(ventana2,text="Ingresá la lista de comandos para el Dron, separados por 'TAB', presione el botón y, luego 'continuar' ")
text2.grid(row=0,column=0)

input2=coso.Text(ventana2)
input2.grid(row=0,column=1)

def save_commands():
    commands=text2.get("1.0",END) #guardamos el texto
    archivo=open(rutita + "\misionVuelo.txt","w") #abrimos el archivo
    archivo.write(commands) #le escribimos le texto guardado
    archivo.close() 

boton2=coso.Button(ventana2,text="Apretá acá",command=save_commands)
boton2.grid(row=2,column=2)

#Cambiar de pantalla 2 a 3:
def SwitchPantallas2():
    ventana2.grid_remove()
    ventana3.grid()

cambio2=coso.Button(ventana2,text="continuar",command=SwitchPantallas2) #Botón "Continuar"
cambio2.grid()

# VENTANA 3:
ventana3=coso.Frame(ventanita) #No le ponemos grid asi no la inicializamos (mostramos)

def leerComandosArchivo():
    miInterfaz.setear_archivo(rutita + "\misionVuelo.txt") #Busca el archivo
    miInterfaz.ejecutar_mision_archivo() #se conecta con el Dron

boton3=coso.Button(ventana3,text="Iniciar misión",command=leerComandosArchivo)
boton3.grid(row=0,column=0)

# AGREGAR TKINTER A LA INTERFAZ
miInterfaz.setear_ventana_tkinter(ventanita)
ventanita.mainLoop()

# --- SECCIÓN CONTROLES REMOTOS ---
velocidadMovimiento = 60 # VELOCIDAD DE MOVIMIENTO

# --- SECCIÓN FINAL ---
miInterfaz.correr() # CORRER LA INTERFAZ