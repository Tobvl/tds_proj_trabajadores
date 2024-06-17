from controlador.ManejadorBD import manejadorBD
from modelo.entidades.Trabajador import Trabajador
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
    _SELECTID = 'SELECT * FROM trabajador WHERE id_usuario=%s'
    _SELECT_USERNAME = 'SELECT * FROM trabajador WHERE nombre_usuario=%s'
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
        fecha_ingreso, \
        modificacion_bloqueada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), FALSE)'
    _UPDATE = 'UPDATE trabajador SET %s=%s WHERE id_usuario=%s'
    _UPDATE_NOMBRE = 'UPDATE trabajador SET nombre=%s WHERE id_usuario=%s'
    _UPDATE_APELLIDO = 'UPDATE trabajador SET apellido=%s WHERE id_usuario=%s'
    _UPDATE_CORREO = 'UPDATE trabajador SET correo=%s WHERE id_usuario=%s'
    _UPDATE_GENERO = 'UPDATE trabajador SET genero=%s WHERE id_usuario=%s'
    _UPDATE_TELEFONO = 'UPDATE trabajador SET telefono=%s WHERE id_usuario=%s'
    _UPDATE_DIRECCION = 'UPDATE trabajador SET direccion=%s WHERE id_usuario=%s'
    _UPDATE_RUN_RUN = 'UPDATE trabajador SET run=%s WHERE id_usuario=%s'
    _UPDATE_RUN_DF = 'UPDATE trabajador SET rundf=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM trabajador WHERE id_usuario=%s'

    _DARBAJA_DELETE = 'DELETE FROM trabajador WHERE id_usuario=%s'
    _DARBAJA_INSERT = 'INSERT INTO trabajadores_baja (id_usuario, \
        nombre_usuario,\
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
        datos_trabajador, \
        fecha_ingreso, \
        modificacion_bloqueada, \
        activo, \
        fecha_baja, \
        administrativo_baja) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, NOW(), %s)'
    
    @classmethod
    def dar_baja(cls, trabajador, administrativo):
        try:
            with manejadorBD() as manager:
                print("obteniendo trabajador a dar de baja")
                manager.execute(cls._SELECTID, (trabajador.id_usuario,))
                trabajador_values = list(manager.fetchone()) 
            print(trabajador_values)
            insert_values = trabajador_values + [administrativo.nombre_usuario]
            print(insert_values)
            with manejadorBD() as manager:
                manager.execute(cls._DARBAJA_INSERT, insert_values)
            
            print("Trabajador dado de baja exitosamente")
            
        except Exception as e:
            raise e
    
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
                            fecha_ingreso=usuario[14],
                            modificacion_bloqueada=usuario[15],
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
                new_trabajador = Trabajador(nombre_usuario=trabajador[1],
                                            run=trabajador[4],
                                            rundf=trabajador[5],
                                            nombre=trabajador[6],
                                            apellido=trabajador[7],
                                            correo=trabajador[8],
                                            genero=trabajador[9],
                                            telefono=trabajador[10],
                                            direccion=trabajador[11],
                                            tipo_usuario=trabajador[12],
                                            datos_trabajador=trabajador[13],
                                            fecha_ingreso=trabajador[14],
                                            modificacion_bloqueada=trabajador[15])
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
            raise e
    
    @classmethod
    def update(cls, trabajador):
        pass

    @classmethod
    def get(cls, nombre_usuario) -> Trabajador:
        try:
            with manejadorBD() as manager:
                manager.execute(cls._SELECT_USERNAME, (nombre_usuario,))
                data = manager.fetchone()
                if data:
                    trabajador = Trabajador(id_usuario=data[0],
                                            nombre_usuario=data[1],
                                            clave=data[2],
                                            run=data[4],
                                            rundf=data[5],
                                            nombre=data[6],
                                            apellido=data[7],
                                            correo=data[8],
                                            genero=data[9],
                                            telefono=data[10],
                                            direccion=data[11],
                                            tipo_usuario=data[12],
                                            datos_trabajador=data[13],
                                            fecha_ingreso=data[14],
                                            modificacion_bloqueada=data[15])
                    return trabajador
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def get_id_by_username(cls, nombre_usuario):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._SELECT_USERNAME, (nombre_usuario,))
                data = manager.fetchone()
                if data:
                    return data[0]
                else:
                    return None
        except Exception as e:
            raise e
    
    @classmethod
    def modificar_nombre(cls, usuario, nuevo_nombre, nuevo_apellido):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_NOMBRE, (nuevo_nombre, int(usuario.id_usuario)))
                manager.execute(cls._UPDATE_APELLIDO, (nuevo_apellido, int(usuario.id_usuario)))
                # print("Nombre y apellido modificado exitosamente")
                return manager.rowcount
        except Exception as e:
            raise e
        
    @classmethod
    def modificar_correo(cls, usuario, nuevo_correo):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_CORREO, (nuevo_correo, int(usuario.id_usuario)))
                # print("Correo modificado exitosamente")
                return manager.rowcount
        except Exception as e:
            raise e
        
    @classmethod
    def modificar_telefono(cls, usuario, nuevo_telefono):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_TELEFONO, (nuevo_telefono, int(usuario.id_usuario)))
                # print("Teléfono modificado exitosamente")
                return manager.rowcount
        except Exception as e:
            raise e
        
    @classmethod
    def modificar_genero(cls, usuario, nuevo_genero):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_GENERO, (nuevo_genero, int(usuario.id_usuario)))
                # print("Género modificado exitosamente")
                return manager.rowcount
        except Exception as e:
            raise e
        
    @classmethod
    def modificar_run(cls, usuario, nuevo_run, nuevo_df):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_RUN_RUN, (nuevo_run, int(usuario.id_usuario)))
                manager.execute(cls._UPDATE_RUN_DF, (nuevo_df, int(usuario.id_usuario)))
                # print("RUN y DF modificado exitosamente")
                return manager.rowcount
        except Exception as e:
            raise e
        
    @classmethod
    def modificar_direccion(cls, usuario, nueva_direccion):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._UPDATE_DIRECCION, (nueva_direccion, int(usuario.id_usuario)))
                # print("Dirección modificada exitosamente!")
                return manager.rowcount
        except Exception as e:
            raise e
    
if __name__ == "__main__":
    trabajadores = TrabajadorDAO.list()
    for trabajador in trabajadores:
        print(trabajador)
        print(trabajador.get_datos_trabajador())
        print(trabajador.get_usuario())
        print('----------------------------------')