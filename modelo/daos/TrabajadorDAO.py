from controlador.ManejadorBD import manejadorBD
from modelo.entidades.Trabajador import Trabajador
from time import sleep as esperar
import bcrypt, os


def hash_password(clave):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(clave.encode('utf-8'), bytes(salt))
    return salt, hashed_pw

def verify_password(clave_almacenada, salt_almacenada, clave_ingresada):
    #print("verificando contraseña")
    
    #print(clave_almacenada)
    #print(salt_almacenada)
    #print(clave_ingresada)
    hashed_pw = bcrypt.hashpw(clave_ingresada.encode('utf-8'), bytes(salt_almacenada, 'utf-8'))
    #print(hashed_pw)
    return hashed_pw == bytes(clave_almacenada, 'utf-8')
    
    
class TrabajadorDAO:
    """
    Clase que maneja la tabla trabajadores de la base de datos.
    
    """
    _SELECT = 'SELECT * FROM trabajador'
    _SELECTID = 'SELECT * FROM trabajador WHERE id_trabajador=%s'
    _INSERT = 'INSERT INTO trabajador (nombre_usuario,\
        clave,\
        clave_salt,\
        run,\
        rundf,\
        nombre,\
        apellido,\
        correo,\
        genero,\
        telefono,\
        direccion,\
        tipo_usuario, \
        fecha_ingreso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())'
    _UPDATE = 'UPDATE trabajador SET id_usuario=%s, id_datos_trabajador=%s WHERE id_trabajador=%s'
    _DELETE = 'DELETE FROM trabajador WHERE id_trabajador=%s'
    
    @classmethod
    def validar_usuario(cls, nombre_usuario, clave):
        with manejadorBD() as manager:
            manager.execute(cls._SELECT)
            data = manager.fetchall()
            for usuario in data:
                #print(usuario[1])
                if usuario[1] == nombre_usuario:
                   # print("coincide username")
                    if verify_password(usuario[2], usuario[3], clave):
                        # Inicio de sesión exitoso
                        objetoUsuario = Trabajador(
                            id_usuario=usuario[0],
                            nombre_usuario=usuario[1],
                            run=usuario[4],
                            rundf=usuario[5],
                            nombre=usuario[6],
                            apellido=usuario[7],
                            correo=usuario[8],
                            genero=usuario[9],
                            telefono=usuario[10],
                            direccion=usuario[11],
                            tipo_usuario=usuario[12],
                            datos_trabajador=usuario[13],
                            fecha_ingreso=usuario[14]
                        )
                        return (True, objetoUsuario)
            return (False)
    
    @classmethod
    def existe_usuario(cls, nombre_usuario):
        with manejadorBD() as manager:
            manager.execute(cls._SELECT)
            data = manager.fetchall()
            for usuario in data:
                if usuario[1] == nombre_usuario:
                    return True
            return False
    
    @classmethod
    def obtener_tipo_usuario(cls, nombre_usuario):
        with manejadorBD() as manager:
            manager.execute(cls._SELECT)
            data = manager.fetchall()
            for trabajador in data:
                if trabajador[1] == nombre_usuario:
                    return trabajador[12]
            return None
    
    
    @classmethod
    def list(cls):
        with manejadorBD() as manager:
            manager.execute(cls._SELECT)
            data = manager.fetchall()
            lista_trabajadores = []
            for trabajador in data:
                new_trabajador = Trabajador(**trabajador)
                lista_trabajadores.append(new_trabajador)
            return lista_trabajadores
    
    @classmethod
    def add(cls, trabajador):
        try:
                
            #Hashear la clave
            clave_salt, clave_hashed = hash_password(trabajador.clave)
            
            values = (trabajador.nombre_usuario,
                    clave_hashed,
                    clave_salt,
                    trabajador.run,
                    trabajador.rundf,
                    trabajador.nombre,
                    trabajador.apellido,
                    trabajador.correo,
                    trabajador.genero,
                    trabajador.telefono,
                    trabajador.direccion,
                    trabajador.tipo_usuario)
            with manejadorBD() as manager:
                manager.execute(cls._INSERT, values)
                return manager.rowcount
        except Exception as e:
            print(e)
            return 0
    
    
if __name__ == "__main__":
    trabajadores = TrabajadorDAO.list()
    for trabajador in trabajadores:
        print(trabajador)
        print(trabajador.get_datos_trabajador())
        print(trabajador.get_usuario())
        print('----------------------------------')