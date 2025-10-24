import streamlit as st
from PIL import Image

st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #EAEAEA;
        font-family: 'Courier New', monospace;
    }
    h1 {
        color: #BB86FC;
        text-align: center;
    }
    .stButton>button {
        background-color: #03DAC6;
        color: black;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #018786;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌙 App Multimodal - Modo Oscuro")
st.header("Diseño elegante y moderno con contrastes brillantes.")
st.write("Interfaz creada para explorar diferentes modalidades interactivas en un entorno oscuro.")

image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Diseño de interfaz', use_column_width=True)

texto = st.text_input('Escribe algo 👇', '')
st.write(f"Texto ingresado: **{texto}**")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Primera columna")
    if st.checkbox('Estoy de acuerdo'):
        st.success('Genial 💫')

with col2:
    modo = st.radio("Modalidad:", ('Visual', 'Auditiva', 'Táctil'))
    st.info(f"Has seleccionado: {modo}")

if st.button('Presiona el botón 🔘'):
    st.balloons()
    st.write('🎉 ¡Gracias por interactuar!')
else:
    st.warning('Aún no has presionado.')

in_mod = st.selectbox("Selecciona la modalidad principal:", ("Audio", "Visual", "Háptico"))
acciones = {"Audio": "Reproducir sonido 🎵", "Visual": "Mostrar video 🎬", "Háptico": "Vibración 🔔"}
st.write("Acción:", acciones[in_mod])

with st.sidebar:
    st.header("⚙️ Configuración de Modalidad")
    st.radio("Selecciona:", ("Visual", "Auditiva", "Háptica"))
