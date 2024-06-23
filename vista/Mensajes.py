# coding: utf8
import datetime
import random, pwinput
from colorama import Fore, Style
from rich.progress import track
from time import sleep as esperar
from itertools import cycle
from modelo.daos.TrabajadorDAO import TrabajadorDAO
from modelo.daos.AccesoDAO import AccesoDAO
from modelo.entidades.Trabajador import Trabajador
from vista.Fechas import Fechas

#Prefijos de Tipos de mensajes
VERDE = f"{Fore.GREEN}"
AMARILLO = f"{Fore.YELLOW}"
ROJO = f"{Fore.RED}"
ROJO_CLARO = f"{Fore.LIGHTRED_EX}"
CIAN = f"{Fore.CYAN}"
separador = f"{AMARILLO} >>{Style.RESET_ALL} "
VERDE_CLARO = f"{Fore.LIGHTGREEN_EX}"
TITULO = f"{Fore.CYAN}CORREO YURY{Style.RESET_ALL}"
VERSION = f"{Fore.CYAN}v1.0.0{Style.RESET_ALL}"
EXITO = f"{VERDE}EXITO{separador}{Fore.LIGHTGREEN_EX}"    
INFO = f"{Fore.WHITE}INFORMACIÓN{separador}"
ADVERTENCIA = f"{AMARILLO}ADVERTENCIA{separador}"
ERROR = f"{Fore.RED}ERROR{separador}{Fore.LIGHTRED_EX}"
tipos = [EXITO, INFO, ADVERTENCIA, ERROR]

class Mensaje():
    """
    Clase que define los mensajes de la aplicación.
    """
     
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
    {VERDE_CLARO}2. {AMARILLO}Salir""")
        
        

    def pregunta(self, pregunta):
        print(f"\n{VERDE}[?] {pregunta}")
        p=input(f"{separador}").strip()
        return p 
    
    def pregunta_clave(self):
        print(f"\n{AMARILLO}[?] Ingresa tu contraseña: {Style.RESET_ALL}    [ENTER para salir]")
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

def modificando5s(mensaje, campo):
            print(\
        f"""
        {VERDE}{mensaje}:
        """)
            for _ in track(range(random.randrange(250, 1500, 1)), description=f"        {VERDE_CLARO}{campo}...\n"):
                esperar(0.0011)

def registrando(mensaje):
            print(\
        f"""
        {AMARILLO}{mensaje}
        """)
            for _ in track(range(random.randrange(400, 1800, 1)), description=f"        {VERDE_CLARO}Registrando nuevo usuario..."):
                esperar(0.001)


def preguntar_tipo_usuario():
    while True:
            tipo_usuario = Mensaje().pregunta(f"""
    Tipo de Usuario:         [0 para salir]
    {VERDE_CLARO}1. {AMARILLO}Trabajador
    {VERDE_CLARO}2. {AMARILLO}Recursos Humanos
    {VERDE_CLARO}3. {AMARILLO}Jefe {ROJO_CLARO}[Administrador]
    """)
            if tipo_usuario != "1" and tipo_usuario != "2" and tipo_usuario != "3" and tipo_usuario != "0":
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
            return tipo_usuario

def digito_verificador(rut):
    # La función recibe el RUT como un entero,
    # y entrega el dígito verificador como un entero.
    # Si el resultado es 10, el RUT es guión K.

    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def validar_rut(rut, dv):
    # La función recibe el RUT y el dígito verificador,
    # y entrega True si el RUT es válido, y False si no lo es.
    if dv == 'k':
        dv = 10
    return digito_verificador(rut) == dv

class MenuInterno:
    
    @classmethod
    def mostrarMenu(self, usuario):
        try:
            Mensaje(f"¡Iniciando sesión de: {usuario.nombre_usuario}!")
            if usuario.tipo_usuario == "Trabajador":
                self.menuTrabajador(usuario)
            elif usuario.tipo_usuario == "Recursos Humanos":
                self.menuRRHH(usuario)
            elif usuario.tipo_usuario == "Jefe":
                self.menuJefe(usuario)
        except Exception as e:
            Mensaje(ERROR, f"Ocurrió un error! Por favor, contacte al administrador. ({e})")
            esperar(0.5)
            return
            
    @classmethod
    def modificarCampo(self, campo, usuario: Trabajador, campo_de_usuario):
        while True:
            nuevo_campo = Mensaje().pregunta(f"Nuevo {campo}:         [0 para salir]")
            if nuevo_campo == "0":
                Mensaje(INFO, "Volviendo al menú principal...")
                esperar(0.5)
                return
            while True:
                confirmar = Mensaje().pregunta(f""" ¿Confirmar cambio de {campo}?:
    {ROJO_CLARO}{campo_de_usuario} ---> {VERDE_CLARO}{nuevo_campo}
    {VERDE_CLARO}1. {AMARILLO}SI
    {VERDE_CLARO}2. {AMARILLO}NO
    {VERDE_CLARO}3. {AMARILLO}{f"Otro {campo}" if campo != "direccion" else f"Otra {campo}"}
    """)            
                if confirmar == "3":
                    break
                elif confirmar == "2":
                    Mensaje(INFO, "Volviendo al menú principal..")
                    esperar(0.5)
                    return
                elif confirmar == "1":
                    if campo == "correo":
                        TrabajadorDAO.modificar_correo(usuario, nuevo_campo)
                        usuario.correo = nuevo_campo

                    elif campo == "telefono":
                        TrabajadorDAO.modificar_telefono(usuario, nuevo_campo)
                        usuario.telefono = nuevo_campo

                    elif campo == "direccion":
                        TrabajadorDAO.modificar_direccion(usuario, nuevo_campo)
                        usuario.direccion = nuevo_campo
                    modificando5s(f"Modificar {campo}", f"Actualizando a {nuevo_campo}")
                    Mensaje(EXITO, f"{campo.title()} modificado con éxito!")
                    return
                else:
                    Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                    esperar(0.5)
                    continue
    @classmethod
    def modificarCampoExt(self, campo, trabajador: Trabajador, campo_de_usuario):
        while True:
            nuevo_campo = Mensaje().pregunta(f"Nuevo {campo}:         [0 para salir]")
            if nuevo_campo == "0":
                Mensaje(INFO, "Volviendo al menú principal...")
                esperar(0.5)
                return
            while True:
                confirmar = Mensaje().pregunta(f""" ¿Confirmar cambio de {campo}?:
    {ROJO_CLARO}{campo_de_usuario} ---> {VERDE_CLARO}{nuevo_campo}
    {VERDE_CLARO}1. {AMARILLO}SI
    {VERDE_CLARO}2. {AMARILLO}NO
    {VERDE_CLARO}3. {AMARILLO}{f"Otro {campo}" if campo != "direccion" else f"Otra {campo}"}
    """)            
                if confirmar == "3":
                    break
                elif confirmar == "2":
                    Mensaje(INFO, "Volviendo atrás...")
                    esperar(0.5)
                    return
                elif confirmar == "1":
                    if campo == "correo":
                        TrabajadorDAO.modificar_correo(trabajador, nuevo_campo)
                    elif campo == "telefono":
                        TrabajadorDAO.modificar_telefono(trabajador, nuevo_campo)
                    elif campo == "genero":
                        TrabajadorDAO.modificar_genero(trabajador, nuevo_campo)
                    elif campo == "direccion":
                        TrabajadorDAO.modificar_direccion(trabajador, nuevo_campo)
                    modificando5s(f"Modificar {campo} de trabajador", f"Actualizando a {nuevo_campo}")
                    Mensaje(EXITO, f"{campo.title()} modificado con éxito!")
                    return
                else:
                    Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                    esperar(0.5)
                    continue
    @classmethod
    def modificarDatosPersonales(self, usuario: Trabajador):
        
        while True:
            Mensaje(f"""
    {VERDE_CLARO}Modificando mis datos personales:
    {VERDE_CLARO}Usuario: {ROJO_CLARO}{usuario.nombre_usuario}
    {VERDE_CLARO}Nombre: {VERDE}{usuario.nombre} {usuario.apellido}
    {VERDE_CLARO}RUN: {ROJO_CLARO}{usuario.run}-{usuario.rundf}
    {VERDE_CLARO}Correo: {VERDE}{usuario.correo}
    {VERDE_CLARO}Género: {ROJO_CLARO}{usuario.genero}
    {VERDE_CLARO}Teléfono: {VERDE}{usuario.telefono}
    {VERDE_CLARO}Dirección: {VERDE}{usuario.direccion}
    {VERDE_CLARO}Fecha de Registro: {ROJO_CLARO}{usuario.fecha_ingreso}
    {VERDE_CLARO}Tipo de Usuario: {ROJO_CLARO}{usuario.tipo_usuario}
    {AMARILLO}Puede modificar su ficha: {f"{ROJO_CLARO} NO" if usuario.modificacion_bloqueada else f"{VERDE}SI"}


    {VERDE_CLARO}1. {AMARILLO}Modificar mi {VERDE}Nombre
    {VERDE_CLARO}2. {AMARILLO}Modificar mi {VERDE}Correo
    {VERDE_CLARO}3. {AMARILLO}Modificar mi {VERDE}Teléfono
    {VERDE_CLARO}4. {AMARILLO}Modificar mi {VERDE}Dirección
    {VERDE_CLARO}0. {AMARILLO}Volver al Menú Principal""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "0":
                Mensaje(INFO, "Volviendo al menú principal...")
                return
            elif pregunta != "1" and pregunta != "2" and pregunta != "3" and pregunta != "4":
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
            else:
                if not usuario.modificacion_bloqueada:
                    if pregunta == "1":
                        # Modificar nombre
                        while True:
                            nuevo_nombre = Mensaje().pregunta("Nuevo nombre:         [0 para salir]")
                            if nuevo_nombre == "0":
                                Mensaje(INFO, "Volviendo al menú principal...")
                                esperar(0.5)
                                break
                            nuevo_apellido = Mensaje().pregunta("Nuevo apellido:         [0 para salir]")
                            if nuevo_apellido == "0":
                                Mensaje(INFO, "Volviendo al menú principal...")
                                esperar(0.5)
                                break
                            while True:
                                confirmar = Mensaje().pregunta(f""" ¿Confirmar cambio de nombre?:
    {ROJO_CLARO}{usuario.nombre} {usuario.apellido} ---> {VERDE_CLARO}{nuevo_nombre} {nuevo_apellido}
    {VERDE_CLARO}1. {AMARILLO}SI
    {VERDE_CLARO}2. {AMARILLO}NO
    {VERDE_CLARO}3. {AMARILLO}Otro nombre
    """)            
                                if confirmar == "3":
                                    break
                                elif confirmar == "2":
                                    Mensaje(INFO, "Volviendo al menú principal...")
                                    esperar(1)
                                    return
                                elif confirmar == "1":
                                    TrabajadorDAO.modificar_nombre(usuario, nuevo_nombre, nuevo_apellido)
                                    usuario.nombre = nuevo_nombre
                                    usuario.apellido = nuevo_apellido
                                    Mensaje(EXITO, "Nombre y apellido modificados con éxito!")
                                    return
                                else:
                                    Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                                    esperar(0.5)
                                    continue
                    elif pregunta == "2":
                        # Modificar correo
                        self.modificarCampo("correo", usuario, usuario.correo)
                    elif pregunta == "3":
                        # Modificar teléfono
                        self.modificarCampo("telefono", usuario, usuario.telefono)
                    elif pregunta == "4":
                        # Modificar dirección
                        self.modificarCampo("direccion", usuario, usuario.direccion)
                else:
                    Mensaje(ADVERTENCIA, "No puedes modificar tu ficha, contacta a tu jefe para más información.")
                    esperar(0.5)
                    return

    
    @classmethod
    def modificarDatosUsuario(self, usuario: Trabajador):
        while True:
            Mensaje(f"""

    {VERDE}Modificando mi usuario: {CIAN}{usuario.nombre} {usuario.apellido} [{VERDE_CLARO}{usuario.nombre_usuario}{CIAN}]

    {VERDE_CLARO}1. {AMARILLO}Modificar mi Contraseña
    {VERDE_CLARO}2. {AMARILLO}Modificar mis Datos Personales
    {VERDE_CLARO}3. {AMARILLO}Modificar mis Datos Laborales
    {VERDE_CLARO}0. {AMARILLO}Volver al Menú Principal""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                # Modificar contraseña
                esperar(2)
            elif pregunta == "2":
                # Modificar datos personales
                self.modificarDatosPersonales(usuario)
            elif pregunta == "3":
                # Modificar datos laborales
                pass
            elif pregunta == "0":
                Mensaje(INFO, "Volviendo al menú principal...")
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
         
    @classmethod 
    def menuDarBajaTrabajador(self, administrativo):
        while True:
            # Dar de baja trabajador
            Mensaje(f"{AMARILLO}Lista de Trabajadores:")
            trabajadores = TrabajadorDAO.list()
            for trabajador in trabajadores:
                Mensaje(f"{VERDE_CLARO}ID: {CIAN}{trabajador.nombre_usuario:12s}{VERDE_CLARO} | {trabajador.nombre} {trabajador.apellido}")
            id_trabajador = Mensaje().pregunta(f"{VERDE}Ingrese {CIAN}ID {VERDE}de trabajador a dar de baja       [0 para salir]: ")
            if id_trabajador == "0":
                Mensaje(INFO, "Volviendo al menú de gestión de trabajadores...")
                esperar(0.5)
                return
            if not TrabajadorDAO.existe_usuario(id_trabajador):
                Mensaje(ADVERTENCIA, "No existe un trabajador con ese ID, inténtelo nuevamente!...")
                esperar(0.5)
                break
            try:
                # Mostrar ficha y confirmar baja
                trabajador = TrabajadorDAO.get(id_trabajador)
                print(trabajador)
                confirmar = Mensaje().pregunta(f"""
    ¿Confirmas Dar de baja a          [0 para salir]
    {trabajador.nombre} {trabajador.apellido} [{trabajador.nombre_usuario}]?:

    {VERDE_CLARO}1. {ROJO}SI, DAR DE BAJA DEL SISTEMA
    {VERDE_CLARO}2. {AMARILLO}NO
    """)
                if confirmar == "1":
                    Mensaje(INFO, "Dando de baja...")
                    esperar(0.5)
                    try:
                        modificando5s(f"Dar de baja", f"Dando de baja a {trabajador.nombre_usuario}")
                        TrabajadorDAO.dar_baja(trabajador, administrativo)
                        Mensaje(EXITO, f"{trabajador.nombre} {trabajador.apellido} ha sido dado de baja del sistema exitosamente!")
                        esperar(1)
                        
                        return
                    except Exception as e:
                        Mensaje(ERROR, f"Error al dar de baja al trabajador {trabajador.nombre_usuario}")
                        esperar(1)
                        return
                elif confirmar == "2":
                    Mensaje(ADVERTENCIA, "Cancelando dar de baja a usuario...")
                    esperar(0.5)
                    break
            except:
                Mensaje(ERROR, "Error al dar de baja al trabajador, intente de nuevo...")
                esperar(0.5)
                return


    @classmethod
    def gestionarTrabajadores(self, usuario: Trabajador):
        while True:
            if usuario.tipo_usuario != "Jefe":
                msj_dardebaja=f"{VERDE_CLARO}5. {AMARILLO}Dar de baja a un trabajador {ROJO_CLARO}(Administrativo)"
            else:
                msj_dardebaja=f"{VERDE_CLARO}5. {AMARILLO}Dar de baja a un trabajador"

            msj=f"""
    {VERDE}Gestionando trabajadores de {TITULO}

    {VERDE_CLARO}1. {AMARILLO}Lista de Trabajadores
    {VERDE_CLARO}2. {AMARILLO}Ingresar Nuevo Trabajador
    {VERDE_CLARO}3. {AMARILLO}Modificar Ficha de Trabajador
    {VERDE_CLARO}4. {AMARILLO}Lista de Trabajadores dados de baja
    {msj_dardebaja}
    {VERDE_CLARO}0. {AMARILLO}Volver al Menú Principal"""
            
            while True:
                Mensaje()
                pregunta = Mensaje(msj).pregunta("Escoge una opción: ")
                if pregunta == "1":

                    orden = {}
                    filtros = {}
                    
                    self.menuListaTrabajadores(orden, filtros)
                elif pregunta == "2":
                    # Ingresar nuevo trabajador
                    Menu.menuRegistro()
                elif pregunta == "3":
                    # Modificar ficha de trabajador
                    Mensaje(f"{AMARILLO}Lista de Trabajadores:")
                    trabajadores = TrabajadorDAO.list()
                    for trabajador in trabajadores:
                        Mensaje(f"{VERDE_CLARO}ID: {CIAN}{trabajador.nombre_usuario:12s}{VERDE_CLARO} | {trabajador.nombre} {trabajador.apellido}")
                    id_trabajador = Mensaje().pregunta(f"{VERDE}Ingrese {CIAN}ID {VERDE}de trabajador a modificar       [0 para salir]: ")
                    if id_trabajador == "0":
                        Mensaje(INFO, "Volviendo al menú de gestión de trabajadores...")
                        esperar(0.5)
                        return
                    if not TrabajadorDAO.existe_usuario(id_trabajador):
                        Mensaje(ADVERTENCIA, "No existe un trabajador con ese ID, inténtelo nuevamente!...")
                        esperar(0.5)
                        break
                    try:
                        self.menuModificarTrabajador(id_trabajador)
                    except:
                        Mensaje(ERROR, "Error al modificar trabajador, intente de nuevo...")
                        esperar(0.5)
                        return
                elif pregunta == "4":
                    # Lista de trabajadores dados de baja
                    self.listarTrabajadoresBaja()
                elif pregunta == "5":
                    # Dar de baja a un trabajador
                    if usuario.tipo_usuario != "Jefe":
                        Mensaje(ADVERTENCIA, "No tienes permisos para realizar esta acción.")
                        esperar(0.5)
                        continue
                    self.menuDarBajaTrabajador(usuario)
                    
                elif pregunta == "0":
                    Mensaje(INFO, "Volviendo al menú principal...")
                    return
                else:
                    Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                    esperar(0.5)
                    continue
    
    @classmethod
    def menuListaTrabajadores(self, orden, filtros):
        
        
        while True:
            if orden.keys():
                valores_ordenados = ', '.join([f"{VERDE}{k}{AMARILLO}:{VERDE_CLARO}{v}" for k, v in orden.items()])
            if filtros.keys():
                valores_filtrados = ', '.join([f"{VERDE}{k}{AMARILLO}:{VERDE_CLARO}{'|'.join([f'{filtro}' for filtro in v])}" for k, v in filtros.items()])

            print(orden)
            print(filtros)
            
            #limpiar diccionario si tiene llaves vacías
            for llave in list(orden.keys()):
                if orden[llave] == "" or orden[llave] == []:
                    del orden[llave]
            for llave in list(filtros.keys()):
                if filtros[llave] == "" or filtros[llave] == []:
                    del filtros[llave]

            if not orden:
                valores_ordenados = 'Sin ordenar'
            if not filtros:
                valores_filtrados = 'Sin filtrar'
            ordenmsj = \
        f"""{CIAN}Orden: {AMARILLO}{valores_ordenados}"""
            filtromsj = \
        f"""{CIAN}Filtros: {AMARILLO}{valores_filtrados}"""
    
            Mensaje(f"""
    {VERDE}Menú Lista de trabajadores
    {ordenmsj}
    {filtromsj}
    {VERDE_CLARO}1. {AMARILLO}Mostrar todos los trabajadores
    {VERDE_CLARO}2. {AMARILLO}Ordenar lista
    {VERDE_CLARO}3. {AMARILLO}Filtrar los trabajadores
    {VERDE_CLARO}4. {AMARILLO}Quitar filtros y orden
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")

            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":

                trabajadores = TrabajadorDAO.list()

                if not filtros and not orden:
                    for trabajador in trabajadores:
                        print(trabajador)
                        
                elif filtros and not orden:
                    #! aplicar filtros sin orden y mostrar
                    self.imprimirTrabajadoresOF(trabajadores, filtros=filtros)

                elif orden and not filtros:
                    #! aplicar orden sin filtros y mostrar
                    self.imprimirTrabajadoresOF(trabajadores, orden=orden)
                    
                elif orden and filtros:
                    #! aplicar orden, filtros y mostrar
                    print("Aplicando orden y filtros...")
                    self.imprimirTrabajadoresOF(trabajadores, orden=orden, filtros=filtros)
                
            elif pregunta == "2":
                # preguntar si quiere ordenar la lista de los trabajadores.
                # ordenar por nombre, fecha_ingreso, etc...

                while True:
                    ordenar_por = Mensaje().pregunta(f"""
    {VERDE_CLARO}Ordenar por:
    {VERDE_CLARO}1. {AMARILLO}Nombre
    {VERDE_CLARO}2. {AMARILLO}Fecha de ingreso
    {VERDE_CLARO}3. {AMARILLO}Genero
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                    if ordenar_por == "1": #ordenar por nombre
                        tipo_orden = Mensaje().pregunta(f"""
    {VERDE_CLARO}Ordenar por nombre:
    {VERDE_CLARO}1. {AMARILLO}Nombre Ascendente
    {VERDE_CLARO}2. {AMARILLO}Nombre Descendente
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_orden == "1":
                            orden["nombre"] = "ASC"
                        elif tipo_orden == "2":
                            orden["nombre"] = "DESC"
                        elif tipo_orden == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif ordenar_por == "2": #ordenar por fecha de ingreso
                        tipo_orden = Mensaje().pregunta(f"""
    {VERDE_CLARO}Ordenar por fecha de ingreso:
    {VERDE_CLARO}1. {AMARILLO}Fecha más reciente primero
    {VERDE_CLARO}2. {AMARILLO}Fecha más antigua primero
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_orden == "1":
                            orden["fecha_ingreso"] = "RECIENTE"
                        elif tipo_orden == "2":
                            orden["fecha_ingreso"] = "ANTIGUA"
                        elif tipo_orden == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif ordenar_por == "3": #ordenar por genero
                        tipo_orden = Mensaje().pregunta(f"""
    {VERDE_CLARO}Ordenar por género:
    {VERDE_CLARO}1. {AMARILLO}Masculinos primero
    {VERDE_CLARO}2. {AMARILLO}Femeninos primero
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_orden == "1":
                            orden["genero"] = "M"
                        elif tipo_orden == "2":
                            orden["genero"] = "F"
                        elif tipo_orden == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif ordenar_por == "0":
                        Mensaje(INFO, "Volviendo atrás...")
                        esperar(0.5)
                        break
                    else:
                        Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                        esperar(0.5)
                        continue
            elif pregunta == "3":
                # preguntar por filtro de los trabajadores
                # filtrar por nombre, apellido, fecha_ingreso, etc...

                while True:
                    filtrar_por = Mensaje().pregunta(f"""
    {VERDE_CLARO}Filtrar por:
    {VERDE_CLARO}1. {AMARILLO}Nombre
    {VERDE_CLARO}2. {AMARILLO}Fecha de ingreso
    {VERDE_CLARO}3. {AMARILLO}Genero
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                    if filtrar_por == "1": # filtrar por nombre
                            
                        tipo_filtro = Mensaje().pregunta(f"""
    {VERDE_CLARO}Filtrar por nombre:
    {VERDE_CLARO}1. {AMARILLO}Que contenga:
    {VERDE_CLARO}2. {AMARILLO}Que no contenga:
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_filtro == "1":
                            if "nombre_incluir" not in filtros:
                                filtros["nombre_incluir"] = []
                            # que contenga
                            texto_a_incluir = Mensaje().pregunta("Ingrese el texto a incluir en el nombre: ")
                            filtros["nombre_incluir"].append(texto_a_incluir)
                        elif tipo_filtro == "2":
                            if "nombre_excluir" not in filtros:
                                filtros["nombre_excluir"] = []
                            # que no contenga
                            texto_a_excluir = Mensaje().pregunta("Ingrese el texto a excluir en el nombre: ")
                            filtros["nombre_excluir"].append(texto_a_excluir)
                        elif tipo_filtro == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif filtrar_por == "2": # filtrar por fecha de ingreso
                        tipo_filtro = Mensaje().pregunta(f"""
    {VERDE_CLARO}Filtrar por fecha de ingreso:
    {VERDE_CLARO}1. {AMARILLO}Incluir los de una fecha
    {VERDE_CLARO}2. {AMARILLO}Excluir los de una fecha
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_filtro == "1":
                            if "fecha_ingreso_incluir" not in filtros:
                                filtros["fecha_ingreso_incluir"] = []
                            # preguntar fecha e incluir
                            fecha_a_incluir = Mensaje().pregunta("Ingrese la fecha de ingreso a incluir   (DIA, MES, AÑO) [01-01-2001]: ")
                            try:
                                fecha_a_incluir = Fechas.verificar_formato_fecha(fecha_a_incluir)
                                filtros["fecha_ingreso_incluir"].append(fecha_a_incluir)
                            except Exception as e:
                                Mensaje(ADVERTENCIA, f"Fecha no válida, intente de nuevo... {e}")
                                esperar(0.5)
                                continue
                        elif tipo_filtro == "2":
                            if "fecha_ingreso_excluir" not in filtros:
                                filtros["fecha_ingreso_excluir"] = []
                            # preguntar fecha y excluir
                            fecha_a_excluir = Mensaje().pregunta("Ingrese la fecha de ingreso a excluir   (DIA, MES, AÑO) [01-01-2001]: ")
                            try:
                                fecha_a_excluir = Fechas.verificar_formato_fecha(fecha_a_excluir)
                                filtros["fecha_ingreso_excluir"].append(fecha_a_excluir)
                            except Exception as e:
                                Mensaje(ADVERTENCIA, f"Fecha no válida, intente de nuevo... {e}")
                                esperar(0.5)
                                continue
                        elif tipo_filtro == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif filtrar_por == "3": # filtrar por genero
                        if "genero" not in filtros:
                            filtros["genero"] = []
                        tipo_filtro = Mensaje().pregunta(f"""
    {VERDE_CLARO}Ordenar por género:
    {VERDE_CLARO}1. {AMARILLO}Masculinos primero
    {VERDE_CLARO}2. {AMARILLO}Femeninos primero
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
                        if tipo_filtro == "1":
                            orden["genero"] = "M"
                        elif tipo_filtro == "2":
                            orden["genero"] = "F"
                        elif tipo_filtro == "0":
                            Mensaje(INFO, "Volviendo atrás...")
                            esperar(0.5)
                            break
                        else:
                            Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                            esperar(0.5)
                            continue
                    elif filtrar_por == "0":
                        Mensaje(INFO, "Volviendo atrás...")
                        esperar(0.5)
                        break
                    else:
                        Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                        esperar(0.5)
                        continue


            
                
                
                ...
            elif pregunta == "4":
                # quitar filtros y orden
                orden = {}
                filtros = {}
                Mensaje(EXITO, "Se han eliminado los filtros y el orden de la lista de trabajadores.")
                continue
            elif pregunta == "0":
                Mensaje(INFO, "Volviendo atrás...")
                return (orden, filtros)

            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue

    @classmethod
    def imprimirTrabajadoresOF(self, lista_trabajadores, orden=None, filtros=None):
        if orden:
            claves_orden = orden
            
            for clave in claves_orden:
                direccion = claves_orden[clave]
                if direccion == "ASC":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave).lower())
                elif direccion == "DESC":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave).lower(), reverse=True)
                elif direccion == "RECIENTE":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave), reverse=True)
                elif direccion == "ANTIGUA":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave))
                elif direccion == "M":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave).lower())
                elif direccion == "F":
                    lista_trabajadores.sort(key= lambda trabajador: getattr(trabajador, clave).lower(), reverse=True)
        if filtros:
            for clave in filtros:
                if clave == "nombre_incluir":
                    lista_trabajadores = [x for x in lista_trabajadores if any([filtro in x.nombre for filtro in filtros[clave]])]
                elif clave == "nombre_excluir":
                    lista_trabajadores = [x for x in lista_trabajadores if all([filtro not in x.nombre for filtro in filtros[clave]])]
                elif clave == "fecha_ingreso_incluir":
                    lista_trabajadores = [x for x in lista_trabajadores if any([filtro in x.fecha_ingreso for filtro in filtros[clave]])]
                elif clave == "fecha_ingreso_excluir":
                    lista_trabajadores = [x for x in lista_trabajadores if all([filtro not in x.fecha_ingreso for filtro in filtros[clave]])]
                elif clave == "genero":
                    lista_trabajadores = [x for x in lista_trabajadores if any([filtro.lower() in x.genero for filtro in filtros[clave]])]
            
        # if orden.keys()>0:
        #     if "nombre" in orden.keys():
        #         print("Ordenando por nombre")
        #         lista_trabajadores = sorted(lista_trabajadores, key=lambda x: x.nombre, reverse=True if orden["nombre"] == "DESC" else False)
        #     if "fecha_ingreso" in orden.keys():
        #         lista_trabajadores = sorted(lista_trabajadores, key=lambda x: x.fecha_ingreso, reverse=True if orden["fecha_ingreso"] == "ANTIGUA" else False)
        #     if "genero" in orden.keys():
        #         lista_trabajadores = sorted(lista_trabajadores, key=lambda x: x.genero, reverse=True if orden["genero"] == "F" else False)
        # if filtros.keys()>0:
        #     if "nombre" in filtros.keys():
        #         lista_trabajadores = [x for x in lista_trabajadores if filtros["nombre"].lower() in x.nombre.lower()]
        #     if "fecha_ingreso" in filtros.keys():
        #         lista_trabajadores = [x for x in lista_trabajadores if filtros["fecha_ingreso"] == x.fecha_ingreso]
        #     if "genero" in filtros.keys():
        #         lista_trabajadores = [x for x in lista_trabajadores if filtros["genero"] == x.genero]
        for trabajador in lista_trabajadores:
            print(trabajador)
        return lista_trabajadores
            
    @classmethod
    def listarTrabajadoresBaja(self):
        lista_trabajadores = TrabajadorDAO.list_baja()
        esperar(1)
        for trabajador in lista_trabajadores:
            print(trabajador)
        esperar(2)
        
    @classmethod
    def menuModificarCampoTrabajador(self, campo, trabajador: Trabajador):
        if campo == "1":
            # Modificar nombre
            while True:
                nuevo_nombre = Mensaje().pregunta("Nuevo nombre:         [0 para salir]")
                if nuevo_nombre == "0":
                    Mensaje(INFO, "Volviendo atrás...")
                    esperar(0.5)
                    break
                nuevo_apellido = Mensaje().pregunta("Nuevo apellido:         [0 para salir]")
                if nuevo_apellido == "0":
                    Mensaje(INFO, "Volviendo atrás...")
                    esperar(0.5)
                    break
                while True:
                    confirmar = Mensaje().pregunta(f""" ¿Confirmar cambio de nombre?:
    {ROJO_CLARO}{trabajador.nombre} {trabajador.apellido} ---> {VERDE_CLARO}{nuevo_nombre} {nuevo_apellido}
    {VERDE_CLARO}1. {AMARILLO}SI
    {VERDE_CLARO}2. {AMARILLO}NO
    {VERDE_CLARO}3. {AMARILLO}Otro nombre
    """)            
                    if confirmar == "3":
                        break
                    elif confirmar == "2":
                        Mensaje(INFO, "Volviendo atrás...")
                        esperar(0.5)
                        return
                    elif confirmar == "1":
                        TrabajadorDAO.modificar_nombre(trabajador, nuevo_nombre, nuevo_apellido)
                        trabajador.nombre = nuevo_nombre
                        trabajador.apellido = nuevo_apellido
                        modificando5s("Modificar nombre", f"Actualizando a {nuevo_nombre} {nuevo_apellido}")
                        Mensaje(EXITO, "Nombre y apellido modificados con éxito!")
                        return
                    else:
                        Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                        esperar(0.5)
                        continue
        else:
            if campo == "2":
                self.modificarRutTrabajador(trabajador, trabajador.run, trabajador.rundf)
            elif campo == "3":
                self.modificarCampoExt("correo", trabajador, trabajador.correo)
            elif campo == "4":
                self.modificarCampoExt("genero", trabajador, trabajador.genero)
            elif campo == "5":
                self.modificarCampoExt("telefono", trabajador, trabajador.telefono)
            elif campo == "6":
                self.modificarCampoExt("direccion", trabajador, trabajador.direccion)
            
            
        if campo == "7":
            campo == "Datos Laborales"
            pass

        
    @classmethod
    def modificarRutTrabajador(self, trabajador: Trabajador, run_anterior, rundf_anterior):
        while True:
            run = Mensaje().pregunta("RUN (Sin puntos ni dígito verificador):        [0 para salir]")
            if run == "0":
                Mensaje(INFO, "Saliendo del cambio de RUN...")
                esperar(0.5)
                return
            rundf = Mensaje().pregunta("Dígito verificador RUN:         [ENTER para salir]")
            if rundf == "":
                Mensaje(INFO, "Saliendo del cambio de RUN...")
                esperar(0.5)
                return
            try:
                if rundf == 'k':
                    rundf == 10
                if not validar_rut(int(run), int(rundf)):
                    Mensaje(ERROR, "El RUT ingresado no es válido, intente de nuevo...")
                    esperar(1)
                    return
            except:
                Mensaje(ERROR, "Error al validar el RUT, intente de nuevo...")
                esperar(1)
                return
            while True:
                confirmar = Mensaje().pregunta(f""" ¿Confirmar cambio de RUN?:
    {ROJO_CLARO}{run_anterior}-{rundf_anterior} ---> {VERDE_CLARO}{run}-{rundf}
    {VERDE_CLARO}1. {AMARILLO}SI
    {VERDE_CLARO}2. {AMARILLO}NO
    {VERDE_CLARO}3. {AMARILLO}Otro RUN
    """)            
                if confirmar == "3":
                    break
                elif confirmar == "2":
                    Mensaje(INFO, "Volviendo atrás...")
                    esperar(0.5)
                    return
                elif confirmar == "1":
                    TrabajadorDAO.modificar_run(trabajador, run, rundf)
                    modificando5s(f"Modificar RUN de trabajador", f"Actualizando a {run}-{rundf}")
                    Mensaje(EXITO, f"RUN modificado con éxito!")
                    return
                else:
                    Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                    esperar(0.5)
                    continue
        
        
            
    @classmethod
    def menuModificarTrabajador(self, nombre_usuario):
        Mensaje(f"{AMARILLO}Modificando ficha de trabajador {CIAN}{nombre_usuario}")

        trabajador_a_modificar = TrabajadorDAO.get(nombre_usuario)

        while True:
            Mensaje(f"""

    {VERDE_CLARO}Modificando ficha de {trabajador_a_modificar.nombre} {trabajador_a_modificar.apellido}!


    {VERDE_CLARO}1. {AMARILLO}Modificar su {VERDE}Nombre
    {VERDE_CLARO}2. {AMARILLO}Modificar su {VERDE}RUT
    {VERDE_CLARO}3. {AMARILLO}Modificar su {VERDE}Correo
    {VERDE_CLARO}4. {AMARILLO}Modificar su {VERDE}Genero
    {VERDE_CLARO}5. {AMARILLO}Modificar su {VERDE}Telefono
    {VERDE_CLARO}6. {AMARILLO}Modificar su {VERDE}Direccion
    {VERDE_CLARO}7. {AMARILLO}Modificar sus {VERDE}Datos Laborales
    {VERDE_CLARO}0. {AMARILLO}Volver atrás""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "0":
                Mensaje(INFO, "Volviendo al menú de gestión de trabajadores...")
                esperar(0.5)
                return
            elif pregunta != "1" and pregunta != "2" and pregunta != "3" and pregunta != "4" and pregunta != "5" and pregunta != "6" and pregunta != "7":
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
            else:
                # 1. nombre, 2. run, 3. correo, 4. genero, 5. telefono, 6. direccion, 7. datos_trabajador
                self.menuModificarCampoTrabajador(pregunta, trabajador_a_modificar)

    
    @classmethod
    def menuTrabajador(self, usuario):
        bienv = 'Bienvenido' if usuario.genero == 'Masculino' else 'Bienvenida' if usuario.genero == 'Femenino' else 'Bienvenid@'
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Trabajador")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}{bienv} {usuario.nombre} {usuario.apellido}!
    {CIAN}(Trabajador)


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mi Usuario
    {VERDE_CLARO}0. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos de usuario
                self.modificarDatosUsuario(usuario)
            elif pregunta == "0":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
                
    
    @classmethod
    def menuRRHH(self, usuario):
        bienv = 'Bienvenido' if usuario.genero == 'Masculino' else 'Bienvenida' if usuario.genero == 'Femenino' else 'Bienvenid@'
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Recursos Humanos")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}{bienv} {usuario.nombre} {usuario.apellido}!
    {CIAN}(Recursos Humanos)


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mi Usuario
    {VERDE_CLARO}3. {AMARILLO}Gestionar Trabajadores
    {VERDE_CLARO}0. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos de usuario
                self.modificarDatosUsuario(usuario)
            elif pregunta == "3":
                # Gestionar trabajadores
                self.gestionarTrabajadores(usuario)
            elif pregunta == "0":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
                
    @classmethod
    def menuJefe(self, usuario):
        bienv = 'Bienvenido' if usuario.genero == 'Masculino' else 'Bienvenida' if usuario.genero == 'Femenino' else 'Bienvenid@'
        # Permite al trabajador ver su ficha personal
        # Permite al trabajador modificar sus datos personales
        esperar5s("Iniciando Menú Administrativo")
        while True:
            Mensaje(f"""

    {VERDE_CLARO}{bienv} {usuario.nombre} {usuario.apellido}!
    {CIAN}(Administrativo)


    {VERDE_CLARO}1. {AMARILLO}Ver mi Ficha Personal
    {VERDE_CLARO}2. {AMARILLO}Modificar mi Usuario
    {VERDE_CLARO}3. {AMARILLO}Gestionar Trabajadores
    {VERDE_CLARO}0. {AMARILLO}Cerrar sesión""")
            pregunta = Mensaje().pregunta("Escoge una opción: ")
            if pregunta == "1":
                print(usuario)
                esperar(2)
            elif pregunta == "2":
                # Modificar datos de usuario
                self.modificarDatosUsuario(usuario)
            elif pregunta == "3":
                # Gestionar trabajadores
                self.gestionarTrabajadores(usuario)
            elif pregunta == "0":
                Mensaje(INFO, "Cerrando sesión...")
                esperar(1)
                return
            else:
                Mensaje(ADVERTENCIA, "Opción no válida, intente de nuevo...")
                esperar(0.5)
                continue
       
class Menu:
    """
    Clase para mostrar los menús de inicio de sesión y registro de usuario.
    """
    def menuInicioSesion() -> bool:
        esperar5s("Menú Inicio de Sesión")
        Mensaje("\nINICIANDO SESIÓN...\n")
        nombre_usuario = Mensaje().pregunta("Nombre de usuario: ")
        clave = Mensaje().pregunta_clave()
        if clave == "":
            Mensaje(INFO, "Saliendo del inicio de sesión...")
            esperar(0.5)
            return False
        # Verificar que tipo de usuario es
        validacion = TrabajadorDAO.validar_usuario(nombre_usuario, clave)
        #print("Validación: ", validacion)
        if not validacion:
            AccesoDAO.add(nombre_usuario, clave)
            Mensaje(ERROR, "Error al Iniciar Sesión, nombre de usuario o contraseña incorrectos.")
            esperar(1)
            return False
        else:
            # Mostrar menú dependiendo del tipo de usuario
            # Registrar acceso
            usuario = validacion[1]
            # print("Objeto usuario: ", usuario)
            AccesoDAO.add(usuario.nombre_usuario, "#AccesoCorrecto")
            Mensaje(EXITO, "Inicio de sesión exitoso!")
            MenuInterno.mostrarMenu(usuario)
            return True

    
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
        if clave == "":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        while len(clave) < 4:
            Mensaje(ERROR, "La contraseña no cumple con los requisitos!.\n")
            esperar(1)
            clave = Mensaje().pregunta_clave()
            if clave == "":
                Mensaje(INFO, "Saliendo del registro de usuario...")
                esperar(0.5)
                return
            continue
        run = Mensaje().pregunta("RUN (Sin puntos ni dígito verificador):        [0 para salir]")
        if run == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        rundf = Mensaje().pregunta("Dígito verificador RUN:         [ENTER para salir]")
        if rundf == "":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        try:
            if rundf == 'k':
                rundf == 10
            if not validar_rut(int(run), int(rundf)):
                
                Mensaje(ERROR, "El RUT ingresado no es válido, intente de nuevo...")
                esperar(1)
                return
        except:
            Mensaje(ERROR, "Error al validar el RUT, intente de nuevo...")
            esperar(1)
            return
        nombre = Mensaje().pregunta("Nombres:          [0 para salir]")
        if nombre == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        apellido = Mensaje().pregunta("Apellidos:          [0 para salir]")
        if apellido == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        correo = Mensaje().pregunta("Correo Electrónico:          [0 para salir]")
        if correo == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        genero = Mensaje().pregunta("""Género:          [0 para salir]
        1. Masculino
        2. Femenino
        3. Otro""")
        if genero == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        if genero == "1":
            genero = "Masculino"
        elif genero == "2":
            genero = "Femenino"
        elif genero == "3":
            genero = "Otro"
        telefono = Mensaje().pregunta("Teléfono:          [0 para salir]")
        if telefono == "0":
            Mensaje(INFO, "Saliendo del registro de usuario...")
            esperar(0.5)
            return
        direccion = Mensaje().pregunta("Dirección Completa:        [0 para salir]")
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
                    Mensaje(ERROR, f"Error al registrar un nuevo usuario {tipo_usuario}: {e}")
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