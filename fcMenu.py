from tkinter import *
from Botones import *


def hacermenu(ventana):
    barraMenu = Menu(ventana)
    ventana.config(menu=barraMenu,padx=20,pady=20)
    ventana.geometry("580x400")
    ventana.title('Cotizador de Sistema de Alarma | Datos del Cliente')

    archivoMenu=Menu(barraMenu,tearoff=0)
    archivoMenu.add_command(label="Nuevo Presupuesto")    
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Productos")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Salir", command=Salir)

    editarMenu=Menu(barraMenu,tearoff=0)
    editarMenu.add_command(label="Buscar Cliente")
    editarMenu.add_command(label="Buscar Presupueto")

    verMenu=Menu(barraMenu,tearoff=0)
    verMenu.add_command(label="Listado de clientes")
    verMenu.add_command(label="Listado de Presupuestos")
    verMenu.add_command(label="Listado de Productos")

    ayudaMenu=Menu(barraMenu,tearoff=0)
    ayudaMenu.add_command(label="Ayuda F1")
    ayudaMenu.add_command(label="Acerca de ...")

    barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
    barraMenu.add_cascade(label="Edición", menu=editarMenu)
    barraMenu.add_cascade(label="Ver", menu=verMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
