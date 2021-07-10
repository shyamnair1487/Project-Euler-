"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divide_all(num):

	div_all = True
	for i in range(1,11):

		if num % i != 0:
			div_all = False
			break
	return div_all