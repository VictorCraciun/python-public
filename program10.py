# Use the libraries tkinter
# Make a Telephone Book
import tkinter as tk
from tkinter import messagebox

# Initialize empty lists for storing contacts
list_first_name = []
list_second_name = []
list_telephone_number = []

def add_contact():
    # Get the input data
    first_name = first_name_entry.get()
    second_name = second_name_entry.get()
    telephone_number = telephone_number_entry.get()

    # Check if any of the fields are empty
    if not first_name or not second_name or not telephone_number:
        messagebox.showerror("Input Error", "Please fill in all fields.")
    else:
        # Append the data to the respective lists
        list_first_name.append(first_name)
        list_second_name.append(second_name)
        list_telephone_number.append(telephone_number)

        # Update result label and clear the input fields
        result_label.config(text='Contact added')
        first_name_entry.delete(0, tk.END)
        second_name_entry.delete(0, tk.END)
        telephone_number_entry.delete(0, tk.END)

def show_contacts():
    # Clear the Listbox before showing the contacts
    contact_listbox.delete(0, tk.END)
    
    if not list_first_name:
        messagebox.showinfo("No Contacts", "No contacts have been added yet.")
    else:
        # Insert each contact into the Listbox
        for i in range(len(list_first_name)):
            contact_listbox.insert(tk.END, f'{list_first_name[i]} {list_second_name[i]}: {list_telephone_number[i]}')

def search_contact():
    # Clear the Listbox before showing the contacts
    contact_listbox.delete(0, tk.END)
    
    if not list_first_name:
        messagebox.showinfo("No Contacts", "No contacts have been added yet.")
    else:
        # Insert each contact into the Listbox
        contact_found = False
        for i in range(len(list_first_name)):
            if list_first_name[i]== first_name_entry.get() or list_second_name[i] == second_name_entry.get() or list_telephone_number[i] == telephone_number_entry.get():
                contact_listbox.insert(tk.END, f'{list_first_name[i]} {list_second_name[i]}: {list_telephone_number[i]}')
                contact_found = True
        if contact_found == False: contact_listbox.insert(tk.END, "Not find this contact")
root = tk.Tk()
root.title("Telephone Book")

tk.Label(root, text="First Name:").pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

tk.Label(root, text="Second Name:").pack()
second_name_entry = tk.Entry(root)
second_name_entry.pack()

tk.Label(root, text="Telephone number:").pack()
telephone_number_entry = tk.Entry(root)
telephone_number_entry.pack()

# Button to add contact
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

# Button to show all contacts
show_button = tk.Button(root, text="Show All Contacts", command=show_contacts)
show_button.pack()

# Button to add contact
search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

contact_listbox = tk.Listbox(root, height=10, width=50)
contact_listbox.pack()

# Run the main loop
root.mainloop()
