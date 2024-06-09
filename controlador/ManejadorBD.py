# Manejador de la BD con MySQL usando Pool de Conexiones

# Importamos las librerías necesarias
import sys
import mysql.connector as conector
from mysql.connector import pooling as pool


# Clase conexión
class Conexion:
    
    # user = adminyury | pw = *
    dbconfig = {
    "host": "127.0.0.1",
    "user": "correoyury",
    "password": "correoyury@2024",
    "database": "correoyury",
    # "user": "root",
    # "password": "",
    # "database": "correoyury",
    "port": "3306",
}
    _NOMBRE_POOL = "pool"
    _MAXCON = 5
    _pool = None
    
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.MySQLConnectionPool(pool_name = cls._NOMBRE_POOL,
                                                    pool_size = cls._MAXCON,
                                                    **cls.dbconfig)
                print('Pool creada exitosamente')
                return cls._pool
            except Exception as e:
                print(f'Error mientras se creaba la pool de la base de datos: {e}')
                sys.exit()
        else:
            return cls._pool
                  
    # Métodos para obtener y devolver conexiones del pool
    @classmethod
    def getConnection(cls):
        connection = cls.getPool().get_connection()
        #print('Conexión obtenida desde la pool.')
        return connection

    @classmethod
    def dropConnection(cls, connection):
        connection.close()
        #print('Conexion guardada en la pool')

# Clase para manejar la base de datos usando with
class manejadorBD:

    def __init__(self):
        self._conexion = None
        self._manager = None
    
    def __enter__(self):
        self._conexion = Conexion.getConnection()
        self._manager = self._conexion.cursor()
        return self._manager
    
    def __exit__(self, e_type, e_value, e_detail):
        if e_value:
            self._conexion.rollback()
            print(f'Ocurrió una excepción: {e_value}')
        else:
            self._conexion.commit()
        self._manager.close()
        Conexion.dropConnection(self._conexion)



try:    
    # Crear tablas al iniciar la app si no existen
    CREATE_TABLES = [
        # Tabla de trabajador
        # id_usuario, nombre_usuario, clave, clave_salt, run, rundf, nombre
        # apellido, correo, genero, telefono, direccion, tipo_usuario
        # 
        "CREATE TABLE IF NOT EXISTS trabajador (id_usuario INT AUTO_INCREMENT PRIMARY KEY,\
        nombre_usuario VARCHAR(100) NOT NULL, clave VARCHAR(255) NOT NULL, clave_salt VARCHAR(255) NOT NULL,\
        run INT NOT NULL, rundf VARCHAR(2) NOT NULL, nombre VARCHAR(100)  NOT NULL, apellido VARCHAR(100) NOT NULL,\
        correo VARCHAR(100), genero VARCHAR(20) NOT NULL, telefono VARCHAR(20) NOT NULL,\
        direccion VARCHAR(100) NOT NULL, tipo_usuario VARCHAR(40) NOT NULL, datos_trabajador INT, fecha_ingreso TIMESTAMP)",

        "CREATE TABLE IF NOT EXISTS acceso (id_acceso INT AUTO_INCREMENT PRIMARY KEY,\
        nombre_usuario VARCHAR(100) NOT NULL, clave VARCHAR(255) NOT NULL,\
        fecha_acceso TIMESTAMP)"
    ]
    with manejadorBD() as manager:
        print("Inicializando conexión a la base de datos...")
        manager.execute(CREATE_TABLES[0])
        manager.execute(CREATE_TABLES[1])
except Exception as e:
    print("Error al inicializar la base de datos:", e)


# hacer select de correoyury y mostrar los datos
# conn = Conexion.getPool().get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM correoyury")
# for row in cursor:
#     print(row)
    
if __name__ == '__main__':
    with manejadorBD() as manager:
        print('inside with block')
        manager.execute('SELECT * FROM correoyury')
        print(manager.fetchall())