# Chequear y conocer valores del Gamepad conectado mediante PYGAME
# De no funcionar:
#	a) Chequear configuración y/o calibración desde Panel de Control del SO
#	b) Testear online buscando "Online Gamepad Test"

# IMPORTACIONES RELATIVAS
import os, sys, inspect

directorio_actual = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
directorio_padre = os.path.dirname(directorio_actual)
sys.path.insert(0,directorio_padre)

import pygame
import moduloInterfaz as moduloInterfaz

# CREAR INTERFAZ
miInterfaz = moduloInterfaz.Interfaz()

# INICIALIZAR PYGAME
pygame.init()
pygame.display.set_caption("Testeo Botones Gamepad")
miVentanaPygame = pygame.display.set_mode([350, 100])

# AGREGAR PYGAME A INTERFAZ
miInterfaz.setear_ventana_pygame(miVentanaPygame)

# CONTROLES GAMEPAD

# Detectar cantidadJoysticks:
cantidadJoysticks = pygame.joystick.get_count()
# Inicializar usando un condicional:
if cantidadJoysticks > 0:
	miGamepad = pygame.joystick.Joystick(0)
	miGamepad.init()

# CONTROLES GAMEPAD - EJES:
# Crear función controladora:

# Agregar función controladora a la interfaz:

# CORRER INTERFAZ (NO BORRAR NI COPIAR)
miInterfaz.correr()

