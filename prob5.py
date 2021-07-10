"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np

# def divide_all(num):

# 	div_all = True
# 	for i in range(1,21):

# 		if num % i != 0:
# 			div_all = False
# 			break
# 	return div_all

# x = 21
# while True:

# 	if divide_all(x):

# 		break
# 	else:
# 		x += 1

# print(x)

def isPrime(num):

	prime = True
	for factor in range(2,num):

		if num % factor == 0:
			prime = False
			break
	return prime

primes = [i for i in range(2,21) if isPrime(i)]
print(f"List of primes: {primes}")
print("")

arr = np.arange(1,21)
print(f"array: {arr}")

LCM =1
for i in primes:

	while any(arr % i ==0):

		arr = np.where(arr % i ==0, arr / i, arr)
		LCM *= i

print("")

print("")
print(f"Lowest Common Mulitple = {LCM}")
