# this file generate the Memory Game.
import random
# from first_project.Live import load_game
from first_project.Utils import screen_cleaner

sequence = []

def generate_sequence(difficulty):

    for i in range(difficulty):
        sequence.append(random.randint(1,101))
    print(sequence)
    screen_cleaner()

guessed_sequence = []

def get_list_from_user(difficulty):

    for i in range(0,difficulty):
        nums = input("After seeing the numbers enter the numbers you saw, each one separated with Enter ")
        nums = int(nums)
        guessed_sequence.append(nums)


def is_list_equal(list_a, list_b):

    if list_a == list_b:
        return True
    else:
        return False

def play_memory(difficulty):
    difficulty = difficulty
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    print(is_list_equal(sequence,guessed_sequence))