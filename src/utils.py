import tkinter as tk
from tkinter import font as tkfont

def resize_window(root, text):
    text.update_idletasks()

    lines = text.get(1.0, tk.END).splitlines()
    max_width = max(len(line) for line in lines)
    
    char_width = tkfont.Font(font = text.cget("font")).measure("0")
    width_needed = max_width * char_width
    
    current_width = root.winfo_width()
    current_height = root.winfo_height()

    new_width = max(width_needed, current_width)
    new_height = current_height

    root.geometry(f"{new_width}x{new_height}")

if __name__ == "__main__":
    resize_window()