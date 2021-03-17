from tkinter import *
import sqlite3
from sqlite3 import *
from tkinter.font import BOLD
from Bd import *

#frame para grilla dentro de pie
class FooterGrilla(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f1f1f1", borderwidth=2, relief=RAISED)
        self.master = master
        self.pack(fill=BOTH)
        self.config(padx=10, pady=10)

        self.widget()

    def widget(self):        
        #busco la última cotización cargada
        conn = Bd()
        puntero = conn.cursor()
        puntero.execute("SELECT MAX(id_cotizacion), id_cliente FROM cotizaciones")
        conn.commit()

        rows = list(puntero)
        id_cotizacion = rows[0][0]
        id_cliente = rows[0][1]

        #cargo el detalle correspondiente
        puntero.execute("SELECT detalles.id_producto, detalles.id_producto, productos.nombre_prod, productos.descripcion_prod, productos.precio, detalles.id_cotizacion, detalles.cant FROM detalles INNER JOIN productos on detalles.id_producto = productos.id_producto WHERE id_cotizacion = '"+str(id_cotizacion)+"'")
        conn.commit()
        rows = list(puntero)

        #cantidad de productos en la cotización         
        cantProd = len(rows)
        cantItem = len(rows[0])
         
        #grilla para el listados de productos
        for i in range(cantProd):
            for j in range(cantItem):
                if j%2==0:        
                    celda = Frame(self, bg='#f1f1f1')
                    celda.grid(row=i, column=j, padx=5, pady=5)
                    lbl_celda = Label(celda, text=rows[i][j], fg="#000000", bg="#f1f1f1")
                    if j==4:
                        lbl_celda = Label(celda, text="$ "+str(rows[i][j])+",00", fg="#000000", bg="#f1f1f1")
                        lbl_celda.grid(padx=5, sticky=E)
                    else:
                        lbl_celda = Label(celda, text=rows[i][j], fg="#000000", bg="#f1f1f1")
                        lbl_celda.grid(padx=5, sticky=W)

        #grilla para los parciales
        total = 0
        for i in range(cantProd):
            for j in range(cantItem):
                if j%2==0:        
                    celda = Frame(self, bg='#f1f1f1')
                    celda.grid(row=i, column=8, padx=5, pady=5) 
                    precio = rows[i][4]  
                    cant = rows[i][6]
                    parcial = cant * precio               
                    lbl_celda = Label(celda, text="$ "+str(parcial)+",00", fg="#000000", bg="#f1f1f1")
                    lbl_celda.grid(padx=60, sticky=E)
            total = total + parcial
        print (total) 

        #fila para el total
        self.celdaTotal = Frame(self, bg="#00695C", width=700)
        self.celdaTotal.grid(row=i+1, column=0, padx=5, pady=5, columnspan=5, sticky=E)       
        self.lTitulo = Label(self.celdaTotal, text="Total Cotización", pady=5, bg="#00695C", fg="#E0F2F1", font=BOLD, width=35)
        self.lTitulo.grid(row=0,column=0, ipadx=10, ipady=10)       
        self.lTotal = Label(self.celdaTotal, text="$ "+str(total)+",00", pady=5, bg="#00695C", fg="#E0F2F1", font=BOLD)
        self.lTotal.grid(row=0,column=1, ipadx=10, ipady=10)
