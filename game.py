import json
import time
from functions import *
ComplexNames = TextNames

##############################################
# GET Player Name
##############################################

def getPlayerName():
    while True:
        playerName = input(f"{ComplexNames.NARRATOR} What should we call you?\n{getColour('RED')}You{getColour('RESET')}: ")
        if playerName:
            clearScreen()
            areYouSure = input(f"{ComplexNames.NARRATOR} Are you sure you want '{playerName}' to be your name? (Y/N)\n{getColour('RED')}You{getColour('RESET')}: ")
            if areYouSure.lower() == 'y':
                return playerName
            else:
                clearScreen()
        else:
            clearScreen()

##############################################
# GET Maximum Word Count
##############################################

def getAttemptsNumber():
    while True:
        numberOfAttempts = input(f"{ComplexNames.NARRATOR} So then how many attempts do you want? ({config['settings']['attempts']['minAttemptAmount']}-{config['settings']['attempts']['maxAttemptAmount']})\n{getColour('RED')}You{getColour('RESET')}: ")
        try:
            numberOfAttempts = int(numberOfAttempts)
            if int(config['settings']['attempts']['minAttemptAmount']) <= numberOfAttempts <= int(config['settings']['attempts']['maxAttemptAmount']):
                clearScreen()
                areYouSure = input(f"{ComplexNames.NARRATOR} Are you sure you want '{numberOfAttempts}' to be the amount of attempts you get? (Y/N)\nYou {getColour('RED')}CANNOT {getColour('RESET')}change this!\n{getColour('RED')}You{getColour('RESET')}: ")
                if areYouSure.lower() == 'y':
                    return numberOfAttempts
                else:
                    clearScreen()
            else:
                clearScreen()
                clickText(f"{ComplexNames.NARRATOR} Hey, don't try and cheat your way out, I said a number between {config['settings']['attempts']['minAttemptAmount']} and {config['settings']['attempts']['maxAttemptAmount']}, not '{numberOfAttempts}'")
        except ValueError:
            clickText(f"{ComplexNames.NARRATOR} '{numberOfAttempts}' is not a valid number")
            clearScreen()

##############################################
# Hangman Class
##############################################

class Hangman:
    # Creator Function 
    def __init__(self, name, attempts):
        self.name = name
        self.attempts = attempts
        self.word = getRandomWord(attempts + 3)
        self.timeStarted = int(time.time())
    
    # GET Display Word
    def getDisplayWord(self, word, index):
        if len(word) != len(index):
            raise ValueError(f"{getColour('RED')} Error: {getColour('RESET')} Word length and index length are not the same.")
        return (' '.join([letter if index[i] else '*' for i, letter in enumerate(word)])).strip()
    
    # GET Next Letter
    def getNextLetter(self, remaining, word, wrong):
        while True:
            guess = input(f"\n{ComplexNames.NARRATOR} Guess a letter or the word.\n{getColour('RED')}You{getColour('RESET')}: ").lower()
            if len(guess) > 1 and guess.lower() == word.lower():
                return True
            elif len(guess) > 1 and guess.lower() != word.lower() and guess.lower().isalpha():
                self.attempts = self.attempts - 1
                return list(filter((guess.lower()).__ne__, remaining))
            elif (len(guess) == 1 and not guess.lower().isalpha()) or (guess.lower() in wrong):
                return list(filter((guess.lower()).__ne__, remaining))
            elif guess.lower() not in remaining:
                self.attempts = self.attempts - 1
                if guess.lower() not in list(self.word.lower()):
                    wrong.append(guess.lower())
                return list(filter((guess.lower()).__ne__, remaining))
            else:
                return list(filter((guess.lower()).__ne__, remaining))

    # Play function
    def play(self):
        remaining = list(self.word.lower())
        index = [letter not in list(self.word.lower()) for letter in remaining]
        wrong = []
        solved = False

        while self.attempts > 0 and not solved:
            clearScreen()
            print(f"{getColour('BLUE')}Word{getColour('RESET')}: {self.getDisplayWord(self.word, index)}")
            print(f"{getColour('BLUE')}Attempts Left{getColour('RESET')}: {self.attempts}")
            print(f"{getColour('BLUE')}Previous Guesses{getColour('RESET')}: {' '.join(wrong)}")

            if len(remaining) == 0:
                solved = True
            else:
                remaining = self.getNextLetter(remaining, self.word, wrong)

            if remaining == True:
                solved = True
            else:
                index = [letter not in remaining for letter in list(self.word.lower())]
        
        clearScreen()

        if solved:
            return [True, int(time.time()) - self.timeStarted, self.attempts]
        else:
            return [False, self.word]