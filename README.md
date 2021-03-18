# app - Cotizador

Trabajo final de Programación II (Python)

Aplicación desarrollada como trabajo final de la materia Programación II, de la carrera Analista de Sistemas.

Podés usar este proyecto para comparar con tu presentación o armar uno mejor o distinto, tomándolo como base.

Se trata de un cotizador que permite realizar el presupuesto de un sistema de alarma.

## Composición de los scripts

- app.py (inicio de la aplicación)
  - Aplicacion.py
    - Main.py
      - MainTitulo.py
      - MainDatos.py
        - DatosCliente.py
        - DatosPropiedad.py
          - ProducosAgregar.py
            - Productos.py
          - Footer.py
            - FooterEncabezado.py
            - FooterHead.py
            - FooterGrilla.py
  - fcMenu.py
  - Bd.py
- base.py (script base de diseño de interfase, luego pasado a objetos)
- base0.py (script base de diseño de interfase modal, luego pasado a objetos)
- cotizador (archivo de base de datos para ser usado con SQLITE)
