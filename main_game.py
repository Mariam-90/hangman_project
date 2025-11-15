import random

from google.api_core.retry import retry_target_stream

from game_functions.display_and_feedback import display_game_status, show_hangman, show_win_message, show_lose_message
from game_functions.game_logic import update_guessed_letters, update_letters_to_be_guessed, check_letter_in_word
from game_functions.game_setup import initialize_alphabet_display, choose_random_word, initialize_letters_to_be_guessed
from game_functions.game_state import is_game_over, check_win_condition
from game_functions.input_and_validations import get_valid_guess

print("Welcome to the Hangman game!")

list_of_words = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic",
    "melon",
    "tomato"
]
letters_alphabet = initialize_alphabet_display("abcdefghijklmnopqrstuvwxyz")
secret_word = choose_random_word(list_of_words)
hidden_letters = initialize_letters_to_be_guessed(secret_word)
guessed_letters = set()
attempts_remaining = 6
incorrect_guesses = 0
if __name__ == '__main__':
    while not is_game_over(hidden_letters, attempts_remaining):
        print(secret_word)
        display_game_status(letters_alphabet, guessed_letters, secret_word, attempts_remaining)
        guess = get_valid_guess(guessed_letters)
        if check_letter_in_word(guess, secret_word):
            update_letters_to_be_guessed(hidden_letters, guess)
        else:
            print(show_hangman(incorrect_guesses))
            incorrect_guesses += 1
            attempts_remaining -= 1

        # update guessed letters
        update_guessed_letters(guess, guessed_letters)
        update_letters_to_be_guessed(hidden_letters, secret_word)
        #displays a win or lose
        if check_win_condition(hidden_letters):
            show_win_message(secret_word)
        else:
            show_lose_message(secret_word)



