import random

word_list = ["Pineapple","Mango","Passionfruit","Grape","Banana"]
word = random.choice(word_list)

def get_guess():
    while True:
        guess = input("Enter a letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            print("Nice length")
            break
        else:
            print("Oops! That is not a valid input")
    return

def main():
    guess = get_guess()
    print(guess)

main()

