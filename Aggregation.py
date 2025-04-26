# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

# Department class
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: storing reference of Employee

    def show_details(self):
        print(f"Department: {self.department_name}")
        print(f"Employee Name: {self.employee.name}")

# Create Employee object
emp1 = Employee("Farhana")

# Create Department object, pass Employee object
dept1 = Department("Information Technology", emp1)

# Show department and employee details
dept1.show_details()
