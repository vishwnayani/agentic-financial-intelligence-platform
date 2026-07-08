import streamlit as st


def render_answer(answer=""):

    st.subheader("📄 Executive Summary")

    with st.container(border=True):

        if answer:

            st.markdown(answer)

        else:

            st.info(
                "Ask a financial question to begin the analysis."
            )