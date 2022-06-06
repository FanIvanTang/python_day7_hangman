# Step 1

import random

import hangman_words
import hangman_art

# word_list = ["aardvark", "baboon", "camel"]


def pick_a_word():

    return hangman_words.word_list[random.randint(0, len(hangman_words.word_list) - 1)]


def initial_display(word):
    dashes = []
    for _ in word:
        dashes.append("_")
    return dashes


def user_guess_letter():
    letter = input("Guess a letter: ")

    return letter.lower()


def is_in_word(l, word):

    result = False

    for this_letter in word:
        if l == this_letter:
            result = True
            break
    return result


def update_display(l, word, display):

    for i in range(len(word)):
        if l == word[i]:
            display[i] = l

    return display


if __name__ == "__main__":

    print(hangman_art.logo)

    live = 6
    picked_word = pick_a_word()
    print(f"The pick_a_word is { picked_word}")
    updated_display = initial_display(picked_word)
    print(" ".join(updated_display))

    guess_all_letters = not ("_" in updated_display)

    # print(guess_all_letters)

    while not guess_all_letters:
        guessed_letter = user_guess_letter()

        if is_in_word(guessed_letter, picked_word):

            updated_display = update_display(
                guessed_letter, picked_word, updated_display
            )
            print(" ".join(updated_display))

        else:

            print(hangman_art.stages[live])
            live -= 1
            if live < 0:
                print("You lost")
                break

        guess_all_letters = not ("_" in updated_display)

        if guess_all_letters:
            print("You win!")
