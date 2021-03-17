from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
from sqlite3 import *
from Bd import Bd

#frame para datos de la propiedad dentro de formularios
class PropUbicacion(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=Y)
        self.config(padx=10 , pady=5, bg="#B2DFDB", relief=RAISED, borderwidth=1, width="450")
        self.widget_ubicacion()
        
    def widget_ubicacion(self):
        self.tituloPropiedad = Label(self, text="Datos de la propiedad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.tituloPropiedad.grid(column=0, row=0, columnspan=10)

        self.lCalle = Label(self, text="Calle", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lCalle.grid(column=0, row=1)
        self.eCalle = Entry(self, bg="#e0f2f1", fg="#000000")
        self.eCalle.grid(column=1, row=1, padx=5, pady=15)

        self.lNum = Label(self, text="Nª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lNum.grid(column=2, row=1)
        self.eNum = Entry(self, bg="#e0f2f1", fg="#000000")
        self.eNum.grid(column=3, row=1, padx=5, pady=15)
        self.eNum.config(width=5)

        self.lPiso = Label(self, text="Pª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lPiso.grid(column=4, row=1)
        self.ePiso = Entry(self, bg="#e0f2f1", fg="#000000")
        self.ePiso.grid(column=5, row=1, padx=5, pady=15)
        self.ePiso.config(width=2)

        self.lDto = Label(self, text="Dª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lDto.grid(column=6, row=1)
        self.eDto = Entry(self, bg="#e0f2f1", fg="#000000")
        self.eDto.grid(column=7, row=1, padx=5, pady=15)
        self.eDto.config(width=2)

        self.lCdad = Label(self, text="Ciudad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lCdad.grid(column=0, row=2)

        #obtengo las ciudades de bd
        self.conn = Bd()
        self.puntero = self.conn.cursor()
        self.puntero.execute("SELECT * FROM ciudades")
        self.ciudades = self.puntero.fetchall()
        

        #self.ciudades = ('Mar del Plata', 'Batan', 'Santa Clara', 'Miramar', 'Necochea')

        self.eCdad = Combobox(self, state='readonly', values=self.ciudades)
        self.eCdad.current(0)
        self.eCdad.grid(column=1, row=2, padx=5, pady=15)
        self.eCdad.config(background="#B2DFDB", foreground="#000000")
   
        