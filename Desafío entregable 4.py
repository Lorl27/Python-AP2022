definicion = "vehículo no tripulado propulsado por un motor -ya sea de explosión,reacción o eléctrico- y están divididos según su uso (terrestres,aéreos y acuáticos) ";
tipo_de_control = "remota, autónoma o supervisada ";
oracion_A = "Un dron es un " +definicion+ ", que se controla de manera " +tipo_de_control+ ".";
denominación = "cuadricóptero";
cantidad_de_motores = 4;
oracion_B = "El dron Tello es un " +denominación+" porque tiene "+str(cantidad_de_motores)+ " motores.";
peso = 87;
velocidad = 28;
oracion_C = "El Dron Tello pesa " +str(peso)+" gramos y puede alcanzar una velocidad de "+str(velocidad)+ " km/h.";

print(oracion_A);
print(oracion_B);
print(oracion_C);