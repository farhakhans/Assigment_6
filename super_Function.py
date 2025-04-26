class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)  # Directly calling Person constructor
        self.subject = subject

# Example
teacher = Teacher("Farhana", "Science")

# Accessing the attributes
print("Teacher Name:", teacher.name)
print("Subject:", teacher.subject)
