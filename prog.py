#import statements
import argparse

#doc string
'''This script calculates the square of a given number. Useage: python prog.py'''

#argparser -- now you can add flags to the program
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--square", type=int, help="display the square of a given number")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")

#set up argparser object
args = parser.parse_args()

def square():
	#calculate the square of the number provided
	answer = args.square**2

	#if the user wanted a verbose answer, print with string, else print just the number
	if args.verbosity:
		print("the square of %i equals %i" % (args.square, answer))
	else:
		print(answer)

square()
