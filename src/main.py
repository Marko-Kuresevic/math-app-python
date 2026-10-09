import tkinter as tk
from app_state import AppState

class MathApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Math App")
        
        self.app_state = AppState(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MathApp()
    app.run()