from movements import app
from flask import render_template, url_for, redirect

@app.route("/")
def listaMovimientos():
    return render_template("movementsList.html", miTexto="Ya veremos si hay o no")