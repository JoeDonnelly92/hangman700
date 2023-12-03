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
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = 5
        self.num_letters = len(set(self.word))
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
            #enumerates over chars in word, if any match guess it reveals them in variable 'word_guessed'
            for i,x in enumerate(self.word):
                if guess == x:
                    self.word_guessed[i] = guess
             #lowers number of remaining letters by 1    
            self.num_letters -=1
            #prints word with correctly guessed letters revealed and all others as underscores.
            print(self.word_guessed)
        else:
            #If letter not present in word, num_lives lowered by 1 and user prompted for input
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} left.")

    def ask_for_input(self): 
        '''The method "ask_for_input" prompts a user for a guess in the form of a single letter.
            The method validates this input to ensure it is a single, alphabetical character and converts it to lowercase. \n
            If the guess is not a valid input, the method continues to prompt.
            Once a valid input is receieved, it is passed to the check_guess function.        
        
        '''
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
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            elif self.num_letters >0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break

def main():
    Hangman(["Pineapple", "Mango", "Passionfruit", "Grape", "Banana"], 5).play_game()
 

if __name__ == "__main__":
    main()

