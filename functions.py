import time
import random
import json
import os
with open('config.json') as configFile:
    config = json.load(configFile)

##############################################
# Colour Picker
##############################################

def getColour(colour):
    colours = {
        'RED': '\033[1;31m',
        'BLUE': '\033[1;34m',
        'CYAN': '\033[1;36m',
        'GREEN': '\033[0;32m',
        'RESET': '\033[0;0m'
    }
    return colours.get(colour, "Invalid")

##############################################
# Screen Clear
##############################################

def clearScreen():
    clear = lambda: os.system('clear')
    clear()

##############################################
# Time Format
##############################################

def formatTime(seconds):
    formattedTime = time.strftime('%H:%M', time.gmtime(seconds))
    splitTime = formattedTime.split(':')
    if (splitTime[0] == '00'):
        return (f"{list(splitTime[1])[1]} Minutes" if splitTime[1].startswith('0') else f"{splitTime[1]} Minutes")
    else:
        return (f"{list(splitTime[0])[1]} Hours, {splitTime[1]} Minutes" if splitTime[0].startswith('0') else f"{splitTime[0]} Hours, {splitTime[1]} Minutes")

##############################################
# GET Random Word
##############################################

def getRandomWord(maxWordCount):
    wordsProcessed = 0
    currentWord = None
    with open('words.txt', 'r') as wordlist:
        for word in wordlist:
            if len(word.strip().lower()) > maxWordCount:
                continue
            wordsProcessed += 1
            if random.randint(1, wordsProcessed) == 1:
                currentWord = word.strip().lower()
    return currentWord

##############################################
# Complex Names
##############################################

def clickText(text):
    input(text + '\n')

##############################################
# Complex Names
##############################################

class TextNames:
    NARRATOR_ITSELF = getColour(config['narrator']['colour']) + config['narrator']['name'] + getColour('RESET')
    NARRATOR = f"{getColour(config['narrator']['colour'])}{config['narrator']['name']} >{getColour('RESET')}"