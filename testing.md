# **The Hangman game!**

## **Contents**
   * [**User Stories Testing**](#User-Stories-Testing)
   * [**Manual Testing**](#Manual-Testing)

### ***User Stories Testing***

|As a First Time User | Outcome|
|---|---|
|I want to easy navigate and interact with the game.| Game allows easy input and navigation trhoug the menu.|
|I want to find instructions on how to play the game.|The instructions page can be easily accessed from the main menu.| 
|I want to get a wide range of random word selection.| Words are ramdomly selected from a database imported to the game, so user can play as many times they want without having repeated words.|
|I want to see a visual feedback when a wrong guess is made.| Every time user input a word, if incorrect game will display a feedback sentence in red, otherwise will display a feedback sentence in red. Color is also used to display letters already chosen.|



|As a user returning to the site| Outcome|
|---|---|
|I want to be able to choose the game difficulty by myself.| When user decide to Start the game from the main menu, a level menu is displayed so users can pick their desired level of difficulty.|


### ***Manual Testing***
|Feature| Expected Response | Actual Response| Outcome|
|---|---|---|---|
|Game intro| When the program loads, the ASCII art and greetings load| On start, everything loads correctly| PASS|
|Main Menu - Start game| When option 1 is selected, level menu should load| Level Menu load correctly| PASS|
|Main Menu - How to play| When option 2 is selected, How to play section should load| How to play section load correctly| PASS|
|Main Menu - Exit| When option 3 is selected, program should end| Program end correctly| PASS|
|Main Menu - Input Validation| If user input a letter or a number different from 1 to 3, program should return an error and reload| Error message display accordingly and program reload Main Menu| PASS| 
|How to play| Instructions should load and also give option to user return to Main Menu or Exit program| Instructions load correctly and two options that are displayed to user works accordingly| PASS|
|Level Menu - Begginer| When option 1 is selected, game should be trigged to start loading begginer level words| When option 1 is selected, system display a feedback message confirming begginer level is loading and game start correctly | PASS|
|Level Menu - Intermediate| When option 2 is selected, game should be trigged to start loading intermediate level words| When option 2 is selected, system display a feedback message confirming intermediate level is loading and game start correctly | PASS|
|Level Menu - Expert| When option 3 is selected, game should be trigged to start loading expert level words| When option 3 is selected, system display a feedback message confirming expert level is loading and game start correctly | PASS|
|Main Game - Start| the game loop starts and it display the array for the hidden word and the hangman picture on stage 0 | Array for hidden word and Hangman stage 0 load accordingly and request user to input a letter| PASS|
|Main Game - Correct answer| When user input a correct letter, this should be added to the hidden word array and also to the letters already guessed and a feedback message should also be displayed in green | When correct letter entered, hidden word and guessed letters array are updated and feedback message also dispplayed accordingly| PASS|
|Main Game - incorrect answer| When user input a incorrect letter, this should build hangman, add letter to letters already guessed and also a feedback message should also be displayed in red | When incorrect letter entered, guessed letters array is updated and feedback message also dispplayed accordingly including number of wrong attemps remaining| PASS|
|Main Game - Input Validation| User is expected to type a single letter at a time, program should return an error| Error message display accordingly| PASS| 
|Game Over - Success| When all of the correct letters are entered, hidden word should be revealed. Program to display congratulations message and user given an option to play again or exit game| The message is printed and the user able to decide if play again or exit game|PASSZ
|Game Over - Fail| When user run out of incorrect letters attempts program chouls reveal the hidden word and display confirmation message. User should be given an option to play again or exit game| The message is printed and the user able to decide if play again or exit game|PASS|
|Game Over - Input Validation| If user input a letter or a number different from 1 and 2, program should return an error and reload| Error message display accordingly|PASS|
