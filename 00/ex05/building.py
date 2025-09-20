import sys

def is_punctuation(c: str) -> bool:
	return (c in '''!()-[]{};:'"\,<>./?@#$%^&*_~''') # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
	
def count_characters(message: str) -> bool:

	count_characters = 0
	upper = 0
	lower = 0
	digits = 0
	spaces = 0
	punctuation = 0

	for char in message:
		count_characters += 1
		print("Char:", char, " - ", count_characters, " is Space: ", char.isspace())
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
	arguments = sys.argv

	if (len(arguments) > 2):
		print("AssertionError: more than one argument is provided")
	elif (len(sys.argv) == 2):
		count_characters(sys.argv[1])
	elif (len(sys.argv) == 1):
		print("What is the text to count?")
		message = sys.stdin.read()
		count_characters(message)

if __name__ == "__main__":
	main()

# For checking the result you can use this website:
# https://countwordsfree.com/
# Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.

# https://www.geeksforgeeks.org/python/string-punctuation-in-python/
# import string
# count = sum(1 for ch in message if ch in string.punctuation)
# print(f"{count} punctuation marks _ 2")