import random
import streamlit as st


def app():
    st.title("Guessing Game")

    # State management for the random number
    if "random_number" not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if "game_data" not in st.session_state:
        st.session_state.game_data = []  # To store game statistics

    if "show_tips" not in st.session_state:
        # This session_state variable is needed to store if the user wants an estimation of their guess
        st.session_state.show_tips = False

    st.write("I have selected a number between 1 and 100. Can you guess it?")
    
    # User input for guessing
    user_guess = st.number_input(
        "Enter your guess:", min_value=1, max_value=100, step=1, format="%d"
    )
    
    # Button to toggle hints
    if st.button("I want quality hints"):
        st.session_state.show_tips = not st.session_state.show_tips

    # Display hint state
    if st.session_state.show_tips:
        st.info("Hints are currently ON!")
    else:
        st.info("Hints are currently OFF!")

    # Submit guess
    submit = st.button("Submit Guess")

    if submit:
        st.session_state.attempts += 1

        # Hint logic
        if st.session_state.show_tips:
            difference = abs(user_guess - st.session_state.random_number)
            if difference < 7:
                grade = "A"
            elif difference < 20:
                grade = "B"
            elif difference < 30:
                grade = "C"
            elif difference < 45:
                grade = "D"
            else:
                grade = "F"

            st.write(f"Hint Grade: {grade}")

        # Evaluate guess
        if user_guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif user_guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success(
                f"Correct! You guessed the number in {st.session_state.attempts} attempts."
            )
            # Record the game statistics
            game_num = len(st.session_state.game_data) + 1
            st.session_state.game_data.append((game_num, st.session_state.attempts))

            # Reset for a new game
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
