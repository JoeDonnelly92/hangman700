while True:
    guess = input("Enter a letter: ")
    if guess.isalpha() == True and len(guess) ==1:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")