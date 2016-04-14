
CREATE TABLE niveles_instruccion (
   id INT PRIMARY KEY NOT NULL,
   descripcion CHAR(60)
);

INSERT INTO niveles_instruccion (id, descripcion) VALUES (1, 'Educacion Preescolar');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (2, 'Educacion Basica');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (3, 'Educacion Media Diversificada y Profesional');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (4, 'Educacion Superior');