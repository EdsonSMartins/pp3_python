import random
import gspread
from google.oauth2.service_account import Credentials
from hangman_art import stages
from hangman_art import logo

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
english_alphabet = ['abcdefghijklmnopqrstuvwxyz']

print(logo)