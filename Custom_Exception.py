import streamlit as st

# Custom exception class
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        return "Age is valid"

# Streamlit app interface
st.title("Age Validation")

# Get user input for age
age = st.number_input("Enter your age:", min_value=0)

# Button to check age
if st.button("Check Age"):
    try:
        result = check_age(age)  # Check if age is valid
        st.success(result)  # If valid, show success message
    except InvalidAgeError as e:
        st.error(f"Error: {e}")  # If exception is raised, show error message
