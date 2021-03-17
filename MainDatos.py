from DatosPropCaracteristicas import *
from DatosPropiedad import *
from DatosCliente import *

#frame para formularios dentro de main
class MainDatos(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=LEFT)
        self.config(padx=10 , pady=10, bg="#B2DFDB", relief=RAISED, borderwidth=2)
        self.widget_cliente()
        self.widget_Propiedad()
        

    def widget_cliente(self):
        self.frameCliente = Cliente(self)

    def widget_Propiedad(self):
        self.framePropiedad = Propiedad(self)
