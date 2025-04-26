class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable

# Example
emp = Employee("Farhana", 50000, "123-45-6789")

# Accessing all variables
print("Name:", emp.name)        # Public variable - accessible
print("Salary:", emp._salary)   # Protected variable - accessible (but should be accessed cautiously)
# print("SSN:", emp.__ssn)      # Private variable - will raise an error if uncommented

# Accessing the private variable using name mangling
print("SSN (private, with name mangling):", emp._Employee__ssn)
