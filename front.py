import streamlit as st
from chatbot import predict_class, get_response, intents

# Título de la aplicación
st.title("🤖 Chatbox CAATECH")

# Inicialización de variables de sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mostrar el mensaje inicial del asistente
if st.session_state.first_message:
    with st.chat_message("assistant"):
        initial_message = "Hola, ¿cómo puedo ayudarte?"
        st.markdown(initial_message)
        st.session_state.messages.append({"role": "assistant", "content": initial_message})
        st.session_state.first_message = False

# Procesar entrada del usuario
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Predicción de intención y generación de respuesta
    try:
        # Obtener intención y manejar errores
        insts = predict_class(prompt)
        if not insts:  # Caso en que no se entienda la intención
            res = "Lo siento, no entendí tu consulta. ¿Podrías reformularla?"
        else:
            res = get_response(insts, intents)  # Obtener respuesta

    except Exception as e:
        # Registrar el error en la consola de Streamlit para depuración
        st.error(f"Error interno: {e}")
        res = "Lo siento, ocurrió un problema al procesar tu solicitud. Inténtalo nuevamente."

    # Mostrar respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(res)
        st.session_state.messages.append({"role": "assistant", "content": res})
import streamlit as st
from chatbot import predict_class, get_response, intents

# Título de la aplicación
st.title("🤖 Chatbox")

# Inicialización de variables de sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mostrar el mensaje inicial del asistente
if st.session_state.first_message:
    with st.chat_message("assistant"):
        initial_message = "Hola, ¿cómo puedo ayudarte?"
        st.markdown(initial_message)
        st.session_state.messages.append({"role": "assistant", "content": initial_message})
        st.session_state.first_message = False

# Procesar entrada del usuario
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Predicción de intención y generación de respuesta
    try:
        # Obtener intención y manejar errores
        insts = predict_class(prompt)
        if not insts:  # Caso en que no se entienda la intención
            res = "Lo siento, no entendí tu consulta. ¿Podrías reformularla?"
        else:
            res = get_response(insts, intents)  # Obtener respuesta

    except Exception as e:
        # Registrar el error en la consola de Streamlit para depuración
        st.error(f"Error interno: {e}")
        res = "Lo siento, ocurrió un problema al procesar tu solicitud. Inténtalo nuevamente."

    # Mostrar respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(res)
        st.session_state.messages.append({"role": "assistant", "content": res})
