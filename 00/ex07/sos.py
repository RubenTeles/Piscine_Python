import sys

def encript_morse_code(text: str):
	NESTED_MORSE = { " ": "/",
		"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
		"G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
		"M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
		"S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
		"Y": "-.--", "Z": "--..",
		"1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
		"6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", }
	
	text = text.upper()
	morseString = ""

	wordsNumber = len(text)
	count = 0
	for char in text:
		count += 1
		if char in NESTED_MORSE:
			morseString += NESTED_MORSE[char]
		else:
			raise AssertionError("the arguments are bad")
		
		if (count != wordsNumber):
			morseString += ' '

	return morseString

def main():
	try:
		arguments = sys.argv

		if (len(arguments) != 2 or len(sys.argv[1]) == 0 or not isinstance(sys.argv[1], str)):
			raise AssertionError("the arguments are bad")
	
		text = sys.argv[1]
		print(encript_morse_code(text))

	except AssertionError as error:
		print("AssertionError:", error)


if __name__ == "__main__":
	main()