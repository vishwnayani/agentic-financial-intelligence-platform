import streamlit as st

from components.header import render_header
from components.chat import render_chat
from components.answer import render_answer
from components.history import render_history
from services.api import ask_question


def dashboard():

    render_header()

    if "answer" not in st.session_state:
        st.session_state.answer = ""

    if "execution" not in st.session_state:
        st.session_state.execution = []

    if "company" not in st.session_state:
        st.session_state.company = ""

    if "document" not in st.session_state:
        st.session_state.document = ""

    # -------------------------
    # Main Layout
    # -------------------------

    left, right = st.columns([1, 3])

    # =========================
    # LEFT COLUMN
    # =========================

    with left:

        st.subheader("📚 History")

        render_history()

    # =========================
    # RIGHT COLUMN
    # =========================

    with right:

        ask, question = render_chat()

        if ask:

            if question.strip() == "":

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Analyzing Financial Documents..."
                ):

                    try:

                        response = ask_question(
                            st.session_state.token,
                            question
                        )

                    except Exception as e:

                        st.error(e)

                        response = None

                if response is not None:

                    if response.status_code == 200:

                        result = response.json()

                        st.session_state.answer = result["answer"]

                        st.session_state.execution = result[
                            "execution_trace"
                        ]

                        st.session_state.company = result[
                            "company"
                        ]

                        st.session_state.document = result[
                            "document_type"
                        ]

                        st.rerun()

                    else:

                        try:

                            st.error(
                                response.json()["detail"]
                            )

                        except Exception:

                            st.error(response.text)

        render_answer(
            st.session_state.answer
        )

        if st.session_state.answer:

            st.download_button(

                "⬇ Download Answer",

                st.session_state.answer,

                file_name="analysis.md",

                mime="text/markdown",

                use_container_width=True

            )

        st.write("")

        st.subheader("⚙ Agent Execution")

        if st.session_state.execution:

            for index, step in enumerate(

                st.session_state.execution,

                start=1

            ):

                st.markdown(

                    f"""
<div class="agent-card">

<b>Step {index}</b><br>

{step}

</div>
""",

                    unsafe_allow_html=True

                )

        else:

            st.info("No execution yet.")

        st.write("")

        st.subheader("📄 Metadata")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(

                "Company",

                st.session_state.company

            )

        with c2:

            st.metric(

                "Document",

                st.session_state.document

            )