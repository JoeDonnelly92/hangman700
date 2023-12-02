import random

class Hangman:
    def __init__(self,word_list,num_lives,list_of_guesses):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = 5
        self.num_letters = int(len(set(word)))
        self.list_of_guesses = []

    def check_guess():
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(): 
        print(list_of_guesses)
        guess = input("Enter a letter: ").lower()
        while True:
            if guess.isalpha() == False and len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = input("Enter a letter: ")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                guess = input("Enter a letter: ")
                continue
            else:   
                self.list_of_guesses.append(guess)
                break
        check_guess(guess)
        return guess

    def main():
        ask_for_input()

Hangman.ask_for_input()