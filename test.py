import sqlite3
from sqlite3 import *
from typing import final
from Bd import *

#listado de productos---------------------------------------------------------------------------------------------------
        
conn =Bd()
puntero = conn.cursor()
puntero.execute("SELECT id_producto, nombre_prod FROM productos WHERE comodato = 0 ORDER BY id_producto ASC")
conn.commit()
producto = list(puntero)
filas = len(producto)
columnas = len(producto[0])

#print (producto)

#listado de productos agregados al carrito
#busco la última cotización
puntero.execute("SELECT MAX(id_cotizacion) FROM cotizaciones")
conn.commit()
cotizacion = list(puntero)
id_cotizacion = cotizacion[0][0]

#detalle de la última cotización---------------------------------------------------------------------------------------------------
puntero.execute("SELECT id_producto, precio, cant FROM detalles WHERE id_cotizacion = '"+str(id_cotizacion)+"'")
conn.commit()
detalle = list(puntero) 
fil_detalle = len(detalle)
col_detalle = len(detalle[0])  

#print (detalle)
completa = []
for i in producto:
    for j in detalle:
        #print("producto :"+ str(i) + "detalle: " + str(j) )
        if i[0]==j[0]:
            completa.append((i[0],i[1],j[1],j[2]))
        else:
            completa.append((i[0],i[1]))

conj = set(completa)
finall = list(conj)
for item in finall:
    print (item)