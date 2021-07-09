# Problem 4 


# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import argparse
import logging
logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()

parser.add_argument('-p','--pal')

args = parser.parse_args()
# converting int to string then splitting in half 


# determining if the two sides are the same

def isPalindrome(num):

	num = str(num)

	half_len = int(0.5* len(num))

	if len(num) % 2 == 0:

		return num[:half_len] == num[half_len:][::-1]

	else:

		return num[:half_len] == num[(half_len+1):][::-1]



# loop to find product of two 3 digit numbers, then determine if its a palindrome
def Main():

	string = args.pal

	if string:

		if isPalindrome(string):

			print(f"{string} is a palindrome")

		else:

			print(f"{string} is NOT a palindrome")


if __name__ == "__main__":

	Main()