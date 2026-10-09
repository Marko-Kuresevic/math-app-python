import tkinter as tk
from utils import resize_window
from multiplication_table import create_mult_table
from select_1 import get_products

def show_table(root, text):
    table = create_mult_table()
    text.delete(1.0, tk.END)
    text.insert(tk.END, table)

    resize_window(root, text)

def show_products(root, text, divisor_entry, odd_var, even_var):
    divisor = int(divisor_entry.get())
    odd = odd_var.get()
    even = even_var.get()

    product_list = get_products(divisor, odd, even)
    
    text.delete(1.0, tk.END)

    for num in product_list:
        text.insert(tk.END, str(num) + "\n")
    
    resize_window(root, text)

def update_checkboxes(option_var, odd_var, even_var):
    if option_var.get() == "All":
        odd_var.set(True)
        even_var.set(True)
    elif option_var.get() == "Odd":
        odd_var.set(True)
        even_var.set(False)
    elif option_var.get() == "Even":
        odd_var.set(False)
        even_var.set(True)

def create_test_ui(root, text):
    frame = tk.Frame(root)
    
    divisor_label = tk.Label(frame, text = "Divisor:")
    divisor_entry = tk.Entry(frame)

    option_var = tk.StringVar(value = "All")
    odd_var = tk.BooleanVar(value = True)
    even_var = tk.BooleanVar(value = True)

    all_radio = tk.Radiobutton(frame, text = "All", variable = option_var, value = "All", command = lambda: update_checkboxes(option_var, odd_var, even_var))
    odd_radio = tk.Radiobutton(frame, text = "Odd", variable = option_var, value = "Odd", command = lambda: update_checkboxes(option_var, odd_var, even_var))
    even_radio = tk.Radiobutton(frame, text = "Even", variable = option_var, value = "Even", command = lambda: update_checkboxes(option_var, odd_var, even_var))

    show_products_button = tk.Button(frame, text = "Show Products", command = lambda: show_products(root, text, divisor_entry, odd_var, even_var))
    mult_table_button = tk.Button(frame, text = "Show multiplication table", command = lambda: show_table(root, text))

    divisor_label.pack(side = tk.TOP, fill = "x")
    divisor_entry.pack(side = tk.TOP, fill = "x")
    all_radio.pack(side = tk.TOP, fill = "x")
    odd_radio.pack(side = tk.TOP, fill = "x")
    even_radio.pack(side = tk.TOP, fill = "x")
    show_products_button.pack(side = tk.TOP, fill = "x")
    mult_table_button.pack(side = tk.TOP, fill = "x")

    return [frame]

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test UI")
    
    text = tk.Text(root, wrap = tk.NONE)
    text.pack(side = tk.BOTTOM, expand = True, fill = "both")
    
    widgets = create_test_ui(root, text)
    
    for widget in widgets:
        widget.pack(side = tk.TOP, fill = "x")
    
    root.mainloop()