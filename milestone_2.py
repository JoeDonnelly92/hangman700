import random

word_list = ["Pineapple","Mango","Passionfruit","Grape","Banana"]
word = random.choice(word_list)

def get_guess():
    guess = input("Enter a letter: ")
    while True:
        if len(guess) == 1 and guess.isalpha() == True:
            print("Nice length")
            break
        else:
            print("Oops! That is not a valid input")
            break
    return guess

def main():
    guess = get_guess()

main()

