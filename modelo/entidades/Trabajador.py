from .DatosTrabajador import DatosTrabajador

class Trabajador:
    def __init__(self,
                 id_usuario=None,
                 nombre_usuario=None,
                 clave=None,
                 run=None,
                 rundf=None,
                 nombre=None,
                 apellido=None,
                 correo=None,
                 genero=None,
                 telefono=None,
                 direccion=None,
                 tipo_usuario=None,
                 datos_trabajador=None,
                 fecha_ingreso=None):
        self._id_usuario = id_usuario
        self._nombre_usuario = nombre_usuario
        self._clave = clave
        self._run = run
        self._rundf = rundf
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._genero = genero
        self._telefono = telefono
        self._direccion = direccion
        self._tipo_usuario = tipo_usuario
        self._datos_trabajador = datos_trabajador
        self._fecha_ingreso = fecha_ingreso
    
    def __str__(self):
        return f"""
    {self._tipo_usuario}: {self._nombre} {self._apellido}
    RUN: {self._run}-{self._rundf}
    Correo: {self._correo}
    Género: {self._genero}
    Teléfono: {self._telefono}
    Dirección: {self._direccion}
    Tipo de Usuario: {self._tipo_usuario}
    """
    
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @property
    def clave(self):
        return self._clave

    @property
    def run(self):
        return self._run
    
    @property
    def rundf(self):
        return self._rundf

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def correo(self):
        return self._correo

    @property
    def genero(self):
        return self._genero

    @property
    def telefono(self):
        return self._telefono

    @property
    def direccion(self):
        return self._direccion

    @property
    def tipo_usuario(self):
        return self._tipo_usuario
    
    @property
    def datos_trabajador(self):
        return self._datos_trabajador

    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso
    
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    @run.setter
    def run(self, run):
        self._run = run
        
    @rundf.setter
    def rundf(self, rundf):
        self._rundf = rundf

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def id_usuario(self, apellido):
        self._apellido = apellido

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @tipo_usuario.setter
    def tipo_usuario(self, tipo_usuario):
        self._tipo_usuario = tipo_usuario
    
    @datos_trabajador.setter
    def datos_trabajador(self, datos_trabajador):
        self._datos_trabajador = datos_trabajador
        
    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso