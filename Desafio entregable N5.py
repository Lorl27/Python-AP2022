"""
GUI para las misiones de vuelo con: titulo, breve descripcion y boton
boton-funcion== pide el nombre del operador(usuario) y lo muestra en pantalla + le da una bienvenida
"""

import tkinter

def Hola():
    #name="Rocco"
    name=input("¿Cuál es su nombre piloto?:")
    text=tkinter.Label(gui,text=("¡Bienvenid@ piloto " + name + "! , ¡Naveguemos!"))
    text.grid(row=1,column=0)

gui=tkinter.Tk()
gui.title("El mejor Dron")
texto=tkinter.Label(gui,text="Aca manejaremos al mejor Dron, tienes suerte de poder hacerlo")
texto.grid(row=0,column=0)
boton=tkinter.Button(gui,text="Aprete aquí para ingresar", command=Hola)
boton.grid(row=0,column=1)
gui.mainloop()