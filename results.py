import streamlit as st


def app():
    st.title("Results")

    if "last_attempts" in st.session_state:
        st.write(f"Your last game took **{st.session_state.last_attempts} attempts**.")
    else:
        st.write("No results yet. Play the game to see your results!")
