import streamlit as st


conversions = {
    "Speed": {
        "m/s": 1,
        "km/h": 3.6,
        "mph": 2.237,
        "knots": 1.944,
    },
    "Length": {
        "m": 1,
        "km": 0.001,
        "cm": 100,
        "mm": 1000,
    },
    "Weight": {
        "kg": 1,
        "g": 1000,
        "lb": 2.205,
        "oz": 35.274,
    },
    "Time": {
        "seconds": 1,
        "minutes": 1/60,
        "hours": 1/3600,
        "days": 1/86400,
    },
}

def convert_units(category, value, from_unit, to_unit):
    if category in conversions:
        factor = conversions[category]
        if from_unit in factor and to_unit in factor:
            return value * (factor[to_unit] / factor[from_unit])
    return None

st.title(" 🔢Unit Converter")

category = st.selectbox("Select Category", ["Speed", "Length", "Weight", "Time"])

titles = {
    "Speed": "SPEED 🚀",
    "Length": "LENGTH 📏",
    "Weight": "WEIGHT ⚖️",
    "Time": "TIME ⏳",
}
st.header(titles[category])

value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=1.0)

units = {
    "Speed": ["m/s", "km/h", "mph", "knots"],
    "Length": ["m", "km", "cm", "mm"],
    "Weight": ["kg", "g", "lb", "oz"],
    "Time": ["seconds", "minutes", "hours", "days"],
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.write(f"### Explanation:")
        st.write(f"1 {from_unit} = {conversions[category][to_unit] / conversions[category][from_unit]:.4f} {to_unit}")
    else:
        st.error("Conversion not available.")

st.write("### Leave a Review 📝")
review = st.text_area("Share your experience:")
if st.button("Submit Review"):
    if review:
        st.success("Thank you for your feedback!")
    else:
        st.error("Please write a review before submitting.")
