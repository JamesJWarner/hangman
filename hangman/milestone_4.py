import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            self.num_letters -= 1
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = letter
                    print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')



    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

# Test
# word_list = ["apple", "banana", "cherry", "pineapple", "grape"]
# test = Hangman(word_list)
# test.ask_for_input()