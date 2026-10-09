import tkinter as tk
from gcd_lcm import compute_gcd_lcm
from prime import compute_prime

def show_gcd_lcm(root, text, num1_entry, num2_entry):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())

    result = compute_gcd_lcm(num1, num2)

    text.delete(1.0, tk.END)

    for row in result[0]:
        text.insert(tk.END, f"{row[0]}, {row[1]} | {row[2]}\n")
    
    text.insert(tk.END, result[1] + "\n")
    text.insert(tk.END, result[2])

def show_prime(root, text, num_entry):
    num = int(num_entry.get())

    result = compute_prime(num)

    text.insert(tk.END, result)

def create_prime_gcd_lcm(root, text):    
    frame = tk.Frame(root)

    num_label = tk.Label(frame, text = "Prime numbers to: ")
    num_entry = tk.Entry(frame)
    prime_button = tk.Button(frame, text = "Show", command = lambda: show_prime(root, text, num_entry))

    num_label.pack(side = tk.TOP, fill= "x")
    num_entry.pack(side = tk.TOP, fill= "x")
    prime_button.pack(side = tk.TOP, fill = "x")

    num1_label = tk.Label(frame, text = "1. number:")
    num1_entry = tk.Entry(frame)
    num2_label = tk.Label(frame, text = "2. number:")
    num2_entry = tk.Entry(frame)
    calculate_button = tk.Button(frame, text = "Calculate GCD and LCM", command = lambda: show_gcd_lcm(root, text, num1_entry, num2_entry))
    
    num1_label.pack(side = tk.TOP, fill= "x")
    num1_entry.pack(side = tk.TOP, fill= "x")
    num2_label.pack(side = tk.TOP, fill= "x")
    num2_entry.pack(side = tk.TOP, fill= "x")
    calculate_button.pack(side = tk.TOP, fill = "x")

    return [frame]

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prime numbers, GCD and LCM")
    
    text = tk.Text(root, wrap = tk.NONE)
    text.pack(side = tk.BOTTOM, expand = True, fill = "both")
    
    widgets = create_prime_gcd_lcm(root, text)
    for widget in widgets:
        widget.pack(side = tk.TOP, fill = "x")
    
    root.mainloop()