# Parent class A
class A:
    def show(self):
        print("Show method from Class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("Show method from Class B")

# Class C inherits from A
class C(A):
    def show(self):
        print("Show method from Class C")

# Class D inherits from B and C
class D(B, C):
    pass

# Create object of D
d = D()

# Call show method
d.show()
