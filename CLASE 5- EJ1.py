"""
Es hora de crear nuestro primer script estructurado en funciones. En particular, vamos a necesitar dos funciones: Una para dar la bienvenida al usuario, y una para despedirlo. Ambas deben poder personalizarse con el nombre que el usuario ingrese por teclado. Te dejamos algunas pautas:

La función saludar, debe mostrar el siguiente mensaje por consola: "¡Hola! Bienvenido/a a Aprende Programando: " . Utilizar la función print().
La función despedir debe mostrar el siguiente mensaje por consola: "Adiós, " .
Vas a necesitar un parámetro para poder personalizar las funciones.
Solicitá al usuario que ingrese su nombre (usando input()) afuera de la función
No olvides incluir la ejecución de ambas funciones al final del script
"""

nombreU=input("¿Cuál es tu nombre?: ")

def Saludar():
    print("¡Hola! Bienvenido/a a Aprende Programando: " + nombreU)

def Despedir():
    print("Adiós, " + nombreU)

Saludar()
Despedir()