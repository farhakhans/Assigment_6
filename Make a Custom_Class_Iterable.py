class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize countdown start number
        self.current = start  # Set the current count to start

    # __iter__ method makes the object iterable
    def __iter__(self):
        return self  # Return the object itself as the iterator

    # __next__ method defines the countdown logic
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when current count reaches 0
        else:
            self.current -= 1  # Decrease the count by 1
            return self.current  # Return the current countdown value

# Create a Countdown object starting from 5
countdown = Countdown(5)

# Using the Countdown object in a for-loop
for number in countdown:
    print(number)
