class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):
        print(f"{self.brand} car is starting...")

# Example
my_car = Car("SWEEFT")

# Accessing from outside
print(my_car.brand)  # Accessing public variable
my_car.start()       # Accessing public method
