# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Background
The goal of this Project was to create a version of the classic game 'Hangman' in order to bring together a number of concepts learned during the Python portion of my AiCore training. These include object-oriented programming, abstraction, user-input validation and working with libraries.

## Installation
The program is written entirely in Python. 

To install, simply clone the repository and run `python milestone_5.py` in the CLI or download and run the file in your interpreter of choice!

## Usage Instructions
### Getting started
The program takes two arguments;

1. `word_list` - a list containing all the words from which the user would like the computer to select from.
2. `num_lives` - a positive integer value representing the number of lives a player would like to have whilst playing.


Once initialised, the program uses `random.choice()` to select a random word from `word_list`. This is stored as a variable `word`. 

A second variable called `'num_letters'` is created which is equal to the number of unique letters in `word`. This represents the number of letters left for a user to correctly guess before they win.

another variable, `word_guessed` is also created. This is a list consisting of a single `'_'` representing each letter in `word`.

<center>

| word | word_guessed |
| ----------- | ----------- |
| `Apple` | `[_,_,_,_,_]` |
| `Orange` | `[_,_,_,_,_,_]` |

</center>
 

### Guessing
The program then begins prompting the user for input using the method `ask_for_input()`.

This input is checked for validity. If anything other than a single letter is entered, the program informs the user that their input is not valid and prompts again.

Once a valid input has been provided, the program will call `check_guess()` to assess whether this letter is present in `word`.
If the letter is present, the program will congratulate the user, replace the corresponding `'_'` in `'word_guessed'` and reduce `num_letters` by 1.

If the letter is not present in `word`, the program will inform the user, reduce `num_lives` by 1 and reprompt for another guess.

If the user has already guessed the given letter, the program will not allow the input and will prompt for another guess without reducing `num_lives`.

### Winning/Losing
A player wins if they guess all letters before `num_lives` reaches zero.