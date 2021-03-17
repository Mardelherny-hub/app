from tkinter import *

root =Tk()
root.title("Agregar Productos")
root.geometry("600x500+50+50")


#frame contenedor
frameMain = Frame(root, bg="#ffffff")
frameMain.pack(expand=True, fill=Y)
frameMain.config(padx=5, pady=5)

#frame de encabezado dentro de main
frameTitulo = Frame(frameMain, bg="#ffffff")
frameTitulo.pack()
frameTitulo.config(padx=10, pady=10)

titulo = Label(frameTitulo, text="Agregar productos a la cotización", bg="#ffffff", fg="#000000")
titulo.pack(fill="both")

#frame para grilla dentro de main

frameEncabezados = Frame(frameMain, bg="#f1f1f1")
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
lblEncabezado = Button(frameEncabezados, text="Terminar", padx=80, pady=5, 
                    bg="yellow", fg="#000000", cursor="hand2", relief=RAISED,
                    borderwidth=2)
lblEncabezado.grid(row=0, column=5, columnspan=3)

frameGrilla = Frame(frameMain, bg="#f1f1f1", borderwidth=2, relief=RAISED)
frameGrilla.pack(expand=TRUE, fill=Y, side=LEFT)
frameGrilla.config(padx=10, pady=10)



#listado de productos
    #código(1) | nombre(2) | descripcion(3) | precio(4) | agregar uno(5) | quitar uno(6)
productos = (1,"artículo 1","descripcion 1",100,
      2,"artículo 2","descripcion 2",200,
      3,"artículo 3","descripcion 3",300,
      4,"artículo 4","descripcion 4",400,
      5,"artículo 5","descripcion 5",500
    )
#listado de productos agregados al carrito
    #del detalle solo necesito la cantidad relacionada con el código(1) | cantidad(2)
detalle = (1,2,
           3,12,
           2,1,
           5,6)
           
#cantidades          
cantProd = int(len(productos))
cantDet = int(len(detalle))
cant = int(cantProd/4) #obtengo la cantidad de productos de la lista 

#grilla para el listados de productos
k = 0
for i in range(cant):
    j = 0    
    while j < 4:              
        for item in productos:        
            celda = Frame(frameGrilla, bg='#f1f1f1')
            celda.grid(row=i, column=j, padx=5, pady=5)
            lbl_celda = Label(celda, text=productos[k], fg="#000000", bg="#f1f1f1")
            lbl_celda.grid()
        j = j + 1
        k = k + 1   
#grilla continuación con las cantidades agregadas
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
         

        
        
#  f"celda {i} | {j} | {k}", relief=RAISED
root.mainloop()