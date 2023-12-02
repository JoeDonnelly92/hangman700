import random
#Create Hangman Class
class Hangman:
    #Initialise attributes
    '''Hangman is a classic guessing game! This implementation is intended to test my skills in Python.\n
        Get started by intialising an instance, passing in a word list (list, word_list) and a number of lives (int, num_lives) and use the "play_game" method.
    '''
    def __init__(self,word_list,num_lives):
        #initialises attributes used during gameplay
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = 5
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self,guess):
        '''This method is invoked once a user's guess has passed validation. \n 
        It checks if the single letter provided by the user is present in the word. \n 
        If the letter is not present, it subtracts a life and re-prompts. \n
        If the letter is present then it will lower the "num_letters" variable and reprompt.
        '''
        #Checks if guessed letter is present in randomly selected word.
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            #intiialise variable to act as stand-in for position of guessed letter in word.
            _ = -1
            for x in self.word:
                _ +=1
                #Iterates through letters in random word and sets variable '_' to the index position of the correct letter(s)
                if guess == x:
                    self.word_guessed[_] = guess
                 
            self.num_letters -=1
            print(self.word_guessed)
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

    def play_game(self):
        num_lives = 5
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            elif self.num_letters >0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break

Hangman(["Pineapple", "Mango", "Passionfruit", "Grape", "Banana"], 5).play_game()

