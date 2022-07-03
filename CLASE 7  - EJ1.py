#Escribí un programa que le pida al usuario que ingrese su edad y le informe si puede volar un dron, y si necesita o no supervisión de un adulto. Recordá que, en Argentina, están autorizados a volar sin supervisión, todos los mayores de 18 años, o los mayores de 16 años con supervisión. Te dejamos un editor para que lo pruebes.

edad=int(input("Ingresa tu edad: "))

if(edad>=18):
    print("Usted puede volar un dron")
elif(edad>=16 and edad<18):
    print("Usted puede volar un dron con supervisión")
else:
    print("Usted no puede volar un dron.")