from Botones import Salir
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Main import *
#from Footer import *
from fcMenu import hacermenu
import sys

class Aplicacion:
    def __init__(self):
        global root
        self.root =tk.Tk()
        self.menu = hacermenu(self.root)
        self.root.title("Cotizador de sistemas de alarmas")
        self.root.geometry("780x550+50+50")
        self.main()
        self.root.mainloop()
        self.salir

    #Area principal para llenado de datos
    def main(self):
        self.main = Main(self.root)    
    
    def salir(self):
        self.root.destroy()