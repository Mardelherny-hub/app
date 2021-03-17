import sqlite3
from sqlite3 import *
from tkinter.font import BOLD
from Bd import *
from Botones import Cerrar
from tkinter import *

#frame contenedor
class Productos(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#B2DFDB")
        self.master = master
        self.pack(expand=TRUE, fill=Y)
        self.config(padx=5, pady=5, bg="#B2DFDB")
        self.titulo_widget()
        self.grilla_widget()
        self.update()
       

    
    def titulo_widget(self):
        self.frameTitulo = Frame(self, bg="#B2DFDB")
        self.frameTitulo.pack()
        self.frameTitulo.config(padx=10, pady=10)

        self.titulo = Label(self.frameTitulo, text="Agregar productos a la cotización", bg="#B2DFDB", fg="#000000", font=BOLD)
        self.titulo.pack(fill="both")

    def grilla_widget(self):
        self.frameEncabezados = Frame(self, bg="#B2DFDB")
        self.frameEncabezados.pack(side=TOP, fill=X)
        self.lblEncabezado = Label(self.frameEncabezados, text="Código", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
        self.lblEncabezado.grid(row=0, column=0, sticky=W)
        self.lblEncabezado = Label(self.frameEncabezados, text="Nombre", padx=90, pady=5, bg="#B2DFDB", fg="#000000")
        self.lblEncabezado.grid(row=0, column=1)        
        self.lblEncabezado = Label(self.frameEncabezados, text="Precio", padx=15, pady=5, bg="#B2DFDB", fg="#000000")
        self.lblEncabezado.grid(row=0, column=3)
        self.lblEncabezado = Label(self.frameEncabezados, text="Cantidad", padx=10, pady=5, bg="#B2DFDB", fg="#000000")
        self.lblEncabezado.grid(row=0, column=4)
        self.lblEncabezado = Label(self.frameEncabezados, text="", padx=75, pady=5, bg="#B2DFDB", fg="#000000")
        self.lblEncabezado.grid(row=0, column=5, columnspan=3)

        self.frameGrilla = Frame(self, bg="#f1f1f1", borderwidth=2, relief=RAISED)
        self.frameGrilla.pack(expand=TRUE, fill=Y, side=LEFT)
        self.frameGrilla.config(padx=10, pady=10)   

        #listado de productos---------------------------------------------------------------------------------------------------
        
        self.conn =Bd()
        self.puntero = self.conn.cursor()
        self.puntero.execute("SELECT id_producto, nombre_prod FROM productos WHERE comodato = 0 ORDER BY id_producto ASC")
        self.conn.commit()
        self.producto = list(self.puntero)
        self.filas = len(self.producto)
        self.columnas = len(self.producto[0])

        #listado de productos agregados al carrito
        #busco la última cotización
        self.puntero.execute("SELECT MAX(id_cotizacion) FROM cotizaciones")
        self.conn.commit()
        self.cotizacion = list(self.puntero)
        self.id_cotizacion = self.cotizacion[0][0]

        #detalle de la última cotización---------------------------------------------------------------------------------------------------
        self.puntero.execute("SELECT id_producto, precio, cant FROM detalles WHERE id_cotizacion = '"+str(self.id_cotizacion)+"'")
        self.conn.commit()
        self.detalle = list(self.puntero) 
        self.fil_detalle = len(self.detalle)
        self.col_detalle = len(self.detalle[0])        
       
        for i in range(self.filas):
            for j in range(self.columnas):
                self.celda = Frame(self.frameGrilla, bg='#f1f1f1')
                self.celda.grid(row=i, column=j, padx=5, pady=5)
                self.lbl_celda = Label(self.celda, text=self.producto[i][j], fg="#000000", bg="#f1f1f1")
                self.lbl_celda.grid(row=i, column=j)
                
        
        for i in range(self.filas):
            for j in range(self.fil_detalle):
                celda = Frame(self.frameGrilla, bg='#f1f1f1')
                celda.grid(row=i, column=3, padx=5, pady=5)
                if self.producto[i][0]==self.detalle[j][0]:
                    lbl_celda = Label(celda, text=self.detalle[j][1], fg="#000000", bg="#f1f1f1")               
                    lbl_celda.grid(row=i, column=3)

        for i in range(self.filas):
            for j in range(self.fil_detalle):
                celda = Frame(self.frameGrilla, bg='#f1f1f1')
                celda.grid(row=i, column=4, padx=5, pady=5)
                if self.producto[i][0]==self.detalle[j][0]:
                    lbl_celda = Label(celda, text=self.detalle[j][2], fg="#000000", bg="#f1f1f1")               
                    lbl_celda.grid(row=i, column=4)
               
        
        #grilla continuación con los botones----------------------------------------------------------------------------------------------------
        for i in range(self.filas):            
            for j in range(self.fil_detalle):
                self.celdaBoton = Frame(self.frameGrilla, borderwidth=2, relief=RAISED , bg="#f1f1f1", padx=5)
                self.celdaBoton.grid(row=i, column=6, padx=5)                
                #si tiene cargado hago un update
                if self.producto[i][0]==self.detalle[j][0]:
                    print (self.detalle[j][2])
                    self.cant = self.detalle[j][2]
                    self.cant = IntVar
                    self.eCeldaBoton = Entry(self.celdaBoton, width=3, bg="#f1f1f1", fg="#000000", textvariable=self.cant)                    
                    self.eCeldaBoton.grid(sticky=W, column=0, row=0, padx=10)
                    self.id_detalle = self.detalle[j][0]
                    
                    self.bBotonAgregar = Button(self.celdaBoton, text="Agregar", bg="#000000", fg="#ffffff", padx=5, cursor="hand2", command=self.update)
                    self.bBotonAgregar.grid(sticky=E, column=1, row=0, padx=10)
                    self.bBotonRetirar = Button(self.celdaBoton, text="Retirar", bg="#FFE57F", fg="#000000", padx=5, cursor="hand2")
                    self.bBotonRetirar.grid(sticky=E, column=2, row=0, padx=10)
            #si no tiene cargado hago un insert
            
            self.eCeldaBoton = Entry(self.celdaBoton, width=3, bg="#f1f1f1", fg="#000000")
            self.eCeldaBoton.grid(sticky=W, column=0, row=0, padx=10)
            self.id_producto =self. producto[i][0]
            #print ("producto: " + str(self.id_producto)+ " " + str(j) )
            self.bBotonAgregar = Button(self.celdaBoton, text="Agregar", bg="#009688", fg="#ffffff", padx=5, cursor="hand2")
            self.bBotonAgregar.grid(sticky=E, column=1, row=0, padx=10)
            self.bBotonRetirar = Button(self.celdaBoton, text="Retirar", bg="#FFE57F", fg="#000000", padx=5, cursor="hand2")
            self.bBotonRetirar.grid(sticky=E, column=2, row=0, padx=10)
            
    def update(self):
        #busco el articulo a sumar y su cantidad
        self.conn =Bd()
        self.puntero = self.conn.cursor()        
        self.puntero.execute("SELECT cant FROM detalles WHERE id_cotizacion = '"+str(self.id_cotizacion)+"' AND '"+str(self.id_producto)+"' = '"+str(self.id_producto)+"'")
        self.conn.commit()
        self.row = list(self.puntero)
        self.agregar = self.eCeldaBoton.get()
        self.cant = self.row[0][0]
        print (self.agregar)
        '''
        self.suma = self.cant + self.agregar
        self.puntero.execute("UPDATE detalles SET cant = '"+str(self.suma)+"' WHERE '"+str(self.id_producto)+"' = '"+str(self.id_producto)+"'")
        self.conn.commit()
        self.conn.close() 
        '''
    

                        