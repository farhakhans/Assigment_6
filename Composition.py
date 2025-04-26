# Engine class
class Engine:
    def start(self):
        return "Engine started!"

# Car class
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Access Engine's method

# Create Engine object
my_engine = Engine()

# Pass Engine object to Car
my_car = Car(my_engine)

# Use Car method to start the engine
print(my_car.start_car())
