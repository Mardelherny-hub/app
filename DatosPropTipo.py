from tkinter import *


#frame para tipos de propiedades dentro de formularios
class PropTipo(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH)
        self.config(padx=10 , pady=25, bg="#B2DFDB", relief=RAISED, borderwidth=1, width="450")
        self.widget_tipo()
        
    def widget_tipo(self):
        self.tipo = IntVar()
        self.tipo.set(1)
        self.casa = Radiobutton(self, text="Casa", value=1, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.depto = Radiobutton(self, text="Depto.", value=2, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.local = Radiobutton(self, text="Local", value=3, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.oficina = Radiobutton(self, text="Oficina", value=4, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.deposito = Radiobutton(self, text="Depósito", value=5, variable=self.tipo, bg="#B2DFDB", fg="#000000")

        self.casa.grid(column=0, row=1, padx=5, pady=5, sticky=W)
        self.depto.grid(column=1, row=1, padx=5, pady=5, sticky=W)
        self.local.grid(column=2, row=1, padx=5, pady=5, sticky=W)
        self.oficina.grid(column=3, row=1, padx=5, pady=5, sticky=W)
        self.deposito.grid(column=4, row=1, padx=5, pady=5, sticky=W)
