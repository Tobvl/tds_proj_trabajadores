class Fechas:
    
    @staticmethod
    def verificar_formato_fecha(fecha):
        # Intentamos separar la fecha en partes
        partes = fecha.split('-')
        
        # Verificamos si la fecha tiene tres partes
        if len(partes) != 3:
            raise ValueError("El formato de la fecha es incorrecto. Debe ser DD-MM-AAAA.")
        
        dia, mes, año = partes
        
        # Verificamos que todas las partes sean números
        if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
            raise ValueError("El formato de la fecha es incorrecto. Día, mes y año deben ser números.")
        
        # Convertimos las partes a enteros
        dia = int(dia)
        mes = int(mes)
        año = int(año)
        
        # Verificamos que el día, mes y año estén en el rango correcto
        if not (1 <= dia <= 31):
            raise ValueError("El día es inválido. Debe estar entre 1 y 31.")
        if not (1 <= mes <= 12):
            raise ValueError("El mes es inválido. Debe estar entre 1 y 12.")
        if año < 1:
            raise ValueError("El año es inválido. Debe ser un número positivo.")

        # Si todas las verificaciones pasan, la fecha es válida
        if mes < 10:
            mes = f"0{mes}"
        if dia < 10:
            dia = f"0{dia}"
        return f"{dia}-{mes}-{año}"
