from app.generator import generator
import streamlit as st


st.set_page_config(page_title='Gym Coach')
st.header('Goat your Gym Coach')
st.text(body='Hi! My name is Goat your personalized AI Gym Coach, confused about workout schedule')
st.text(body='no tension I got your back! Just let me know which muscle your planing to hit today!')
st.text('')

input=st.text_input("Enter the Muscle name for which your planing to hit today!: ",key="muscle_name")
submit=st.button("Get workout")

if input:
    response = generator.invoke({'question': input})
    st.subheader("Here's your Answer")
    st.write(response)
