from movements import app, acciones
from movements.forms import FormMovimientos
from flask import render_template, request, url_for, redirect 

DBFILE = app.config['DBFILE'] 

@app.route('/')
def listadoMovimientos():
    ingresos = acciones.busqueda('SELECT fecha, hora, monedafrom, cantidadfrom, monedato, cantidadto, conversion, id FROM movimientos;')
    return render_template("movimientos.html", datos=ingresos, title="Todos los movimientos") 
    

@app.route('/nuevacompra', methods=['GET', 'POST'])
def transaccion():
    fecha=acciones.fecha()
    hora=acciones.hora()
    monedasDisponibles = acciones.busqueda('SELECT DISTINCT monedato FROM movimientos')
    resultado=["EUR"]
    for d in monedasDisponibles:
        resultado.extend(list(d.values()))
    conversion=10
    form = FormMovimientos()
    form.monedafrom.choices=resultado
    if request.method == 'POST': 
        if form.validate():
            acciones.busqueda ('INSERT INTO movimientos (fecha, hora, monedafrom, monedato, cantidadfrom, cantidadto, conversion) VALUES (?,?, ?, ?, ?,?,?);',
                    (
                        fecha,
                        hora,
                        form.monedafrom.data,
                        form.monedato.data,
                        form.cantidadfrom.data,
                        form.cantidadto.data,
                        conversion
                    )
            )

            return redirect(url_for('listadoMovimientos'))
        else:
            return render_template("alta.html", form=form) 
            

    return render_template("alta.html", form=form)