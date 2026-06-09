import streamlit as st

st.set_page_config(
    page_title="ICT in Smart Agriculture",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 ICT in Smart Agriculture")
st.subheader("Agricultural Input Calculator")

st.markdown("""
This application helps farmers estimate the required quantity of:
- Seeds
- Fertilizer
- Pesticide Spray
- Estimated Cost

based on the cultivated land area (Acres).
""")

# User Input
acres = st.number_input(
    "Enter Land Area (Acres)",
    min_value=1.0,
    value=1.0,
    step=0.5
)

# Standard values per acre
seed_per_acre = 20      # kg
fertilizer_per_acre = 50 # kg
spray_per_acre = 2      # liters

seed_cost_per_kg = 250      # PKR
fertilizer_cost_per_kg = 120
spray_cost_per_liter = 1800

# Calculations
total_seed = acres * seed_per_acre
total_fertilizer = acres * fertilizer_per_acre
total_spray = acres * spray_per_acre

seed_cost = total_seed * seed_cost_per_kg
fertilizer_cost = total_fertilizer * fertilizer_cost_per_kg
spray_cost = total_spray * spray_cost_per_liter

total_cost = seed_cost + fertilizer_cost + spray_cost

st.header("📊 Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Seeds Required", f"{total_seed:.1f} kg")

with col2:
    st.metric("Fertilizer Required", f"{total_fertilizer:.1f} kg")

with col3:
    st.metric("Spray Required", f"{total_spray:.1f} L")

st.subheader("💰 Estimated Cost")

st.write(f"🌱 Seed Cost: **PKR {seed_cost:,.0f}**")
st.write(f"🧪 Fertilizer Cost: **PKR {fertilizer_cost:,.0f}**")
st.write(f"🚜 Spray Cost: **PKR {spray_cost:,.0f}**")

st.success(f"Total Estimated Cost = PKR {total_cost:,.0f}")

st.header("📈 Cost Breakdown")

cost_data = {
    "Seeds": seed_cost,
    "Fertilizer": fertilizer_cost,
    "Spray": spray_cost
}

st.bar_chart(cost_data)

st.header("👨‍💻 Project Team")

st.markdown("""
- **Maqsood Ahmad (25ME142)**
- **M. Abdullah (25ME162)**
- **M. Haseeb (54)**
- **Azmat u Allah (25ME198)**
- **Syed Sabih Gillani (25ME226)**
""")

st.info("ICT in Smart Agriculture | Streamlit Project")
