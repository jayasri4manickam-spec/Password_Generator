import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Password Logic ---------------- #

def generate_password():
    length = length_var.get()

    chars = ""
    if upper_var.get():
        chars += string.ascii_uppercase
    if lower_var.get():
        chars += string.ascii_lowercase
    if number_var.get():
        chars += string.digits
    if symbol_var.get():
        chars += "!@#$%^&*()_+-="

    if chars == "":
        messagebox.showwarning("Warning", "Select at least one character type")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    update_strength(password)


def update_strength(password):
    score = 0
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=" for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score == 3:
        strength_label.config(text="Medium", fg="orange")
    elif score == 4:
        strength_label.config(text="Strong", fg="blue")
    else:
        strength_label.config(text="Very Strong", fg="green")


def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("Password Generator")
window.geometry("420x560")
window.configure(bg="#020617")
window.resizable(False, False)

# Title
tk.Label(
    window, text="Password Generator",
    bg="#020617", fg="white",
    font=("Segoe UI", 20, "bold")
).pack(pady=10)

tk.Label(
    window, text="Create strong, secure passwords instantly",
    bg="#020617", fg="#9ca3af",
    font=("Segoe UI", 10)
).pack()

# Password display
password_var = tk.StringVar(value="Click Generate")

frame = tk.Frame(window, bg="#020617")
frame.pack(pady=20)

entry = tk.Entry(
    frame, textvariable=password_var,
    font=("Consolas", 14),
    width=22, bd=0, justify="center"
)
entry.pack(side="left", padx=5)

tk.Button(frame, text="📋", command=copy_password).pack(side="left")
tk.Button(frame, text="🔄", command=generate_password).pack(side="left")

# Strength
strength_frame = tk.Frame(window, bg="#020617")
strength_frame.pack(pady=10, fill="x", padx=20)

tk.Label(
    strength_frame, text="Password Strength",
    bg="#020617", fg="white"
).pack(side="left")

strength_label = tk.Label(
    strength_frame, text="—",
    bg="#020617", fg="white", font=("Segoe UI", 10, "bold")
)
strength_label.pack(side="right")

# Length slider
length_var = tk.IntVar(value=16)

length_frame = tk.Frame(window, bg="#020617")
length_frame.pack(pady=10, fill="x", padx=20)

tk.Label(
    length_frame, text="Password Length",
    bg="#020617", fg="white"
).pack(side="left")

tk.Label(
    length_frame, textvariable=length_var,
    bg="#020617", fg="#3b82f6"
).pack(side="right")

tk.Scale(
    window, from_=6, to=32,
    orient="horizontal",
    variable=length_var,
    bg="#020617", fg="white",
    troughcolor="#1e3a8a",
    highlightthickness=0
).pack(fill="x", padx=20)

# Options
tk.Label(
    window, text="Character Types",
    bg="#020617", fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=10)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

def option(text, var):
    f = tk.Frame(window, bg="#020617")
    f.pack(fill="x", padx=40, pady=4)
    tk.Checkbutton(
        f, text=text, variable=var,
        bg="#020617", fg="white",
        selectcolor="#020617",
        activebackground="#020617"
    ).pack(anchor="w")

option("Uppercase (A-Z)", upper_var)
option("Lowercase (a-z)", lower_var)
option("Numbers (0-9)", number_var)
option("Symbols (!@#$)", symbol_var)

# Generate button
tk.Button(
    window, text="🔄 Generate New Password",
    command=generate_password,
    bg="#2563eb", fg="white",
    font=("Segoe UI", 12),
    bd=0, height=2
).pack(pady=20, fill="x", padx=40)

window.mainloop()
