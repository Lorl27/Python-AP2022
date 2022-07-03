"""
usar frame A para etiqueta, entrada grande y boton. COLOR VERDE
usar frame B para etiqueta y botón que oculte frame A (Color amarillo el botón)
"""

import tkinter
from tkinter.constants import END 

ventana= tkinter.Tk()
ventana.title("Testeando asuntos...")

#A

frameA=tkinter.Frame(ventana,bg="green")
frameA.grid(row=0,column=0)

etiquetteA=tkinter.Label(frameA,text="Texto A")
etiquetteA.grid()

caja=tkinter.Text(frameA)
caja.grid()

def save_txt():
    ingreso=caja.get("1.0",END)
    print(ingreso)

botonA=tkinter.Button(frameA,text="Soy un botón A",command=save_txt)
botonA.grid()

#B

frameB=tkinter.Frame(ventana,bg="yellow")
frameB.grid(row=0,column=1)

etiquetteB=tkinter.Label(frameB,text="Texto B")
etiquetteB.grid()

def delete_frameA():
    frameA.grid_remove()

botonB=tkinter.Button(frameB,text="Soy un botón B",command=delete_frameA,bg="yellow",fg="blue")
botonB.grid()

ventana.mainloop()