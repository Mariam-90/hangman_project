
# HANGMAN GAME - DISPLAY & FEEDBACK

# --- FUNCTION 1 ---
# Write a function that returns the hangman ASCII art based on incorrect guesses.
# Use the stages from the "ascii_art.py" file.

from common.ascii_art import hangman_7_stages
from game_functions import game_logic, game_state


def show_hangman(incorrect_guesses, hangman_art: list[str]=hangman_7_stages):
    return hangman_art[incorrect_guesses]


# --- FUNCTION 2 ---
# Write a function that displays the current game status.
# It should print: current display, alphabet with strikethroughs, and attempts remaining.
# Example output:
# Word: _ _ t h _ _
# Letters: a̶ b c d e̶ f g h i̶ j k l m n o p q r s t̶ u v w x y z
# Attempts remaining: 4

# Note:
#   This function requires the alphabet_display_with_guessed_letters_marked function
#   from game_logic.py to work properly

def display_game_status(letters_alphabet, guessed_letters, hidden_word, attempts_remain):
    word = game_logic.get_hidden_word_with_visible_guessed_letters(hidden_word,guessed_letters)
    print(f"Word: {word}")
    letters = game_logic.alphabet_display_with_guessed_letters_marked(letters_alphabet,guessed_letters)
    print(f"Letters: {letters}")
    print(f"Attempts remaining: {attempts_remain}")


# --- FUNCTION 3 ---
# Write a function that displays a win message.
# Example: "Congratulations! You guessed the word: python"

def show_win_message(word):
        print(f"Congratulations! You guessed the word: {word}")



# --- FUNCTION 4 ---
# Write a function that displays a lose message.
# Example: "Game Over! The word was: python"

def show_lose_message(word):
        print(f"Game Over! The word was:{word}")
