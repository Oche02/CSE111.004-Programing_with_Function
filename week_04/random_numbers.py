"""
Author: Augustine Okpe Oche
Program: Random numbers and words
"""

import random


def append_random_numbers(numbers_list, quantity=1):
    """
    append quantity numbers into the numbers_list between o and 100.
    parameter
        numbers_list: lists of numbers
        quantity: number of random numbers to append
    return
        nothing.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):
    """
    append quantity words into the words_list between
    parameter
        words_list: lists of words
        quantity: number of random words to append
    return
        nohing.
    """
    words = ["saw", "eggs", "mat", "shoe", "pen", "ten", 'join', 'love', 'smile', 'love', 'cloud', 'head']
    for _ in range(quantity):
        random_word = random.choice(words)
        words_list.append(random_word)


def main():
    # Create a list of numbers
    numbers_list = [16.2, 75.1, 52.3]
    print(f"{numbers_list}")

    # aappend random number into the list and print the list
    append_random_numbers(numbers_list)
    print(numbers_list)

    # append three random numbers to the list and print the list
    append_random_numbers(numbers_list, 3)
    print(f"{numbers_list}")

    # Create list of words
    words_list = []

    # append random choiced words in the word list.
    append_random_words(words_list, 5)
    print(f"{words_list}")

    # append random choiced words in the word list.
    append_random_words(words_list, 8)
    print(f"{words_list}")

if __name__ == "__main__":
    main()
