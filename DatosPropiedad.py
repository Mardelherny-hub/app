from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
from sqlite3 import *
from Bd import Bd
from ProductosAgregar import *
from Footer import *
from DatosCliente import Cliente

#frame para datos de la propiedad dentro de formularios
class Propiedad(Frame):
    #--------------------------------------------------------------------------------------------
    
    cont = 0
    
    #--------------------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master, relief=RAISED, borderwidth=2)
        self.master = master
        self.pack(fill=BOTH)
        self.config(padx=10 , pady=5, bg="#B2DFDB")
        self.widget_ubicacion()
        self.widget_tipo()
        self.widget_caracteristicas()
        self.widget_botones()  
        self.cargarProp      
    
    def widget_ubicacion(self):
        self.frameUbicacion = Frame(self.master)
        self.frameUbicacion.pack(fill=Y)
        self.frameUbicacion.config(padx=10 , pady=5, bg="#B2DFDB", borderwidth=1)

        self.tituloPropiedad = Label(self.frameUbicacion, text="Datos de la propiedad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.tituloPropiedad.grid(column=0, row=0, columnspan=8)

        self.lCalle = Label(self.frameUbicacion, text="Calle", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lCalle.grid(column=0, row=1)
        self.eCalle = Entry(self.frameUbicacion, bg="#e0f2f1", fg="#000000")
        self.eCalle.grid(column=1, row=1, padx=7, pady=15)

        self.lNum = Label(self.frameUbicacion, text="Nª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lNum.grid(column=2, row=1)
        self.eNum = Entry(self.frameUbicacion, bg="#e0f2f1", fg="#000000")
        self.eNum.grid(column=3, row=1, padx=7, pady=15)
        self.eNum.config(width=5)

        self.lPiso = Label(self.frameUbicacion, text="Pª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lPiso.grid(column=4, row=1)
        self.ePiso = Entry(self.frameUbicacion, bg="#e0f2f1", fg="#000000")
        self.ePiso.grid(column=5, row=1, padx=5, pady=15)
        self.ePiso.config(width=2)

        self.lDto = Label(self.frameUbicacion, text="Dª", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lDto.grid(column=6, row=1)
        self.eDto = Entry(self.frameUbicacion, bg="#e0f2f1", fg="#000000")
        self.eDto.grid(column=7, row=1, padx=7, pady=15)
        self.eDto.config(width=2)

        self.lCdad = Label(self.frameUbicacion, text="Ciudad", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lCdad.grid(column=0, row=2, columnspan=2)

        #obtengo las ciudades de bd
        self.conn = Bd()
        self.puntero = self.conn.cursor()
        self.puntero.execute("SELECT ciudad FROM ciudades")
        self.ciudades = list(self.puntero)
        self.nombres_ciudades = []    
        #armo una lista con los nombres
        for nombre in  self.ciudades:
            self.nombres_ciudades.append(nombre[0]) 

        self.eCdad = Combobox(self.frameUbicacion, state='readonly', values=self.nombres_ciudades)
        self.eCdad.current(0)
        self.eCdad.grid(column=1, row=2, padx=5, pady=15, columnspan=7)
        self.eCdad.config(background="#B2DFDB", foreground="#000000")
   
    def widget_tipo(self): 
        self.frameTipo = Frame(self.master)
        self.frameTipo.pack(fill=BOTH)
        self.frameTipo.config(padx=10 , pady=25, bg="#B2DFDB", borderwidth=1)

        self.tipo = IntVar()
        self.tipo.set(1)
        self.casa = Radiobutton(self.frameTipo, text="Casa", value=1, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.depto = Radiobutton(self.frameTipo, text="Depto.", value=2, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.local = Radiobutton(self.frameTipo, text="Local", value=3, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.oficina = Radiobutton(self.frameTipo, text="Oficina", value=4, variable=self.tipo, bg="#B2DFDB", fg="#000000")
        self.deposito = Radiobutton(self.frameTipo, text="Depósito", value=5, variable=self.tipo, bg="#B2DFDB", fg="#000000")

        self.casa.grid(column=0, row=1, padx=5, pady=5, sticky=W)
        self.depto.grid(column=1, row=1, padx=5, pady=5, sticky=W)
        self.local.grid(column=2, row=1, padx=5, pady=5, sticky=W)
        self.oficina.grid(column=3, row=1, padx=5, pady=5, sticky=W)
        self.deposito.grid(column=4, row=1, padx=5,  pady=5, sticky=W)

    def widget_caracteristicas(self):
        self.frameCaracteristicas = Frame(self.master)
        self.frameCaracteristicas.pack(fill=BOTH)
        self.frameCaracteristicas.config(padx=10 , pady=25, bg="#B2DFDB", borderwidth=1)

        self.telProp = IntVar()
        self.telProp.set(1)

        self.lTelefonoP = Label(self.frameCaracteristicas, text="Teléfono", bg="#B2DFDB", fg="#000000")
        self.lTelefonoP.grid(column=0, row=0, padx=5, pady=10)

        self.checkTel1 = Radiobutton(self.frameCaracteristicas, text="Fijo", value=1, variable=self.telProp, bg="#B2DFDB", fg="#000000")
        self.checkTel1.grid(column=1, row=0, pady=10)

        self.checkTel2 = Radiobutton(self.frameCaracteristicas, text="Móvil", value=2, variable=self.telProp, bg="#B2DFDB", fg="#000000")
        self.checkTel2.grid(column=2, row=0, padx=1, pady=10, )

        self.lAmbientes = Label(self.frameCaracteristicas, text="Ambientes", bg="#B2DFDB", fg="#000000")
        self.lAmbientes.grid(column=3, row=0, padx=10, pady=10)

        self.eAmbientes = Entry(self.frameCaracteristicas, bg="#e0f2f1", fg="#000000")
        self.eAmbientes.grid(column=4,row=0, pady=10)
        self.eAmbientes.config(width=3)

        self.lAberturas = Label(self.frameCaracteristicas, text="Abertutas", bg="#B2DFDB", fg="#000000")
        self.lAberturas.grid(column=5, row=0, padx=10, pady=10, sticky=W)

        self.eAberturas = Entry(self.frameCaracteristicas, bg="#e0f2f1", fg="#000000")
        self.eAberturas.grid(column=6,row=0, pady=10, sticky=W)
        self.eAberturas.config(width=3)

    def widget_botones(self):
        self.framebotones = Frame(self.master)
        self.framebotones.pack(fill=BOTH)
        self.framebotones.config(padx=10 , pady=10, bg="#B2DFDB")

        self.bNuevoCliente = Button(self.framebotones, text="Cargar\nPropiedad", bg="#e0f2f1", fg="#000000", cursor="hand2", command=self.cargarProp)
        self.bNuevoCliente.grid(column=0, row=0, padx=15, pady=5)
        if self.cont == 0:
            self.bNuevoCliente.config(bg="#009688", fg="#ffffff", width=10, height=2)
        else:
            self.bNuevoCliente.config(bg="#009688", fg="#ffffff", width=10, height=2, state=DISABLED)       

        self.bAgregar = Button(self.framebotones, text="Agregar\nProductos", cursor="hand2", command=ProductosAgregar)
        self.bAgregar.grid(column=1, row=0, padx=35, pady=5)
        self.bAgregar.config(bg="#FFE57F", fg="#000000", width=10, height=2)

        self.bVer = Button(self.framebotones, text="Ver\nCotización", cursor="hand2", command=Footer)
        self.bVer.grid(column=2, row=0, padx=15, pady=5)
        self.bVer.config(bg="#FFE57F", fg="#000000", width=10, height=2)

    def cargarProp(self):
        calle = self.eCalle.get()
        num = self.eNum.get()
        piso = self.ePiso.get()
        depto = self.eDto.get()
        ciudad = self.eCdad.get()       
        tipo = self.tipo.get()
        telefono = self.telProp.get()
        ambientes = self.eAmbientes.get()
        aberturas = self.eAberturas.get()
        
        #validaciones------------------------------------------------------------------------------

        if calle == '':
            messagebox.showinfo("Faltan Datos", "Ingrese una calle!")
        elif num == '':
            messagebox.showinfo("Faltan Datos", "Faltó el número!")
        elif not all(num.isdigit() for i in num):
            messagebox.showwarning("Datos Incorrectos", "Nº de Calle\ndebe ser un número!")
        elif ambientes == '':
            messagebox.showinfo("Faltan Datos", "Faltan ambientes!")
        elif not all(ambientes.isdigit() for j in ambientes):
            messagebox.showwarning("Datos Incorrectos", "Ambientes\ndebe ser un número!")
        elif aberturas == '':
            messagebox.showinfo("Faltan Datos", "Faltan aberturas!")
        elif not all(aberturas.isdigit() for k in aberturas):
            messagebox.showwarning("Datos Incorrectos", "Aberturas\ndebe ser un número!")
        else:
            #debo tomar el id_cliente de bd - cotizaciones
            #conexion a bd
            conn = Bd()
            puntero = conn.cursor()
###############################################################################################################################################
############Aquí empieza el armado de la cotización############################################################################################
###############################################################################################################################################
            #busco el último ingreso a cotizaciones
            puntero.execute("SELECT MAX(id_cotizacion) FROM cotizaciones")
            conn.commit()

            rows = list(puntero)
            for row in rows:
                id_cotizacion = str(row[0])

            puntero.execute("SELECT * FROM cotizaciones WHERE id_cotizacion = '"+id_cotizacion+"' ")
            conn.commit()

            cot = list(puntero)

            for cotiz in cot:
                id_cliente = cotiz[1]
                fecha = cotiz[2]
                current_cot = cotiz[3]

            print ("Cotizacion: " + id_cotizacion)

            print ("Current: " + str(current_cot))

            print ("id_cliente: " + str(id_cliente))

            print ("Fecha: " + fecha)

            print ("ciudad: " + ciudad)

            puntero.execute("SELECT id_ciudad FROM ciudades WHERE ciudad LIKE '%"+ciudad+"%'")
            conn.commit()
            rows = list(puntero) 
            for row in rows:
                id_ciudad = row[0]
            print ("id ciudad: " + str(id_ciudad))

            #verifico que el cliente fue cargado current = 0
            if current_cot!=0: 
                #si no esta el cliente se avisa
                messagebox.showwarning("Faltan Datos!", "Debe registrar el cliente primero!")
###############################################################################################################################################
################Aquí empieza el armado de la propiedad para la cotización######################################################################
###############################################################################################################################################
            else:
                #si esta cliente le asigno la propiedad:id_cliente, calle, numero piso depto id_ciudad      
                nueva_prop = ((id_cliente, calle, num, piso, depto, id_ciudad, tipo ),)
                cargo_prop = puntero.executemany("INSERT INTO propiedades VALUES(NULL,?,?,?,?,?,?,?)", nueva_prop)
                conn.commit()
                if cargo_prop:
                    puntero.execute("SELECT * FROM clientes WHERE id_cliente = '"+str(id_cliente)+"'")
                    rows = list(puntero)
                    for row in rows:
                        nombre_cl = row[1]
                        apellido_cl = row[2]
                    messagebox.showinfo("Nuevo Presupuesto", "Propiedad asiganada a "+ nombre_cl + " "+ apellido_cl)
                else:
                    messagebox.showwarning("Nuevo Presupuesto", "Hubo un error")
                #una vez registrado el cliente al que se le asignó una propiedad y se generó una cotización:
                #1º: modifico el current de la cotización
                puntero.execute("UPDATE cotizaciones SET current = '1' WHERE id_cotizacion = '"+id_cotizacion+"'")
                conn.commit()                

###############################################################################################################################################
################Aquí empieza el armado del detalle de la cotización############################################################################
###############################################################################################################################################
                #detalle: se carga id_cotización | id_producto | cant | precio
                #un producto que va en todas las cotizaciones es el kit básico id = 8
                
                #otro producto va obligatorio si la propiedad no tiene teléfono fijo es el GPRS id = 11
                if telefono == 2:
                    puntero.execute("SELECT * FROM productos WHERE id_producto = '11'")
                    rows = list(puntero)
                    producto2 =(id_cotizacion, rows[0][0], 1, rows[0][3])
                else:
                    producto2 = (id_cotizacion, rows[0][0], "", rows[0][3])
                puntero.execute("SELECT * FROM productos WHERE id_producto = '8'")
                rows = list(puntero)
                producto1 = (id_cotizacion, rows[0][0], 1, rows[0][3])
                #según la cantidad de ambientes es la cantidad de sensores infrarrojos a agregar id = 2
                puntero.execute("SELECT * FROM productos WHERE id_producto = '2'")
                rows = list(puntero)
                producto3 =[id_cotizacion, rows[0][0], self.eAmbientes.get(), rows[0][3]]

                #según la cantidad de aberturas es la cantidad de magnéticos a agregar id = 4
                puntero.execute("SELECT * FROM productos WHERE id_producto = '4'")
                rows = list(puntero)
                producto4 =(id_cotizacion, rows[0][0], self.eAberturas.get(), rows[0][3])

                cotizacion = (producto1, producto2, producto3, producto4)
                print (cotizacion)

                puntero.executemany("INSERT INTO detalles VALUES(NULL,?,?,?,?)", cotizacion)
                conn.commit()

                messagebox.showinfo("Cotización","Cotización Iniciada\nPuede Agregar Productos")
            self.cont = 1