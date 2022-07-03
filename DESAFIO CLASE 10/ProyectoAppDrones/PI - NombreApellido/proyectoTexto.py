# coding: utf8
import recursos.moduloTello as moduloTello
import recursos.moduloInterfaz as moduloInterfaz
import os

miDron = moduloTello.Tello()
miInterfaz = moduloInterfaz.Interfaz()
miInterfaz.setear_dron_controlado(miDron)
miPath = os.path.dirname(os.path.abspath(__file__))
miInterfaz.setear_archivo_inicio(miPath+"/misionVuelo.txt")
miInterfaz.correr()
