from datetime import datetime #para obtener la fecha de hoy
from datetime import date
from Bd import *

#Día actual
#today = date.today()

#Fecha actual
#now = datetime.now()

#print(today)
#print(now)
#####################################################################################

conn = Bd()
puntero = conn.cursor()

puntero.execute("SELECT MAX(id_cliente) FROM clientes")

rows = list(puntero)

for row in rows:
    id_nuevo_cliente = row[0] 

print (id_nuevo_cliente)