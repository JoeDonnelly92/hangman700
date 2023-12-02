import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" * len(word)]
        self.num_lives = num_lives
        self.num_letters = int(len(set(word)))
        self.list_of_guesses = []
