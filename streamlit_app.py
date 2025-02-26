import streamlit as st
import random
import time
from academic_assistant import AcademicAssistant

# Función para mostrar un tablero de sudoku (ejemplo simple)
def open_sudoku():
    st.header("Juego de Sudoku")
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    for row in board:
        st.write(row)

# Crear instancia del asistente académico para el flujo normal
assistant = AcademicAssistant()

def get_bot_response(user_input, mode):
    prompt_template = assistant.select_prompt_template(mode)
    response_content = assistant.generate_response(user_input, prompt_template)
    return response_content

def response_generator(message: str):
    time.sleep(2)
    for word in message.split():
        yield word + " "
        time_to_sleep = random.random() * 0.1
        time.sleep(time_to_sleep)

# Estado inicial en session_state
if "mode" not in st.session_state:
    st.session_state.mode = "Repaso 🧠"  # Modo predeterminado
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sudoku_pending" not in st.session_state:
    st.session_state.sudoku_pending = False

USER_AVATAR = "assets/student_logo.svg"
BOT_AVATAR = "assets/assistant_logo.svg"

st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <h2>Modo de Estudio</h2>
    </div>
    """, unsafe_allow_html=True
)

mode = st.sidebar.radio(
    "Seleccione el modo de estudio",
    ["Repaso 🧠", "Simulacro 📝"],
    label_visibility="collapsed",
    index=0
)
st.session_state.mode = mode

st.sidebar.markdown("<br><br>"*10, unsafe_allow_html=True)

if st.sidebar.button("🗑️ Borrar chat", key="clear_chat"):
    st.session_state.messages = []
    st.sidebar.success("¡El historial del chat ha sido borrado!")

st.markdown(
    "<h1 style='text-align: center;'>Asistente Virtual CC</h1>",
    unsafe_allow_html=True
)
mode_text = f"Modo: {st.session_state.mode}"
st.markdown(
    f"<h3 style='text-align: center;'>{mode_text}</h3>",
    unsafe_allow_html=True
)

# Mostrar historial del chat
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=USER_AVATAR if message["role"] == "user" else BOT_AVATAR):
        st.markdown(message["content"])

# Campo de entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)
    
    # Si la entrada contiene "sudoku", activamos la bandera
    if "sudoku" in prompt.lower():
        st.session_state.sudoku_pending = True
    
    # Si hay un comando de sudoku pendiente, mostramos la confirmación
    if st.session_state.sudoku_pending:
        confirm = st.radio(
            "Se detectó un comando relacionado con Sudoku. ¿Desea iniciar el juego de Sudoku?",
            options=["Sí", "No"],
            key="sudoku_confirm"
        )
        if confirm == "Sí":
            with st.chat_message("assistant", avatar=BOT_AVATAR):
                st.write("Iniciando el juego de Sudoku...")
            open_sudoku()
            st.session_state.messages.append({"role": "assistant", "content": "Juego de Sudoku iniciado."})
        else:
            # Si el usuario no confirma, continúa el flujo normal (podrías enviar el mensaje al chatbot)
            try:
                bot_response = get_bot_response(prompt, st.session_state.mode[:-2].lower())
            except Exception as e:
                bot_response = "No se pudo conectar con el servidor."
            with st.chat_message("assistant", avatar=BOT_AVATAR):
                st.write_stream(response_generator(bot_response))
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
        # Una vez confirmada la opción (Sí o No), reiniciamos la bandera
        st.session_state.sudoku_pending = False
    else:
        # Flujo normal: enviar el mensaje al chatbot
        try:
            bot_response = get_bot_response(prompt, st.session_state.mode[:-2].lower())
        except Exception as e:
            bot_response = "No se pudo conectar con el servidor."
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.write_stream(response_generator(bot_response))
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
