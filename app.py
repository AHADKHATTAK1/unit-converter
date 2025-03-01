import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

st.title("Unit Converter🔀")

categories = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour"],
}

category = st.selectbox("Select a category", list(categories.keys()))

from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])

value = st.number_input("Enter value", min_value=0.0, step=0.1)

if st.button("Convert"):
    try:
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")