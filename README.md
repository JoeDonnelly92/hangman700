# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

#Background
In this Project I sought to create a version of the classic game 'Hangman' in order to bring together a number of concepts learned during the Python portion of my AiCore training.

#Implementation
This simple Python program will use the 'Random' package to generate a random word from a pre-defined list. In the interest of keeping things simple for now, this list is short, consisting of 5 fruits. Once the program has selected (using random.choice()), it will begin to prompt the user for input in the form of a single letter.