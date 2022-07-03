#3 pilotos->informar cuantos minutos de vuelo tienen permitidos segun su bateria.Usar if/elif/else para decidir el valor de la variable "minutosMax" e imprimir un mensaje basándome en esa var.

piloto1="Juan"
piloto1B=100

piloto2="María"
piloto2B=75

piloto3="Robertino"
piloto3B=20



if(piloto1B==50 or piloto2B==50 or piloto3B==50):
    minutosMax=5;
    print(piloto1 + " /" + piloto2 + " /" + piloto3 + " tienen " + str(minutosMax) + " minutos de batería restante ")
elif(piloto1B==20):
    minutosMax=2;
    print(piloto1 + " /" + piloto2 + " /" + piloto3 + " tienen " + str(minutosMax) + " minutos de batería restante ")
else:
    minutosMax=100;
    print(piloto1 + " /" + piloto2 + " /" + piloto3 + " tienen " + str(minutosMax) + " minutos de batería restante ")