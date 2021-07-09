# Problem 4 

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


import logging
logging.basicConfig(Level=logging.DEBUG)




# converting int to string then splitting in half 


# determining if the two sides are the same

def isPalindrome(num):

	num = str(num)

	hal_len = int(0.5* len(num))

	if len(num) % 2 == 0:

		return num[:hal_len] == num[half_len:]

	else:

		return num[:half_len] == num[(half_len+1):]



# loop to find product of two 3 digit numbers, then determine if its a palindrome