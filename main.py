#!/usr/bin/python3/

import script
import score

# Initialize paths of welcome message, rules and questions files
path_welcome_message = "welcome.txt"
path_rules = "rules.txt"
path_questions = "questions.txt"

game = script.play_game(path_welcome_message,path_rules,path_questions)

# Load the necessary files
game.load_welcome_message()
game.load_rules()
game.load_questions()

# Print the welcome screen and initialize the player
game.get_welcome_screen()
game.get_username()

# Print the game rules
game.get_rules()

# Start the main game loop
while True:
    # Set the question and its parameters
    game.set_question_parameters()

    # Display the question and options
    game.get_question()
    game.get_options()

    while True:
        # Get user answer
        user_answer = str(input("Please select an option: "))
        # Check the answer
        if game.check_answer(user_answer) is not None:
            break

    quit_game = input("Do you want to keep playing (Y/n): ").upper()
    if quit_game == "N":
        break

print("Thank you for playing!")
