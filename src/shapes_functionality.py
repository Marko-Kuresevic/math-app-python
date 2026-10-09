import tkinter as tk

def draw_shape(canvas, shape, *params):
    canvas.delete("all")
    if shape == "rectangle":
        width, height = params
        canvas.create_rectangle(50, 50, 50 + int(width), 50 + int(height), outline = "blue", fill = "lightblue")
    elif shape == "circle":
        radius = int(params[0])
        canvas.create_oval(50, 50, 50 + 2 * radius, 50 + 2 * radius, outline = "green", fill = "lightgreen")
    elif shape == "triangle":
        base, height = map(int, params)

        x0, y0 = 50, 50
        x1, y1 = x0, y0 + height
        x2, y2 = x0 + base, y0 + height
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline = "red", fill = "lightcoral")

def update_params(frame, canvas, shape, param_entries, draw_button):
    for widget in param_entries:
        widget.destroy()
    param_entries.clear()

    if shape == "rectangle":
        tk.Label(frame, text= "Width:").pack(side = tk.LEFT)
        width_entry = tk.Entry(frame)
        width_entry.pack(side = tk.LEFT)
        param_entries.append(width_entry)

        tk.Label(frame, text = "Height:").pack(side = tk.LEFT)
        height_entry = tk.Entry(frame)
        height_entry.pack(side = tk.LEFT)
        param_entries.append(height_entry)

    elif shape == "circle":
        tk.Label(frame, text = "Radius:").pack(side = tk.LEFT)
        radius_entry = tk.Entry(frame)
        radius_entry.pack(side = tk.LEFT)
        param_entries.append(radius_entry)

    elif shape == "triangle":
        tk.Label(frame, text = "Side A:").pack(side = tk.LEFT)
        side_a_entry = tk.Entry(frame)
        side_a_entry.pack(side = tk.LEFT)
        param_entries.append(side_a_entry)

        tk.Label(frame, text = "Side B:").pack(side = tk.LEFT)
        side_b_entry = tk.Entry(frame)
        side_b_entry.pack(side = tk.LEFT)
        param_entries.append(side_b_entry)
        
    draw_button.config(command = lambda: draw_shape(canvas, shape, *map(lambda e: e.get(), param_entries)))

def shape_changed(shape_var, frame, canvas, param_entries, draw_button):
    shape = shape_var.get()
    update_params(frame, canvas, shape, param_entries, draw_button)

def create_shape(root, text):
    frame = tk.Frame(root)
    frame.pack(side = tk.TOP, fill = tk.X)

    canvas = tk.Canvas(root)
    canvas.pack()    

    shape_var = tk.StringVar(value = "rectangle")
    shapes = ["rectangle", "circle", "triangle"]

    tk.Label(frame, text = "Select Shape:").pack(side = tk.LEFT)
    shape_menu = tk.OptionMenu(frame, shape_var, *shapes)
    shape_menu.pack(side = tk.LEFT)

    param_entries = []
    draw_button = tk.Button(frame, text = "Draw")
    draw_button.pack(side = tk.LEFT)

    shape_var.trace_add("write", lambda *args: shape_changed(shape_var, frame, canvas, param_entries, draw_button))
    
    update_params(frame, canvas, shape_var.get(), param_entries, draw_button)

    return [frame, canvas]

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Draw Shapes Example")

    text = tk.Text(root, wrap = tk.NONE)
    text.pack(side = tk.BOTTOM, expand = True, fill = "both")
    
    widgets = create_shape(root, text)
    for widget in widgets:
        widget.pack(side = tk.TOP, fill = "x")

    root.mainloop()