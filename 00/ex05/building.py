import sys


def is_punctuation(c: str) -> bool:
    """
    Check if a character is a punctuation symbol.

    Args:
        c (str): A single character.

    Returns:
        bool: True if the character is punctuation, otherwise False.
    """
    return c in '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''


def count_characters(message: str) -> bool:
    """
    Count types of characters in a message.

    Args:
        message (str): The text to analyze.

    Returns:
        tuple: A tuple containing (upper, lower, digits, spaces, punctuation).
    """
    count_characters = 0
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuation = 0

    for char in message:
        count_characters += 1
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif is_punctuation(char):
            punctuation += 1

    print(f"The text contains {count_characters} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

    return (upper, lower, digits, spaces, punctuation)


def main():
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        elif (len(sys.argv) == 2):
            count_characters(sys.argv[1])
        elif (len(sys.argv) == 1):
            print("What is the text to count?")
            message = sys.stdin.read()
            count_characters(message)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()

# For checking the result you can use this website:
# https://countwordsfree.com/

# https://www.geeksforgeeks.org/python/string-punctuation-in-python/
# import string
# count = sum(1 for ch in message if ch in string.punctuation)
# print(f"{count} punctuation marks _ 2")
