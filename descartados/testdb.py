import sqlite3
from sqlite3 import *
from Bd import *

conn = Bd()
puntero = conn.cursor()
id_producto = 8
puntero.execute("SELECT max(id_cotizacion) FROM cotizaciones")
conn.commit()
max = list(puntero)
max_cot = max[0][0]
print (max_cot)
puntero.execute("SELECT cant FROM detalles WHERE id_cotizacion = '"+str(max_cot)+"' AND id_producto = '"+str(id_producto)+"'")
conn.commit()
row = list(puntero)
cant = row[0][0]
print (cant)
suma = cant + 2
puntero.execute("UPDATE detalles SET cant = '"+str(suma)+"' WHERE id_producto = '"+str(id_producto)+"'")
conn.commit()