from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Productos import *

class ProductosAgregar(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.title("Agregar Productos")
        self.geometry("700x780+50+50")
        self.frameProductos = Productos(self)
        #deshabilitar la otra ventana
        self.grab_set()
        #ventana tipo modal
        self.transient(master=self)