import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

# -------------------- Main Function to Generate Password -------------------- #
def generate_password():
    try:
        length = int(length_var.get())

        # Collect selected character sets
        characters = ""
        if use_upper.get():
            characters += string.ascii_uppercase
        if use_lower.get():
            characters += string.ascii_lowercase
        if use_digits.get():
            characters += string.digits
        if use_symbols.get():
            characters += string.punctuation

        # Validation
        if not characters:
            message_label.config(text="⚠️ Select at least one character type!", fg="red")
            return

        if length < 4:
            message_label.config(text="⚠️ Use at least 4 characters for safety.", fg="red")
            return

        # Generate the password securely
        password = ''.join(secrets.choice(characters) for _ in range(length))
        output_field.delete(0, tk.END)
        output_field.insert(0, password)
        message_label.config(text="✅ Password generated successfully!", fg="green")

    except ValueError:
        message_label.config(text="⚠️ Please enter a valid number!", fg="red")


# ---------------------- Copy Password to Clipboard ------------------------- #
def copy_to_clipboard():
    password = output_field.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# ------------------------ GUI Setup Starts Here ---------------------------- #

# Create main window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x380")
root.resizable(False, False)
root.config(bg="#f5f5f5")

# ------------------------ Title Label ------------------------ #
tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"), bg="#f5f5f5").pack(pady=10)

# ------------------------ Length Input ------------------------ #
length_frame = tk.Frame(root, bg="#fff")
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f5f5f5").pack(side=tk.LEFT, padx=5)
length_var = tk.StringVar()
tk.Entry(length_frame, textvariable=length_var, width=5, font=("Arial", 12), justify='center').pack(side=tk.LEFT)

# ------------------------ Checkboxes ------------------------ #
checkbox_frame = tk.Frame(root, bg="#fff")
checkbox_frame.pack(pady=10)

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(checkbox_frame, text="Uppercase (A-Z)", variable=use_upper, bg="#f5f5f5").grid(row=0, column=0, sticky="w")
tk.Checkbutton(checkbox_frame, text="Lowercase (a-z)", variable=use_lower, bg="#f5f5f5").grid(row=1, column=0, sticky="w")
tk.Checkbutton(checkbox_frame, text="Numbers (0-9)", variable=use_digits, bg="#f5f5f5").grid(row=0, column=1, sticky="w")
tk.Checkbutton(checkbox_frame, text="Symbols (!@#)", variable=use_symbols, bg="#f5f5f5").grid(row=1, column=1, sticky="w")

# ------------------------ Generate Button ------------------------ #
tk.Button(root, text="🎲 Generate Password", font=("Arial", 12, "bold"),
          bg="#4CAF50", fg="white", command=generate_password).pack(pady=15)

# ------------------------ Output Field ------------------------ #
output_field = tk.Entry(root, font=("Arial", 14), width=30, justify="center", bd=2, relief=tk.GROOVE)
output_field.pack(pady=5)

# ------------------------ Copy Button ------------------------ #
tk.Button(root, text="📋 Copy to Clipboard", command=copy_to_clipboard,
          font=("Arial", 10), bg="#2196F3", fg="white").pack(pady=8)

# ------------------------ Message Label ------------------------ #
message_label = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5")
message_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
