import streamlit as st
from styles.themes import load_css
from utils.session import initialize_session

from views.login import login_page

from views.dashboard import dashboard


st.set_page_config(

    page_title="Agentic Financial Intelligence Platform",

    page_icon="📈",

    layout="wide",

    initial_sidebar_state="collapsed"

)

load_css()


initialize_session()


if st.session_state.logged_in:

    dashboard()

else:

    login_page()