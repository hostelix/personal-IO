
CREATE TABLE sexos (
   id INT PRIMARY KEY NOT NULL,
   descripcion CHAR(20)
);

INSERT INTO niveles_instruccion (id, descripcion) VALUES (1, 'Masculino');
INSERT INTO niveles_instruccion (id, descripcion) VALUES (2, 'Femenino');