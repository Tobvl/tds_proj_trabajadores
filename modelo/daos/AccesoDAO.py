from controlador.ManejadorBD import manejadorBD

class AccesoDAO:
    """
    Clase que maneja la tabla acceso en la base de datos.
    
    """
    _SELECT = 'SELECT * FROM acceso'
    _SELECTID = 'SELECT * FROM acceso WHERE id_acceso=%s'
    _INSERT = 'INSERT INTO acceso (nombre_usuario,\
    clave) VALUES (%s, %s)'
    _DELETE = 'DELETE FROM acceso WHERE id_acceso=%s'
    
    @classmethod
    def add(cls, usuario, clave):
        with manejadorBD() as manager:
            manager.execute(cls._INSERT, (usuario, clave))