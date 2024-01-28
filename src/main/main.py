from src.main.handlers.game import *

ComplexNames = TextNames


def clear_and_click(message):
    clear_screen()
    click_text(message)


def welcome_message():
    welcome_messages = [
        f"Mystery Man > Welcome traveler, you seem lost, allow me to introduce myself, I'm {ComplexNames.NARRATOR_ITSELF}"
    ]
    for message in welcome_messages:
        clear_and_click(message)


def introduction(player_name):
    introduction_messages = [
        f"{ComplexNames.NARRATOR} Hi {player_name}, welcome to the mystery realm, it seems you're trapped here.",
        f"{ComplexNames.NARRATOR} The only way to exit this realm is to participate in our ancient game of Hangman.",
        f"{ComplexNames.NARRATOR} Before we begin, the ancient council has allowed you to pick the amount of chances you get.",
        f"{ComplexNames.NARRATOR} You should know though, the more chances you get, the harder the words will be."
    ]
    for message in introduction_messages:
        clear_and_click(message)


def play_level(level_number, player_name, attempts):
    level = Hangman(player_name, attempts)
    level_result = level.play()

    if not level_result[0]:
        clear_and_click(
            f"{ComplexNames.NARRATOR} Oh no! You failed at level {level_number}.\n{get_colour('BLUE')}Word: {get_colour('RESET')}{level_result[1]}")
        clear_and_click(f"{get_colour('RED')}YOU DIED")
        exit()


def main():
    welcome_message()

    player_name = get_player_name()
    introduction(player_name)

    attempts = get_attempts_number()

    for level_number in range(1, 4):
        play_level(level_number, player_name, attempts)
        clear_and_click(f"{ComplexNames.NARRATOR} Well done! You passed level {level_number}.")

    completion_messages = [
        f"{ComplexNames.NARRATOR} I guess you're free to go, feel free to come back anytime."
    ]
    for message in completion_messages:
        clear_and_click(message)


if __name__ == "__main__":
    main()
    exit()