import tkinter as tk

# Clase principal de la calculadora
class Calculadora:

    # Declaramos la ventana, Titulo, Dimensiones, No escalable, Color de fondo
    def __init__(self):
        # Estado inicial
        self.numero_1 = None
        self.operacion = None

        # Creamos la ventana
        self.ventana = tk.Tk()
        self.ventana.title("CALCULADORA")
        self.ventana.geometry("500x600")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#1E1E1E")

        # Creamos la interfaz
        self.secciones()
        self.botones_numeros()
        self.botones_operaciones()

    # Funcion de frames
    def secciones(self):
        # Primer frame recuadro de resultados
        self.frame1 = tk.Frame(
            self.ventana,
            width=460,
            height=160,
            bg="#272727"
        )

        self.frame1.place(x=20, y=20)

        # Creamos el entry

        self.entry = tk.Entry(
            self.frame1,
            bg="#272727",
            fg="#F2F2F2",
            font=("DejaVu Sans", 42, "bold"),
            bd=0,
            relief="flat",
            highlightthickness=0,
            justify="right",
            insertbackground="#F2F2F2"
        )

        self.entry.place(
            x=20,
            y=45,
            width=420,
            height=90
         )

        
    
        # Segundo frame numeros
        self.frame_botones = tk.Frame(
            self.ventana,
            width=460,
            height=350,
            bg="#272727"
        )

        self.frame_botones.grid_propagate(False)
        
        for columna in range(4):
            self.frame_botones.grid_columnconfigure(columna, weight=1)

        for fila in range(4):
            self.frame_botones.grid_rowconfigure(fila, weight=1)

        self.frame_botones.place(x=20,y=230)

    def pulsar_numeros(self, numero):
        self.entry.insert("end",str(numero))

    def borrar(self):
        self.entry.delete(0, tk.END)
        self.numero_1 = None
        self.operacion = None

    def pulsar_operaciones(self, operacion):
        texto = self.entry.get()
        if texto == "" or texto =="Error":
            return
        self.numero_1 = float(texto)
        self.operacion = operacion
        self.entry.delete(0, tk.END)

    def calcular(self):
        texto = self.entry.get()
        if texto == "" or self.operacion is None:
            return
        numero_2 = float(texto)
        if self.operacion == "+":
            resultado = self.numero_1 + numero_2
        elif self.operacion == "-":
            resultado = self.numero_1 - numero_2
        elif self.operacion == "x":
            resultado = self.numero_1 * numero_2
        elif self.operacion == "÷":
            if numero_2 == 0:
                resultado = "Error"
            else:
                resultado = self.numero_1 / numero_2

        # Imprimir numero entero decimales o texto y mostrar dos decimales    
        self.entry.delete(0, tk.END)

        if isinstance(resultado, str):
            self.entry.insert(0, resultado)
        elif resultado.is_integer():
            self.entry.insert(0, int(resultado))
        else:
            self.entry.insert(0, round(resultado, 2))

    def botones_numeros(self):
 
        # Crear botones numericos

        botones_numeros = [
            (7, 0, 0),
            (8, 0, 1),
            (9, 0, 2),

            (4, 1, 0),
            (5, 1, 1),
            (6, 1, 2),

            (1, 2, 0),
            (2, 2, 1),
            (3, 2, 2),

            (0, 3, 1)
        ]
        
        for numero, fila, columna in botones_numeros:

            boton = tk.Button(
                   self.frame_botones,
                    text=str(numero),
                    bg="#3A3A3A",
                    fg="#F2F2F2",
                    activebackground="#484848",
                    activeforeground="#FFFFFF",
                    cursor="hand2",
                    bd=0,
                    relief="flat",
                    highlightthickness=0,
                    font=("DejaVu", 20, "bold"),
                    command=lambda n=numero: self.pulsar_numeros(n)
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=5,
                pady=5,
                sticky="nsew"
            )

       

    
    def botones_operaciones(self):

        operaciones = [
            ("+", 3, 3),
            ("-", 2, 3),
            ("x", 1, 3),
            ("÷", 0, 3)
        ]

        for operacion, fila, columna in operaciones:
            boton = tk.Button(
                self.frame_botones,
                text=operacion,
                    bg="#505050",
                    fg="#F2F2F2",
                    activebackground="#626262",
                    activeforeground="#FFFFFF",
                    cursor="hand2",
                    bd=0,
                    relief="flat",
                    highlightthickness=0,
                    font=("DejaVu", 20, "bold"),
                    command=lambda op=operacion: self.pulsar_operaciones(op)
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=5,
                pady=5,
                sticky="nsew"
            )

        # Boton igual
        boton_igual = tk.Button(
        self.frame_botones,
        text="=",
        bg="#7FAF8A",# Fondo de el boton
        fg="#F2F2F2",# Color de numero de el boton
        activebackground="#91C19C",
        activeforeground="#FFFFFF",
        cursor="hand2",
        bd=0,
        relief="flat",
        highlightthickness=0,
        font=("DejaVu", 20, "bold"),
        )
                        
        boton_igual.grid(row=3, column=2,padx=5, pady=5, sticky="nsew")

        boton_igual.config(command=self.calcular)

        # Boton borrar
        boton_borrar = tk.Button(
        self.frame_botones,
        text="C",
        bg="#6B4545",# Fondo de el boton
        fg="#F2F2F2",# Color de numero de el boton
        activebackground="#805353",
        activeforeground="#FFFFFF",
        cursor="hand2",
        bd=0,
        relief="flat",
        highlightthickness=0,
        font=("DejaVu", 20, "bold"),
        )
                        
        boton_borrar.grid(row=3, column=0,padx=5, pady=5, sticky="nsew")

        # Borra pantalla
        boton_borrar.config(command=self.borrar)
        

    def iniciar(self):
        self.ventana.mainloop()


app = Calculadora()
app.iniciar()