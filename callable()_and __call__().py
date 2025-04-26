class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor

    def __call__(self, number):
        return number * self.factor  # Multiply input by factor

# Create Multiplier object with factor 5
multiplier = Multiplier(5)

# Test with callable()
print(callable(multiplier))  # Should return True

# Call the object like a function
result = multiplier(10)  # This will call __call__ method
print(f"Result of multiplication: {result}")
