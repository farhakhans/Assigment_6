import streamlit as st

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            st.error("Price can't be negative!")
        else:
            self._price = value

    # Deleter for price
    @price.deleter
    def price(self):
        st.warning("Deleting price...")
        del self._price

# Streamlit app interface
st.title("Product Price Management")

# Create product object with an initial price
product = Product(100)

# Display current price
st.subheader("Current Product Price:")
st.write(f"Price: ${product.price}")

# Input field for updating price
new_price = st.number_input("Enter new price:", min_value=0, value=int(product.price))

# Button to update price
if st.button("Update Price"):
    product.price = new_price
    st.success(f"Price updated to: ${product.price}")

# Button to delete price
if st.button("Delete Price"):
    del product.price
    st.info("Price has been deleted.")

