import tkinter as tk
from auth import Auth

class AuthManager:
    def __init__(self, root, auth_callback):
        self.root = root
        self.auth = Auth()
        self.auth_callback = auth_callback

    def authenticate(self, operation):
        def on_authenticate():
            username = username_entry.get()
            password = password_entry.get()

            if username == "" or password == "":
                error_label.config(text = "You need to enter username and password.")
                return

            if self.auth.authentication(username, password, operation):
                auth_window.destroy()
                self.auth_callback(success = True)
            else:
                if operation == "signup":
                    switch_button.pack()
                    error_label.config(text = "Sign up failed: Username already exists. Please log in.")
                else:
                    error_label.config(text = "Log in failed: Invalid username or password.")
        
        def switch_mode():
            nonlocal operation

            if operation == "signup":
                operation = "login"
                switch_button.pack()
                auth_window.title("Log in page")
                auth_button.config(text = "Log in")
            
            error_label.config(text = "")
            switch_button.pack_forget()

        auth_window = tk.Toplevel(self.root)
        auth_window.title(f"{operation.capitalize()} page")

        tk.Label(auth_window, text = "Username:").pack()
        username_entry = tk.Entry(auth_window)
        username_entry.pack()

        tk.Label(auth_window, text = "Password:").pack()
        password_entry = tk.Entry(auth_window, show = "*")
        password_entry.pack()
        
        auth_button = tk.Button(auth_window, text = operation.capitalize(), command = on_authenticate)
        auth_button.pack()

        switch_button = tk.Button(auth_window, text = "Switch to Log in", command = switch_mode)
        switch_button.pack_forget()

        error_label = tk.Label(auth_window, text = "", fg = "red")
        error_label.pack()

if __name__ == "__main__":
    auth_manager = AuthManager()