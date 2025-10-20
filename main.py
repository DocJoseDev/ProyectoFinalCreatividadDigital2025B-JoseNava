import tkinter as tk

# Instancia de la ventana principal
ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Mi Ventana")
ventana.geometry("400x300")

# Creación de una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

# Creación de un botón
boton = tk.Button(ventana, text="Haz clic aquí")
boton.pack()

# Creacion de entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Creacionde cuadro de texto muliples lineas
cuadro_texto = tk.Text(ventana, height=5, width=30)
cuadro_texto.pack()

# Creación de una casilla de verificación
casilla = tk.Checkbutton(ventana, text="Acepto los términos y condiciones")
casilla.pack()

# Creacion de una barra de progreso
barra_progreso = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL)
barra_progreso.pack()

# Ejecución del bucle principal de la ventana
ventana.mainloop()


