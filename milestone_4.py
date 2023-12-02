import random
#Create Hangman Class
class Hangman:
    #Initialise attributes
    '''Hangman is a classic guessing game! This implementation is intended to test my skills in Python.'''
    def __init__(self,word_list,num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = 5
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self,guess):
        #Checks if guessed letter is present in randomly selected word.
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            _ = 0
            for x in self.word:
                #Iterates through letters in random word and sets variable '_' to the index position of the correct letter(s)
                if guess == x:
                    _ +=1
                    self.word_guessed[_] = guess
            self.num_letters -=1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} left.")

    def ask_for_input(self): 
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
        self.check_guess(guess)
        return guess


hangman = Hangman(word_list=["Pineapple","Mango","Passionfruit","Grape","Banana"],num_lives=5)
hangman.ask_for_input()

