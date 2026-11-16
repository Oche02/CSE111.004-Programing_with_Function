"""
author: Augustine Okpe Oche
program: Password Strength Checker
creativity: I added a clearer message for the user to understand the strength of their password and how to improve it.
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

# These files are used to reject dictionary words and commonly used passwords.
WORDLIST_FILE = __file__.replace("passwords.py", "wordlist.txt")
TOP_PASSWORDS_FILE = __file__.replace("passwords.py", "toppasswords.txt")


def word_in_file(word, filename, case_sensitive=False):

    # Check each line in the selected file for a matching word.
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:

            # Remove the line ending before comparing complete list entries.
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            elif word.casefold() == file_word.casefold():
                return True
    return False


def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):

    # Count how many different character groups the password uses.
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity


def password_strength(password, min_length=10, strong_length=16):

    # Reject weak passwords before evaluating length or complexity.
    if word_in_file(password, WORDLIST_FILE):
        print("Not secure: this is a dictionary word. Choose a unique password instead.")
        return 0

    if word_in_file(password, TOP_PASSWORDS_FILE, case_sensitive=True):
        print("Not secure: this password appears in a common-password list. Choose a different one.")
        return 0

    if len(password) < min_length:
        print(f"Weak: use at least {min_length} characters; this password has {len(password)}.")
        return 1

    # Give long passwords the maximum score before checking character variety.
    if len(password) >= strong_length:
        print(
            f"Strong length: {len(password)} characters meets the "
            f"{strong_length}-character target. Try to use a mix of character types too."
        )
        return 5

    # Score shorter passwords based on the number of character groups they use.
    strength = 1 + word_complexity(password)
    if strength == 1:
        print("Very weak: use lowercase or uppercase letters, numbers, or symbols.")
    elif strength == 2:
        print("Weak: only one checked character type is present; add more types.")
    elif strength == 3:
        print("Fair: two checked character types are present; add another type.")
    elif strength == 4:
        print("Good: three checked character types are present; add the remaining type.")
    else:
        print("Strong: all four checked character types are present.")
    return strength


def main():
    # Keep checking passwords until the user enters Q.
    while True:
        password = input("Enter a password to check (or Q to quit): ")
        if password in ("q", "Q"):
            break

        strength = password_strength(password)
        print(f"Password strength: {strength} out of 5.")

if __name__ == "__main__":
    main()
