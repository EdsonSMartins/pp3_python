'''
Module with all required imports to this project
'''
import sys
import random
import os
import time
import colorama
from colorama import Fore
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Constants
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')
WORDS = SHEET.worksheet('words')

# Word selection
BEGGINER_WORDS = WORDS.col_values(1)
INTERMEDIATE_WORDS = WORDS.col_values(2)
EXPERT_WORDS = WORDS.col_values(3)

# To initialize colorama
colorama.init(autoreset=True)


def check_input(u_inpt):
    """
    Function to validate user input and return a valid options
    and alpha validation
    """
    if len(u_inpt) == 1:
        try:
            int(u_inpt)
            return 1
        except ValueError:
            is_alpha = u_inpt.isalpha()
            if is_alpha is True:
                return 2
    else:
        return 3


def pre_game():
    """
    Display main menu
    Checks if the user enters an interger, else raises an error
    If valid number entered, lets user pick game or rules
    """
    print('''
    \n        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
    \r        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
    \r        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
    \r        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
    \r        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
    ''')
    print('''
    \r            ------------------ MAIN MENU ------------------------
    \r           |                                                     |
    \r           |    Please select one of the following options:      |
    \r           |                                                     |
    \r           |         (1) to Start the Game                       |
    \r           |         (2) to See the how to play the Game         |
    \r           |         (3) to Exit Game                            |
    \r           |                                                     |
    \r           |            *Press a number + ENTER                  |
    \r           |_____________________________________________________|
    ''')
    number = input('')
    interger = check_input(number)
    while True:
        if interger == 1:
            number = int(number)
            if number == 1:
                print('Starting game...')
                os.system("clear")
                return 1
            if number == 2:
                print('Showing How to play...')
                os.system("clear")
                return 2
            if number == 3:
                print('Exiting Game...')
                sys.exit()
            else:
                print('Please only enter 1, 2 or 3')
                main()
        else:
            print('Please enter a number')
            main()


def show_rules():
    """
    Brief instructions will be displayed once this option is selected
    """
    print('''
    \n       ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
    \r       ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
    \r       ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
    \r       ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
    \r       ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
    ''')
    print('''
    \r       Welcome to The Hangman game, this is how to play:
    \n       # Guess one letter at a time to reveal the secret word.
    \n       # Each incorrect guess adds another part to the hangman.
    \n       # Chalange your knowledge by selecting the level of difficulty.
    \n       # Be careful, you have only 7 incorrect guesses!
    ''')
    print('1. Return home 2. End game')
    x_x = input('')
    if check_input(x_x) == 1:
        x_x = int(x_x)
        if x_x == 1:
            os.system("clear")
            main()
        elif x_x == 2:
            sys.exit()
        else:
            print('Please only enter 1 or 2')
            show_rules()
    else:
        print(f'Error: input {x_x} is invalid')
        print('Please enter a valid number')
        show_rules()


def select_level():
    """
    Define level of difficulty from begginer to expert
    also get a word from rescpective column
    """
    print('''
    \n        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
    \r        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
    \r        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
    \r        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
    \r        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
    ''')
    print('''
    \r            --------------------- Levels ------------------------
    \r           |                                                     |
    \r           |    Please select the level you want to play:        |
    \r           |                                                     |
    \r           |             (1) for Begginer                        |
    \r           |             (2) for Intermediate                    |
    \r           |             (3) for Expert                          |
    \r           |                                                     |
    \r           |            *Press a number + ENTER                  |
    \r           |_____________________________________________________|
    ''')
    level = input('')
    if check_input(level) == 1:
        level = int(level)
        if level == 1:
            print(f'{Fore.GREEN}Begginer level loading...{Fore.RESET}')
            time.sleep(1.2)
            os.system("clear")
            return 1
        if level == 2:
            print(f'{Fore.YELLOW}Intermediate level loading...{Fore.RESET}')
            time.sleep(1.2)
            os.system("clear")
            return 2
        if level == 3:
            print(f'{Fore.RED}Expert level loading...{Fore.RESET}')
            time.sleep(1.2)
            os.system("clear")
            return 3
        else:
            print('Please select a level: ')
    else:
        print(f'Error: input {level} is invalid')
        print('Please enter a valid number')
        select_level()


def select_word(level):
    """
    Game's words are defined by taken the value of level selected
    """
    choice = random.randrange(30)
    if level == 1:
        hidden_word = BEGGINER_WORDS[choice]
    elif level == 2:
        hidden_word = INTERMEDIATE_WORDS[choice]
    elif level == 3:
        hidden_word = EXPERT_WORDS[choice]
    return hidden_word


def show_word(hidden_word):
    """
    Get and display word by level
    """
    letters = []
    s_word = []
    for letter in range(len(hidden_word)):
        letters.append(hidden_word[letter])
    for letter in letters:
        s_word.append('_')
    print(stages[6])
    print(s_word)
    hangman(letters, s_word)


def hangman(letters, s_word):
    """
    Tests user responses against the hidden word,
    reveals the secret word when guessed
    """
    incorrect_guesses = 7
    already_guessed = []

    while '_' in s_word and incorrect_guesses > 0:
        user_guess = input('Choose a letter: ')
        os.system("clear")
        is_letter = check_input(user_guess)
        print(stages[(incorrect_guesses - 1)])
        correct_guess = 0
        if is_letter == 2:
            user_guess = user_guess.lower()
            if user_guess not in already_guessed:
                already_guessed.append(user_guess)
                # u_inpt value is used to iterate through blank list
                u_inpt = 0
                for letter in letters:
                    if user_guess == letter:
                        s_word[u_inpt] = user_guess
                        correct_guess += 1
                    u_inpt += 1
                print(s_word)
                print(f'{Fore.YELLOW}Letters you tried: {(already_guessed)}')
                if correct_guess > 0:
                    print(f'{Fore.GREEN} Well done! Correct answer!')
                else:
                    incorrect_guesses -= 1
                    print(f'{Fore.RED}No good, wrong answer! Please try again')
                    print(f'You have: {(incorrect_guesses)} guesses remaining')
            else:
                print('Letter already guessed. Please try again!')
                print(f'{Fore.YELLOW}Letters you tried: {(already_guessed)}')
        else:
            print(f'Error: input {user_guess} is invalid')
            print('Only Eglish alphabet letters are valid, please try again!')
            print(f'{Fore.YELLOW}Letters you tried: {(already_guessed)}')
    os.system("clear")
    end_game(incorrect_guesses, letters)


def end_game(incorrect_guesses, letters):
    """
    ends the game and displays the user's score
    """
    score = incorrect_guesses * len(letters)
    print('''
    \n  ██████   █████  ███    ███ ███████     ██████  ██    ██ ███████ ██████
    \r ██       ██   ██ ████  ████ ██         ██    ██ ██    ██ ██      ██   ██
    \r ██   ███ ███████ ██ ████ ██ █████      ██    ██ ██    ██ █████   ██████
    \r ██    ██ ██   ██ ██  ██  ██ ██         ██    ██  ██  ██  ██      ██   ██
    \r  ██████  ██   ██ ██      ██ ███████     ██████    ████   ███████ ██   ██
    ''')
    if score > 0:
        print(f'''
                      {Fore.GREEN}Congratulations!{Fore.RESET}
                      Your score is: {score}
        ''')
    else:
        print(f'''
        {Fore.RED}Sorry! Unfortunately, you didn't guess the word.{Fore.RESET}
            The word was {letters}
        ''')
    print('Play again? \n Y. Play again N. End Game')
    play_again = input('')
    play_again = play_again.lower()
    # Input validation
    is_valid = check_input(play_again)
    if is_valid == 2:
        if play_again == 'y':
            os.system("clear")
            main()
        elif play_again == 'n':
            exit_program()
        else:
            print('Please enter either Y or N')
    else:
        print(f'Error: input {play_again} is invalid')
        print('Please only enter Y or N')


def exit_program():
    """
    This function closes the program
    """
    confirm = input(
        f"{Fore.YELLOW}Are you sure you want to exit the program? \n \
             Press 'y' to confirm or 'n' to play again: {Fore.RESET}")
    if confirm.lower() == "y":
        print("Exiting program...")
        sys.exit()
    else:
        os.system("clear")
        main()


def main():
    """
    main function calls
    """
    print(fr''' {Fore.YELLOW}
                        |/|
                        |/|
                        |/|
                        |/| /¯)
                        |/|/\/
                        |/|\/
                       (¯¯¯)
                       (¯¯¯)
                       (¯¯¯)
                       (¯¯¯)
                       (¯¯¯)
                       /¯¯/\{Fore.WHITE}        The Hangman Game!{Fore.RESET}
 {Fore.YELLOW}                     / ,^./\
                     / /   \/\
                    / /     \/\      Test your knoledge,
                   ( (       )/)    but don't loose your head!
                   | |       |/|
                   | |       |/|
                   | |       |/|
                   ( (       )/)
                    \ \     / /
                     \ `---' /
                      `-----'     {Fore.RESET}''')
    print('\nLoading...')
    time.sleep(4)
    os.system("clear")
    run_game = pre_game()
    if run_game == 1:
        difficulty = select_level()
        hidden_word = select_word(difficulty)
        show_word(hidden_word)
    elif run_game == 2:
        show_rules()
    elif run_game == 3:
        exit_program()


main()
