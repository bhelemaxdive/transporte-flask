from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "transporte.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["usuario"] == "admin" and request.form["clave"] == "admin":
            return redirect("/menu")
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    return render_template("login.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/rutas")
def rutas():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT r.id, r.nombre, e.nombre FROM Rutas r JOIN Empresas e ON r.empresa_id = e.id")
    data = cur.fetchall()
    conn.close()
    return render_template("rutas.html", rutas=data)

@app.route("/detalle/<int:ruta_id>")
def detalle(ruta_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT e.nombre, e.imagen FROM Empresas e JOIN Rutas r ON e.id = r.empresa_id WHERE r.id = ?", (ruta_id,))
    empresa = cur.fetchone()

    cur.execute("SELECT nombre FROM Paraderos WHERE ruta_id = ?", (ruta_id,))
    paraderos = [p[0] for p in cur.fetchall()]

    cur.execute("""
        SELECT d.nombre FROM Distritos d
        JOIN Ruta_Distrito rd ON d.id = rd.distrito_id
        WHERE rd.ruta_id = ?
    """, (ruta_id,))
    distritos = [d[0] for d in cur.fetchall()]
    conn.close()
    return render_template("detalle.html", empresa=empresa, paraderos=paraderos, distritos=distritos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
