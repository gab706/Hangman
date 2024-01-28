import time
import os
import json
from src.main.handlers.functions import TextNames, get_random_word, clear_screen, click_text, get_colour

ComplexNames = TextNames

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
config_path = os.path.join(project_dir, 'data', 'config.json')

with open(config_path) as configFile:
    config = json.load(configFile)


def get_player_name():
    while True:
        player_name = input(
            f"{ComplexNames.NARRATOR} What should we call you?\n{get_colour('RED')}You{get_colour('RESET')}: ")
        if player_name:
            clear_screen()
            are_you_sure = input(
                f"{ComplexNames.NARRATOR} Are you sure you want '{player_name}' to be your name? (Y/N)\n{get_colour('RED')}You{get_colour('RESET')}: ")
            if are_you_sure.lower() == 'y':
                return player_name
            else:
                clear_screen()
        else:
            clear_screen()


def get_attempts_number():
    min_attempts = int(config['settings']['attempts']['minAttemptAmount'])
    max_attempts = int(config['settings']['attempts']['maxAttemptAmount'])

    while True:
        try:
            num_attempts = int(input(
                f"{ComplexNames.NARRATOR} How many attempts do you want? ({min_attempts}-{max_attempts})\n{get_colour('RED')}You{get_colour('RESET')}: "))

            if min_attempts <= num_attempts <= max_attempts:
                clear_screen()
                are_you_sure = input(
                    f"{ComplexNames.NARRATOR} Are you sure you want '{num_attempts}' attempts? (Y/N)\nYou {get_colour('RED')}CANNOT {get_colour('RESET')}change this!\n{get_colour('RED')}You{get_colour('RESET')}: ")

                if are_you_sure.lower() == 'y':
                    return num_attempts
                else:
                    clear_screen()
            else:
                clear_screen()
                click_text(
                    f"{ComplexNames.NARRATOR} Enter a number between {min_attempts} and {max_attempts}, not '{num_attempts}'")
        except ValueError:
            click_text(f"{ComplexNames.NARRATOR} '{num_attempts}' is not a valid number")
            clear_screen()


def get_display_word(word, index):
    if len(word) != len(index):
        raise ValueError(
            f"{get_colour('RED')} Error: {get_colour('RESET')} Word length and index length are not the same.")
    return ' '.join([letter if index[i] else '*' for i, letter in enumerate(word)]).strip()


class Hangman:
    def __init__(self, name, attempts):
        self.name = name
        self.attempts = attempts
        self.word = get_random_word(attempts + 3)
        self.time_started = int(time.time())

    def get_next_letter(self, remaining, wrong):
        while True:
            guess = input(
                f"\n{ComplexNames.NARRATOR} Guess a letter or the word.\n{get_colour('RED')}You{get_colour('RESET')}: ")
            if len(guess) > 1 and guess.lower() == self.word.lower():
                return True
            elif len(guess) > 1 and guess.lower() != self.word.lower() and guess.lower().isalpha():
                self.attempts -= 1
                return list(filter((guess.lower()).__ne__, remaining))
            elif (len(guess) == 1 and not guess.lower().isalpha()) or (guess.lower() in wrong):
                return list(filter((guess.lower()).__ne__, remaining))
            elif guess.lower() not in remaining:
                self.attempts -= 1
                if guess.lower() not in list(self.word.lower()):
                    wrong.append(guess.lower())
                return list(filter((guess.lower()).__ne__, remaining))
            else:
                return list(filter((guess.lower()).__ne__, remaining))

    def play(self):
        remaining = list(self.word.lower())
        index = [letter not in list(self.word.lower()) for letter in remaining]
        wrong = []
        solved = False

        while self.attempts > 0 and not solved:
            clear_screen()
            print(f"{get_colour('BLUE')}Word{get_colour('RESET')}: {get_display_word(self.word, index)}")
            print(f"{get_colour('BLUE')}Attempts Left{get_colour('RESET')}: {self.attempts}")
            print(f"{get_colour('BLUE')}Previous Guesses{get_colour('RESET')}: {' '.join(wrong)}")

            if len(remaining) == 0:
                solved = True
            else:
                remaining = self.get_next_letter(remaining, wrong)

            if remaining:
                solved = True
            else:
                index = [letter not in remaining for letter in list(self.word.lower())]

        clear_screen()

        if solved:
            return [True, int(time.time()) - self.time_started, self.attempts]
        else:
            return [False, self.word]