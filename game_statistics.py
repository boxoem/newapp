import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

plt.style.use("dark_background")


def app():
    st.title("Game Statistics")

    # Check if statistics exist in the session state
    if "game_data" not in st.session_state:
        st.session_state.game_data = []

    game_data = st.session_state.game_data

    if not game_data:
        st.write("No statistics available yet. Play a game to see your stats!")
        return

    # Convert game data to DataFrame for analysis
    df = pd.DataFrame(game_data, columns=["Game", "Attempts"])

    # Summary statistics
    total_games = len(game_data)
    avg_attempts = np.mean(df["Attempts"])
    best_score = np.min(df["Attempts"])

    st.subheader("Summary")
    st.write(f"**Total Games Played:** {total_games}")
    st.write(f"**Average Attempts per Game:** {avg_attempts:.2f}")
    st.write(f"**Best Score (Fewest Attempts):** {best_score}")

    # Histogram of attempts
    st.subheader("Attempts Distribution")
    fig, ax = plt.subplots()
    ax.hist(
        df["Attempts"],
        bins=range(1, max(df["Attempts"]) + 2),
        alpha=0.7,
        color="blue",
        edgecolor="black",
    )
    ax.set_xlabel("Attempts")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Attempts")
    st.pyplot(fig)

    # Display detailed game data
    st.subheader("Game History")
    st.table(df)
