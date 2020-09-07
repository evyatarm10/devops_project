from first_project.GuessGame import play_guess_game
from first_project.MemoryGame import play_memory
from first_project.Utils import ERROR_MESSAGE


# This function makes introduction to the user.
def welcome():
    name = input("For starters please enter your name: ")
    return "Hello " + name + " and welcome to the World of Games (WoG).\n""here you can find many cool games to play."


# This function is loading a game that the user choose with the level of difficulty that he ask for.
def load_game():
    print(
        "Please choose a game to play: \n""1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
        "2. Guess Game - guess a number and see if you chose like the computer")

    games = 1 or 2

    chosen_game = input("What is your choice?: ")
    chosen_game = int(chosen_game)

    while chosen_game != games :
        input(ERROR_MESSAGE)
        break

    difficulty_level = input("Please choose game difficulty from 1 to 5:")
    difficulty_level = int(difficulty_level)

    while difficulty_level != 1 or 2 or 3 or 4 or 5:
            input(ERROR_MESSAGE)
            break

    if chosen_game == 1:
        play_guess_game(difficulty_level)
    else:
        play_memory(difficulty_level)