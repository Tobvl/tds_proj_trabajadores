class DatosTrabajador:
    """
    Clase para tabla de datos laborales
    """
    def __init__(self,
                 id_datoslaborales: int,
                 id_contacto_emergencia: int,
                 id_carga_familiar: int,):
        self.id_datoslaborales = id_datoslaborales
        self.id_contacto_emergencia = id_contacto_emergencia
        self.id_carga_familiar = id_carga_familiar
        