import streamlit as st
import requests
import random
import time
from academic_assistant import AcademicAssistant

 # Crear instancia del asistente académico
assistant = AcademicAssistant()

# obtener respuesta del chatbot
def get_bot_response(user_input, mode):
    prompt_template = assistant.select_prompt_template(mode)
    response_content = assistant.generate_response(user_input, prompt_template)
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
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <h2>Modo de Estudio</h2>
    </div>
    """,
    unsafe_allow_html=True
)





# Radio buttons para seleccionar el modo
mode = st.sidebar.radio(
    "Seleccione el modo de estudio",
    ["Repaso 🧠", "Simulacro 📝"],
    label_visibility="collapsed",
    index=0
)
st.session_state.mode = mode

# Espaciador para centrar el botón de borrar chat
st.sidebar.markdown(
    "<br><br>"*10, 
    unsafe_allow_html=True
    )


# Botón de borrado del chat
if st.sidebar.button("🗑️ Borrar chat", key="clear_chat"):
    st.session_state.messages = []
    st.sidebar.success("¡El historial del chat ha sido borrado!")



# Pantalla principal del chatbot

# Título centrado
st.markdown(
    "<h1 style='text-align: center;'>Asistente Academico</h1>",
    unsafe_allow_html=True
)

# Texto del modo centrado con emoji
mode_text = f"Modo: {st.session_state.mode}"
st.markdown(
    f"<h3 style='text-align: center;'>{mode_text}</h3>",
    unsafe_allow_html=True
)




# Mostrar mensajes del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=USER_AVATAR if message["role"] == "user" else BOT_AVATAR):
        st.markdown(message["content"])

# Campo de entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje:"):

    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostrar el mensaje del usuario con su avatar
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    #Obtener respuesta del bot
    try:
        bot_response = get_bot_response( prompt , st.session_state.mode[:-2].lower())

    except:
        bot_response = "No se pudo conectar con el servidor."

    # Mostrar respuesta del bot con animación
    with st.chat_message( "assistant", avatar=BOT_AVATAR ):
        st.write_stream( response_generator(bot_response))

    # Agregar respuesta al historial
    st.session_state.messages.append({"role": "assistant", "content": bot_response})



