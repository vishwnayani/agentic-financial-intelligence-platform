import streamlit as st

from services.api import login


def login_page():

    st.title("📈 Agentic Financial Intelligence Platform")

    st.subheader("AI-powered Financial Document Analysis")

    st.write("")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        response = login(
            email,
            password
        )

        if response.status_code == 200:

            token = response.json()["access_token"]

            st.session_state.logged_in = True
            st.session_state.token = token
            st.session_state.email = email

            st.rerun()

        else:

            st.error("Invalid email or password.")