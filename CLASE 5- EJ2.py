"""
Una función calcular_perímetro_cuadrado()
Una función calcular_superficie_cuadrado()
Una función calcular_perimetro_circulo()
Una función calcular_superficie_circulo()
"""
import math

def calcular_perimetro_cuadrado(lado):
    resultado=str(lado*4)
    print("El perimetro del cuadrado mide: " + resultado + "cm")

def calcular_superficie_cuadrado(lado1,lado2):
    result=str(lado1*lado2)
    print("El area del cuadrado mide: " + result + "cm cubicos")

def calcular_perimetro_circulo(radio):
    calculo=str(2*math.pi*radio)
    redondearNum=round(float(calculo),2)
    print("El perimetro es de: " + calculo + "cm, redondeado sería: " + str(redondearNum) + "cm")

def calcular_superficie_circulo(radio):
    operacion=str(math.pi*(math.pow(radio,2)))
    print("El area es de: " + operacion + "cm cubicos, redondeado sería: " + str(round(float(operacion),2)) + "cm") #round (num,num1) num = numero a redondear ; num1= cantidad de caracteres luego de la ,

calcular_perimetro_cuadrado(25)
calcular_superficie_cuadrado(4,5)
calcular_perimetro_circulo(18)
calcular_superficie_circulo(696)
