from ascii_hangman import man
from functions import guess_list
from functions import spaces
from functions import check_word
from functions import check_guesses
from random import randint


def load_words():
    return [line.rstrip('\n') for line in open('words.txt')]


def random_word(words):
    return word_list[randint(0, len(words)-1)]

word_list = load_words()

print("Welcome to Hangman!\n")

while 1:
    correct = False
    answer = random_word(word_list)
    guessed = set()
    lives = 6
    display = True

    while not correct and lives > 0:
        if display:
            print("Guessed:", guess_list(guessed))
            print(man(lives))
            print(spaces(guessed, answer))
        display = True

        guess = input("\nGuess a letter! ")
        if len(guess) > 1:
            if check_word(guess, answer):
                correct = True
            else:
                lives = 0
        else:
            if guess in guessed:
                print("You've already guessed that!")
                display = False
            else:
                guessed.add(guess)
                if guess in list(answer):
                    if check_guesses(guessed, answer):
                        correct = True
                else:
                    lives -= 1

    if correct:
        print("\nCongratulations! You won!")
    else:
        print("\n", man(lives), "\nSorry, you lost! The word was:", answer)

    playAgain = input("\nWould you like to play again?")

    if playAgain == "no":
        break

print("\nthanks for playing")

