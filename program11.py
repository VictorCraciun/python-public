# Use the libraries tkinter
# Tax calculator
import tkinter as tk
from tkinter import messagebox

#function for calulate tax
def calculate():
    employees_income = float(income_entry.get())
    if company_entry.get().lower() != "alltrade":
        company_entry.value = ""
        messagebox.showerror("Input Error", "Incorrect company name. Please enter the correct one:")
    else:
        if employees_income <= 20000:
            tax = 0
        elif employees_income <= 100000:
            tax = (employees_income - 20000) * 0.2
        else:
            tax = (employees_income - 100000) * 0.45 + (100000 - 20000) * 0.2

       # Update result label
        result_label.config(text=f'{full_name_entry.get()} needs to pay tax of {tax:.2f}')

root = tk.Tk()

#Labels to show entry details
root.title("Tax calculation")

tk.Label(root, text="Full Name:").pack()
full_name_entry = tk.Entry(root)
full_name_entry.pack()

tk.Label(root, text="Company:").pack()
company_entry = tk.Entry(root)
company_entry.pack()

tk.Label(root, text="Income:").pack()
income_entry = tk.Entry(root)
income_entry.pack()

# Button to calculate tax
calculate_tax_button = tk.Button(root, text="Calculate TAX", command=calculate)
calculate_tax_button.pack()

# Label to show results
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
