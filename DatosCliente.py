from tkinter import *
from tkinter import messagebox
from typing import get_args
from Bd import *
import re   #para validar correo
from datetime import datetime #para obtener la fecha de hoy
from datetime import date


#frame para datos de cliente dentro de formularios
class Cliente(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=LEFT)
        self.config(padx=5 , pady=5, bg="#B2DFDB", relief=RAISED, borderwidth=2)
        self.widget_form()
        self.limpiar
        

    def widget_form(self):
        #declaración de variables para asociar a los campos del formulario
        self.varNombre = StringVar()
        self.varApellido = StringVar()
        self.varEmail = StringVar()
        self.varTelefono = StringVar()        

        self.lTituloCliente = Label(self, text="Datos del Cliente", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lTituloCliente.grid(column=0, row=0, columnspan="2")

        self.lNombre = Label(self, text="Nombre", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
        self.lNombre.grid(column=0, row=1)
        self.eNombre = Entry(self, bg="#e0f2f1", fg="#000000", textvariable=self.varNombre)
        self.eNombre.grid(column=1, row=1, padx=5, pady=5)

        self.lApellido = Label(self, text="Apellido", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
        self.lApellido.grid(column=0, row=2)
        self.eApellido = Entry(self, bg="#e0f2f1", fg="#000000", textvariable=self.varApellido)
        self.eApellido.grid(column=1, row=2, padx=5, pady=5)

        self.lEmail = Label(self, text="Email", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
        self.lEmail.grid(column=0, row=3)
        self.eEmail = Entry(self, bg="#e0f2f1", fg="#000000", textvariable=self.varEmail)
        self.eEmail.grid(column=1, row=3, padx=5, pady=5)

        self.lTelefono = Label(self, text="Telefono", padx=5, pady=5, bg="#B2DFDB", fg="#000000")
        self.lTelefono.grid(column=0, row=4)
        self.eTelefono = Entry(self, bg="#e0f2f1", fg="#000000", textvariable=self.varTelefono)
        self.eTelefono.grid(column=1, row=4, padx=5, pady=5)

        self.lTituloObs= Label(self, text="Observaciones", padx=5, pady=15, bg="#B2DFDB", fg="#000000")
        self.lTituloObs.grid(column=0, row=5, columnspan="2")

        self.tObs = Text(self, width=27, height=6)
        self.tObs.grid(column=0, row=6, columnspan=2)
        self.tObs.config(padx=5, pady=5, bg="#e0f2f1", fg="#000000")

        self.bNuevoCliente = Button(self, text="Registrar\nCliente", bg="#e0f2f1", fg="#000000", cursor="hand2", command=self.cargar)
        self.bNuevoCliente.grid(column=1, row=9, padx=5, pady=5, sticky=W, columnspan=2)
        self.bNuevoCliente.config(bg="#009688", fg="#ffffff", width=10, height=2)

    def limpiar(self):
        self.varNombre.set("")
        self.varApellido.set("")
        self.varEmail.set("")
        self.varTelefono.set("")
        self.tObs.delete(1.0,END)
        
    def cargar(self):
        self.nombre = self.eNombre.get()
        self.apellido = self.eApellido.get()
        self.email = self.eEmail.get()
        self.telefono = self.eTelefono.get()
        self.observ = self.tObs.get("1.0", END)        
        
        #validaciones
        
        #para email
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        
        if self.nombre == '':
            messagebox.showinfo("Faltan Datos", "Faltó el Nombre!")
        elif self.apellido == '':
            messagebox.showinfo("Faltan Datos", "Faltó el Apellido!")
        elif self.email == '':
            messagebox.showinfo("Faltan Datos", "Faltó el email!")
        elif re.match(expresion_regular, self.email) is None:
            messagebox.showwarning("Datos Incorrectos", "Correo inválido!")
        elif self.telefono == '':
            messagebox.showinfo("Faltan Datos", "Faltó el Teléfono!")
        elif not all(num.isdigit() for num in self.telefono):
            messagebox.showwarning("Datos Incorrectos", "Teléfono inválido!")
        else:
            #llamo a la bd
            conn = Bd()
            puntero = conn.cursor()
            #busco si el cliente se encuentra cargado-----------------------------------------
            puntero.execute("SELECT * FROM clientes WHERE correo ='" +self.email+ "'")
            
            rows = list(puntero)        #guardo la consulta
            for i in rows:
                print (i)
                self.id_cliente = i[0]       #si el cliente está cargado rescato el id
            
            cant = len(rows)

            #Día actual para cargar en bd
            fecha = date.today()
            #declaro la variable current_cot = 0 para avisar que hay un cliente cargado en bd a la espera de una cotización
            #en bd: current = 0 (no tiene cotización) | current = 1 (ya tiene la cotización)
            current_cot = 0

            #si no hay un cliente en bd lo cargo ahora
            if cant == 0:
                datos = ((self.nombre, self.apellido, self.telefono, self.email, self.observ),) 
                
                puntero.executemany("INSERT INTO  clientes VALUES (NULL,?,?,?,?,?)", datos)

                #rescato el id del nuevo cliente---------------------------------------------
                puntero.execute("SELECT MAX(id_cliente) FROM clientes")
                conn.commit()

                rows = list(puntero)

                for row in rows:
                    self.id_cliente = row[0] 

                print (self.id_cliente)
                #-----------------------------------------------------------------------------
                #armo la cotización para este cliente-------------------------------------------


                nueva_cotizacion = ((self.id_cliente, fecha, current_cot),)

                puntero.executemany("INSERT INTO cotizaciones VALUES (NULL,?,?,?)", nueva_cotizacion)
                conn.commit()

                messagebox.showinfo("Nuevo Cliente", "Haremos un presupuesto para:\n" + self.nombre + " " + self.apellido )
                
                print ("datos cargados")
                #-------------------------------------------------------------------------------
            #si el cliente está cargado
            else:
                print ("cliente existente")
                resultado = messagebox.askquestion("Cliente Existente","El cliente está regitrado\nDesea continuar?")
                if resultado == "yes":
                    messagebox.showinfo("Cliente Existente", "Haremos un nuevo presupuesto para:\n" + self.nombre + " " + self.apellido )
                    
                    #armo una nueva cotizacion para el cliente existente
                    cotizacion = ((self.id_cliente, fecha, current_cot),)

                    puntero.executemany("INSERT INTO cotizaciones VALUES (NULL,?,?,?)", cotizacion)
                    conn.commit()

                else:
                    #limpio el form si no quiere hacer un presupuesto para el cliente cargado
                    self.limpiar()
            conn.close()
            