import streamlit as st


def render_chat():

    st.subheader("💬 Ask a Financial Question")

    question = st.text_area(

        "",

        placeholder="Example: Summarize NVIDIA's AI investments...",

        height=150,

        label_visibility="collapsed",

        key="question"

    )

    ask = st.button(

        "🚀 Analyze",

        type="primary",

        use_container_width=True,

        key="analyze"

    )

    return ask, question