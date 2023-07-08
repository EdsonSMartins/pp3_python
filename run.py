import random
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages

LOGO = ''' 
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/    
'''


GAME_NAME = "HANGMAN"
DEFAULT_NAME = "ANONIMUS"
ALPHABET = ['abcdefghijklmnopqrstuvwxyz']
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')
WORDS = SHEET.worksheet('words')


def check_input(x):
    """
    Checks the type of input and returns data based on that
    """
    if len(x) == 1:
        try:
            int(x)
            return 1
        except ValueError:
            is_alpha = x.isalpha()
            if is_alpha is True:
                return 2
            else:
                return 3
    else:
        return 3


def start_game():
    """
    Checks if the user enters an interger, else raises an error
    If valid number entered, lets user pick game or rules
    """
    print(LOGO)
    print('''
           1. Start game 2. See rules
                3. Exit Game
        ''')
    number = input('')
    interger = check_input(number)
    if interger == 1:
        number = int(number)
        if number == 1:
            print('Starting game...')
            return 1
        if number == 2:
            print('Showing rules...')
            return 2
        if number == 3:                
            print('Exiting Game...')
            exit()
        else:
            print('Please only enter 1, 2 or 3')
    else:
        print('Please enter a number')
        main()


def show_rules():
    """
    The game rules will be displayed once this option is selected 
    """
    print(LOGO)
    print('''
    This a game of hangman
    1. On the main menu select "Play Game" by pressing 1
    2. Select your game mode
    - Beginner easy, Intermediate or Expert by pressing 1, 2, or 3
    3. When prompted please enter a letter into the terminal
    4. The program will then test your answer against the scecret word
    5. If your answer is correct, it will be displayed in the secret word
    6. If your answer is incorrect, a line will be added to the hangman
    7. You only get 6 incorrect guesses - so be careful!''')
    print('1. Return home 2. End game')
    x = input('')
    if check_input(x) == 1:
        x = int(x)
        if x == 1:
            main()
        elif x == 2:
            exit()
        else:
            print('Please only enter 1 or 2')
            show_rules()
    else:
        print(f'Error: input {x} is invalid')
        print('Please enter a valid number')
        show_rules()


def main():
    """
    main function calls
    """   
    run_game = start_game()
    if run_game == 1:
        pass
    elif run_game == 2:
        pass
    elif run_game == 3:
        pass


main()    

