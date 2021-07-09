# Problem 4 


# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import argparse
import logging
logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()

# parser.add_argument('-p','--pal', help="Pass in the string to be evaluated as a palindrome")
parser.add_argument('num', type=int, help="Number of digits to be multiplied", choices={2,3})

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
def largest_palindrome(n_digits):

	largest_product = 0

	low_range = 10**(n-1)
	high_range = 10**n

	for i in range(low_range, high_range):

		for j in range(low_range, high_range):

			if (i * j) > largest_product and isPalindrome(i*j):

				largest_product = i * j

	return largest_product
		



def Main():
	num = args.num
	string = args.pal

	if string:

		if isPalindrome(string):

			print(f"{string} is a palindrome")

		else:

			print(f"{string} is NOT a palindrome")


	print(num)		

if __name__ == "__main__":

	Main()