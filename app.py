import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Mi App Multimodal",
    page_icon="✨",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background-color: #f9f7fd;
        color: #3a2e5f;
        font-family: 'Poppins', sans-serif;
    }

    /* Títulos */
    h1 {
        color: #7b2cbf;
        text-align: center;
        font-weight: 700;
    }

    h2, h3 {
        color: #9c4dcc;
    }

    /* Botones */
    div.stButton > button {
        background-color: #9c4dcc;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
        border: none;
        transition: all 0.3s ease;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #7b2cbf;
        transform: scale(1.03);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f3e8ff;
        color: #3a2e5f;
    }

    /* Selectbox y radio buttons */
    .stSelectbox, .stRadio {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 0.5em;
    }

    /* Inputs */
    input, textarea {
        border-radius: 8px !important;
        border: 1px solid #c9a9ff !important;
    }

    /* Texto del sidebar */
    .sidebar-content {
        padding: 10px;
        color: #3a2e5f;
    }

    </style>
""", unsafe_allow_html=True)


# --- CONTENIDO PRINCIPAL ---
st.title("🌸 Mi Primera App Multimodal 🌸")
st.write("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Aquí combino elementos de interacción visual, auditiva y táctil para mejorar la experiencia del usuario.")

# Imagen principal
image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Interfaces Multimodales', use_container_width=True)

# Texto de entrada
texto = st.text_input('💬 Escribe algo:', 'Este es mi texto')
st.write('Tu texto es:', f"**{texto}**")

# --- COLUMNAS INTERACTIVAS ---
st.subheader("🎨 Interacción por columnas")
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('¡Correcto!')

with col2:
    st.markdown("##### Segunda columna")
    modo = st.radio("¿Qué modalidad es principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.info('👁️ La vista es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.info('🎧 La audición es fundamental para tu interfaz.')
    else:
        st.info('✋ El tacto es fundamental para tu interfaz.')

# --- BOTÓN Y SELECTBOX ---
st.subheader("🪄 Interacción adicional")

if st.button('Presiona el botón ✨'):
    st.balloons()
    st.success('¡Gracias por presionar el botón!')
else:
    st.write('Aún no has presionado el botón.')

in_mod = st.selectbox(
    "Selecciona la modalidad principal:",
    ("Audio", "Visual", "Háptico"),
)

acciones = {
    "Audio": "🔊 Reproducir sonido",
    "Visual": "🎞️ Reproducir video",
    "Háptico": "💫 Activar vibración"
}
st.write("La acción correspondiente es:", acciones[in_mod])

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Configuración")
    st.markdown("Personaliza tu experiencia multimodal:")
    mod_radio = st.radio("Escoge la modalidad a usar:", ("Visual", "Auditiva", "Háptica"))
    st.markdown("---")
    st.markdown("🌷 *App creada por María José Velásquez*")

