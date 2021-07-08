"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
Answer:  6857
"""


import argparse

from math import sqrt, ceil

parser = argparse.ArgumentParser()

parser.add_argument("number", type =int)

args = parser.parse_args()





def isPrime(num):

	prime = True
	for factor in range(2,num):

		if num % factor == 0:
			prime = False
			break
	return prime


def final_prime_factor(num):

	sq = ceil(sqrt(num))
	for factor in range(sq,1,-1):

		if num % factor == 0 and isPrime(factor):

			num = factor
			break
	return num



def Main():

	num = args.number

	
	ans = final_prime_factor(num)

	print("")
	print(f"The largest prime factor of {num} is {ans}")	
	


if __name__ == "__main__":

	Main()