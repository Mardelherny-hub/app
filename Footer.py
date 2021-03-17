from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from FooterGrilla import FooterGrilla
from FooterEncabezado import *
from FooterHead import FooterHead

#frame footer dentro de root
class Footer(Toplevel):
    def __init__(self, master=None):
        super().__init__(master, bg="#ffffff")
        self.title("COTIZACIÓN")
        self.geometry("700x600+50+50")
        self.frameHead = FooterHead(self)
        self.frameEncabezado = FooterEncabezado(self)
        self.frameGrilla = FooterGrilla(self)
        
        self.grab_set()

        self.transient(master=self)