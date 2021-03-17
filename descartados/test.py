from Bd import *

nombre = "eNombre"
apellido = "eApellido"
email = "v@h"
telefono = "eTelefono"
observ = "tObs.get"

datos = ((nombre, apellido,
email,telefono, observ),) 
#llamo a la bd
conn = sqlite3.connect("cotizador")
puntero = conn.cursor()


#puntero = Bd()
#puntero.execute("SELECT * from productos")

rows = puntero.fetchall

for item in datos:
    print (item)
cant = len(datos)
print (cant)
print (datos)

print ("*"*10)
puntero.execute("SELECT correo FROM clientes WHERE correo = 'email'")
clienta = list(puntero)
print (clienta)
cant = len(clienta)
print (cant)
print ("*"*10)
#for row in rows:
 #   print (row)
#print (rows)
puntero.executemany("INSERT INTO  clientes VALUES (NULL,?,?,?,?,?)", datos)
#conn.commit()

conn.close()