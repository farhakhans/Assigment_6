class Bank:
    bank_name = "Al_Habib"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
b2 = Bank()

print("Before changing:")
print(b1.bank_name)
print(b2.bank_name)

# Change bank name
Bank.change_bank_name("Sindh Bank")

print("\nAfter changing:")
print(b1.bank_name)
print(b2.bank_name)
