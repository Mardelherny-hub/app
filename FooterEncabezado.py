from tkinter import *


#frame de encabezado dentro de pie
class FooterEncabezado(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f1f1f1")
        self.master = master
        self.pack(side=TOP, fill=BOTH)
        self.widget()

    def widget(self):
        self.lblEncabezado = Label(self, text="Código", padx=10, pady=5,
                    bg="#ffffff", fg="#000000")
        self.lblEncabezado.grid(row=0, column=0, sticky=W)
        self.lblEncabezado = Label(self, text="Nombre", padx=100, pady=5, 
                            bg="#ffffff", fg="#000000")
        self.lblEncabezado.grid(row=0, column=1)
        self.lblEncabezado = Label(self, text="Precio", padx=50, pady=5, 
                            bg="#ffffff", fg="#000000")
        self.lblEncabezado.grid(row=0, column=2)
        self.lblEncabezado = Label(self, text="Cantidad", padx=25, pady=5, 
                            bg="#ffffff", fg="#000000")
        self.lblEncabezado.grid(row=0, column=3)
        self.lblEncabezado = Label(self, text="Total", padx=40, pady=5, 
                            bg="yellow", fg="#000000", relief=RAISED, borderwidth=2)
        self.lblEncabezado.grid(row=0, column=4, columnspan=3)