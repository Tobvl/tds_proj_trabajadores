# coding: utf8
# Main
# Llamar a la función principal de la aplicación (vista)

# Path: proyecto_correodeyury/tds_proj_trabajadores/vista/MenuPrincipal.py
# Importar la vista
import vista
from vista.MenuPrincipal import menuPrincipal

import sys
sys.path.append("..")
sys.path.append(".")

# Llamar a la función principal de la aplicación

try:
    menuPrincipal()
except KeyboardInterrupt:
    print("\nHasta la próxima!")
    exit(0)


