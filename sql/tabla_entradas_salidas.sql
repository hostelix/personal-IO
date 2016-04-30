
CREATE TABLE IF NOT EXISTS entradas_salidas (
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   cedula CHAR(8),
   hora_entrada TEXT,
   hora_salida TEXT
);