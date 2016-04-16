
CREATE TABLE personal (
   id INT PRIMARY KEY NOT NULL,
   primer_nombre CHAR(15),
   segundo_nombre CHAR(15),
   primer_apellido CHAR(15),
   segundo_apellido CHAR(15),
   cedula CHAR(8),
   id_cargo INT,
   id_nivel_instruccion INT,
   email CHAR(20),
   id_sexo INT
);
