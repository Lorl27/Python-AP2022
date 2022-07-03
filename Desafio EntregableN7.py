import tkinter
from tkinter import font

def Nombre():
    ingreso=entrada.get()
    print("¡Bienvenid@ piloto " + ingreso + "!, ¡Naveguemos!")

gui=tkinter.Tk()
gui.title("El mejor Dron")

texto=tkinter.Label(gui,text="Aca manejaremos al mejor Dron, tienes suerte de poder hacerlo...")
texto.grid(row=0,column=0)

entrada=tkinter.Entry(bg="white",width=20,bd=4,justify="center",selectbackground="red",selectforeground="white",font=font.Font(family="MV Boli",size=12,slant=font.ITALIC))
entrada.grid(row=2,column=1)


boton=tkinter.Button(gui,text="Aprete aquí una vez que ingreso su nombre", command=Nombre)
boton.grid(row=3,column=1)

gui.mainloop()