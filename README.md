# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the user enters a list of words for the computer to choose from at random. Then the user guesses letters and tries to find which word the computer has chosen.

## How to play
Open the hangman_updated.py file, located in this folder, replace the words in the [] next to where it says word_list (make sure each word is seperated by a comma i.e [word1, word2, ..., final word] ).

Save the file so that the words you wish to play with are updated. Once you have done this, these steps do not need to be repeated unless you wish to change the word choices for the computer again.

Then simply run the file, and start guessing!
After each game a prompt will ask you if you would like to play another round, simply type, yes, if you would like to or, no, if you would like the game to come to an end.
At the end you will be told your final score, so try and win as many rounds as you can.

## Milestones

The milestone python files are steps in creating the game.

- milestone_2: basic setup of random word from list and a letter guess.

- milestone_3: more advanced version of milestone 2 with functions.

- milestone_4: Created a Hangman class with added functionality of updating the word-guessed variable and also displaying number of lives. 

- milestone_5: Defined a function called play-game which would use the class created in milestone-4.
It also has the added functionality of telling the user if they win or lose

## Hangman_updates

After finishing the milestones, I wanted to add some other functionalites to the game. These updates will be applied to the hangman_updated.py file. The previous milestones can still be found in the hangman folder.

### Updates

- Play again: the user can now play multiple games while only running the file once.

- Final score: the user will now be able to see their number of wins and losses when they finally enter no when asked if they would like to play again.
