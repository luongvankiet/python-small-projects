import random
from hangman_words import word_list
from hangman_art import logo, stages

selected_word = random.choice(word_list)

letters = ""
user_guesses = []
life = 6

print(logo)

while letters != selected_word and life > 0:
    if len(user_guesses) < 1:
        for i in range(len(selected_word)):
            letters += "_"

    print(f"Word to guess: {letters}")
    user_guess = input("Guess a letter: ")

    user_guesses.append(user_guess)

    letters_in_list = list(letters)

    if user_guess in selected_word:
        for i in range(len(selected_word)):
            if user_guess == selected_word[i]:
                letters_in_list[i] = user_guess

        letters = "".join(letters_in_list)
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        life -= 1

    print(stages[life])

    print(f"Your guesses: {user_guesses}")
    print(f"Results: {letters}")

    print(f"****************************{life}/6 LIVES LEFT****************************")

if life > 0:
    print("You win!")
else:
    print("You lose!")