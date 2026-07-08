import streamlit as st


def initialize_session():

    defaults = {

        "logged_in": False,

        "token": "",

        "email": "",

        "answer": "",

        "execution_trace": [],

        "company": "",

        "document_type": ""

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value