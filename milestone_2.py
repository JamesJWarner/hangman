import random

word_list = ["apple", "banana", "cherry", "pineapple", "grape"]
# print(word_list)
word = random.choice(word_list)
print(word)

guess = input("Guess a single letter: ")

if guess.isalpha() == True and len(guess) == 1:
    print("good guess")
else:
    print("Oops! That is not a valid input.")
