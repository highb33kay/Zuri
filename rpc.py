
# If the two players choose the same “character” it’s a tie, and the game repeats
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
# You have been tasked to create a simple version of this game with Python. In your version, one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player). 

# You should make use of the inbuilt Python module random and its choice method.

# Instructions:

# Create a new Python file and call it main.py. Inside it you'll create your game.
# Create a list to store all possible options:
# "R" for "rock", 
# "P" for "paper", 
# "S" for "scissors".
# When the program is run, ask the user to pick an option between "R", "P" or "S"
# If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
# Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
# Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
# Check both player's moves: 
# If there is a winner, print the winner, and the program ends. 
# If it's a tie (the computer and player pick the same move), restart the game from step 3


# Create a list to store all possible options:R, P, S

import random



options = ["r","p", "s"]

# When the program is run, ask the user to pick an option between "R", "P" or "S"
user_option = input('make a choice between R, P, S where R" for "rock", "P" for "paper", "S" for "scissors".: ').lower()
comp_choice = random.choice(options)

# if comp_choice == user_option:

while user_option in options:
    if comp_choice == "r" and user_option == "s":
        print(
            f"Computer choice:{ comp_choice } and User Choice is {user_option}.Winner = Computer ")
    elif comp_choice != "r" and user_option == "s":
        print(f"Computer choice:{ comp_choice } and User Choice is {user_option}. winner = User")
    elif comp_choice == "p" and user_option == "r":
        print(f"Computer choice:{ comp_choice } and User Choice is {user_option}. winner = Computer ")
    elif comp_choice == "s" and user_option == "p":
        print(f"Computer choice:{ comp_choice } and User Choice is {user_option}. winner = Computer")
    else:
        print(f"Computer choice:{ comp_choice } and User Choice is {user_option}. Draw")
else:
    
