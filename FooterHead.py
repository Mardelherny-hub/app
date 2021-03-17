from tkinter import *
import sqlite3
from sqlite3 import *
from tkinter.font import BOLD
from Bd import *

#frame de encabezado dentro de pie
class FooterHead(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#ffffff")
        self.master = master
        self.pack(side=TOP, fill=BOTH)
        
        self.widget_head()
    

    def widget_head(self):
        conn = Bd()
        puntero = conn.cursor()
        puntero.execute("SELECT MAX(id_cotizacion), clientes.nombre, clientes.apellido, fecha, propiedades.calle, propiedades.numero, propiedades.piso, propiedades.depto, ciudades.ciudad FROM cotizaciones INNER JOIN clientes ON cotizaciones.id_cliente = clientes.id_cliente INNER JOIN propiedades ON cotizaciones.id_cliente = propiedades.id_cliente INNER JOIN ciudades ON propiedades.id_ciudad = ciudades.id_ciudad")
        conn.commit()

        rows = list(puntero)
        id_cotizacion = rows[0][0]
        nombre = rows[0][1]
        apellido = rows[0][2]
        fecha = rows[0][3]
        calle = rows[0][4]
        num = rows[0][5]
        piso = rows[0][6]
        depto = rows[0][7]
        ciudad = rows[0][8]
        

        self.head = Frame(self, bg="#00695C")
        self.head.pack(fill=BOTH)

        self.lblEncabezado = Label(self.head, text="COTIZACIÓN", pady=10, bg="#00695C", fg="#E0F2F1",font=BOLD)
        self.lblEncabezado.grid(row=0, column=0, columnspan=2)
        self.lblEncabezado = Label(self.head, text="Para: "+ nombre +" "+ apellido, padx=100, pady=15, bg="#00695C", fg="#E0F2F1", font=BOLD)
        self.lblEncabezado.grid(row=1, column=0, sticky=W)
        self.lblEncabezado = Label(self.head, text=fecha, padx=100, pady=15, bg="#00695C", fg="#E0F2F1")
        self.lblEncabezado.grid(row=1, column=1, sticky=W)
        self.lblEncabezado = Label(self.head, text="Propiedad: "+ calle +" "+ num+" |Piso: "+ piso+" |Depto: "+ depto+" | "+ ciudad, padx=100, pady=15, bg="#00695C", fg="#E0F2F1")
        self.lblEncabezado.grid(row=2, column=0, sticky=W, columnspan=2)
        
        

        