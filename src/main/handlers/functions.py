import time
import random
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
config_path = os.path.join(project_dir, 'data', 'config.json')

with open(config_path) as configFile:
    config = json.load(configFile)


def get_colour(colour):
    colours = {'RED': '\033[1;31m', 'BLUE': '\033[1;34m', 'CYAN': '\033[1;36m', 'GREEN': '\033[0;32m',
               'RESET': '\033[0;0m'}
    return colours.get(colour, "Invalid")


def clear_screen():
    os.system('clear')


def format_time(seconds):
    formatted_time = time.strftime('%H:%M', time.gmtime(seconds))
    split_time = formatted_time.split(':')
    return f"{list(split_time[0])[1]} Hours, {split_time[1]} Minutes" if split_time[0].startswith(
        '0') else f"{split_time[0]} Hours, {split_time[1]} Minutes" if split_time[
                                                                           0] != '00' else f"{list(split_time[1])[1]} Minutes" if \
        split_time[1].startswith('0') else f"{split_time[1]} Minutes"


def get_random_word(max_word_count):
    words_processed = 0
    current_word = None
    with open('../data/words.txt', 'r') as wordlist:
        for word in wordlist:
            if len(word.strip().lower()) > max_word_count:
                continue
            words_processed += 1
            if random.randint(1, words_processed) == 1:
                current_word = word.strip().lower()
    return current_word


def click_text(text):
    input(text + '\n')


class TextNames:
    NARRATOR_ITSELF = f"{get_colour(config['narrator']['colour'])}{config['narrator']['name']}{get_colour('RESET')}"
    NARRATOR = f"{get_colour(config['narrator']['colour'])}{config['narrator']['name']} >{get_colour('RESET')}"
