SELECT 'DANDO PERMISOS A USUARIO pma' AS '';
CREATE USER 'pma'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'pma'@'%' IDENTIFIED BY '';
FLUSH PRIVILEGES;

SELECT 'CREANDO TABLAS' AS '';

-- CREACIÓN DE TABLAS
USE correoyury;

-- TABLA DE CARGA FAMILIAR
CREATE TABLE `correoyury`.`carga_familiar` (
        `id_cargafamiliar` INT NOT NULL AUTO_INCREMENT ,
         `nombre` VARCHAR(150) NOT NULL ,
          `edad` INT NOT NULL ,
           `parentesco` VARCHAR(50) NOT NULL ,
            PRIMARY KEY (`id_cargafamiliar`)
            );

-- TABLA DE CONTACTO DE EMERGENCIA
CREATE TABLE `correoyury`.`contacto_emergencia` (
        `id_contactoemergencia` INT NOT NULL AUTO_INCREMENT ,
         `nombre` VARCHAR(150) NOT NULL ,
          `telefono` INT NOT NULL ,
            PRIMARY KEY (`id_contactoemergencia`)
            );

-- TABLA DE DATOS TRABAJADOR
CREATE TABLE `correoyury`.`datos_trabajador` (
        `id_datos_trabajador` INT NOT NULL AUTO_INCREMENT ,
         `id_contacto_emergencia` INT ,
          `id_carga_familiar` INT ,
           PRIMARY KEY (`id_datos_trabajador`),
           FOREIGN KEY (`id_contacto_emergencia`) REFERENCES `contacto_emergencia`(`id_contactoemergencia`),
           FOREIGN KEY (`id_carga_familiar`) REFERENCES `carga_familiar`(`id_cargafamiliar`)
           );

-- TABLA DE TRABAJADORES
CREATE TABLE IF NOT EXISTS `correoyury`.`trabajador` (
  `id_usuario` int NOT NULL AUTO_INCREMENT ,
  `nombre_usuario` varchar(100),
  `clave` varchar(255) NOT NULL,
  `clave_salt` varchar(255) NOT NULL,
  `run` int NOT NULL,
  `rundf` varchar(2) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(100),
  `genero` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `tipo_usuario` varchar(40) NOT NULL,
  `datos_trabajador` int,
  `fecha_ingreso` TIMESTAMP,
  `modificacion_bloqueada` BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (`id_usuario`),
  FOREIGN KEY (`datos_trabajador`) REFERENCES `datos_trabajador`(`id_datos_trabajador`)
);
        

-- TABLA DE TRABAJADORES DADOS DE BAJA
CREATE TABLE IF NOT EXISTS `correoyury`.`trabajadores_baja` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(100) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `clave_salt` varchar(255) NOT NULL,
  `run` int(11) NOT NULL,
  `rundf` varchar(2) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `genero` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `tipo_usuario` varchar(40) NOT NULL,
  `datos_trabajador` int(11) DEFAULT NULL,
  `fecha_ingreso` date DEFAULT NULL,
  `modificacion_bloqueada` tinyint(1) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_baja` date NOT NULL,
  `administrativo_baja` varchar(50) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  FOREIGN KEY (`datos_trabajador`) REFERENCES `datos_trabajador`(`id_datos_trabajador`)
);

-- TABLA DE ACCESOS
CREATE TABLE IF NOT EXISTS `correoyury`.`acceso` (
        `id_acceso` INT AUTO_INCREMENT PRIMARY KEY,\
        `nombre_usuario` VARCHAR(100) NOT NULL, 
        `clave` VARCHAR(255) NOT NULL,
        `fecha_acceso` TIMESTAMP);

-- INSERCIÓN DE DATOS
SELECT 'INSERTANDO DATOS' AS '';
SELECT 'INSERTANDO DATOS' AS '';


INSERT IGNORE INTO `correoyury`.`datos_trabajador` (
        `id_contacto_emergencia`, 
        `id_carga_familiar`
) VALUES ( 
        NULL, 
        NULL);

INSERT IGNORE INTO `correoyury`.`datos_trabajador` (
        `id_contacto_emergencia`, 
        `id_carga_familiar`
) VALUES ( 
        NULL, 
        NULL);

INSERT IGNORE INTO `correoyury`.`datos_trabajador` (
        `id_contacto_emergencia`, 
        `id_carga_familiar`
) VALUES ( 
        NULL, 
        NULL);

INSERT IGNORE INTO `correoyury`.`trabajador` (
        `id_usuario`, 
        `nombre_usuario`, 
        `clave`, 
        `clave_salt`, 
        `run`, 
        `rundf`, 
        `nombre`, 
        `apellido`, 
        `correo`, 
        `genero`, 
        `telefono`, 
        `direccion`, 
        `tipo_usuario`, 
        `datos_trabajador`, 
        `fecha_ingreso`, 
        `modificacion_bloqueada`) VALUES (
                NULL, 'admin', 
                '$2b$12$yJIsnYmsWIR7pOzngXUrh.3/PTEIc45l.C0HfvH/XCe2J9XDreSZS', 
                '$2b$12$yJIsnYmsWIR7pOzngXUrh.', 
                '1', 
                '9', 
                'Administrador', 
                'Admin', 
                'admin@admin.com', 
                'Otro', 
                '912345678', 
                'Dirección de Administrador #123', 
                'Jefe', 
                1, 
                '2024-06-22', 
                '0');
                
INSERT IGNORE INTO `correoyury`.`trabajador` (
        `id_usuario`, 
        `nombre_usuario`, 
        `clave`, 
        `clave_salt`, 
        `run`, 
        `rundf`, 
        `nombre`, 
        `apellido`, 
        `correo`, 
        `genero`, 
        `telefono`, 
        `direccion`, 
        `tipo_usuario`, 
        `datos_trabajador`, 
        `fecha_ingreso`, 
        `modificacion_bloqueada`) VALUES (
                NULL, 
                'trabajador', 
                '$2b$12$vJAzqlFQYv79qxHApq.WHeDpiu6q/stBcOaXYvIk9DUovYg3AwmQm', 
                '$2b$12$vJAzqlFQYv79qxHApq.WHe', 
                '1', 
                '9', 
                'Trabajador', 
                'Apellido trabajador', 
                'trabajador@trabajador.com', 
                'Masculino', 
                '912345678', 
                'Calle de Trabajador #321', 
                'Trabajador', 
                2, 
                '2024-06-30 00:18:08', 
                '0');

INSERT IGNORE INTO `correoyury`.`trabajador` (
        `id_usuario`, 
        `nombre_usuario`, 
        `clave`, 
        `clave_salt`, 
        `run`, 
        `rundf`, 
        `nombre`, 
        `apellido`, 
        `correo`, 
        `genero`, 
        `telefono`, 
        `direccion`, 
        `tipo_usuario`, 
        `datos_trabajador`, 
        `fecha_ingreso`, 
        `modificacion_bloqueada`) VALUES (
                NULL, 
                'recursoshumanos', 
                '$2b$12$H5m6M2omlwPwWZOYsGVjm.Wb.0XKLfvSLgH3PGsz9oeiA5ddVvhHa', 
                '$2b$12$H5m6M2omlwPwWZOYsGVjm.', 
                '1', 
                '9', 
                'Recursos Humanos', 
                'Apellido RRHH', 
                'rrhh@rrhh.com', 
                'Femenino', 
                '987654321', 
                'Calle de recursos humanos #992 depto 2', 
                'Recursos Humanos', 
                3, 
                '2024-06-30 00:20:20', 
                '0');


SELECT 'FIN DE INSERCIÓN DE DATOS' AS '';
SELECT 'FIN DE INSERCIÓN DE DATOS' AS '';