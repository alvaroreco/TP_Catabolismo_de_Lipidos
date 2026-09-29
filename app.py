import streamlit as st

st.title("Gemelo Digital de la Mitocondria")

tejido = st.selectbox(
    "Tejido",
    ["Hígado", "Corazón", "Músculo"]
)

estado = st.selectbox(
    "Estado nutricional",
    ["Alimentado", "Ayuno 24h", "Ayuno 48h"]
)

if st.button("Simular"):
    st.success(f"Simulación para {tejido}")
