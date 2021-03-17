from tkinter import *
from tkinter.font import BOLD

#frame de encabezado dentro de main
class MainTitulo(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=TOP)
        #self.config(padx=10 , pady=10)
        self.widget()

    def widget(self):
        self.frameTitulo = Frame(self, width="750", bg="#e0f2f1")
        self.frameTitulo.pack(side=TOP)
        self.frameTitulo.config(padx=10, pady=10)

        self.titulo = Label(self, text="Cotizador de sistemas de Alarma", bg="#e0f2f1", fg="#000000", font=BOLD)
        self.titulo.pack(fill="both")