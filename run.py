import random
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages
from hangman_art import LOGO

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


def select_level():
    """
    Define level of difficulty from begginer to expert
    also get a word from rescpective column
    """
    print(LOGO)
    print('Select your level\n 1. Begginer 2. Intermediate 3. Expert')
    mode = input('')
    if check_input(mode) == 1:
        mode = int(mode)
        if mode == 1:
            print('Begginer mode loading...')
            return 1
        elif mode == 2:
            print('Intermediate mode loading...')
            return 2
        elif mode == 3:
            print('Expert mode loading...')
            return 3
        else:
            print('Please select a level: ')
    else:
        print(f'Error: input {mode} is invalid')
        print('Please enter a valid number')
        select_level()


# Word selection
begginer_words = WORDS.col_values(1)
intermediate_words = WORDS.col_values(2)
expert_words = WORDS.col_values(3)


def select_word(level):
    """
    Game's word is defined by taken the value of 'select_level'
    """
    choice = random.randrange(25)
    if level == 1:
        hidden_word = begginer_words[choice]
    elif level == 2:
        hidden_word = intermediate_words[choice]
    elif level == 3:
        hidden_word = expert_words[choice]
    return hidden_word


def show_word(hidden_word):
    """
    display word by level   
    """
    letters = []
    to_test = []
   
    for letter in range(len(hidden_word)):
        letters.append(hidden_word[letter])
    for letter in letters:
        to_test.append('_')
    print(stages[6])
    print(to_test)
    hangman(letters, to_test)


def hangman(letters, to_test):
    """
    Tests user responses against the hidden word
    Reveals the secret word when guessed

    """ 
    incorrect_guesses = 7
    already_guessed = []

    while '_' in to_test and incorrect_guesses > 0:
        user_guess = input('Choose a letter: ') 
        is_letter = check_input(user_guess)
        print(stages[(incorrect_guesses - 1)])
        correct_guess = 0
        if is_letter == 2:
            user_guess = user_guess.lower()
            if user_guess not in already_guessed:
                print(already_guessed)
                already_guessed.append(user_guess)
                # x value is used to iterate through blank list
                x = 0
                for letter in letters:
                    if user_guess == letter:
                        to_test[x] = user_guess
                        correct_guess += 1
                    x += 1 
                print(to_test)
                if correct_guess > 0:
                    print('Well done! Correct answer!')
                else:
                    incorrect_guesses -= 1
                    print('No good, wrong answer! Please try again')
                    print(f'You have: {(incorrect_guesses)} guesses remaining')
            else:
                print('Letter already guessed\n Please try again!')
        else:
            print(f'Error: input {user_guess} is invalid')            
    end_game(incorrect_guesses, letters)


def end_game(incorrect_guesses, letters):
    """
    ends the game and displays the user's score
    """
    score = incorrect_guesses * len(letters)
    print(LOGO)
    print('Game Over!!')
    if score > 0:
        print(f'Congratulations!\nYour score is: {score}')
    else:
        print(f'The word was {letters}')
        print("Sorry! You were unable to save the man")
    print('Play again? \n Y. Play again N. End Game')
    play_again = input('')
    play_again = play_again.lower()
    # Input validation 
    is_valid = check_input(play_again)
    if is_valid == 2:
        if play_again == 'y':
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
        "Are you sure you want to exit the program? \n \
             Press 'y' to confirm or 'n' to play again: ")
    if confirm.lower() == "y":
        print("Exiting program...")
        exit()
    else:
        main()


def main():
    """
    main function calls
    """   
    run_game = start_game()
    if run_game == 1:
        difficulty = select_level()
        hidden_word = select_word(difficulty)
        show_word(hidden_word)
    elif run_game == 2:
        show_rules()
    elif run_game == 3:
        pass


main()    

