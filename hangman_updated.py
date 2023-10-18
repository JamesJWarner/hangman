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
        guess = input("Guess a single letter: ")
        if guess.isalpha() == False or len(guess) != 1: # checks if input is not only letters or if it is longer than one character
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            guess = guess.lower() # turns guess into lower case so for example a and A are treated as the same guess
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    '''
    This function is used to start the game, run the game and then end the game.

    Args:
        word_list (list): list of possible words.

    Returns:
        A message depening on number of wins and loss, and also prints the exact number of each.
    '''
    def repeat_game_option():
        '''
        This function is used to determine if the user would like to continue with the game.

        Returns:
            A variable called repeat_option which has the value of either yes or no
        '''
        while True:
            repeat_option = input("Do you want to play again? yes or no: ")
            if repeat_option.isalpha() == False:
                print("Invalid answer. Make sure to avoid any non alphabetical characters!")
            elif repeat_option.lower() != "yes" and repeat_option.lower() != "no":
                print("Invalid answer. Please give yes or no answer only!")
            else:
                break
        return repeat_option.lower()

    def run_game(word_list, num_wins, num_losses):
        '''
        This function is used to create an instance of the Hangman class and run the game.

        Args:
            word_list (list): list of possible words.
            num_wins (int): Total number of times the user wins the game
            num_losses (int): Total number of times the user losses the game

        Returns:
            Tells user if they win or lose the game, and updates the num of wins and losses
        '''
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print("You lost!")
                num_losses += 1
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                num_wins += 1
                break
        return num_wins, num_losses
    
    played_game = run_game(word_list, 0, 0) # This runs the first game, hence 0 wins, 0 losses
    num_wins = played_game[0]
    num_losses = played_game[1]
    repeat_option = repeat_game_option() # Need this to trigger while loop
    while repeat_option == "yes":
        new_played_game = run_game(word_list, num_wins, num_losses) # This runs future games, hence variable args instead of 0's
        num_wins = new_played_game[0]
        num_losses = new_played_game[1]
        repeat_option = repeat_game_option() # Need this to end while loop

    print(f'You won: {num_wins} games, and lost: {num_losses} games')
    if num_wins > num_losses:
        print("Well done, you won more games than you lost. I'll try and beat you more next time!")
    elif num_wins < num_losses:
        print("Sadly you lost more games than you won, better luck next time!")
    else:
        print("You're just as good at winning as you are at losing HAHAHA. Rematch me again soon!")


# Test
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "pineapple", "grape"]
    play_game(word_list)
