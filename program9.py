# Use the libraries tkinter
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = int(first_number_entry.get())
        num2 = int(second_number_entry.get())
        total = num1 + num2
        avg = total / 2
        result_label.config(text=f'Sum: {total}, Average: {avg}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")


root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="First Number:").pack()
first_number_entry = tk.Entry(root)
first_number_entry.pack()

tk.Label(root, text="Second Number:").pack()
second_number_entry = tk.Entry(root)
second_number_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
