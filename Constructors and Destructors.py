class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example
log = Logger()

# When program ends or object is deleted
del log
