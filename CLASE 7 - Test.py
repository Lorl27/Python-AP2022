import tkinter
from tkinter import font

cuadro=tkinter.Tk()
cuadro.title("Testeando")

texto=tkinter.Label(cuadro,text="Aca manejaremos al mejor Dron, tienes suerte de poder hacerlo")
texto.grid(row=0,column=0)

#cuadros
ingresos=tkinter.Entry()
ingresos.grid(row=2,column=4)

test1= tkinter.Entry(fg="white", bg="red", width=50) #fg == color de texto | bg==color de fondo (1)
#[fieldbackground y foreground]
test1.grid(row=3,column=4)


test2= tkinter.Entry(bd=4) #bd== tamaño del borde, default 2. cursor== cambia el patrón del ratón (arrox,dot,etc)
test2.grid(row=4,column=4)


test3= tkinter.Entry(selectbackground="orange",selectforeground="yellow",selectborderwidth=2) #selectbackground== fondo del texto seleccionado | selectborderwidth== ancho del borde del texto seleccionado, default 1px. || selectforeground== color del texto seleccionado
#(2)
test3.grid(row=5,column=4)


test4= tkinter.Entry(font=font.Font(family="Times",size=14))
test4.grid(row=6,column=4)


#para saber las fuentes disponibles:

#import tkinter
#ia= tkinter.Tk()
abc=font.families()
print(abc)

#también puede ser... :
test4_1= tkinter.Entry(font=font.Font(family="Courier",size=14,weight=font.BOLD,slant=font.ITALIC,overstrike=True,underline=True)) #negrita,cusiva,tachado y subrayado
test4_1.grid(row=6,column=5)


test5=tkinter.Entry(show="*",exportselection=0,highlightcolor="pink",justify="center")
#justify= como se alinea el text | highlightcolor= se ilumina la caja cuando es clickeada | exportselection= por default, se copia al portapapeles. si pones 0 no lo hace | xscrollcommand= ponemos linker mi cuadro a un scrollbar (x si tienen q poer mucho texto) | show== para hacer q parexca contraseña se usa "*" , mostrará eso en la pantalla. | command= agregras un comando cada vez que cambia el estado de la caja . HIGHLIGHT COLOR NO sirve
test5.grid(row=7,column=4)


#test6= tkinter.Entry(insertcolor="green",insertwidth=3) # color del cursor y ancho del mismo (px)
#(3)

cuadro.mainloop()
