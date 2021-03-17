from tkinter import *
from tkinter import messagebox
from ProductosAgregar import *
from Botones import *

#frame para botones dentro del main
class MainBotonera(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=LEFT, fill=BOTH)
        self.config(padx=10 , pady=10, bg="#B2DFDB", relief=RAISED, borderwidth=2, width=465, height=80)
        self.widget_botonera()
        
        
    def widget_botonera(self):
        
        self.bCerrar = Button(self, text="Cerrar", bg="#FFE57F", fg="#000000", cursor="hand2", command=Salir)
        self.bCerrar.place(x=10, y=5, width=100, height=50)

        self.bAgregar = Button(self, text="Agregar\nProductos", cursor="hand2", command=ProductosAgregar)
        self.bAgregar.place(x=170, y=5, width=100, height=50)
        self.bAgregar.config(bg="#009688", fg="#ffffff")

        self.bPresupuesto = Button(self, text="Cotizar", cursor="hand2")
        self.bPresupuesto.place(x=330, y=5, width=100, height=50)
        self.bPresupuesto.config(bg="#ff6f00", fg="#ffffff")