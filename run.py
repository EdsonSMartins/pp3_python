import random
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages
from hangman_art import logo

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

# Letter validation
ALPHABET = ['abcdefghijklmnopqrstuvwxyz']


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
    print('logo')
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
            print('Displaying rules...')
            return 2
        if number == 3:                
            print('Exiting Game...')
            exit()
        else:
            print('Please only enter 1, 2 or 3')
    else:
        print('Please enter a number')
        main()


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

