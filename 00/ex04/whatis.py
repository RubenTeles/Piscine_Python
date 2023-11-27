import sys

arguments = sys.argv

if (len(sys.argv) > 2):
	print("AssertionError: more than one argument is provided")
elif (len(sys.argv) > 1):
	try:
		number = int(sys.argv[1])
		if (number % 2 == 1):
			print("I'm Odd.")
		else:
			print("I'm Even.")
	except:
		print("AssertionError: argument is not an integer")