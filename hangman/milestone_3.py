import random

def ran_word():
    word_list = ["apple", "banana", "cherry", "pineapple", "grape"]
    # print(word_list)
    word = random.choice(word_list)
    return word

def ask_for_input(word):
    while True:
        guess = input("Guess a single letter: ")
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, word)
    

def check_guess(guess, word):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

word = ran_word()
ask_for_input(word)