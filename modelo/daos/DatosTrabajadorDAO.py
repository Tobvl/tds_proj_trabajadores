from controlador.ManejadorBD import manejadorBD
from modelo.entidades.Trabajador import Trabajador

class DatosTrabajadorDAO:

    _SELECT_DATOS_TRABAJADOR = "SELECT * FROM datos_trabajador WHERE id_datos_trabajador = %s"
    _CREAR_DATOS_TRABAJADOR = "INSERT INTO datos_trabajador (id_contacto_emergencia, id_carga_familiar) VALUES (NULL, NULL)"
    _ASIGNAR_DATOS_TRABAJADOR = "UPDATE trabajador SET datos_trabajador = %s WHERE id_usuario = %s"

    _SELECT_ID_CONTACTOEMERGENCIA = "SELECT id_contacto_emergencia FROM datos_trabajador WHERE id_datos_trabajador = %s"
    _SELECT_ID_CARGAFAMILIAR = "SELECT id_carga_familiar FROM datos_trabajador WHERE id_datos_trabajador = %s"
    _SELECT_INFO_CONTACTOEMERGENCIA = "SELECT * FROM contacto_emergencia WHERE id_contactoemergencia = %s"
    _SELECT_INFO_CARGAFAMILIAR = "SELECT * FROM carga_familiar WHERE id_cargafamiliar = %s"

    _INSERT_CONTACTOEMERGENCIA = "INSERT INTO contacto_emergencia (nombre, telefono) VALUES (%s, %s)"
    _MODIFY_DATOSLABORALES_CONTACTOEMERGENCIA = "UPDATE datos_trabajador SET id_contacto_emergencia = %s WHERE id_datos_trabajador = %s"
    _INSERT_CARGAFAMILIAR = "INSERT INTO carga_familiar (nombre, edad, parentesco) VALUES (%s, %s, %s)"
    _MODIFY_DATOSLABORALES_CARGAFAMILIAR = "UPDATE datos_trabajador SET id_carga_familiar = %s WHERE id_datos_trabajador = %s"

    _UPDATE_CONTACTOEMERGENCIA = "UPDATE contacto_emergencia SET nombre = %s, telefono = %s WHERE id_contactoemergencia = %s"
    _UPDATE_CARGAFAMILIAR = "UPDATE carga_familiar SET nombre = %s, edad = %s, parentesco = %s WHERE id_cargafamiliar = %s"

    @classmethod
    def agregar_contacto_emergencia(cls, datos_laborales, nombre, telefono):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._INSERT_CONTACTOEMERGENCIA, (nombre, telefono))
                manager.execute(cls._MODIFY_DATOSLABORALES_CONTACTOEMERGENCIA, (manager.lastrowid, datos_laborales))
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def agregar_carga_familiar(cls, datos_laborales, nombre, edad, parentesco):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._INSERT_CARGAFAMILIAR, (nombre, edad, parentesco))
                manager.execute(cls._MODIFY_DATOSLABORALES_CARGAFAMILIAR, (manager.lastrowid, datos_laborales))
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e
    
    @classmethod
    def get_datos_trabajador(cls, trabajador: Trabajador):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._SELECT_DATOS_TRABAJADOR, (trabajador.datos_trabajador,))
                data = manager.fetchone()
                if data:
                    return data[0]
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def get_ultimo_id(cls):
        try:
            with manejadorBD() as manager:
                manager.execute("SELECT MAX(id_datos_trabajador) FROM datos_trabajador")
                data = manager.fetchone()
                if data:
                    return data[0]
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def crear_datos_trabajador(cls):
        try:
            with manejadorBD() as manager:
                manager.execute(cls._CREAR_DATOS_TRABAJADOR)
                data = manager.lastrowid
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e
    
    @classmethod
    def get_idcontacto_emergencia(cls, id_datos_trabajador):
        try:
            with manejadorBD() as manager:
                # buscar el contacto de emergencia correspondiente a esos datos laborales
                values = (id_datos_trabajador,)
                manager.execute(cls._SELECT_ID_CONTACTOEMERGENCIA, values)
                data = manager.fetchone()
                if data:
                    return data[0]
                else:
                    return None
        except Exception as e:
            raise e
    
    @classmethod
    def get_infocontacto_emergencia(cls, id_contacto_emergencia):
        try:
            with manejadorBD() as manager:
                # buscar la información del contacto de emergencia
                values = (id_contacto_emergencia,)
                manager.execute(cls._SELECT_INFO_CONTACTOEMERGENCIA, values)
                data = manager.fetchone()
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    
    @classmethod
    def get_idcarga_familiar(cls, id_datos_trabajador):
        try:
            with manejadorBD() as manager:
                values = (id_datos_trabajador,)
                # buscar la carga familiar correspondiente a esos datos laborales
                manager.execute(cls._SELECT_ID_CARGAFAMILIAR, values)
                data = manager.fetchone()
                if data:
                    return data[0]
                else:
                    return None
        except Exception as e:
            raise e
    
    @classmethod
    def get_infocarga_familiar(cls, id_carga_familiar):
        try:
            with manejadorBD() as manager:
                # buscar la información de la carga familiar
                values = (id_carga_familiar,)
                manager.execute(cls._SELECT_INFO_CARGAFAMILIAR, values)
                data = manager.fetchone()
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def modificar_contacto_emergencia(cls, id_contacto_emergencia, nombre, telefono):
        try:
            with manejadorBD() as manager:
                
                values = (nombre, telefono, id_contacto_emergencia)
                manager.execute(cls._UPDATE_CONTACTOEMERGENCIA, values,)
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def eliminar_contacto_emergencia(self, id_contacto_emergencia):
        try:
            with manejadorBD() as manager:
                # Eliminar contacto de emergencia de datos laborales
                manager.execute("UPDATE datos_trabajador SET id_contacto_emergencia = NULL WHERE id_contacto_emergencia = %s", (id_contacto_emergencia,))
                # Eliminar registro de contacto de emergencia
                manager.execute("DELETE FROM contacto_emergencia WHERE id_contactoemergencia = %s", (id_contacto_emergencia,))
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def modificar_carga_familiar(cls, id_carga_familiar, nombre, edad, parentesco):
        try:
            with manejadorBD() as manager:
                
                values = (nombre, edad, parentesco, id_carga_familiar)
                manager.execute(cls._UPDATE_CARGAFAMILIAR, values,)
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e

    @classmethod
    def eliminar_carga_familiar(self, id_carga_familiar):
        try:
            with manejadorBD() as manager:
                # Eliminar carga familiar de datos laborales
                manager.execute("UPDATE datos_trabajador SET id_carga_familiar = NULL WHERE id_carga_familiar = %s", (id_carga_familiar,))
                # Eliminar registro de carga familiar
                manager.execute("DELETE FROM carga_familiar WHERE id_carga_familiar = %s", (id_carga_familiar,))
                data = manager.rowcount
                if data:
                    return data
                else:
                    return None
        except Exception as e:
            raise e