# Project With - Kwabena - skwgya1
# Cameron Williams - cawil69 - Also submitted on edstem.
# Printing Status
def print_win_message(word):
    print(f"Congrats, you won! The word: {word}.")


def print_lose_message(word):
    print(f"Sorry you lost. The word: {word}.")


def print_status(progress, wrong_letters, num_guesses):
    print(f"Word: {progress}")
    print(f"Wrong: {wrong_letters}")
    print(f"Guesses remaining: {num_guesses}")


# Reading Guesses
def get_user_guess():
    T = True
    while T == True:
        guess = input("Guess a letter: ")
        guess = str(guess)
        if len(guess) == 1 and guess.isalpha() == True:
            T = False
        else:
            print("You must guess a single letter")
    return guess


# Updating Process
def update_progress(word, current_progress, guessed_letter):
    new_progress = ""
    for i in range(len(word)):
        if word[i] == guessed_letter:
            new_progress += guessed_letter
        else:
            new_progress += current_progress[i]
    return new_progress
