#This file has several "accessories" in it to prevent malfunctions and keep the game running in demand.
import os

scores_file_name = "Scores.txt"

ERROR_MESSAGE = "Invalid act, Please try again: "


def screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")
