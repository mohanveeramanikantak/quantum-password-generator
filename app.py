import streamlit as st
from quantum_password import generate_password, check_strength

st.set_page_config(page_title="Quantum Password Generator", page_icon="🔐")

st.title("Quantum Password Generator")
st.write("Generate secure passwords using quantum randomness.")

length = st.slider("Select password length", 6, 32, 12)

if st.button("Generate Password"):
    password = generate_password(length)
    strength = check_strength(password)

    st.subheader("Generated Password")
    st.code(password)

    st.subheader("Password Strength")
    st.success(strength)