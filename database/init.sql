-- Insertar usuario admin por defecto
select 'Inserting ADMIN...' AS '';

USE correoyury;

CREATE TABLE IF NOT EXISTS trabajador (id_usuario INT AUTO_INCREMENT PRIMARY KEY,\
        nombre_usuario VARCHAR(100) NOT NULL, clave VARCHAR(255) NOT NULL, clave_salt VARCHAR(255) NOT NULL,\
        run INT NOT NULL, rundf VARCHAR(2) NOT NULL, nombre VARCHAR(100)  NOT NULL, apellido VARCHAR(100) NOT NULL,\
        correo VARCHAR(100), genero VARCHAR(20) NOT NULL, telefono VARCHAR(20) NOT NULL,\
        direccion VARCHAR(100) NOT NULL, tipo_usuario VARCHAR(40) NOT NULL, datos_trabajador INT, fecha_ingreso TIMESTAMP, \
        modificacion_bloqueada BOOLEAN DEFAULT FALSE);

CREATE TABLE IF NOT EXISTS acceso (id_acceso INT AUTO_INCREMENT PRIMARY KEY,\
        nombre_usuario VARCHAR(100) NOT NULL, clave VARCHAR(255) NOT NULL,\
        fecha_acceso TIMESTAMP);

CREATE TABLE IF NOT EXISTS `trabajadores_baja` (
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
  PRIMARY KEY (`id_usuario`)
);

INSERT IGNORE INTO `trabajador` (`id_usuario`, `nombre_usuario`, `clave`, `clave_salt`, `run`, `rundf`, `nombre`, `apellido`, `correo`, `genero`, `telefono`, `direccion`, `tipo_usuario`, `datos_trabajador`, `fecha_ingreso`, `modificacion_bloqueada`) VALUES (NULL, 'admin', '$2b$12$yJIsnYmsWIR7pOzngXUrh.3/PTEIc45l.C0HfvH/XCe2J9XDreSZS', '$2b$12$yJIsnYmsWIR7pOzngXUrh.', '1', '9', 'Administrador', 'Admin', 'admin@admin.com', 'Otro', '912345678', 'Dirección de Administrador #123', 'Jefe', NULL, '2024-06-22', '0')