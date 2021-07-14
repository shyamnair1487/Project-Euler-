"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('-n', "--num", default=2000000, type=int, help="number below which to find summation of all primes")

args = parser.parse_args()

def isPrime(num):
    if num <= 1:
        return False
    
    square = math.ceil(math.sqrt(num)) + 1
    
    if num < 1000:
        square = num
    else:
        square += 1
    for i in range(2,square):
        if num % i == 0:
            return False
    return True

def Main():

	limit = args.num
	
	
	prime_sum = 0
	number = 1

	while number < 2000000:

		if isPrime(number):
			prime_sum += number  
		number += 1

	print(f"Sum of primes below {limit} is {prime_sum}")

if __name__ == "__main__":

	Main()