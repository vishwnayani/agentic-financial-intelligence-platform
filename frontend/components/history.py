import streamlit as st

from services.api import (

    get_history,

    get_conversation,

    delete_conversation

)


def render_history():

    response = get_history(

        st.session_state.token

    )

    if response.status_code != 200:

        st.error("Unable to load history.")

        return

    history = response.json()

    if len(history) == 0:

        st.info("No conversations yet.")

        return

    for item in history:

        title = item["question"][:35]

        cols = st.columns([5, 1])

        with cols[0]:

            if st.button(

                title,

                key=f"history_{item['id']}",

                use_container_width=True

            ):

                detail = get_conversation(

                    st.session_state.token,

                    item["id"]

                )

                if detail.status_code == 200:

                    conversation = detail.json()

                    st.session_state.answer = conversation["answer"]

                    trace = conversation["execution_trace"]

                    if isinstance(trace, str):

                        trace = trace.split("\n")

                    st.session_state.execution = trace

                    st.session_state.company = conversation["company"]

                    st.session_state.document = conversation["document_type"]

                    st.rerun()

        with cols[1]:

            if st.button(

                "🗑",

                key=f"delete_{item['id']}",

                use_container_width=True

            ):

                response = delete_conversation(

                    st.session_state.token,

                    item["id"]

                )

                if response.status_code == 200:

                    st.rerun()

                else:

                    st.error("Unable to delete.")