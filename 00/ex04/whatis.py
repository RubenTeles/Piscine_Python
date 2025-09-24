import sys


def whatis(number: int):
    """Determine whether a given integer is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: "I'm Even." if the number is even, otherwise "I'm Odd."
    """
    return "I'm Even." if number % 2 == 0 else "I'm Odd."


def main(argv):
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        elif (len(sys.argv) == 2):
            try:
                number = int(sys.argv[1])
                print(whatis(number))
            except Exception:
                raise AssertionError("argument is not an integer\n")
        else:
            print()
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main(sys.argv)
