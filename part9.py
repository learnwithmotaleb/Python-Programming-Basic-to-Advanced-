
# name = input("Enter your name:")
# print("Welcome to ",name)

# age = int(input("Enter your age: "))
# pi = float(input("Enter the value of pi: "))

# print("Your age is : ",age, "and the pi is ",pi)

import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("User Input Example")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Entry (Input Box)
entry = tk.Entry(root)
entry.pack(pady=5)

# Function to show input
def show_input():
    name = entry.get()
    messagebox.showinfo("Result", f"Hello, {name}!")

# Button
button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

# Run App
root.mainloop()
