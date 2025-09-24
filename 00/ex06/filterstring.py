import sys
from ft_filter import ft_filter


def main():
    try:
        arguments = sys.argv
        if (len(arguments) == 3):
            try:
                text = sys.argv[1]
                number = int(sys.argv[2])

                ft_list = text.split(' ')

                # print(ft_filter.__doc__)
                print(list(ft_filter(lambda x: len(x) > number, ft_list)))
            except ValueError:
                raise AssertionError("the arguments are bad")
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()

# print("---------------- Correct Result:")
# print(filter.__doc__)
# print(list(filter(lambda x: len(x) > number, ft_list)))
