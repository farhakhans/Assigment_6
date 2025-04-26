import streamlit as st

st.title("🌡️ Temperature Converter")

st.subheader("Convert Celsius (°C) to Fahrenheit (°F)")

# Input from user
celsius = st.number_input("Enter Temperature in Celsius:", format="%.2f")

# Formula
fahrenheit = (celsius * 9/5) + 32

# Display result nicely
st.success(f"🌟 {celsius}°C = {fahrenheit}°F")
