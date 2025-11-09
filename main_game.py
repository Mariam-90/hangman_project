print("Welcome to the Hangman game!")

def  check_letter():
    letter = input("Enter a letter: ")
    if letter.isalpha() and len(letter) == 1:
        return letter
    return False

print(check_letter())