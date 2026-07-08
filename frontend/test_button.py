import streamlit as st

st.title("Button Test")

if st.button("Click Me"):
    st.success("Button clicked!")
    print("BUTTON CLICKED")