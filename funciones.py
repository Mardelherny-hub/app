from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from base import *

#comandos para botones
def salir():    
    a = messagebox.askyesno(title="Cerrar", message="Confirma salir de la aplicación?")
    if a == TRUE:
        root.destroy()