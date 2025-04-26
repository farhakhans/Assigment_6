class Counter:
    objects_made = 0

    def __init__(self):
        type(self).objects_made += 1

    @classmethod
    def total(cls):
        print("Created:", cls.objects_made)

# Example
x = Counter()
y = Counter()
z = Counter()

x.total()
