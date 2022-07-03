 # coding: utf8
import recursos.moduloTello as moduloTello
import recursos.moduloInterfaz as moduloInterfaz
#import pygame
import tkinter
#import threading
import datetime
import os
miRuta = os.path.dirname(os.path.abspath(__file__))

# --- SECCIÓN INICIALIZACION ---

# INICIALIZAR DRON
miDron = moduloTello.Tello()
# miDron = moduloTello.TelloSinEstados() # Si existen problemas al decodificar según versión SDK

# CREAR INTERFAZ
miInterfaz = moduloInterfaz.Interfaz()

# SETEAR DRON CONTROLADO A LA INTERFAZ
miInterfaz.setear_dron_controlado(miDron)

# CONSULTAR POR CONSOLA NOMBRE OPERADOR FCC

#CREAR ARCHIVO DE REGISTRO


# ACTIVAR TRANSMISIÓN DE VIDEO

# --- SECCIÓN TKINTER ---

# CREAR TKINTER (TÍTULO, LABELS)


# FUNCIONES BOTONES TKINTER


# CREAR y AGREGAR BOTONES A VENTANA


# AGREGAR TKINTER A LA INTERFAZ

# --- SECCIÓN PYGAME ---

# INICIALIZAR PYGAME


# AGREGAR PYGAME A INTERFAZ

# --- SECCIÓN CONTROLES REMOTOS ---

# VELOCIDAD DE MOVIMIENTO
velocidadMovimiento = 60

# CONTROLES KEYDOWN TECLADO (OPCIONAL)
"""
def controlesKeyDown(tecla):
	if tecla == pygame.K_w:
		miInterfaz.velocidad_abajo_arriba = velocidadMovimiento
	elif tecla == pygame.K_s:
		miInterfaz.velocidad_abajo_arriba = -velocidadMovimiento
	# AGREGÁ LOS CONTROLES DE TECLADO QUE DESEES:


miInterfaz.setear_controles_key_down(controlesKeyDown)

# CONTROLES KEYUP TECLADO (OPCIONAL)
def controlesKeyUp(tecla):
	if tecla == pygame.K_w or tecla == pygame.K_s:
		miInterfaz.velocidad_abajo_arriba = 0
	elif tecla == pygame.K_t:
		miDron.despegar()
		miInterfaz.habilitar_controles_remotos()
	elif tecla == pygame.K_l:
		miDron.aterrizar()
		miInterfaz.deshabilitar_controles_remotos()
	# AGREGÁ LOS CONTROLES DE TECLADO QUE DESEES:

miInterfaz.setear_controles_key_up(controlesKeyUp)

# CONTROLES GAMEPAD
# Copiá y pegá aquí lo trabajado en "test_gamepad_botones.py"





# CONTROLES GAMEPAD - EJES
# Copiá y pegá aquí lo trabajado en "test_gamepad_ejes.py"




"""
# --- SECCIÓN FINAL ---
 
# CORRER LA INTERFAZ
miInterfaz.correr()

# CERRAR ARCHIVO DE REGISTRO

