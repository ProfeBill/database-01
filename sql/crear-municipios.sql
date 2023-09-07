
CREATE TABLE municipios (
	codigo_municipio varchar(40) NOT NULL,
	nombre_municipio text NULL,
	codigo_departamento varchar(40) NULL,
	CONSTRAINT municipios_pk PRIMARY KEY (codigo_municipio)
);