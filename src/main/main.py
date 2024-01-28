import time
from functions import *
from game import *
ComplexNames = TextNames

clearScreen()

clickText(f"Mystery Man > Welcome traveler, you seem lost, allow me to introduce myself, I'm {ComplexNames.NARRATOR_ITSELF}")
clearScreen()

playerName = getPlayerName()
clearScreen()

clickText(f"{ComplexNames.NARRATOR} Hi {playerName}, welcome to the mystery realm, it seems you're trapped here.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} The only way to exit this realm is to participate in our ancient game of Hangman.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} Before we begin the ancient council has allowed you to pick the amount of chances you get")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} You should know though, the more chances you get, the harder the words will be")
clearScreen()

attempts = getAttemptsNumber()
clearScreen()

levelOne = Hangman(playerName, attempts)
levelOneResult = levelOne.play()

if not levelOneResult[0]:
    clickText(f"{ComplexNames.NARRATOR} Ha, did you really fail after the first game, that is unfortunate.\n{getColour('BLUE')}Word: {getColour('RESET')}{levelOneResult[1]}")
    clearScreen()
    print(f"{getColour('RED')}YOU DIED")
    exit()

clickText(f"{ComplexNames.NARRATOR} Well well well, it seems you're smarter than I anticipated.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} None the less, you still have two more games to win.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} Otherwise you'll be stuck here forever.")
clearScreen()

levelTwo = Hangman(playerName, attempts)
levelTwoResult = levelTwo.play()

if not levelTwoResult[0]:
    clickText(f"{ComplexNames.NARRATOR} At least you managed to make it halfway through, none the less you failed.\n{getColour('BLUE')}Word: {getColour('RESET')}{levelTwoResult[1]}")
    clearScreen()
    print(f"{getColour('RED')}YOU DIED")
    exit()

clickText(f"{ComplexNames.NARRATOR} I just can't seem to get you to lose.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} This is the last round, if you win you'll be let go, if not, well then.")
clearScreen()

levelThree = Hangman(playerName, attempts)
levelThreeResult = levelThree.play()

if not levelThreeResult[0]:
    clickText(f"{ComplexNames.NARRATOR} Ohhhh so close, that's unlucky.\n{getColour('BLUE')}Word: {getColour('RESET')}{levelThreeResult[1]}")
    clearScreen()
    print(f"{getColour('RED')}YOU DIED")
    exit()

clickText(f"{ComplexNames.NARRATOR} Bu-but, that's not possible.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} The games are rig- I mean too difficult for any human to win.")
clearScreen()

clickText(f"{ComplexNames.NARRATOR} I guess you're free to go, feel free to come back anytime.")
clearScreen()

exit()