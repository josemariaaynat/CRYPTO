from movements import app
from flask import render_template, url_for, redirect, request
import csv
import sqlite3
from datetime import datetime, date, time

DBFILE = app.config['DB_FILE']


@app.route("/")
def listaMovimientos():
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    c.execute("SELECT fecha,hora,from_currency,from_quantity,to_currency,to_quantity from movimientos;" )
    print(c.fetchall())

    ingresos=c.fetchall()

    total = 0
    for ingreso in ingresos:
        total+= float(ingreso [6])
    conn.close()

    return render_template("movementsList.html",datos=ingresos, total=total)

@app.route("/nuevacompra", methods=["GET","POST"])
def nuevaCompra():
    if request.method == 'POST':
        conn = sqlite3.connect(DBFILE)

        c = conn.cursor()
        now=datetime.now().time()

        c.execute('INSERT INTO movimientos (fecha,hora,from_currency,from_quantity,to_currency,to_quantity) VALUES (?, ? ,?,?,?,?);', 
                    (
                        date.today(),
                        str(now),
                        request.form.get("from_currency"),
                        float(request.form.get("from_quantity")),
                        request.form.get("to_currency"),
                        float(request.form.get("to_quantity"))
                    )
            )

        conn.commit()
        conn.close()

        return redirect(url_for("listaMovimientos"))

    return render_template("alta.html")


@app.route("/resumen", methods=["GET","POST"])
def Resumen():
            conn = sqlite3.connect(DBFILE)
        c = conn.cursor()