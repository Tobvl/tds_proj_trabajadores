# Taller de Desarrollo, Proyecto Trabajadores
## Correo de Yury

Sistema que permite almacenar la información de empleados con variadas funcionalidades

La empresa “El correo de Yury” esta comenzando a entrar al mercado, y se ha dado cuenta que la nómina de trabajadores ya no puede mantenerla en planillas Excel. Es por esto por lo que requiere de un sistema que permita almacenar la información de sus empleados con las siguientes funcionalidades"
El nombre de archivo, el nombre de directorio o la sintaxis de la etiqueta del volumen no son correctos.

## Requisitos
- Python 3.8+
- Docker compose
- Git

## Modo de uso
1. Clonar el repositorio

```
git clone https://github.com/Tobvl/tds_proj_trabajadores.git
```

2. Ingresar al directorio del proyecto

```
cd tds_proj_trabajadores
```

3. Instalar dependencias del proyecto

```
pip install -r requiremientos.txt
```

4. Levantar base de datos

```
docker compose up -d
```

5. Ejecutar el proyecto

```
python main.py
```