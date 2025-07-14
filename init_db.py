import sqlite3

conn = sqlite3.connect("transporte.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Empresas")
c.execute("DROP TABLE IF EXISTS Rutas")
c.execute("DROP TABLE IF EXISTS Paraderos")
c.execute("DROP TABLE IF EXISTS Distritos")
c.execute("DROP TABLE IF EXISTS Ruta_Distrito")

c.execute("CREATE TABLE Empresas (id INTEGER PRIMARY KEY, nombre TEXT, imagen TEXT)")
c.execute("CREATE TABLE Rutas (id INTEGER PRIMARY KEY, nombre TEXT, empresa_id INTEGER)")
c.execute("CREATE TABLE Paraderos (id INTEGER PRIMARY KEY, nombre TEXT, ruta_id INTEGER)")
c.execute("CREATE TABLE Distritos (id INTEGER PRIMARY KEY, nombre TEXT)")
c.execute("CREATE TABLE Ruta_Distrito (ruta_id INTEGER, distrito_id INTEGER)")

c.execute("INSERT INTO Empresas VALUES (1, 'Empresa A', 'empresa_a.png')")
c.execute("INSERT INTO Rutas VALUES (1, 'Ruta 101', 1)")
c.execute("INSERT INTO Paraderos VALUES (1, 'Paradero 1', 1), (2, 'Paradero 2', 1)")
c.execute("INSERT INTO Distritos VALUES (1, 'Miraflores'), (2, 'Surco'), (3, 'Barranco')")
c.execute("INSERT INTO Ruta_Distrito VALUES (1, 1), (1, 2)")

conn.commit()
conn.close()
print("✔️ Base de datos creada")
