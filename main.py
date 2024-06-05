import time
import streamlit as st
from app.generator import generator
from langchain_core.messages import AIMessage, HumanMessage


st.set_page_config(page_title='Gym Coach')
st.header('Goat your Gym Coach')
st.text(body='Hi! My name is Goat your personalized AI Gym Coach, confused about workout schedule')
st.text(body='no tension I got your back! Just let me know which muscle your planing to hit today!')
st.text('')

input = st.chat_input(
    "Enter the Muscle name for which your planing to hit today!: ")


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [AIMessage('Hi! I am your Workout Coach. How can I help you?')]


for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)
    else:
        with st.chat_message('AI'):
            st.write(message.content)

if input:
    response = generator.stream({'question': input})
    with st.chat_message('Human'):
        st.write(input)
        st.session_state.chat_history.append(HumanMessage(content=input))
    with st.chat_message("AI"):
        ans = st.write_stream(response)
        st.session_state.chat_history.append(AIMessage(content=ans))
