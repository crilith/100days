import random
from hangman_words import word_list
from hangman_art import stages,logo

# Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word, you have {lives} lives left")

        if lives == 0:
            game_over = True

            # Give the user the correct word they were trying to guess.
            print(f"***YOU LOSE*** the word was {chosen_word}")
    print(stages[lives])
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")