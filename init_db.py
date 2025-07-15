import sqlite3

conn = sqlite3.connect("transporte.db")
c = conn.cursor()

# Borrar si existe
c.executescript("""
DROP TABLE IF EXISTS Empresas;
DROP TABLE IF EXISTS Rutas;
DROP TABLE IF EXISTS Paraderos;
DROP TABLE IF EXISTS Distritos;
DROP TABLE IF EXISTS Ruta_Distrito;
""")

# Crear tablas
c.execute("CREATE TABLE Empresas (id INTEGER PRIMARY KEY, nombre TEXT, imagen TEXT)")
c.execute("CREATE TABLE Rutas (id INTEGER PRIMARY KEY, nombre TEXT, empresa_id INTEGER)")
c.execute("CREATE TABLE Paraderos (id INTEGER PRIMARY KEY, nombre TEXT, ruta_id INTEGER)")
c.execute("CREATE TABLE Distritos (id INTEGER PRIMARY KEY, nombre TEXT)")
c.execute("CREATE TABLE Ruta_Distrito (ruta_id INTEGER, distrito_id INTEGER)")

# Empresas
c.execute("INSERT INTO Empresas VALUES (1, 'Empresa A', 'empresa_a.png')")
c.execute("INSERT INTO Empresas VALUES (2, 'Empresa B', 'empresa_b.png')")

# Rutas
c.execute("INSERT INTO Rutas VALUES (1, 'Ruta 101', 1)")
c.execute("INSERT INTO Rutas VALUES (2, 'Ruta 202', 2)")
c.execute("INSERT INTO Rutas VALUES (3, 'Ruta 303', 1)")

# Paraderos
c.executemany("INSERT INTO Paraderos (nombre, ruta_id) VALUES (?, ?)", [
    ('Paradero 1', 1),
    ('Paradero 2', 1),
    ('Paradero 3', 2),
    ('Paradero 4', 2),
    ('Paradero 5', 3)
])

# Distritos
c.executemany("INSERT INTO Distritos (id, nombre) VALUES (?, ?)", [
    (1, 'Miraflores'),
    (2, 'Surco'),
    (3, 'Barranco'),
    (4, 'San Miguel'),
    (5, 'La Molina'),
])

# Ruta-Distrito
c.executemany("INSERT INTO Ruta_Distrito VALUES (?, ?)", [
    (1, 1), (1, 2),
    (2, 3), (2, 4),
    (3, 1), (3, 5),
])

conn.commit()
conn.close()
print("✔️ Base de datos ampliada")
