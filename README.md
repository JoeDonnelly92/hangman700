# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Background
In this Project I sought to create a version of the classic game 'Hangman' in order to bring together a number of concepts learned during the Python portion of my AiCore training. These include object-oriented programming, abstraction, user input validation and more.

## Implementation
This simple Python program takes two arguments;
 
1. `word_list` a list containing all the words from which the user would like the computer to select from
2. `num_lives` a positive integer value representing the number of lives a player would like to have whilst playing.


Once the program has selected (using random.choice()), it will begin to prompt the user for input in the form of a single letter.

This input is checked for validity. If anything other than a single letter is entered, the program prompts again.

Once a valid input has been provided, the program will check whether this letter is present in the randomly selected word.