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

	print(f"The text contains {len(message)} characters:")
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
	else:
		print("No argument provided, please provide a string")

if __name__ == "__main__":
	main()