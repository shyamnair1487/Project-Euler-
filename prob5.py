"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

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