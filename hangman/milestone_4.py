import random

class Hangman:
        
    '''
    This class is used to run the Hangman game.

    Attributes:
        word_list (list): list of possible words.
        num_lives (int): number of lives left.
        word (str): random selected word from word_list.
        word_guessed (list): list showing the guessed letters of word with unguessed letters represented as a _.
        num_letters (int): the number of unique letters in the word.
        list_of_guesses (list): a list of all letters guessed, empty list of no guesses made.
    '''
    def __init__(self, word_list, num_lives = 5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        '''
        This function is used to check if the letter guessed is in the word or not.

        Args:
            guess (str): a string of a single alphabetical letter.

        Returns:
            Message to user if guess is in word or not and also updates num_lives if guess not in word.
        '''
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
        '''
        This function is used to recieve guesses from user and check if each guess is a valid input or not.
        Then it calls the check_guess function on said guesses.

        Returns:
            Message to user if guess is invalid or if it has been repeated.
        '''
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