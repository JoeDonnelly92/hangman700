# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Background
The goal of this Project was to create a version of the classic game 'Hangman' in order to bring together a number of concepts learned during the Python portion of my AiCore training. These include object-oriented programming, abstraction, user-input validation and working with libraries.

## Implementation
This is a simple programme written entirely in Python. It takes two arguments;

1. `word_list` - a list containing all the words from which the user would like the computer to select from.
2. `num_lives` - a positive integer value representing the number of lives a player would like to have whilst playing.


Once initialised, the program uses `random.choice()` to select a random word from `word_list`. This is stored as a variable `word`. A second variable called `word_guessed` is also created. This is a list consisting of a single `_` representing each letter in `word`.
For example;
> If `word` was equal to `Apple` 
> `word_guessed` would be initialised as `[_,_,_,_l_e]`
The program then begins prompting the user for input using the method `ask_for_input()`.

This input is checked for validity. If anything other than a single letter is entered, the program informs the user that their input is not valid and prompts again.

Once a valid input has been provided, the program will call `check_guess()` to assess whether this letter is present in `word`.
If the letter is present, the program 