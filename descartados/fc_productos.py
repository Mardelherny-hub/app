import sqlite3
from sqlite3 import *
from Bd import *

def update(id_cotizacion, id_producto, cantidad):
    #busco el articulo a sumar
    conn =Bd()
    puntero = conn.cursor()
    
    puntero.execute("SELECT cant FROM detalles WHERE id_cotizacion = '"+str(id_cotizacion)+"' AND id_producto = '"+str(id_producto)+"'")
    conn.commit()
    row = list(puntero)
    cant = row[0][0]
    print (cant)
    suma = cant + cantidad
    puntero.execute("UPDATE detalles SET cant = '"+suma+"' WHERE id_producto = '"+id_producto+"'")
    conn.commit()