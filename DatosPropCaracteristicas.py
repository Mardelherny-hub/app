from tkinter import *
from tkinter.ttk import Combobox

#frame para caracteristicas de la propiedad dentro de formularios
class PropCaracteristicas(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH)
        self.config(padx=10 , pady=15, bg="#B2DFDB", relief=RAISED, borderwidth=1)
        self.widget_caracteristicas()
        
    def widget_caracteristicas(self):
        self.telProp = IntVar()
        self.telProp.set(1)

        self.lTelefonoP = Label(self, text="Teléfono", bg="#B2DFDB", fg="#000000")
        self.lTelefonoP.grid(column=0, row=0, rowspan=2, padx=10, pady=10)

        self.checkTel1 = Radiobutton(self, text="Fijo", value=1, variable=self.telProp, bg="#B2DFDB", fg="#000000")
        self.checkTel1.grid(column=1, row=0, padx=10, pady=10)

        self.checkTel2 = Radiobutton(self, text="Móvil", value=2, variable=self.telProp, bg="#B2DFDB", fg="#000000")
        self.checkTel2.grid(column=1, row=1, padx=10, pady=10)

        self.lAmbientes = Label(self, text="Ambientes", bg="#B2DFDB", fg="#000000")
        self.lAmbientes.grid(column=3, row=0, rowspan=2, padx=10, pady=10)

        self.eAmbientes = Entry(self, bg="#e0f2f1", fg="#000000")
        self.eAmbientes.grid(column=4,row=0, rowspan=2, padx=10, pady=10)
        self.eAmbientes.config(width=3)

        self.lAberturas = Label(self, text="Abertutas", bg="#B2DFDB", fg="#000000")
        self.lAberturas.grid(column=5, row=0, rowspan=2, padx=10, pady=10, sticky=W)

        self.eAberturas = Entry(self, bg="#e0f2f1", fg="#000000")
        self.eAberturas.grid(column=6,row=0, rowspan=2, padx=10, pady=10, sticky=W)
        self.eAberturas.config(width=3)