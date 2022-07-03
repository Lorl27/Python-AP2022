"""
1-Creá una lista que almacene informes de misiones de vuelo de 4 pilotos. Los elementos que debe tener cada informe son:
Nombre del / la piloto.
Apellido del / la piloto.
Edad del / la piloto.
Motivo de la misión.
Fecha de la misión.

2-Cuando la lista esté creada, mostrá por consola la información

3-Ahora, queremos conocer sólo el motivo de cada misión. Imprimí por consola el elemento correspondiente. Recordá que, para acceder a un elemento de una lista anidada, debés utilizar subíndices.

4-Necesitamos modificar el nombre del tercer piloto, ya que descubrimos que contiene un error de ortografía.

5-Por último, usá un bucle for para imprimir cada misión guardada en la lista.
"""

listaP=[["Amalia","Juanés",27,"Recreativa","27/07/2022"],["Fernando","Rominez",20,"Comercial","01/09/2020"],["Jimbu","Chalin",45,"Educativa","05/12/2001"],["Martha","Lomingui",33,"Comercial","16/03/2020"]] #1

print(listaP) #2

print(listaP[0][3]) #3.0 [PILOTO 1]
print(listaP[1][3]) #3.1 [PILOTO 2]
print(listaP[2][3]) #3.2 [PILOTO 3]
print(listaP[3][3]) #3.3 [PILOTO 4]

listaP[2][0]="Jimbú" #4.0
print(listaP) #4.1

for x in listaP:  #5
    print(x)