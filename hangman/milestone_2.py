import random

def ran_word():
    word_list = ["apple", "banana", "cherry", "pineapple", "grape"]
    # print(word_list)
    word = random.choice(word_list)
    return word

def letter_guess():
    guess = input("Guess a single letter: ")

    if guess.isalpha() == True and len(guess) == 1:
        print("good guess")
    else:
        print("Oops! That is not a valid input.")

    return guess