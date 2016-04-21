
CREATE TABLE IF NOT EXISTS cargos (
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   descripcion CHAR(60)
);

INSERT INTO niveles_instruccion (id, descripcion) VALUES (1, 'Docente');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (2, 'Obrero');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (3, 'Otros');