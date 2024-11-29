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
        #this session_state variable is needed to store if the user wants an estimation of his/her guess
        st.session_state.show_tips = False
    if "grade" not in st.session_state:
        st.session_state.grade = "A"
    st.write("I have selected a number between 1 and 100. Can you guess it?")
    
    user_guess = st.number_input(
        "Enter your guess:", min_value=1, max_value=100, step=1, format="%d"
    )
    if st.button("I want quality hints"):
        # allows to toggle between hints on and off state
        st.session_state.show_tips = not st.session_state.show_tips
     
        
        
    submit = st.button("Submit Guess")
    #button to submit guess and start evaluating it (see below v)

    if submit:
        difference = abs(user_guess - st.session_state.random_number)
            #this assigns the difference between the guess and the goal and now gives the user a hint based on that difference
        if difference <= 7:
            st.session_state.grade = "A"
        elif difference <= 20:
            st.session_state.grade = "B"
        elif difference <= 30:
            st.session_state.grade = "C"
        else:
            st.session_state.grade = "D"
        
        if st.session_state.show_tips:
            #this if-loop is only evaluated when the "i want hints"-checkbox is selected
           
            # grades are assigned based on how far off the user is to the secret number
            
            st.write(f"Hint grade: {st.session_state.grade}")
        #st.write("Difference: ", (user_guess - st.session_state.random_number))
        st.session_state.attempts += 1
        if user_guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
            
        elif user_guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        # evaluation based on whether guess is too high or too low
        else:
            st.success(
                f"Correct! You guessed the number in {st.session_state.attempts} attempts."
            )
            # Record the game statistics
            game_num = len(st.session_state.game_data) + 1
            st.session_state.game_data.append((game_num, st.session_state.attempts))

            # Reset for a new game
            st.session_state.last_attempts = st.session_state.attempts
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
