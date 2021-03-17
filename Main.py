from MainTitulo import *
from MainDatos import *


#frame contenedor
class Main(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=TRUE)
        self.titulo_widget()
        self.datos_widget()       

    def titulo_widget(self):
        self.frameTitulo = MainTitulo(self)

    def datos_widget(self):
        self.frameDatos = MainDatos(self)