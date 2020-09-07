# this file generate new guess game.
# from first_project.Live import load_game
import random

# function to generate a random number for the user to guess
def generate_number(difficulty):
    return random.randint(1, difficulty)

# this function get the guessed number that the user prompted
def get_guess_from_user(difficulty):
    guess = input("Please guess a number between 1 to " + str(difficulty))
    return guess


# function to compare the the guessed number with the right number
def compare_results(difficulty, secret_number):

    if difficulty == secret_number:
        return True

    else:
        return False


# This function activates the game.
def play_guess_game(difficulty):

    generate_number(difficulty)
    get_guess_from_user(difficulty)
    compare_results(difficulty,)