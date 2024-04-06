import tkinter as tk
import math

# Função para criar um polígono
def create_polygon(canvas, points, **kwargs):
    return canvas.create_polygon(points, **kwargs)

# Função para desenhar os eixos x e y
def draw_axes(canvas, width, height):
    # Desenha eixo x
    canvas.create_line(0, height // 2, width, height // 2, fill="black")
    # Desenha eixo y
    canvas.create_line(width // 2, 0, width // 2, height, fill="black")

# Função para realizar a translação de um polígono
def translate_polygon(canvas, polygon, dx, dy):
    canvas.move(polygon, dx, dy)

# Função para realizar a escala de um polígono
def scale_polygon(canvas, polygon, sx, sy):
    coords = canvas.coords(polygon)
    center_x = sum(coords[::2]) / len(coords[::2])
    center_y = sum(coords[1::2]) / len(coords[1::2])
    for i in range(0, len(coords), 2):
        x = coords[i]
        y = coords[i + 1]
        new_x = center_x + sx * (x - center_x)
        new_y = center_y + sy * (y - center_y)
        coords[i] = new_x
        coords[i + 1] = new_y
    canvas.coords(polygon, *coords)

# Função para realizar a rotação de um polígono
def rotate_polygon(canvas, polygon, angle):
    coords = canvas.coords(polygon)
    center_x = sum(coords[::2]) / len(coords[::2])
    center_y = sum(coords[1::2]) / len(coords[1::2])
    angle_rad = math.radians(angle)
    for i in range(0, len(coords), 2):
        x = coords[i]
        y = coords[i + 1]
        new_x = center_x + math.cos(angle_rad) * (x - center_x) - math.sin(angle_rad) * (y - center_y)
        new_y = center_y + math.sin(angle_rad) * (x - center_x) + math.cos(angle_rad) * (y - center_y)
        coords[i] = new_x
        coords[i + 1] = new_y
    canvas.coords(polygon, *coords)

# Função para realizar a reflexão de um polígono
def reflect_polygon(canvas, polygon, axis):
    coords = canvas.coords(polygon)
    center_x = sum(coords[::2]) / len(coords[::2])
    center_y = sum(coords[1::2]) / len(coords[1::2])
    if axis == "x":
        for i in range(0, len(coords), 2):
            x = coords[i]
            coords[i] = center_x - (x - center_x)
    elif axis == "y":
        for i in range(1, len(coords), 2):
            y = coords[i]
            coords[i] = center_y - (y - center_y)
    canvas.coords(polygon, *coords)

# Função para realizar o cisalhamento de um polígono
def shear_polygon(canvas, polygon, shx, shy):
    coords = canvas.coords(polygon)
    for i in range(0, len(coords), 2):
        coords[i] += shx * coords[i + 1]
        coords[i + 1] += shy * coords[i]
    canvas.coords(polygon, *coords)

# Função para aplicar a translação quando o botão é clicado
def translate_button_click():
    dx = int(dx_entry.get())
    dy = int(dy_entry.get())
    translate_polygon(canvas, polygon, dx, dy)

# Função para aplicar a escala quando o botão é clicado
def scale_button_click():
    sx = float(sx_entry.get())
    sy = float(sy_entry.get())
    scale_polygon(canvas, polygon, sx, sy)

# Função para aplicar a rotação quando o botão é clicado
def rotate_button_click():
    angle = float(angle_entry.get())
    rotate_polygon(canvas, polygon, angle)

# Função para aplicar a reflexão quando o botão é clicado
def reflect_button_click():
    axis = axis_var.get()
    reflect_polygon(canvas, polygon, axis)

# Função para aplicar o cisalhamento quando o botão é clicado
def shear_button_click():
    shx = float(shx_entry.get())
    shy = float(shy_entry.get())
    shear_polygon(canvas, polygon, shx, shy)

# Função principal
def main():
    # Configurações da janela
    window = tk.Tk()
    window.title("Transformações Geométricas")

    # Configurações do canvas
    canvas_width = 400
    canvas_height = 400
    global canvas
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Desenha os eixos x e y
    draw_axes(canvas, canvas_width, canvas_height)

    # Define as coordenadas do polígono (triângulo) centralizado
    polygon_coords = [canvas_width / 2, canvas_height / 2 - 50,
                      canvas_width / 2 - 50, canvas_height / 2 + 50,
                      canvas_width / 2 + 50, canvas_height / 2 + 50]

    # Cria o polígono
    global polygon
    polygon = create_polygon(canvas, polygon_coords, fill="blue")

    # Entradas para os parâmetros das transformações
    tk.Label(window, text="Translação (dx, dy):").pack()
    global dx_entry
    dx_entry = tk.Entry(window)
    dx_entry.pack()
    global dy_entry
    dy_entry = tk.Entry(window)
    dy_entry.pack()

    tk.Label(window, text="Escala (sx, sy):").pack()
    global sx_entry
    sx_entry = tk.Entry(window)
    sx_entry.pack()
    global sy_entry
    sy_entry = tk.Entry(window)
    sy_entry.pack()

    tk.Label(window, text="Rotação (ângulo):").pack()
    global angle_entry
    angle_entry = tk.Entry(window)
    angle_entry.pack()

    tk.Label(window, text="Reflexão:").pack()
    global axis_var
    axis_var = tk.StringVar()
    axis_var.set("x")
    tk.Radiobutton(window, text="Eixo X", variable=axis_var, value="x").pack()
    tk.Radiobutton(window, text="Eixo Y", variable=axis_var, value="y").pack()

    tk.Label(window, text="Cisalhamento (shx, shy):").pack()
    global shx_entry
    shx_entry = tk.Entry(window)
    shx_entry.pack()
    global shy_entry
    shy_entry = tk.Entry(window)
    shy_entry.pack()

    # Botões para aplicar as transformações
    tk.Button(window, text="Translação", command=translate_button_click).pack()
    tk.Button(window, text="Escala", command=scale_button_click).pack()
    tk.Button(window, text="Rotação", command=rotate_button_click).pack()
    tk.Button(window, text="Reflexão", command=reflect_button_click).pack()
    tk.Button(window, text="Cisalhamento", command=shear_button_click).pack()

    window.mainloop()

if __name__ == "__main__":
    main()
