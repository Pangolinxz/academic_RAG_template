import streamlit as st
import random
import time
from influencer_assistant import InfluencerAssistant
import datetime
import calendar

class DateNode:
    def __init__(self, date):
        self.date = date
        self.events = []
        self.adjacent_nodes = {}  
    def add_adjacent_node(self, key, node):
        self.adjacent_nodes[key] = node

    def __repr__(self):
        return f"DateNode({self.date.strftime('%Y-%m-%d')})"

class CalendarGraph:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.nodes = {}
        self._generate_nodes()
        self._connect_adjacent_nodes()

    def _generate_nodes(self):
        num_days = calendar.monthrange(self.year, self.month)[1]
        for day in range(1, num_days + 1):
            date = datetime.date(self.year, self.month, day)
            self.nodes[date] = DateNode(date)

    def _connect_adjacent_nodes(self):
        for date in list(self.nodes.keys()):
            node = self.nodes[date]

            next_day = date + datetime.timedelta(days=1)
            if next_day in self.nodes:
                node.add_adjacent_node('next_day', self.nodes[next_day])

            prev_day = date - datetime.timedelta(days=1)
            if prev_day in self.nodes:
                node.add_adjacent_node('prev_day', self.nodes[prev_day])

            next_week = date + datetime.timedelta(weeks=1)
            if next_week in self.nodes:
                node.add_adjacent_node('next_week', self.nodes[next_week])

            prev_week = date - datetime.timedelta(weeks=1)
            if prev_week in self.nodes:
                node.add_adjacent_node('prev_week', self.nodes[prev_week])

    def add_event(self, date, event_name, event_time):
        if date in self.nodes:
            self.nodes[date].events.append({
                'name': event_name,
                'time': event_time
            })
        else:
            raise ValueError("Date not in calendar")

    def display_calendar(self):
        cal = calendar.Calendar()
        weeks = cal.monthdays2calendar(self.year, self.month)
        print(f"Calendar for {datetime.date(self.year, self.month, 1).strftime('%B %Y')}:\n")
        for week in weeks:
            week_str = []
            for day, _ in week:
                if day == 0:
                    week_str.append('  ')
                else:
                    date = datetime.date(self.year, self.month, day)
                    node = self.nodes[date]
                    event_count = len(node.events)
                    week_str.append(f"{day:2}({event_count})")
            print(' '.join(week_str))

assistant = InfluencerAssistant()

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
    st.session_state.mode = "Asistente"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "calendars" not in st.session_state:
    st.session_state.calendars = {}
if "selected_date" not in st.session_state:
    st.session_state.selected_date = datetime.date.today()

USER_AVATAR = "assets/influencer_logo.svg"
BOT_AVATAR = "assets/assistant_logo.svg"

st.sidebar.markdown(
    "<div style='text-align: center;'><h2>Modo de Asistente</h2></div>",
    unsafe_allow_html=True
)
mode = st.sidebar.radio(
    "Seleccione el modo de Asistente",
    ["Asistente  ", "Calendario"],
    label_visibility="collapsed",
    index=0
)
st.session_state.mode = mode

st.sidebar.markdown("<br><br>" * 10, unsafe_allow_html=True)
if st.sidebar.button("🗑️ Borrar chat", key="clear_chat"):
    st.session_state.messages = []
    st.sidebar.success("¡El historial del chat ha sido borrado!")

st.markdown("<h1 style='text-align: center;'>Asistente Virtual CC</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>Modo: {st.session_state.mode}</h3>", unsafe_allow_html=True)


if st.session_state.mode == "Calendario":
    selected_date = st.date_input("Seleccionar fecha", st.session_state.selected_date)
    st.session_state.selected_date = selected_date
    
    current_year = selected_date.year
    current_month = selected_date.month

    if (current_year, current_month) not in st.session_state.calendars:
        st.session_state.calendars[(current_year, current_month)] = CalendarGraph(current_year, current_month)
    
    current_calendar = st.session_state.calendars[(current_year, current_month)]
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        with st.form("event_form"):
            event_name = st.text_input("Nombre del evento")
            event_time = st.time_input("Hora del evento")
            add_event = st.form_submit_button("➕ Añadir evento")
            
            if add_event and event_name:
                try:
                    current_calendar.add_event(
                        selected_date,
                        event_name,
                        event_time.strftime("%H:%M")
                    )
                    st.success("Evento añadido correctamente!")
                    current_calendar.display_calendar()
                except ValueError:
                    st.error("Fecha no válida para este mes")

    with col2:
        st.subheader(f"Calendario de {selected_date.strftime('%B %Y')}")
        

        cal = calendar.Calendar()
        weeks = cal.monthdays2calendar(current_year, current_month)
        
        st.markdown("""
        <style>
        .calendar-day {
            border: 1px solid #e1e4e8;
            padding: 10px;
            min-height: 100px;
        }
        </style>
        """, unsafe_allow_html=True)


        for week in weeks:
            cols = st.columns(7)
            for i, (day, _) in enumerate(week):
                with cols[i]:
                    if day != 0:
                        date = datetime.date(current_year, current_month, day)
                        node = current_calendar.nodes[date]
                        
                        if date == selected_date:
                            st.markdown(f"<div style='background-color: #e3f2fd;' class='calendar-day'>", unsafe_allow_html=True)
                        else:
                            st.markdown("<div class='calendar-day'>", unsafe_allow_html=True)
                        
                        st.markdown(f"**{day}**")
                        for event in node.events:
                            st.markdown(f"⏰ {event['time']} {event['name']}")
                        st.markdown("</div>", unsafe_allow_html=True)
else:

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=USER_AVATAR if message["role"]=="user" else BOT_AVATAR):
            st.markdown(message["content"])


    if prompt := st.chat_input("Escribe tu mensaje:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)
        

        try:
            bot_response = get_bot_response(prompt, st.session_state.mode[:-2].lower())
        except Exception as e:
            bot_response = "No se pudo conectar con el servidor."
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.write_stream(response_generator(bot_response))
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
