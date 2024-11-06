import streamlit as st

st.title("My Streamlit App")

st.write("Welcome to my first Streamlit app!")

number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")

if st.button("Click me!"):
    st.balloons()