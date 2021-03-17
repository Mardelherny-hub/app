from tkinter import *
import tkinter
from Aplicacion import *

class Salir(Tk):
    def __init__(self):
        self.salir()

    #metodo para destruir la ventana
    def salir(self):
        self.destroy()

class Cerrar(Toplevel):
    def __init__(self):
        self.salir()

    #metodo para destruir la ventana
    def salir(self):
        self.destroy()

class Nueva(Tk):
    def __init__(self):
        global root
        self.root =Tk()
        self.menu = hacermenu(self.root)
        self.root.title("Cotizador de sistemas de alarmas")
        self.root.geometry("780x550+50+50")
        self.main()
        self.root.mainloop()

    #Area principal para llenado de datos
    def main(self):
        self.main = Main(self.root)   