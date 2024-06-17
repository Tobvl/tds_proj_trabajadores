import os
print("menuprincipal.py cwd:",os.getcwd())
from .Mensajes import Mensaje as msj
from .Mensajes import Menu as menu
from .Mensajes import ADVERTENCIA, ERROR, EXITO, INFO
from modelo.entidades.Trabajador import Trabajador
from modelo.daos.TrabajadorDAO import TrabajadorDAO
from time import sleep as esperar

# Menú Principal Correo de Yury
def menuPrincipal():
    
    while True:
        # Menú para Iniciar sesión
        msj().bienvenida()

        # Opciones de Inicio de Sesión
        pregunta = msj().pregunta("Escoge una opción: ")
    
        if pregunta == "1":
            # Inicio de sesión
            menu.menuInicioSesion()
            
        elif pregunta == "2":
            # Salir
            msj("Hasta la próxima!")
            break
        else:
            msj().opcion_invalida()
            continue


if __name__ == "__main__":

    print(os.getcwd())
    menuPrincipal()