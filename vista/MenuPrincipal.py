import os
# print("menuprincipal.py cwd:",os.getcwd())
from time import sleep as esperar
from colorama import Fore, Style

AMARILLO = f"{Fore.YELLOW}"
VERDE = f"{Fore.GREEN}"
separador = f"{AMARILLO} >>{Style.RESET_ALL} "
ADVERTENCIA = f"{AMARILLO}ADVERTENCIA{separador}"
VERDE_CLARO = f"{Fore.LIGHTGREEN_EX}"
TITULO = f"{Fore.CYAN}CORREO YURY{Style.RESET_ALL}"
VERSION = f"{Fore.CYAN}v1.0.1{Style.RESET_ALL}"

ERROR = f"{Fore.RED}ERROR{separador}{Fore.LIGHTRED_EX}"

def bienvenida():
    print(f"""

        {VERDE_CLARO}Bienvenid@ a {TITULO} {VERSION} {VERDE_CLARO}


        {VERDE_CLARO}1. {AMARILLO}Iniciar Sesión
        {VERDE_CLARO}2. {AMARILLO}Salir""")
    
def pregunta(pregunta):
    print(f"\n{VERDE}[?] {pregunta}")
    p=input(f"{separador}").strip()
    return p 

def opcion_invalida():
    print(ADVERTENCIA + "Opción no válida, intente de nuevo...\n")
    esperar(.5)

# Menú Principal Correo de Yury
def menuPrincipal():
    while True:
        # Menú para Iniciar sesión
        bienvenida()

        # Opciones de Inicio de Sesión
        preg = pregunta("Escoge una opción: ")
    
        if preg == "1":
            # Inicio de sesión
            valor = False 
            try:
                from .Mensajes import Menu as menu
                from controlador.ManejadorBD import Conexion as bd
                if bd.testConnection():
                    valor = True
            except Exception as e:
                print(f"{ERROR}Ha ocurrido un error inesperado! ({e}){Style.RESET_ALL}")
                valor = False
                
            if valor: 
                try:
                    print("valor:",valor)
                    menu.menuInicioSesion()
                except Exception as e:
                    valor = False
                    print(f"{ERROR}Ha ocurrido un error inesperado! ({e}){Style.RESET_ALL}")
                    continue
            valor = False
            
        elif preg == "2":
            # Salir
            print("Hasta la próxima!")
            break
        else:
            opcion_invalida()
            continue
