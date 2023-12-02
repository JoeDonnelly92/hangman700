import random

word_list = ["Pineapple","Mango","Passionfruit","Grape","Banana"]
word = random.choice(word_list)


def ask_for_input(): 
    guess = input("Enter a letter: ").lower()
    while True:
        if guess.isalpha() == True and len(guess) ==1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("Enter a letter: ")
            continue
    check_guess(guess)
    return guess

def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def main():
    ask_for_input()



if __name__ == "__main__":
    main()
