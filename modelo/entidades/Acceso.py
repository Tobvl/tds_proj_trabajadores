# Controlar accesos a la aplicación

class Acceso:
    def __init__(self, nombre_usuario, clave):
        self._nombre_usuario = nombre_usuario
        self._clave = clave
    
    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @property
    def clave(self):
        return self._clave
    
    