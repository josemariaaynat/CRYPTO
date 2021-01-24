from movements import app
import sqlite3
import time
import datetime

DBFILE = app.config['DBFILE'] 


def busqueda(query, params=()):
    conn = sqlite3.connect(DBFILE) 
    cursor = conn.cursor() 

    cursor.execute(query, params) 
    conn.commit()

    registros = cursor.fetchall()
    conn.close()
    listaDeDiccionarios=consulta(registros,cursor)
    return listaDeDiccionarios

def consulta(registros,cursor):
    if len(registros) == 0:
        return registros

    columnNames = []
    for columnName in cursor.description:
        columnNames.append(columnName[0])

    listaDeDiccionarios = []

    for fila in registros:
        d = {}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila[ix]
        listaDeDiccionarios.append(d)

    return listaDeDiccionarios

def hora():
    hora=time.strftime("%X")
    return hora

def fecha():
    fecha=datetime.date.today()
    return fecha
