import streamlit as st
from calculator import Operations

st.title("Basic Calculator")

# Get user input
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Create an instance of Operations
calc = Operations(num1, num2)

# Select operation
ops = st.selectbox("Choose operation", ["Addition", "Subtraction", "Multiplication", "Division", "Power"])

# Perform operation based on selection
if ops == "Addition":
    result = calc.addition()
elif ops == "Subtraction":
    result = calc.subtraction()
elif ops == "Multiplication":
    result = calc.multiplication()
elif ops == "Division":
    try:
        result = calc.division()
    except ValueError as e:
        result = str(e)
else:
    result = calc.power()

# Display the result
st.write(f"Result: {result}")
