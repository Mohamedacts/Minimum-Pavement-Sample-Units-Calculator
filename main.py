import streamlit as st
import math

# --- User Info ---
NAME = "Mohamed Ali"
ROLE = "Pavement Engineer"
PHONE = "00966581764292"

st.set_page_config(page_title="Minimum Pavement Sample Units Calculator", page_icon="🛣️")

st.title("🛣️ Minimum Pavement Sample Units Calculator")
st.write("Calculate the minimum number of sample units to inspect for road PCI surveys (ASTM D6433-07).")

# --- Input Section ---
st.header("1. Pavement Information")

pavement_type = st.selectbox(
    "Select Pavement Type:",
    ("Flexible (Asphalt Concrete)", "Rigid (Portland Cement Concrete)")
)

area = st.number_input(
    "Enter total pavement area (m²):",
    min_value=1,
    value=5000,
    step=1
)

if pavement_type == "Flexible (Asphalt Concrete)":
    s = 10
    sample_unit_area = 225  # m²
    st.info("Standard deviation (s) for Flexible Pavement: 10\nSample unit area: 225 m²")
else:
    s = 15
    sample_unit_area = 225  # For simplicity, use 225 m² per sample unit (you can adjust for slabs if needed)
    st.info("Standard deviation (s) for Rigid Pavement: 15\nSample unit area: 225 m² (adjust for slab size if known)")

e = 5  # Acceptable error in PCI points

# --- Calculation Section ---
st.header("2. Calculation")

# Total sample units
N = math.ceil(area / sample_unit_area)

# Minimum sample units to survey (ASTM D6433-07 formula)
numerator = N * s**2
denominator = ((e**2) / 4) * (N - 1) + s**2
n = math.ceil(numerator / denominator)

st.write(f"**Total number of sample units:** {N}")
st.write(f"**Minimum number of sample units to survey (for 95% confidence):** {n}")

st.markdown("---")

# --- Credentials Section ---
st.header("About the Developer")
st.write(f"**Name:** {NAME}")
st.write(f"**Role:** {ROLE}")
st.write(f"**Phone:** {PHONE}")

