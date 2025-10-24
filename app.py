import streamlit as st
from PIL import Image

st.markdown("""
    <style>
    body {
        background-color: #F6F5F2;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #FFE66D;
        color: #222;
        border-radius: 20px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌼 App Multimodal Minimalista 🌼")
st.header("Un diseño limpio y equilibrado para una mejor experiencia de usuario.")
st.write("En este entorno puedes experimentar con distintos componentes de Streamlit.")

image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Interfaz limpia y moderna', use_column_width=True)

texto = st.text_input('💬 Escribe algo:', '')
st.write("Tu texto:", texto)

col1, col2 = st.columns(2)
with col1:
    if st.checkbox('Estoy de acuerdo'):
        st.success('Perfecto 🌸')
with col2:
    modo = st.radio("Modalidad:", ('Visual', 'Auditiva', 'Táctil'))
    st.info(f"Modo seleccionado: {modo}")

if st.button('Presiona 🌼'):
    st.success('¡Gracias por interactuar!')

opcion = st.selectbox("Selecciona la modalidad principal:", ("Audio", "Visual", "Háptico"))
st.write("Acción seleccionada:", opcion)

with st.sidebar:
    st.header("Configuración 🌈")
    st.radio("Escoge la modalidad:", ("Visual", "Auditiva", "Háptica"))

