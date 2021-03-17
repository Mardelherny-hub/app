from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
#from funciones import *
from fcMenu import hacermenu

root =Tk()

hacermenu(root)

root.title("Cotizador de sistemas de alarmas")
root.geometry("900x800+50+50")

#frame contenedor
frameMain = Frame(root)
frameMain.pack(expand=True)
frameMain.config(padx=5, pady=5, bg="#e0f2f1")

#frame de encabezado dentro de main
frameTitulo = Frame(frameMain, width="800", bg="#e0f2f1")
frameTitulo.pack(side="top")
frameTitulo.config(padx=10, pady=10)

titulo = Label(frameTitulo, text="Cotizador de sistemas de Alarma", bg="#e0f2f1", fg="#000000")
titulo.pack(fill="both")

#frame para formularios dentro de main
frameDatos = Frame(frameMain, width="650", bg="#B2DFDB")
frameDatos.pack(side="left")
frameDatos.config(padx=10, pady=10)

#frame para datos de cliente dentro de formularios
frameCliente = Frame(frameDatos, width="200")
frameCliente.pack(side="left")
frameCliente.config(padx=5, pady=5, bg="#B2DFDB", relief=RAISED, borderwidth=1)

lTituloCliente = Label(frameCliente, text="Datos del Cliente", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lTituloCliente.grid(column=0, row=0, columnspan="2")

lNombre = Label(frameCliente, text="Nombre", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
lNombre.grid(column=0, row=1)
eNombre = Entry(frameCliente, bg="#e0f2f1", fg="#000000")
eNombre.grid(column=1, row=1, padx=5, pady=5)

lApellido = Label(frameCliente, text="Apellido", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
lApellido.grid(column=0, row=2)
eApellido = Entry(frameCliente, bg="#e0f2f1", fg="#000000")
eApellido.grid(column=1, row=2, padx=5, pady=5)

lEmail = Label(frameCliente, text="Email", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
lEmail.grid(column=0, row=3, sticky="e")
eEmail = Entry(frameCliente, bg="#e0f2f1", fg="#000000")
eEmail.grid(column=1, row=3, padx=5, pady=5)

lTelefono = Label(frameCliente, text="Telefono", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
lTelefono.grid(column=0, row=4)
eTelefono = Entry(frameCliente, bg="#e0f2f1", fg="#000000")
eTelefono.grid(column=1, row=4, padx=5, pady=5)

lTituloObs= Label(frameCliente, text="Observaciones", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lTituloObs.grid(column=0, row=5, columnspan="2")

tObs = Text(frameCliente, width=27, height=6)
tObs.grid(column=0, row=6, columnspan=2)
tObs.config(padx=5, pady=5, bg="#e0f2f1", fg="#000000")

#frame para datos de la propiedad dentro de formularios
framePropiedad = Frame(frameDatos, width="450", bg="#B2DFDB")
framePropiedad.pack(fill="y")
framePropiedad.config(padx=10, pady=5, relief=RAISED, borderwidth=1)

tituloPropiedad = Label(framePropiedad, text="Datos de la propiedad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
tituloPropiedad.grid(column=0, row=0, columnspan=10)

lCalle = Label(framePropiedad, text="Calle", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lCalle.grid(column=0, row=1)
eCalle = Entry(framePropiedad, bg="#e0f2f1", fg="#000000")
eCalle.grid(column=1, row=1, padx=5, pady=15)

lNum = Label(framePropiedad, text="Nª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lNum.grid(column=2, row=1)
eNum = Entry(framePropiedad, bg="#e0f2f1", fg="#000000")
eNum.grid(column=3, row=1, padx=5, pady=15)
eNum.config(width=5)

lPiso = Label(framePropiedad, text="Pª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lPiso.grid(column=4, row=1)
ePiso = Entry(framePropiedad, bg="#e0f2f1", fg="#000000")
ePiso.grid(column=5, row=1, padx=5, pady=15)
ePiso.config(width=2)

lDto = Label(framePropiedad, text="Dª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lDto.grid(column=6, row=1)
eDto = Entry(framePropiedad, bg="#e0f2f1", fg="#000000")
eDto.grid(column=7, row=1, padx=5, pady=15)
eDto.config(width=2)

lCdad = Label(framePropiedad, text="Ciudad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
lCdad.grid(column=0, row=2)

ciudades = ('Mar del Plata', 'Batan', 'Santa Clara', 'Miramar', 'Necochea')

eCdad = Combobox(framePropiedad, state='readonly', values=ciudades)
eCdad.current(0)
eCdad.grid(column=1, row=2, padx=5, pady=15)
eCdad.config(foreground="#e0f2f1", background="#e0f2f1")


#frame para tipo de propiedad

frameTipo = Frame(frameDatos)
frameTipo.pack(fill="both")
frameTipo.config(padx=10, pady=25, bg="#B2DFDB", relief=RAISED, borderwidth=1)

tipo = IntVar()
tipo.set(1)
casa = Radiobutton(frameTipo, text="Casa", value=1, variable=tipo, bg="#B2DFDB", fg="#000000")
depto = Radiobutton(frameTipo, text="Depto.", value=2, variable=tipo, bg="#B2DFDB", fg="#000000")
local = Radiobutton(frameTipo, text="Local", value=3, variable=tipo, bg="#B2DFDB", fg="#000000")
oficina = Radiobutton(frameTipo, text="Oficina", value=4, variable=tipo, bg="#B2DFDB", fg="#000000")
deposito = Radiobutton(frameTipo, text="Depósito", value=5, variable=tipo, bg="#B2DFDB", fg="#000000")

casa.grid(column=0, row=1, padx=5, pady=5, sticky=W)
depto.grid(column=1, row=1, padx=5, pady=5, sticky=W)
local.grid(column=2, row=1, padx=5, pady=5, sticky=W)
oficina.grid(column=3, row=1, padx=5, pady=5, sticky=W)
deposito.grid(column=4, row=1, padx=5, pady=5, sticky=W)

#frame para caracteŕisticas de la propiedad dentro del frame formularios

frameCaracteristicas = Frame(frameDatos, bg="#B2DFDB")
frameCaracteristicas.pack(fill="both")
frameCaracteristicas.config(padx=10, pady=15, relief=RAISED, borderwidth=1)

telProp = IntVar()
telProp.set(1)

lTelefonoP = Label(frameCaracteristicas, text="Teléfono", bg="#B2DFDB", fg="#000000")
lTelefonoP.grid(column=0, row=0, rowspan=2, padx=10, pady=10)

checkTel1 = Radiobutton(frameCaracteristicas, text="Fijo", value=1, variable=telProp, bg="#B2DFDB", fg="#000000")
checkTel1.grid(column=1, row=0, padx=10, pady=10)

checkTel2 = Radiobutton(frameCaracteristicas, text="Móvil", value=2, variable=telProp, bg="#B2DFDB", fg="#000000")
checkTel2.grid(column=1, row=1, padx=10, pady=10)

lAmbientes = Label(frameCaracteristicas, text="Ambientes", bg="#B2DFDB", fg="#000000")
lAmbientes.grid(column=3, row=0, rowspan=2, padx=10, pady=10)

eAmbientes = Entry(frameCaracteristicas, bg="#e0f2f1", fg="#000000")
eAmbientes.grid(column=4,row=0, rowspan=2, padx=10, pady=10)
eAmbientes.config(width=3)

lAberturas = Label(frameCaracteristicas, text="Abertutas", bg="#B2DFDB", fg="#000000")
lAberturas.grid(column=5, row=0, rowspan=2, padx=10, pady=10, sticky=W)

eAberturas = Entry(frameCaracteristicas, bg="#e0f2f1", fg="#000000")
eAberturas.grid(column=6,row=0, rowspan=2, padx=10, pady=10, sticky=W)
eAberturas.config(width=3)


#acciones para los botones          ************************************************************************************************************************************

def salir():    
    a = messagebox.askokcancel(title="Cerrar", message="Confirma salir de la aplicación?")
    if a == TRUE:
        root.destroy()

#frame para botones dentro del main ************************************************************************************************************************************
frameBotones = Frame(frameDatos, bg="#e0f2f1", relief=RAISED, borderwidth=1, width=465)
frameBotones.pack(fill=BOTH, side=LEFT)
frameBotones.config(padx=10, pady=10, height=80)

bCerrar = Button(frameBotones, text="Cerrar", bg="#FFE57F", fg="#000000", cursor="hand2", command=salir)
bCerrar.place(x=5, y=10, width=100, height=25)

bAgregar = Button(frameBotones, text="Agregar\nProductos", cursor="hand2")
bAgregar.place(x=125, y=10, width=100, height=50)
bAgregar.config(bg="#009688", fg="#ffffff")

bPresupuesto = Button(frameBotones, text="Cotizar", cursor="hand2")
bPresupuesto.place(x=375, y=10, width=100, height=50)
bPresupuesto.config(bg="#ff6f00", fg="#ffffff")

#frame para pie dentro de root

framePie = Frame(root, bg="#e0f2f1")
framePie.pack(side="bottom", expand=True, fill=Y)
framePie.config(padx=5, pady=5)

#frame de encabezado dentro de pie
frameTituloPie = Frame(framePie, bg="#e0f2f1")
frameTituloPie.pack()
frameTituloPie.config(padx=10, pady=10)

tituloPie = Label(frameTituloPie, text="COTIZACIÓN", bg="#e0f2f1", fg="#000000")
tituloPie.pack(fill="both")

#frame para grilla dentro de pie

frameEncabezados = Frame(framePie, bg="#f1f1f1")
frameEncabezados.pack(side=TOP)
lblEncabezado = Label(frameEncabezados, text="Código", pady=5,
                    bg="#ffffff", fg="#000000")
lblEncabezado.grid(row=0, column=0, sticky=W)
lblEncabezado = Label(frameEncabezados, text="Nombre", padx=10, pady=5, 
                    bg="#ffffff", fg="#000000")
lblEncabezado.grid(row=0, column=1)
lblEncabezado = Label(frameEncabezados, text="Descripción", padx=10, pady=5, 
                    bg="#ffffff", fg="#000000")
lblEncabezado.grid(row=0, column=2)
lblEncabezado = Label(frameEncabezados, text="Precio", padx=5, pady=5, 
                    bg="#ffffff", fg="#000000")
lblEncabezado.grid(row=0, column=3)
lblEncabezado = Label(frameEncabezados, text="Cantidad", padx=10, pady=5, 
                    bg="#ffffff", fg="#000000")
lblEncabezado.grid(row=0, column=4)
lblEncabezado = Label(frameEncabezados, text="Total", padx=80, pady=5, 
                    bg="yellow", fg="#000000", relief=RAISED, borderwidth=2)
lblEncabezado.grid(row=0, column=5, columnspan=3)

frameGrilla = Frame(framePie, bg="#f1f1f1", borderwidth=2, relief=RAISED)
frameGrilla.pack(expand=TRUE, fill=Y, side=LEFT)
frameGrilla.config(padx=10, pady=10)

#detalle de la cotización
    #código(1) | nombre(2) | descripcion(3) | precio(4) | cantidad(5) | total item(6)
productos = (1,"artículo 1","descripcion 1",100,2,
      2,"artículo 2","descripcion 2",200,1,
      3,"artículo 3","descripcion 3",300,12,
      5,"artículo 5","descripcion 5",500,6
    )

#cantidades          
cantProd = int(len(productos))

cant = int(cantProd/5) #obtengo la cantidad de productos de la lista 

#grilla para el listados de productos
k = 0
for i in range(cant):
    j = 0    
    while j < 5:              
        for item in productos:        
            celda = Frame(frameGrilla, bg='#f1f1f1')
            celda.grid(row=i, column=j, padx=5, pady=5)
            lbl_celda = Label(celda, text=productos[k], fg="#000000", bg="#f1f1f1")
            lbl_celda.grid()
        j = j + 1
        k = k + 1   
#grilla continuación con los totales productos[4]*productos[5]
'''
k = 0
for j in range(cantProd):
    if j%4 == 0:        
        for i in range(cantDet):
            if i%2 == 0:
                celda = Frame(frameGrilla, bg='#f1f1f1', padx=5)
                celda.grid(row=k, column=5, padx=5, pady=5)
                if productos[j]==detalle[i]:                    
                    lbl_celda = Label(celda, text=detalle[i+1], fg="#000000", bg="#f1f1f1",
                                     relief=RAISED, borderwidth=1, padx=5, pady=7, width=4)
                lbl_celda.grid()
        k = k + 1
'''
#grilla continuación con los botones
for i in range(cant):
    j = 0    
    while j < 4:              
        for item in productos:        
            celdaBoton = Frame(frameGrilla, borderwidth=2, relief=RAISED , bg="#f1f1f1",
                                 padx=5)
            celdaBoton.grid(row=i, column=6, padx=5)
            eCeldaBoton = Entry(celdaBoton, width=3, bg="#f1f1f1", fg="#000000")
            eCeldaBoton.grid(sticky=W, column=0, row=0, padx=10)
            bBotonAgregar = Button(celdaBoton, text="Agregar", bg="green", fg="#ffffff",
                                 padx=5, cursor="hand2")
            bBotonAgregar.grid(sticky=E, column=1, row=0, padx=10)
            bBotonRetirar = Button(celdaBoton, text="Retirar", bg="red", fg="#ffffff",
                                 padx=5, cursor="hand2")
            bBotonRetirar.grid(sticky=E, column=2, row=0, padx=10)
        j = j + 1
         

root.mainloop()