class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable for dog's name

    def bark(self):
        print(f"{self.name} is barking!")

# Example
dog = Dog("Scoby")
dog.bark()  # Calling the bark method
