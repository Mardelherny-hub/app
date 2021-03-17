import sqlite3
from sqlite3 import *
from Bd import Bd

conn = Bd()
puntero = conn.cursor()

puntero.execute("SELECT distinct productos.id_producto, productos.nombre_prod, detalles.cant, detalles.precio FROM detalles INNER JOIN productos on productos.id_producto=detalles.id_producto  WHERE productos.comodato = 0 and detalles.id_cotizacion=54 order by productos.id_producto asc")
conn.commit()
producto = list(puntero) #listado de productos-------------------------

for item in producto:
    print (item)