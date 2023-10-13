import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        





# def ask_for_input(self, word):
#     while True:
#         guess = input("Guess a single letter: ")
#         if guess.isalpha() == True and len(guess) == 1:
#             break
#         else:
#             print("Invalid letter. Please, enter a single alphabetical character.")
#     check_guess(guess, word)  

# def check_guess(self, guess, word):
#     guess.lower()
#     if guess in word:
#         print(f'Good guess! {guess} is in the word.')
#     else:
#         print(f'Sorry, {guess} is not in the word. Try again.')

# word = ran_word()
# ask_for_input(word)