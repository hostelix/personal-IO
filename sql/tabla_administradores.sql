CREATE TABLE IF NOT EXISTS administradores (
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   usuario CHAR(20),
   password CHAR(50),
   email CHAR(30)
);

INSERT INTO administradores (id,usuario, password, email) VALUES (1,'admin', 'admin', 'admin@gmail.com');