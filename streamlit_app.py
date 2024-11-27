import streamlit as st
import requests
import random
import time
from academic_assistant import AcademicAssistant

# Crear instancia del asistente académico
assistant = AcademicAssistant()

# obtener respuesta del chatbot
def get_bot_response(user_input, mode):
    prompt_template = assistant.__________(mode)
    response_content = assistant._________(user_input, prompt_template)
    return response_content



# Simulación de respuesta del bot palabra por palabra
def response_generator(message: str):
    import time
    time.sleep(2)
    for word in message.split():
        yield word + " "
        time_to_sleep = random.random() * 0.1
        time.sleep(time_to_sleep)




# Configuración inicial del estado
if "mode" not in st.session_state:
    st.session_state.mode = "Repaso 🧠"  # Modo predeterminado
if "messages" not in st.session_state:
    st.session_state.messages = []




# Ruta del avatar del usuario
USER_AVATAR = "assets/student_logo.svg"
BOT_AVATAR = "assets/assistant_logo.svg"





# Barra lateral para selección del modo (centrado)
st.sidebar.______(
    """
    <div style="text-align: center;">
        <h2>Modo de Estudio</h2>
    </div>
    """,
    unsafe_allow_html=True
)





# Radio buttons para seleccionar el modo
mode = st._______.______(
    "Seleccione el modo de estudio",
    ["Repaso 🧠", "Simulacro 📝"],
    label_visibility="collapsed",
    index=0
)
st.session_state.mode = mode

# Espaciador para centrar el botón de borrar chat
st._____.______(
    "<br><br>"*10, 
    unsafe_allow_html=True
    )


# Botón de borrado del chat
if st.______("🗑️ Borrar chat", key="clear_chat"):
    st.______.______ = []
    st.sidebar.______("¡El historial del chat ha sido borrado!")



# Pantalla principal del chatbot

# Título centrado
st.______(
    "<h1 style='text-align: center;'>_________________</h1>",
    unsafe_allow_html=True
)

# Texto del modo centrado con emoji
mode_text = f"Modo: {st.session_state.mode}"
st.markdown(
    f"<h3 style='text-align: center;'>{mode_text}</h3>",
    unsafe_allow_html=True
)




# Mostrar mensajes del historial
for message in st.___________.____________:
    with st.___________(message["role"], avatar=USER_AVATAR if message["role"] == "user" else BOT_AVATAR):
        st.____________(message["content"])

# Campo de entrada del usuario
if prompt := st.______________("Escribe tu mensaje:"):

    # Agregar mensaje del usuario al historial
    st.session_state.___________.___________({"role": "user", "content": prompt})

    # Mostrar el mensaje del usuario con su avatar
    with st.___________("user", avatar=USER_AVATAR):
        st.____________(prompt)

    # Obtener respuesta del bot
    try:
        bot_response = ______________( _____________ , _____________[:-2].lower())

    except:
        bot_response = "No se pudo conectar con el servidor."

    # Mostrar respuesta del bot con animación
    with st.____________( "assistant", avatar=BOT_AVATAR ):
        st._____________( response_generator(bot_response) )

    # Agregar respuesta al historial
    st.___________.___________._________({"role": "assistant", "content": bot_response})



