"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
import argparse, math

parser = argparse.ArgumentParser()

parser.add_argument("n", type=int, help="where n is the nth prime number")

args = parser.parse_args()

def isPrime(num):
    
    square = math.ceil(math.sqrt(num))
    if num < 1000:
        square = num
    else:
        square += 1
    prime = True 
    for i in range(2,square):
        if num % i == 0:
            prime = False
            break
    return prime


def Main():

	n = args.n
	print(n)
	for i in range(2,50):
		if isPrime(i):
			print(i, end=" ")


if __name__ == "__main__":

	Main()