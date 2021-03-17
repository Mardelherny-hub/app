import sqlite3
from sqlite3 import *


def Bd():
    try:
        conn = sqlite3.connect("cotizador")  
        
        print ("Conectado!")
        
        return (conn)

    except:
        print ("Error en la conexión")