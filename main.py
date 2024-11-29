import streamlit as st

from game import app as game_app
from game_statistics import app as statistics_app
from home import app as home_app
from results import app as results_app

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        "Navigation",
        ["Home", "Game", "Results", "Statistics"],
        # icons=["house", "controller", "trophy"],
        # menu_icon="cast",
        # default_index=0,
    )

# Routing to the selected page
if selected == "Home":
    home_app()
elif selected == "Game":
    game_app()
elif selected == "Results":
    results_app()
elif selected == "Statistics":
    statistics_app()
