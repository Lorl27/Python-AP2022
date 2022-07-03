# coding: utf8
import recursos.moduloTello as moduloTello

# INICIALIZAR DRON
miDron = moduloTello.Tello()
miDron.despegar()
miDron.mover_arriba(20)
miDron.aterrizar()
# CONSULTAS POR CONSOLA A OPERADOR DE LA FCC




