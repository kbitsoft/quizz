import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Invalid username or password")

root = tk.Tk()
root.geometry("300x200")
root.title("Login Form")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
