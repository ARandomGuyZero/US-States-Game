"""
U.S. States Game

Author: Alan
Date: September 12th 2024

This script generates a game where the user can guess the name of the states.
A map is shown and the user will type as many states they remember.
If the state is in the list, the name will appear in the state's location in the map.
The user can exit typing 'Exit', and the game will create a file with the missing states!
"""

import turtle
import pandas

# Create a new screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set a turtle with the image of the map as the shape
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# Store the state data in a variable using pandas library
state_data = pandas.read_csv("50_states.csv")

# List of states with Strings containing each state's name
list_of_states = state_data.state.to_list()

# Turtle object that will help us as a cursor, it will write the name of each city we write
cursor = turtle.Turtle()
cursor.speed("fastest") # Set high speed
cursor.hideturtle() # Make it invisible
cursor.penup() # Disable writing

# List of our guessed states
guessed_states = []

# Simple loop to keep our game running as long as the user hasn't guessed each state
while len(guessed_states) < 50:

    # Ask the player for input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()

    # If the answer is the secret word Exit, it will create a new list for the user to learn
    if answer_state == "Exit":

        # New list with the states to learn
        states_to_learn = [state for state in list_of_states if state not in guessed_states]

        # Convert the list to a DataFrame
        new_csv = pandas.DataFrame(states_to_learn)

        # Create new file
        new_csv.to_csv("StatesToLearn.csv")

        # Close game
        break

    # If the answer is in the list of states, then executes the code
    if answer_state in list_of_states:

        # Get the information of that state in the DataFrame
        state_info = state_data[state_data.state == answer_state]

        # Get both x and y coordinates
        x_cor = int(state_info.x.item())
        y_cor = int(state_info.y.item())

        # Move the cursor to the coordinates
        cursor.goto(x_cor, y_cor)

        # Write the state's name
        cursor.write(answer_state, align="center")

        # Add the name to the list of states
        guessed_states.append(answer_state)
