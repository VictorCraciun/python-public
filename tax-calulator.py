import ipywidgets as widgets
from IPython.display import display

# Employee class to store and calculate tax for an employee
class Employees:
    def __init__(self, full_name, company_name, employees_income):
        self.full_name = full_name
        self.company_name = company_name
        self.employees_income = employees_income

    # Method to calculate the tax based on income
    def calculate_tax(self):
        if self.employees_income <= 20000:
            tax = 0
        elif self.employees_income <= 100000:
            tax = (self.employees_income - 20000) * 0.2
        else:
            tax = (self.employees_income - 100000) * 0.45 + (100000 - 20000) * 0.2
        return tax

    # Method to determine the tax band based on income
    def get_tax_band(self):
        if self.employees_income <= 20000:
            return "0% (No Tax)"
        elif self.employees_income <= 100000:
            return "20% Tax Band"
        else:
            return "45% Tax Band"

    # Method to calculate the net pay (income - tax)
    def calculate_net_pay(self):
        return self.employees_income - self.calculate_tax()

    # Method to display a payslip for the employee
    def generate_payslip(self):
        tax = self.calculate_tax()
        net_pay = self.calculate_net_pay()
        tax_band = self.get_tax_band()

        payslip = f"""
        Payslip for {self.full_name}:
        -----------------------------------
        Company Name: {self.company_name}
        Income: ${self.employees_income:,.2f}
        Tax Band: {tax_band}
        Income Tax: ${tax:,.2f}
        Net Pay: ${net_pay:,.2f}
        -----------------------------------
        """
        return payslip

# List to store multiple employee objects
employee_list = []

# Function to add an employee to the list and display tax details
def add_employee(change):
    output.clear_output()

    # Input validation
    if not full_name.value.strip():
        with output:
            print("Please enter a valid full name.")
        return

    if company_name.value.lower() != "alltrade":
        company_name.value = ""
        with output:
            print("Incorrect company name. Please enter the correct one (Alltrade):")
        return

    if employees_income.value <= 0:
        with output:
            print("Please enter a valid income greater than 0.")
        return

    # Add employee if all inputs are valid
    employee = Employees(full_name.value, company_name.value, employees_income.value)
    employee_list.append(employee)
    
    # Display added employee details and calculated tax
    with output:
        print(f'{employee.full_name} added. Needs to pay tax of ${employee.calculate_tax():,.2f}')

# Function to generate and display payslips for all employees
def generate_payslips(change):
    output.clear_output()
    with output:
        if employee_list:
            for employee in employee_list:
                print(employee.generate_payslip())
        else:
            print("No employees available to generate payslips.")

# Widgets for user input
full_name = widgets.Text(description="Full Name")
company_name = widgets.Text(description="Company Name")
employees_income = widgets.FloatText(description="Income:")

# Buttons
add_button = widgets.Button(description="Add Employee")
add_button.on_click(add_employee)

payslip_button = widgets.Button(description="Generate Payslips")
payslip_button.on_click(generate_payslips)

# Output widget to display messages
output = widgets.Output()

# Display the input fields, buttons, and output on the screen
display(full_name, company_name, employees_income, add_button, payslip_button, output)
