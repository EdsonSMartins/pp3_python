import random
import os
import time
import colorama
from colorama import Fore
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages

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


# To initialize colorama
colorama.init(autoreset=True)


def check_input(x):
    """
    Function to validate user input and return a valid options
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
    \r           | - Press (1) to Start the Game                       |
    \r           | - Press (2) to See the how to play the Game         |
    \r           | - Press (3) to Exit Game                            |
    \r           |_____________________________________________________|
           
        ''')
    number = input('')
    interger = check_input(number)
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
            exit()
        else:
            print('Please only enter 1, 2 or 3')
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
    \n       1. Guess one letter at a time to reveal the secret word.
    \n       2. Each incorrect guess adds another part to the hangman.
    \n       3. Chalange your knowledge by selecting the level of difficulty.       
    \n       4. Be careful, you have only 6 incorrect guesses!
    ''')
    print('1. Return home 2. End game')
    x = input('')
    if check_input(x) == 1:
        x = int(x)
        if x == 1:
            os.system("clear")
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
    print('''
    \n        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
    \r        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
    \r        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
    \r        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
    \r        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████                     
    ''')
    print('''        
    \n            --------------------- Levels ------------------------
    \r           |                                                     |
    \r           |    Please select the level you want to play:        |
    \r           |                                                     |
    \r           | - Press (1) for Begginer                            |
    \r           | - Press (2) for Intermediate                        |
    \r           | - Press (3) for Expert                              |
    \r           |_____________________________________________________|
           
    ''')
    level = input('')
    if check_input(level) == 1:
        level = int(level)
        if level == 1:            
            print('Begginer level loading...')
            os.system("clear")
            return 1
        elif level == 2:
            print('Intermediate level loading...')
            os.system("clear")
            return 2
        elif level == 3:            
            print('Expert level loading...')
            os.system("clear")
            return 3
        else:
            print('Please select a level: ')
    else:
        print(f'Error: input {level} is invalid')
        print('Please enter a valid number')
        select_level()


# Word selection
begginer_words = WORDS.col_values(1)
intermediate_words = WORDS.col_values(2)
expert_words = WORDS.col_values(3)


def select_word(level):
    """
    Game's words are defined by taken the value of level selected
    """
    choice = random.randrange(30)
    if level == 1:
        hidden_word = begginer_words[choice]
    elif level == 2:
        hidden_word = intermediate_words[choice]
    elif level == 3:
        hidden_word = expert_words[choice]
    return hidden_word


def show_word(hidden_word):
    """
    Get and display word by level, display hangman stages
    and also display words already guessed    
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
                # x value is used to iterate through blank list
                x = 0
                for letter in letters:
                    if user_guess == letter:
                        s_word[x] = user_guess
                        correct_guess += 1
                    x += 1 
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
            pre_game()
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
        exit()
    else:
        os.system("clear")
        main()


def main():
    """
    main function calls
    """
    print(fr''' {Fore.WHITE}                               
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
                             /¯¯/\
                            / ,^./\
                           / /   \/\
                          / /     \/\
                         ( (       )/)
                         | |       |/|         Welcome to
                         | |       |/|          the Hangman Game!
                         | |       |/|
                         ( (       )/)
                          \ \     / /
                           \ `---' /
                            `-----'     {Fore.RESET}   ''')
    print('\nLoading...')
    time.sleep(5)
    print('Completed')
    time.sleep(1)
    os.system("clear")   
    run_game = pre_game()
    if run_game == 1:
        difficulty = select_level()
        hidden_word = select_word(difficulty)
        show_word(hidden_word)
    elif run_game == 2:
        show_rules()
    elif run_game == 3:
        pass


main()    

