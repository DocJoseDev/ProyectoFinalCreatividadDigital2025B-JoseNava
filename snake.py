import tkinter as tk

import random

import constantes

# Instanciar una ventana nueva
ventana = tk.Tk()

# Asignarle dimensiones y titulo
ventana.title("Mi Ventana")
ventana.geometry(f"{constantes.ancho_ventana}x{constantes.alto_ventana}")

# Remover configuracion de la ventana por defecto
ventana.resizable(False, False)

# Agregar un lienzo a la ventana
lienzo = tk.Canvas(ventana, width=780, height=480, background="black")
lienzo.pack_configure(expand=True, anchor="center")
lienzo.pack()

# Aleatoriedad en el punto a comer cuando aparezca
x = random.randint(0, 780)
y = random.randint(0, 480)

#Agregar un rectangulo (punto a comer) al lienzo
lienzo.create_rectangle(x, y, x + constantes.punto, y + constantes.punto, fill="white")


# Configurar serpiente
segmento = constantes.punto
inicial_x = constantes.ancho_ventana // 2 - segmento // 2
inicial_y = constantes.alto_ventana // 2 - segmento // 2

# lista de coordenadas (head first) y ids de rectángulos en el lienzo
snake_coords = [
    (inicial_x, inicial_y),
    (inicial_x - segmento, inicial_y),
    (inicial_x - 2 * segmento, inicial_y),
]
snake_ids = []
for (sx, sy) in snake_coords:
    snake_ids.append(lienzo.create_rectangle(sx, sy, sx + segmento, sy + segmento, fill="green"))

# Dirección inicial (derecha)
dx, dy = segmento, 0

# Delay entre movimientos (ms). Usa constantes.velocidad si existe, sino 100ms.
delay = getattr(constantes, "velocidad", 100)

def on_key_press(event):
    global dx, dy
    key = event.keysym.lower()
    # nuevas direcciones según tecla
    if key in ("left", "a"):
        ndx, ndy = -segmento, 0
    elif key in ("right", "d"):
        ndx, ndy = segmento, 0
    elif key in ("up", "w"):
        ndx, ndy = 0, -segmento
    elif key in ("down", "s"):
        ndx, ndy = 0, segmento
    else:
        return
    # evitar invertir la dirección directamente
    if (ndx, ndy) != (-dx, -dy):
        dx, dy = ndx, ndy

def move_snake():
    global snake_coords, snake_ids
    head_x, head_y = snake_coords[0]
    new_x = (head_x + dx) % constantes.ancho_ventana
    new_y = (head_y + dy) % constantes.alto_ventana

    # crear nuevo head
    new_id = lienzo.create_rectangle(new_x, new_y, new_x + segmento, new_y + segmento, fill="green")
    snake_coords.insert(0, (new_x, new_y))
    snake_ids.insert(0, new_id)

    # eliminar cola para mantener mismo tamaño (no crecimiento por ahora)
    tail_id = snake_ids.pop()
    lienzo.delete(tail_id)
    snake_coords.pop()

    # programar siguiente movimiento
    ventana.after(delay, move_snake)

# Enlazar teclado y empezar movimiento
ventana.bind("<Key>", on_key_press)
ventana.focus_set()
ventana.after(delay, move_snake)

# Configuracion para que se vea la ventana
ventana.mainloop()