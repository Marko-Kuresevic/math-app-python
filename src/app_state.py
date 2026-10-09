import tkinter as tk
from test_functionality import create_test_ui
from primes_gcd_lcm_functionality import create_prime_gcd_lcm
from shapes_functionality import create_shape
from auth_ui import AuthManager

class AppState:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.current_func = None

        self.auth_frame = tk.Frame(root)
        self.auth_frame.pack(side = tk.TOP, anchor = tk.NE, fill = tk.Y, padx = 5, pady = 5)

        self.sign_up_button = tk.Button(self.auth_frame, text = "Sign Up", command = self.sign_up)
        self.log_in_button = tk.Button(self.auth_frame, text = "Log In", command = self.log_in)
        self.log_out_button = tk.Button(self.auth_frame, text = "Log Out", command = self.log_out)

        self.func_frame = tk.Frame(root)
        self.func_frame.pack(side = tk.LEFT, fill = tk.Y)

        tk.Frame(self.func_frame).pack(side = tk.TOP, fill = tk.Y, expand = True)
        tk.Frame(self.func_frame).pack(side = tk.BOTTOM, fill = tk.Y, expand = True)
        
        self.test_button = tk.Button(self.func_frame, text = "Test", command = lambda: self.switch_functionality("test"))
        self.primes_gcd_lcm_button = tk.Button(self.func_frame, text = "Primes, GCD, LCM", command = lambda: self.switch_functionality("primes, gcd, lcm"))
        self.shapes_button = tk.Button(self.func_frame, text = "Shapes", command = lambda: self.switch_functionality("shapes"))

        self.text = tk.Text(root, wrap = tk.NONE)

        self.functionalities = {
            "test": create_test_ui,
            "primes, gcd, lcm": create_prime_gcd_lcm,
            "shapes": create_shape
        }
        
        self.auth_ui = AuthManager(root, self.auth_callback)
        self.show_auth_widgets()

    def show_auth_widgets(self):
        self.hide_func_widgets()
        self.sign_up_button.pack(side = tk.RIGHT, padx = 5, pady = 5)
        self.log_in_button.pack(side = tk.RIGHT, padx = 5, pady = 5)
        self.text.pack_forget()

    def show_func_widgets(self):        
        self.hide_auth_widgets()

        self.test_button.pack(side = tk.TOP, padx = 5, pady = 5)
        self.primes_gcd_lcm_button.pack(side = tk.TOP, padx = 5, pady = 5)
        self.shapes_button.pack(side = tk.TOP, padx = 5, pady = 5)

        self.log_out_button.pack(side = tk.RIGHT, anchor = tk.NE, padx = 5, pady = 5)

        self.text.pack(side = tk.BOTTOM, expand = True, fill = "both")

        if self.current_func:            
            self.clear_widgets()

            self.widgets = self.functionalities[self.current_func](self.root, self.text)

            for widget in self.widgets:
                widget.pack(side = tk.TOP, fill = "x")

    def hide_auth_widgets(self):        
        self.sign_up_button.pack_forget()
        self.log_in_button.pack_forget()

    def hide_func_widgets(self):
        self.test_button.pack_forget()
        self.primes_gcd_lcm_button.pack_forget()
        self.shapes_button.pack_forget()
        self.log_out_button.pack_forget()
        self.text.pack_forget()

        self.clear_widgets()

    def clear_widgets(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets = []
        self.text.delete(1.0, tk.END)

        if self.current_func == "shapes":
            for widget in self.widgets:
                if isinstance(widget, tk.Canvas):
                    widget.delete("all")

    def sign_up(self):
        self.auth_ui.authenticate("signup")

    def log_in(self):
        self.auth_ui.authenticate("login")

    def log_out(self):
        self.show_auth_widgets()

    def auth_callback(self, success):
        if success:
            self.show_func_widgets()

    def switch_functionality(self, func_name):
        if func_name in self.functionalities:
            self.current_func = func_name
            self.show_func_widgets()
    
    def set_auth_ui(self, auth_ui):
        self.auth_ui = auth_ui

if __name__ == "__main__":
    app_state = AppState()