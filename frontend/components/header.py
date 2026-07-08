import streamlit as st

from utils.auth import logout


def render_header():

    left, right = st.columns([8, 2])

    with left:

        st.title("📈 Agentic Financial Intelligence Platform")

        st.caption(
            "Multi-Agent Financial Analysis using LangGraph + RAG"
        )

    with right:

        st.write("")
        st.write("")

        st.caption("Logged In")

        st.write(f"👤 **{st.session_state.email}**")

        st.write("")

        if st.button(
            "Logout",
            use_container_width=True
        ):
            logout()

    st.divider()