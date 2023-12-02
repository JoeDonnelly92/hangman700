import random

word_list = ["Pineapple","Mango","Passionfruit","Grape","Banana"]
word = random.choice(word_list)

def get_guess:
while True:
    guess = input("Enter a letter: ")
    if guess.isalpha() == True and len(guess) ==1:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
return guess 

