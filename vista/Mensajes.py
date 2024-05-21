from colorama import Fore, Style
from rich.progress import track
from time import sleep as esperar
from modelo.daos.TrabajadorDAO import TrabajadorDAO
from modelo.daos.AccesoDAO import AccesoDAO
from modelo.entidades.Trabajador import Trabajador
import random, pwinput

#Prefijos de Tipos de mensajes
VERDE = f"{Fore.GREEN}"
AMARILLO = f"{Fore.YELLOW}"
ROJO = f"{Fore.RED}"
CIAN = f"{Fore.CYAN}"
separador = f"{AMARILLO} >>{Style.RESET_ALL} "
VERDE_CLARO = f"{Fore.LIGHTGREEN_EX}"
TITULO = f"{Fore.CYAN}CORREO YURY{Style.RESET_ALL}"
VERSION = f"{Fore.CYAN}v1.0.0{Style.RESET_ALL}"
EXITO = f"{VERDE}EXITO{separador}"    
INFO = f"{Fore.WHITE}INFORMACIÓN{separador}"
ADVERTENCIA = f"{AMARILLO}ADVERTENCIA{separador}"
ERROR = f"{Fore.RED}ERROR{separador}"
tipos = [EXITO, INFO, ADVERTENCIA, ERROR]

class Mensaje():    
    def __init__(self, tipo=None, mensaje=None):
        
        self.mensaje = mensaje
        self.tipo = tipo
        if self.tipo in tipos:
            print(f"\n{tipo}{mensaje}{Style.RESET_ALL}")
            return
        elif tipo is None and mensaje is None:
            return
        elif mensaje is None:
            print(f"\n{VERDE}{tipo}{Style.RESET_ALL}")
            return
            
    def bienvenida(self):
        Mensaje(f"""

    {VERDE_CLARO}Bienvenid@ a {TITULO} {VERSION} {VERDE_CLARO}


    {VERDE_CLARO}1. {AMARILLO}Iniciar Sesión
    {VERDE_CLARO}2. {AMARILLO}Registrarse
    {VERDE_CLARO}3. {AMARILLO}Salir""")
        
        

    def pregunta(self, pregunta):
        print(f"\n{VERDE}[?] {pregunta}")
        return input(f"{separador}")
    
    def pregunta_clave(self):
        print(f"\n{AMARILLO}[?] Ingresa tu contraseña: {Style.RESET_ALL}")
        return pwinput.pwinput(f"{separador}", mask="*")
    
    def opcion_invalida(self):
        Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...\n")
        esperar(.5)
    
    def __str__(self):
        return f"\n{self.tipo}{self.mensaje}"

def esperar5s(mensaje):
            print(\
        f"""
        {VERDE}{mensaje}:
        """)
            for _ in track(range(random.randrange(250, 1500, 1)), description=f"        {VERDE_CLARO}Cargando Interfaz..."):
                esperar(0.001)
                
def registrando(mensaje):
            print(\
        f"""
        {AMARILLO}{mensaje}
        """)
            for _ in track(range(random.randrange(400, 1800, 1)), description=f"        {VERDE_CLARO}Registrando nuevo usuario..."):
                esperar(0.001)


def preguntar_tipo_usuario():
    while True:
            tipo_usuario = Mensaje().pregunta("""
Tipo de Usuario:         [0 para salir]
1. Trabajador
2. Recursos Humanos
3. Jefe [Administrador]
""")
            if tipo_usuario != "1" and tipo_usuario != "2" and tipo_usuario != "3" and tipo_usuario != "0":
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
            return tipo_usuario


class MenuInterno:
    
    @classmethod
    def mostrarMenu(self, usuario):
        if usuario.tipo_usuario == "Trabajador":
            Mensaje(AMARILLO, f"¡Bienvenido {usuario.nombre_usuario}!")
            self.menuTrabajador(usuario)
        elif usuario.tipo_usuario == "RRHH":
            self.menuRRHH(usuario)
        elif usuario.tipo_usuario == "Jefe":
            self.menuJefe(usuario)

    @classmethod
    def menuTrabajador(self, usuario):
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Trabajador")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}Hola {usuario.nombre} {usuario.apellido}!


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mis Datos Personales
    {VERDE_CLARO}3. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos personales
                pass
            elif pregunta == "3":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
                
    
    @classmethod
    def menuRRHH(self, usuario):
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Recursos Humanos")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}Hola {usuario.nombre} {usuario.apellido}!


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mis Datos Personales
    {VERDE_CLARO}3. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos personales
                pass
            elif pregunta == "3":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
                
    @classmethod
    def menuJefe(self, usuario):
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Administrativo")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}Hola {usuario.nombre} {usuario.apellido}!


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mis Datos Personales
    {VERDE_CLARO}3. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos personales
                pass
            elif pregunta == "3":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
                
    

class Menu:
    def menuInicioSesion() -> bool:
        esperar5s("Menú Inicio de Sesión")
        Mensaje("\nINICIANDO SESIÓN...\n")
        nombre_usuario = Mensaje().pregunta("Nombre de usuario: ")
        clave = Mensaje().pregunta_clave()
        # Verificar que tipo de usuario es
        validacion = TrabajadorDAO.validar_usuario(nombre_usuario, clave)
        print("Validación: ", validacion)
        if not validacion:
            AccesoDAO.add(nombre_usuario, clave)
            Mensaje(ERROR, "Error al Iniciar Sesión, nombre de usuario o contraseña incorrectos.")
            esperar(1)
            return False
        else:
            # Mostrar menú dependiendo del tipo de usuario
            # Registrar acceso
            usuario = validacion[1]
            print("Objeto usuario: ", usuario)
            AccesoDAO.add(usuario.nombre_usuario, "#AccesoCorrecto")
            Mensaje(EXITO, "Inicio de sesión exitoso!")
            MenuInterno.mostrarMenu(usuario)
            return False

    
    def menuRegistro():
        esperar5s("Menú Registro de Usuario")
        Mensaje("\nREGISTRANDO NUEVO USUARIO...\n")
        nombre_usuario = Mensaje().pregunta("Nombre de usuario:       [0 para salir]")
        if nombre_usuario == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        while TrabajadorDAO.existe_usuario(nombre_usuario):
            Mensaje(ERROR, "El nombre de usuario ya existe, intente con otro...")
            nombre_usuario = Mensaje().pregunta("Nombre de usuario:       [0 para salir]")
        clave = Mensaje().pregunta_clave()
        while clave == "":
            Mensaje(ERROR, "La contraseña no puede estar vacía!.\n")
            esperar(1)
            clave = Mensaje().pregunta_clave()
            continue
        run = Mensaje().pregunta("RUN:        [0 para salir]")
        if run == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        rundf = Mensaje().pregunta("RUN (Dígito verificador):         [0 para salir]")
        if rundf == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        nombre = Mensaje().pregunta("Nombre:          [0 para salir]")
        if nombre == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        apellido = Mensaje().pregunta("Apellido:          [0 para salir]")
        if apellido == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        correo = Mensaje().pregunta("Correo:          [0 para salir]")
        if correo == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        genero = Mensaje().pregunta("Género:          [0 para salir]")
        if genero == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        telefono = Mensaje().pregunta("Teléfono:          [0 para salir]")
        if telefono == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        direccion = Mensaje().pregunta("Dirección:        [0 para salir]")
        if direccion == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        tipo_usuario = preguntar_tipo_usuario()
        if tipo_usuario == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        while True:
            if tipo_usuario in ["Trabajador", "Recursos Humanos", "Jefe"]:
                pass
            else:
                tipo_usuario = 'Trabajador' if tipo_usuario == '1' else ('Recursos Humanos' if tipo_usuario == '2' else ('Jefe' if tipo_usuario == '3' else 'Trabajador'))
            confirmar = Mensaje().pregunta(f"""
¿Confirmar registro de usuario?:         [0 para salir]
{tipo_usuario} | Nombre: {nombre} {apellido} [{run}-{rundf}]
1. SI
2. NO
3. Cambiar tipo de usuario
""")
            if confirmar == "0":
                Mensaje(INFO, "Saliendo del registro de usuario...")
                esperar(0.5)
                return
            if confirmar == "1":
                nuevo_trabajador = Trabajador(nombre_usuario=nombre_usuario,
                                                clave=clave,
                                                run=run,
                                                rundf=rundf,
                                                nombre=nombre,
                                                apellido=apellido,
                                                correo=correo,
                                                genero=genero,
                                                telefono=telefono,
                                                direccion=direccion,
                                                tipo_usuario=tipo_usuario)
                try:
                    registrando(f"Registrando {tipo_usuario}...")
                    TrabajadorDAO.add(nuevo_trabajador)
                    Mensaje(EXITO, f"{tipo_usuario} registrado con éxito!")
                    esperar(1)
                    # Volver al login
                    return
                except Exception as e:
                    Mensaje(ERROR, f"Error al registrar {tipo_usuario}: {e}")
                    esperar(1)
                    return
            elif confirmar == "2":
                Mensaje(ADVERTENCIA, "Cancelando registro...")
                esperar(0.5)
                break
            elif confirmar == "3":
                tipo_usuario = preguntar_tipo_usuario()
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue



















if __name__ == "__main__":
    # Mensajes de prueba
    # msj = Mensaje().bienvenida()
    # msj = Mensaje(INFO, "Iniciando Sesión...")
    # msj = Mensaje(ERROR, "Error al Iniciar Sesión")
    # msj = Mensaje(ADVERTENCIA, "Usuario no encontrado")
    Mensaje().menuInicioSesion()
    Mensaje("""
    MENSAJE DE PRUEBA
    MULTILINEA
    JASJKDAJKD""")