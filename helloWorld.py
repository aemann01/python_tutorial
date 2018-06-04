#!/usr/bin/python3
#import statements
import sys

#doc string explaining what/how to use the program
'''Usage: python helloWorld.py <your name>'''

#a simple function
def main():
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	else:
		print("Please enter your name:")
		name = input()
	print('Hello', name)

#standard way of calling the main function
if __name__ == '__main__':
	main()
